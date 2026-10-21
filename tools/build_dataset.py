#!/usr/bin/env python3
"""Scrape the BlueDot Introduction to Digital Minds course into a hierarchical dataset.

Stages (each can be run on its own):
  scrape   - pull every unit's __NEXT_DATA__ into course/course.json
  layout   - write units/<unit>/<section>/page.md (verbatim page content) and course/links.json
  fetch    - download every reading/reference to sources/ as plain text or markdown
"""
import concurrent.futures as cf
import gzip
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
COURSE = "digital-minds"
BASE = f"https://bluedot.org/courses/{COURSE}"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

TIER_RANK = {"Core": 0, "Further": 1, "Maybe": 2}


def slugify(s, maxlen=60):
    s = re.sub(r"[’'`\"]", "", s.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:maxlen].rstrip("-") or "untitled"


def norm_url(u):
    u = u.strip().replace("\\_", "_")
    u = re.sub(r"[\"'>/]+$", "", u) if u.endswith(('"/>', '">')) else u
    return u.rstrip("/") if urlparse(u).path not in ("", "/") else u


def url_key(u):
    return hashlib.sha1(norm_url(u.split("#")[0]).encode()).hexdigest()[:8]


def next_data(html):
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    return json.loads(m.group(1))["props"]["pageProps"]


# --------------------------------------------------------------------------- scrape

def scrape():
    units = []
    landing = next_data(requests.get(BASE, headers=HEADERS, timeout=60).text)
    for n in range(1, len(landing["courseData"]["course"]["units"]) + 1):
        pp = next_data(requests.get(f"{BASE}/{n}/1", headers=HEADERS, timeout=60).text)
        unit = dict(pp["unit"])
        unit["title"] = unit["title"].strip()
        unit["chunks"] = sorted(pp["chunks"], key=lambda c: int(c["chunkOrder"]))
        units.append(unit)
    out = {"course": landing["courseData"]["course"], "units": units,
           "scrapedFrom": BASE}
    (ROOT / "course").mkdir(exist_ok=True)
    (ROOT / "course/course.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"scraped {len(units)} units")


# --------------------------------------------------------------------------- layout

SKIP_DOMAINS = ("linkedin.com", "slack.com", "miniextensions.com", "luma.com", "spotify.com")
SKIP_EXT = (".gguf", ".jpg", ".jpeg", ".png", ".gif")
EMBED_RE = re.compile(r'<iframe[^>]*src="(https://www\.youtube\.com/embed/[^"]+)"[^>]*/?>|'
                      r'(https://www\.youtube\.com/embed/[A-Za-z0-9_\\-]+)')
MDLINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
BARE_RE = re.compile(r"(?<![\(\"])https?://[^\s)\]\"<>]+")
ANY_URL_RE = re.compile(r"https?://[^\s)\]\"<>]+")


def with_scheme(u):
    return u if re.match(r"^[a-z]+://", u) else f"https://{u}"


def exercise_label(e):
    return e.get("title") or f"Exercise {e.get('exerciseNumber')}"


def unit_dir(u):
    return f"{u['unitNumber']}-{slugify(u['title'])}"


def section_dir(u, c):
    return f"{u['unitNumber']}.{c['chunkOrder']}-{slugify(c['chunkTitle'])}"


def ordered_resources(c):
    return sorted(c["resources"], key=lambda r: (TIER_RANK.get(r.get("coreFurtherMaybe"), 3),
                                                 float(r.get("readingOrder") or 99)))


def paragraph_around(text, start):
    lo = text.rfind("\n\n", 0, start)
    hi = text.find("\n\n", start)
    return text[lo + 2 if lo >= 0 else 0: hi if hi >= 0 else len(text)].strip()


def youtube_id(u):
    p = urlparse(u)
    if "youtu.be" in p.netloc:
        return p.path.strip("/")
    if "/embed/" in p.path:
        return p.path.split("/embed/")[1].split("/")[0]
    return parse_qs(p.query).get("v", [None])[0]


def classify_ref(u):
    low = u.lower()
    if any(d in urlparse(low).netloc for d in SKIP_DOMAINS) or low.endswith(SKIP_EXT):
        return "link-only"
    return "reference"


def layout():
    data = json.loads((ROOT / "course/course.json").read_text())
    links = []  # every link occurrence in the course
    seen_refs = set()

    def add_ref(link):
        k = (link["section"], url_key(norm_url(link["url"])))
        if k not in seen_refs:
            seen_refs.add(k)
            links.append(link)

    for u in data["units"]:
        for c in u["chunks"]:
            sdir = f"units/{unit_dir(u)}/{section_dir(u, c)}"
            ctx = {"unit": int(u["unitNumber"]), "unitTitle": u["title"],
                   "section": f"{u['unitNumber']}.{c['chunkOrder']}",
                   "sectionTitle": c["chunkTitle"], "sectionDir": sdir,
                   "sectionUrl": f"{BASE}/{u['unitNumber']}/{c['chunkOrder']}"}
            body = (c.get("chunkContent") or "").replace("\\_", "_")

            seen_embed = set()
            for m in EMBED_RE.finditer(body):
                url = (m.group(1) or m.group(2)).rstrip("\\")
                vid = youtube_id(url)
                if vid in seen_embed:
                    continue
                seen_embed.add(vid)
                links.append({**ctx, "kind": "embedded-video", "tier": "reading",
                              "url": f"https://www.youtube.com/watch?v={vid}",
                              "anchor": "Embedded video", "context": paragraph_around(body, m.start())})

            for i, r in enumerate(ordered_resources(c), 1):
                links.append({**ctx, "kind": "resource", "tier": "reading", "order": i,
                              "url": with_scheme(r["resourceLink"].strip()), "title": r["resourceName"].strip(),
                              "authors": r.get("authors"), "year": r.get("year"),
                              "coreFurtherMaybe": r.get("coreFurtherMaybe"),
                              "timeMins": r.get("timeFocusOnMins"),
                              "guide": (r.get("resourceGuide") or "").strip(),
                              "audio": r.get("syncedAudioUrl")})
                for m in ANY_URL_RE.finditer(r.get("resourceGuide") or ""):
                    gu = m.group(0).rstrip(".,")
                    add_ref({**ctx, "kind": "guide-link", "tier": classify_ref(gu), "url": gu,
                             "anchor": f"Link in the guide for '{r['resourceName'].strip()}'",
                             "context": (r.get("resourceGuide") or "").strip()})

            for m in MDLINK_RE.finditer(body):
                add_ref({**ctx, "kind": "inline-link", "tier": classify_ref(m.group(2)),
                         "url": m.group(2), "anchor": m.group(1).strip(),
                         "context": paragraph_around(body, m.start())})

            for e in c["exercises"]:
                for f in ("description", "answer", "options"):
                    for m in ANY_URL_RE.finditer(e.get(f) or ""):
                        eu = m.group(0).rstrip(".,")
                        add_ref({**ctx, "kind": "exercise-link", "tier": classify_ref(eu), "url": eu,
                                 "anchor": f"Link in exercise '{exercise_label(e)}'",
                                 "context": (e.get("description") or "").strip()})

    # assign stable source files (one per unique URL) and per-occurrence summary files
    used_names = {}
    for l in links:
        l["url"] = norm_url(l["url"])
        key = url_key(l["url"])
        name = l.get("title") or l.get("anchor") or urlparse(l["url"]).netloc
        if l["kind"] == "embedded-video":
            name = f"video-{youtube_id(l['url'])}"
        l["sourceKey"] = key
        l["sourceFile"] = f"sources/{slugify(name, 50)}__{key}.md"
        if l["tier"] == "reading":
            prefix = "00-video" if l["kind"] == "embedded-video" else f"{l['order']:02d}"
            l["summaryFile"] = f"{l['sectionDir']}/readings/{prefix}-{slugify(l.get('title') or name)}.md"
        elif l["tier"] == "reference":
            base = f"{l['sectionDir']}/references/{slugify(l['anchor'] if l['kind'] == 'inline-link' else urlparse(l['url']).netloc + urlparse(l['url']).path, 55)}"
            n = used_names.get(base, 0)
            used_names[base] = n + 1
            l["summaryFile"] = f"{base}{'' if n == 0 else f'-{n+1}'}.md"
    # a source file is named after its first occurrence
    first = {}
    for l in links:
        first.setdefault(l["sourceKey"], l["sourceFile"])
        l["sourceFile"] = first[l["sourceKey"]]

    (ROOT / "course/links.json").write_text(json.dumps(links, indent=1, ensure_ascii=False))

    for u in data["units"]:
        for c in u["chunks"]:
            write_page(u, c, [l for l in links if l["section"] == f"{u['unitNumber']}.{c['chunkOrder']}"])
    kinds = {}
    for l in links:
        kinds[(l["kind"], l["tier"])] = kinds.get((l["kind"], l["tier"]), 0) + 1
    print(f"{len(links)} link occurrences, {len({l['sourceKey'] for l in links})} unique URLs")
    for k, v in sorted(kinds.items()):
        print(f"  {k}: {v}")


def rel(from_dir, path):
    return str(Path(path).relative_to(from_dir)) if path.startswith(from_dir) else \
        "../" * len(Path(from_dir).parts) + path


def write_page(u, c, links):
    sdir = f"units/{unit_dir(u)}/{section_dir(u, c)}"
    out = [f"# {u['unitNumber']}.{c['chunkOrder']} {c['chunkTitle']}", "",
           f"- **Unit {u['unitNumber']}:** {u['title']}",
           f"- **Page:** {BASE}/{u['unitNumber']}/{c['chunkOrder']}"]
    if c.get("estimatedTime"):
        out.append(f"- **Estimated time:** {c['estimatedTime']} min")
    out += ["", "> Verbatim page content scraped from BlueDot. Agent-written analysis lives in "
            "`synthesis.md`, `readings/` and `references/`.", ""]

    body = (c.get("chunkContent") or "").strip().replace("\\_", "_")
    if body:
        body = EMBED_RE.sub(lambda m: f"\n\n▶ **Embedded video:** https://www.youtube.com/watch?v="
                            f"{youtube_id(m.group(1) or m.group(2))}\n\n", body)
        out += ["## Page text", "", body, ""]

    res = [l for l in links if l["kind"] == "resource"]
    if res:
        out += ["## Resources", ""]
        for l in res:
            meta = " · ".join(x for x in [l.get("coreFurtherMaybe"), l.get("authors"),
                                          str(l["year"]) if l.get("year") else None,
                                          f"{l['timeMins']} min" if l.get("timeMins") else None] if x)
            out += [f"### {l['order']}. [{l['title']}]({l['url']})", "", f"*{meta}*", ""]
            if l.get("guide"):
                out += ["**Why read this (course guide):**", "", l["guide"], ""]
            if l.get("audio"):
                out += [f"Audio version: {l['audio']}", ""]
            out += [f"→ Summary: [{Path(l['summaryFile']).name}]({rel(sdir, l['summaryFile'])})", ""]

    if c["exercises"]:
        out += ["## Exercises", ""]
        for e in sorted(c["exercises"], key=lambda e: int(e.get("exerciseNumber") or 0)):
            heading = f"Exercise {e.get('exerciseNumber')}" + (f": {e['title']}" if e.get("title") else "")
            out += [f"### {heading}", "",
                    f"*{e.get('type')} · {e.get('status')}*", "", (e.get("description") or "").strip(), ""]
            if e.get("options"):
                out += ["**Options:**", ""] + [f"- {o.strip()}" for o in e["options"].strip().split("\n") if o.strip()] + [""]
            if e.get("answer"):
                out += ["<details><summary>Answer (spoiler)</summary>", "", e["answer"].strip(), "", "</details>", ""]

    others = [l for l in links if l["kind"] not in ("resource",)]
    if others:
        out += ["## Other links on this page", "",
                "| Kind | Anchor | URL | Notes |", "|---|---|---|---|"]
        for l in others:
            note = f"[summary]({rel(sdir, l['summaryFile'])})" if l.get("summaryFile") else "not fetched (link only)"
            out.append(f"| {l['kind']} | {l['anchor'].replace('|', '/')} | {l['url']} | {note} |")
        out.append("")

    p = ROOT / sdir / "page.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(out))


# --------------------------------------------------------------------------- fetch

CONTENT_SELECTORS = ["#postBody", ".PostsPage-postContent", ".available-content", "article .body",
                     "article", "main", "[role=main]", ".post-content", ".entry-content", "#content"]


def html_to_markdown(html, url):
    soup = BeautifulSoup(html, "html.parser")
    title = (soup.title.string or "").strip() if soup.title and soup.title.string else ""
    if "bluedot.org/courses/" in url and "__NEXT_DATA__" in html and "chunks" in next_data(html):
        pp = next_data(html)  # course unit page: the server-rendered HTML holds only one chunk
        parts = [f"# {title}"]
        for ch in pp.get("chunks") or []:
            parts += [f"## {ch['chunkTitle']}", ch.get("chunkContent") or ""]
            for r in ch.get("resources") or []:
                parts.append(f"- Resource: {r['resourceName']} ({r['resourceLink']}) — {r.get('resourceGuide') or ''}")
        return "\n\n".join(parts)
    for t in soup(["script", "style", "noscript", "svg", "iframe", "form", "button"]):
        t.decompose()
    node = None
    for sel in CONTENT_SELECTORS:
        cand = soup.select_one(sel)
        if cand and len(cand.get_text(" ", strip=True).split()) > 150:
            node = cand
            break
    if node is None:
        node = soup.body or soup
        for t in node(["nav", "header", "footer", "aside"]):
            t.decompose()
    md = subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
                        input=str(node), capture_output=True, text=True).stdout
    md = re.sub(r"\n{3,}", "\n\n", md)
    return f"# {title}\n\n{md}" if title else md


def pdf_to_text(data):
    p = ROOT / "sources/.tmp" / hashlib.sha1(data[:4096]).hexdigest()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.with_suffix(".pdf").write_bytes(data)
    subprocess.run(["pdftotext", str(p.with_suffix(".pdf")), str(p.with_suffix(".txt"))], check=True)
    pages = subprocess.run(["pdfinfo", str(p.with_suffix(".pdf"))], capture_output=True, text=True).stdout
    n = re.search(r"Pages:\s+(\d+)", pages)
    txt = p.with_suffix(".txt").read_text(errors="replace")
    p.with_suffix(".pdf").unlink()
    p.with_suffix(".txt").unlink()
    return txt, int(n.group(1)) if n else None


def vtt_to_text(vtt):
    lines, last = [], None
    for ln in vtt.splitlines():
        if not ln.strip() or "-->" in ln or ln.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        ln = re.sub(r"<[^>]+>", "", ln).strip()
        if ln and ln != last:
            lines.append(ln)
            last = ln
    # auto-captions roll: drop lines fully contained in the next line's prefix
    text = " ".join(lines)
    return re.sub(r"\s+", " ", text)


def fetch_youtube(url):
    vid = youtube_id(url)
    tmp = ROOT / "sources/.tmp" / vid
    tmp.parent.mkdir(parents=True, exist_ok=True)
    for f in tmp.parent.glob(f"{vid}*"):
        f.unlink()
    subprocess.run(["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs",
                    "--sub-langs", "en,en-US,en-GB,en-orig", "--sub-format", "vtt",
                    "--write-info-json", "--sleep-subtitles", "2", "-o", str(tmp) + ".%(ext)s",
                    f"https://www.youtube.com/watch?v={vid}"], capture_output=True, text=True)
    info = {}
    if (tmp.parent / f"{vid}.info.json").exists():
        info = json.loads((tmp.parent / f"{vid}.info.json").read_text())
    subs = sorted(tmp.parent.glob(f"{vid}*.vtt"), key=lambda p: ("orig" in p.name, p.stat().st_size))
    manual = [p for p in subs if "orig" not in p.name]
    transcript = vtt_to_text((manual or subs)[0].read_text()) if subs else ""
    for f in tmp.parent.glob(f"{vid}*"):
        f.unlink()
    head = [f"# {info.get('title', vid)}", "",
            f"- Channel: {info.get('channel', '?')}",
            f"- Uploaded: {info.get('upload_date', '?')}",
            f"- Duration: {round((info.get('duration') or 0) / 60, 1)} min",
            f"- URL: https://www.youtube.com/watch?v={vid}", "",
            "## Description", "", info.get("description") or "", "",
            "## Transcript", "", transcript or "(no transcript available)"]
    return "\n".join(head), "youtube", bool(transcript)


FORUM_HOSTS = ("www.lesswrong.com", "www.alignmentforum.org", "forum.effectivealtruism.org")


def fetch_forum_post(url):
    """ForumMagnum sites render comments around the post; the GraphQL API returns just the post."""
    p = urlparse(url)
    post_id = p.path.split("/posts/")[1].split("/")[0]
    q = ('{post(input:{selector:{_id:"%s"}}){result{title postedAt user{displayName} htmlBody}}}' % post_id)
    r = requests.post(f"https://{p.netloc}/graphql", json={"query": q}, headers=HEADERS, timeout=60)
    r.raise_for_status()
    post = r.json()["data"]["post"]["result"]
    md = subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
                        input=post["htmlBody"], capture_output=True, text=True).stdout
    head = f"# {post['title']}\n\n- Author: {post['user']['displayName']}\n- Posted: {post['postedAt'][:10]}\n\n"
    return head + md, "forum-api", True


def notion_rich_text(prop):
    out = []
    for seg in prop or []:
        text = seg[0]
        for ann in (seg[1] if len(seg) > 1 else []):
            if ann[0] == "a":
                text = f"[{text}]({ann[1]})"
            elif ann[0] == "lm":  # link mention
                lm = ann[1]
                by = f" — {lm['link_author']}" if lm.get("link_author") else ""
                text = f"[{lm.get('title') or lm['href']}]({lm['href']}){by}"
            elif ann[0] == "b":
                text = f"**{text}**"
        out.append(text)
    return "".join(out)


def fetch_notion(url):
    """Public Notion pages are client-rendered; read their block tree through the page-chunk API."""
    p = urlparse(url)
    api = f"https://{p.netloc}/api/v3"
    page_id = re.search(r"([0-9a-f]{32})", p.path.replace("-", ""))
    if page_id:
        raw = page_id.group(1)
    else:  # vanity slug: the page id is embedded in the server-rendered HTML
        html = curl_get(url).decode("utf-8", errors="replace")
        raw = re.findall(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", html)[-1].replace("-", "")
    pid = f"{raw[:8]}-{raw[8:12]}-{raw[12:16]}-{raw[16:20]}-{raw[20:]}"
    blocks = {}

    def load(root):
        cursor, chunk = {"stack": []}, 0
        while True:
            r = requests.post(f"{api}/loadCachedPageChunk", headers=HEADERS, timeout=60, json={
                "page": {"id": root}, "limit": 500, "cursor": cursor, "chunkNumber": chunk,
                "verticalColumns": False})
            r.raise_for_status()
            d = r.json()
            for k, v in d["recordMap"].get("block", {}).items():
                blocks[k] = v["value"].get("value", v["value"])
            cursor, chunk = d.get("cursor", {"stack": []}), chunk + 1
            if not cursor.get("stack") or chunk > 20:
                break

    load(pid)
    for _ in range(3):  # children the first chunk didn't include (e.g. inside toggles)
        missing = {c for b in blocks.values() for c in b.get("content", [])} - blocks.keys()
        if not missing:
            break
        for i in missing:
            try:
                load(i)
            except (requests.RequestException, ValueError, KeyError):
                pass
    prefix = {"header": "# ", "sub_header": "## ", "sub_sub_header": "### ", "bulleted_list": "- ",
              "numbered_list": "1. ", "to_do": "- [ ] ", "quote": "> ", "toggle": "▸ ", "callout": "> 💡 "}
    lines = []

    def walk(bid, depth):
        b = blocks.get(bid)
        if not b:
            return
        t = b.get("type")
        props = b.get("properties", {})
        text = notion_rich_text(props.get("title"))
        if t == "table_row":
            lines.append("| " + " | ".join(notion_rich_text(v) for v in props.values()) + " |")
        elif t in ("image", "video", "embed", "bookmark", "file", "pdf"):
            src = (b.get("format", {}) or {}).get("display_source") or notion_rich_text(props.get("source"))
            lines.append(f"{'  ' * depth}[{t}: {text or src}]")
        elif t == "divider":
            lines.append("---")
        elif text or t == "page":
            lines.append(("  " * depth if t in ("bulleted_list", "numbered_list", "to_do") else "")
                         + prefix.get(t, "# " if t == "page" and depth == 0 else "") + text)
        for c in b.get("content", []) if (t != "page" or depth == 0) else []:
            walk(c, depth + (1 if t in ("bulleted_list", "numbered_list", "toggle", "to_do") else 0))

    walk(pid, 0)
    return "\n\n".join(lines), "notion-api", True


def fetch_arena(url):
    """ARENA's Streamlit apps are generated from markdown in its GitHub repo; keep each exercise set's
    introduction and learning objectives rather than the full multi-MB exercise text."""
    chapter = re.search(r"arena-(chapter\d)", url).group(1)
    repo = "https://api.github.com/repos/ARENA-education/ARENA_materials/contents"
    dirs = requests.get(repo, headers=HEADERS, timeout=60).json()
    cdir = next(d["name"] for d in dirs if d["name"].startswith(chapter.replace("chapter", "chapter")))
    raw = f"https://raw.githubusercontent.com/ARENA-education/ARENA_materials/main/{cdir}/instructions"
    home = requests.get(f"{raw}/Home.py", headers=HEADERS, timeout=60).text
    parts = ["# ARENA " + cdir, "## Chapter home page", "\n".join(re.findall(r'r"""(.*?)"""', home, re.S))]
    pages = requests.get(f"{repo}/{cdir}/instructions/pages", headers=HEADERS, timeout=60).json()
    for pg in sorted(p["name"] for p in pages if p["name"].endswith(".md")):
        md = requests.get(f"{raw}/pages/{requests.utils.quote(pg)}", headers=HEADERS, timeout=60).text
        intro = re.split(r"\n# 1️⃣|\n# \S*1️⃣", md, maxsplit=1)[0]
        intro = re.sub(r"```.*?```", "", intro, flags=re.S)
        parts += [f"## Exercise set: {pg.removesuffix('.md')}", " ".join(intro.split()[:1800])]
    return "\n\n".join(parts), "github", True


def osf_preprint_download(preprint_id):
    """OSF preprint pages are client-rendered; the API names the preprint's primary file."""
    h = {"User-Agent": UA, "Accept": "application/vnd.api+json"}
    d = requests.get(f"https://api.osf.io/v2/preprints/{preprint_id}/", headers=h, timeout=60).json()["data"]
    f = requests.get(d["relationships"]["primary_file"]["links"]["related"]["href"], headers=h, timeout=60).json()
    return f["data"]["links"]["download"]


def curl_get(url):
    out = subprocess.run(["curl", "-sL", "--compressed", "-A", "Mozilla/5.0", "--max-time", "120", url],
                         capture_output=True)
    if out.returncode != 0 or not out.stdout:
        raise RuntimeError(f"curl failed for {url}")
    return out.stdout


def fetch_url(url):
    p = urlparse(url)
    if "youtube.com" in p.netloc or "youtu.be" in p.netloc:
        return fetch_youtube(url)
    if p.netloc in FORUM_HOSTS and "/posts/" in p.path:
        return fetch_forum_post(url)
    if p.netloc.endswith("notion.site"):
        return fetch_notion(url)
    if p.netloc.startswith("arena-chapter") and p.netloc.endswith("streamlit.app"):
        return fetch_arena(url)
    fetch = url
    if "docs.google.com/document/d/" in url:
        doc_id = url.split("/document/d/")[1].split("/")[0]
        fetch = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    elif "drive.google.com/file/d/" in url:
        fid = url.split("/file/d/")[1].split("/")[0]
        fetch = f"https://drive.google.com/uc?export=download&id={fid}"
    elif "github.com" in p.netloc and "/blob/" in url:
        fetch = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    elif p.netloc == "ar5iv.org" and p.path.startswith("/pdf/"):
        fetch = "https://arxiv.org/pdf/" + p.path.split("/pdf/")[1].removesuffix(".pdf")
    elif p.netloc == "arxiv.org" and p.path.startswith("/abs/"):
        fetch = "https://arxiv.org/pdf/" + p.path.split("/abs/")[1]
    elif p.netloc == "www.dropbox.com":
        fetch = re.sub(r"([?&])dl=0", r"\1dl=1", url)
    elif p.netloc == "osf.io" and p.path.startswith("/preprints/"):
        fetch = osf_preprint_download(p.path.rstrip("/").split("/")[-1])
    try:
        r = requests.get(fetch, headers=HEADERS, timeout=120, allow_redirects=True)
        r.raise_for_status()
        content, ctype = r.content, r.headers.get("content-type", "")
    except requests.HTTPError:
        content, ctype = curl_get(fetch), ""
    if content[:2] == b"\x1f\x8b":
        content = gzip.decompress(content)
    if content[:4] == b"%PDF" or "application/pdf" in ctype:
        txt, pages = pdf_to_text(content)
        return f"<!-- PDF, {pages} pages -->\n\n{txt}", "pdf", True
    text = content.decode("utf-8", errors="replace")
    if "text/plain" in ctype or fetch.endswith(("format=txt", ".md")) or "raw.githubusercontent" in fetch:
        return text, "text", True
    return html_to_markdown(text, url), "html", True


def fetch(only_failed=False):
    links = json.loads((ROOT / "course/links.json").read_text())
    manifest_p = ROOT / "sources/manifest.json"
    manifest = json.loads(manifest_p.read_text()) if manifest_p.exists() else {}
    todo = {}
    for l in links:
        if l["tier"] == "link-only":
            continue
        todo.setdefault(l["sourceKey"], l)
    if only_failed:
        todo = {k: v for k, v in todo.items() if manifest.get(k, {}).get("status") != "ok"}
    (ROOT / "sources").mkdir(exist_ok=True)

    def run(item):
        key, l = item
        try:
            text, method, ok = fetch_url(l["url"])
            words = len(text.split())
            (ROOT / l["sourceFile"]).write_text(f"<!-- source: {l['url']} -->\n\n{text}")
            status = "ok" if ok and words > 150 else "thin"
            return key, {"url": l["url"], "file": l["sourceFile"], "method": method,
                         "words": words, "status": status}
        except Exception as e:  # noqa: BLE001 - record and continue
            return key, {"url": l["url"], "file": l["sourceFile"], "status": "error", "error": str(e)[:300]}

    yt = [i for i in todo.items() if "youtu" in i[1]["url"]]
    rest = [i for i in todo.items() if "youtu" not in i[1]["url"]]
    with cf.ThreadPoolExecutor(8) as ex:
        for key, rec in ex.map(run, rest):
            manifest[key] = rec
            print(f"{rec['status']:5} {rec.get('words', '-'):>7} {rec['url']}", flush=True)
    for item in yt:
        key, rec = run(item)
        manifest[key] = rec
        print(f"{rec['status']:5} {rec.get('words', '-'):>7} {rec['url']}", flush=True)
        time.sleep(3)
    manifest_p.write_text(json.dumps(manifest, indent=1))
    bad = [r for r in manifest.values() if r["status"] != "ok"]
    print(f"\n{len(manifest)} sources, {len(bad)} not ok")
    for r in bad:
        print(f"  {r['status']}: {r['url']} {r.get('error', '')} ({r.get('words')})")


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    if stage in ("scrape", "all"):
        scrape()
    if stage in ("layout", "all"):
        layout()
    if stage in ("fetch", "all"):
        fetch()
    if stage == "refetch":
        fetch(only_failed=True)
