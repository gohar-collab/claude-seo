#!/usr/bin/env python3
"""
Generate a single PDF from the 5 nonairesumes.com SEO strategy markdown files.
"""

import os
import sys
from pathlib import Path
from datetime import datetime

try:
    import markdown
except ImportError:
    print("Error: markdown required. pip install markdown", file=sys.stderr)
    sys.exit(1)

try:
    from weasyprint import HTML, CSS
except ImportError:
    print("Error: weasyprint required. pip install weasyprint", file=sys.stderr)
    sys.exit(1)

BRAND = {
    "primary": "#1e3a5f",
    "accent": "#b8860b",
    "success": "#2d6a4f",
    "warning": "#d4740e",
    "danger": "#c53030",
    "light_bg": "#faf9f7",
    "grid": "#d6d3cc",
    "muted": "#6b7280",
}

DOCS_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent / "docs" / "strategies" / "nonairesumes"
OUT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent / "pdf"
OUT_DIR.mkdir(exist_ok=True)

FILES_IN_ORDER = [
    ("SEO-STRATEGY.md",          "SEO Strategy"),
    ("COMPETITOR-ANALYSIS.md",   "Competitor Analysis"),
    ("CONTENT-CALENDAR.md",      "Content Calendar"),
    ("IMPLEMENTATION-ROADMAP.md","Implementation Roadmap"),
    ("SITE-STRUCTURE.md",        "Site Structure"),
]

CSS_STYLES = f"""
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');

@page {{
    size: A4;
    margin: 20mm 18mm 20mm 18mm;
    @bottom-center {{
        content: counter(page) " of " counter(pages);
        font-family: Inter, sans-serif;
        font-size: 9pt;
        color: {BRAND['muted']};
    }}
}}

@page :first {{
    margin: 0;
    @bottom-center {{ content: none; }}
}}

* {{ box-sizing: border-box; }}

body {{
    font-family: 'Source Serif 4', 'Times New Roman', serif;
    font-size: 10.5pt;
    line-height: 1.65;
    color: #1a1a2e;
    background: white;
}}

/* ── Title Page ─────────────────────────────────── */
.title-page {{
    background: {BRAND['primary']};
    color: white;
    width: 210mm;
    height: 297mm;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 30mm;
    page-break-after: always;
}}

.title-page .brand {{
    font-family: Inter, sans-serif;
    font-size: 11pt;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: {BRAND['accent']};
    margin-bottom: 16px;
}}

.title-page h1 {{
    font-family: Inter, sans-serif;
    font-size: 32pt;
    font-weight: 700;
    color: white;
    margin: 0 0 12px 0;
    line-height: 1.2;
    border: none;
}}

.title-page .subtitle {{
    font-size: 14pt;
    color: rgba(255,255,255,0.75);
    margin-bottom: 40px;
}}

.title-page .divider {{
    width: 60px;
    height: 3px;
    background: {BRAND['accent']};
    margin: 0 auto 40px;
}}

.title-page .meta {{
    font-family: Inter, sans-serif;
    font-size: 10pt;
    color: rgba(255,255,255,0.6);
    line-height: 1.8;
}}

/* ── TOC Page ────────────────────────────────────── */
.toc-page {{
    page-break-after: always;
    padding: 8mm 0;
}}

.toc-page h2 {{
    font-family: Inter, sans-serif;
    font-size: 18pt;
    color: {BRAND['primary']};
    border-bottom: 3px solid {BRAND['accent']};
    padding-bottom: 8px;
    margin-bottom: 24px;
}}

.toc-item {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid {BRAND['grid']};
}}

.toc-item .toc-title {{
    font-family: Inter, sans-serif;
    font-size: 11pt;
    font-weight: 600;
    color: {BRAND['primary']};
}}

.toc-item .toc-num {{
    font-family: Inter, sans-serif;
    font-size: 9pt;
    color: {BRAND['muted']};
    background: {BRAND['light_bg']};
    padding: 2px 8px;
    border-radius: 12px;
}}

/* ── Section Divider ─────────────────────────────── */
.section-divider {{
    background: {BRAND['primary']};
    color: white;
    padding: 14mm 18mm;
    margin: 0 -18mm;
    page-break-before: always;
    page-break-after: avoid;
}}

.section-divider .section-num {{
    font-family: Inter, sans-serif;
    font-size: 9pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: {BRAND['accent']};
    margin-bottom: 6px;
}}

.section-divider h2 {{
    font-family: Inter, sans-serif;
    font-size: 22pt;
    font-weight: 700;
    color: white;
    margin: 0;
    border: none;
}}

/* ── Content Typography ──────────────────────────── */
.content-body {{
    padding-top: 8mm;
}}

h1 {{
    font-family: Inter, sans-serif;
    font-size: 18pt;
    color: {BRAND['primary']};
    border-bottom: 3px solid {BRAND['accent']};
    padding-bottom: 8px;
    margin-top: 24px;
    margin-bottom: 16px;
}}

h2 {{
    font-family: Inter, sans-serif;
    font-size: 14pt;
    color: {BRAND['primary']};
    margin-top: 28px;
    margin-bottom: 10px;
    padding-bottom: 4px;
    border-bottom: 1px solid {BRAND['grid']};
}}

h3 {{
    font-family: Inter, sans-serif;
    font-size: 11.5pt;
    color: {BRAND['primary']};
    margin-top: 20px;
    margin-bottom: 8px;
}}

h4 {{
    font-family: Inter, sans-serif;
    font-size: 10.5pt;
    color: {BRAND['muted']};
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 16px;
    margin-bottom: 6px;
}}

p {{ margin: 0 0 10px 0; }}

ul, ol {{
    margin: 0 0 12px 0;
    padding-left: 22px;
}}

li {{
    margin-bottom: 4px;
    line-height: 1.55;
}}

/* ── Tables ──────────────────────────────────────── */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 9.5pt;
    font-family: Inter, sans-serif;
}}

thead tr {{
    background: {BRAND['primary']};
    color: white;
}}

thead th {{
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    font-size: 9pt;
}}

tbody tr:nth-child(even) {{
    background: {BRAND['light_bg']};
}}

tbody td {{
    padding: 7px 10px;
    border-bottom: 1px solid {BRAND['grid']};
    vertical-align: top;
}}

/* ── Code / Pre ──────────────────────────────────── */
pre {{
    background: #1a1a2e;
    color: #e2e8f0;
    padding: 14px 16px;
    border-radius: 6px;
    font-size: 8.5pt;
    font-family: 'Courier New', monospace;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    margin: 12px 0;
    line-height: 1.5;
}}

code {{
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    background: #eef2f7;
    color: {BRAND['danger']};
    padding: 1px 4px;
    border-radius: 3px;
}}

pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
    font-size: 8.5pt;
}}

/* ── Blockquote ──────────────────────────────────── */
blockquote {{
    border-left: 4px solid {BRAND['accent']};
    padding: 8px 16px;
    margin: 12px 0;
    background: {BRAND['light_bg']};
    color: {BRAND['muted']};
    font-style: italic;
}}

/* ── Horizontal Rule ─────────────────────────────── */
hr {{
    border: none;
    border-top: 1px solid {BRAND['grid']};
    margin: 20px 0;
}}

/* ── Strong / Em ─────────────────────────────────── */
strong {{ color: {BRAND['primary']}; font-weight: 700; }}
em {{ color: {BRAND['muted']}; }}

/* ── Checkbox items ──────────────────────────────── */
li input[type="checkbox"] {{
    margin-right: 6px;
}}
"""


def md_to_html(md_text: str) -> str:
    """Convert markdown to HTML with extensions."""
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "nl2br"],
    )


def build_title_page() -> str:
    today = datetime.now().strftime("%B %d, %Y")
    return f"""
<div class="title-page">
  <div class="brand">Claude SEO — Strategy Report</div>
  <h1>SEO Strategy<br>nonairesumes.com</h1>
  <div class="subtitle">Human Resume Writing Service</div>
  <div class="divider"></div>
  <div class="meta">
    Prepared: {today}<br>
    Business Type: Career Services · Anti-AI Resume Niche<br>
    Market: Global (AU-based operations)<br>
    Timeline: 12-Month Implementation Roadmap
  </div>
</div>
"""


def build_toc() -> str:
    items_html = ""
    for i, (_, title) in enumerate(FILES_IN_ORDER, 1):
        items_html += f"""
  <div class="toc-item">
    <span class="toc-title">{i}. {title}</span>
    <span class="toc-num">Section {i}</span>
  </div>"""

    return f"""
<div class="toc-page">
  <h2>Table of Contents</h2>
  {items_html}
</div>
"""


def build_section(num: int, title: str, md_content: str) -> str:
    body_html = md_to_html(md_content)
    return f"""
<div class="section-divider">
  <div class="section-num">Section {num}</div>
  <h2>{title}</h2>
</div>
<div class="content-body">
{body_html}
</div>
"""


def generate_pdf(out_path: Path):
    sections_html = ""
    for i, (filename, title) in enumerate(FILES_IN_ORDER, 1):
        fpath = DOCS_DIR / filename
        if not fpath.exists():
            print(f"Warning: {fpath} not found, skipping.", file=sys.stderr)
            continue
        md_text = fpath.read_text(encoding="utf-8")
        sections_html += build_section(i, title, md_text)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SEO Strategy — nonairesumes.com</title>
</head>
<body>
{build_title_page()}
{build_toc()}
{sections_html}
</body>
</html>"""

    print("Generating PDF...", file=sys.stderr)
    HTML(string=full_html).write_pdf(
        str(out_path),
        stylesheets=[CSS(string=CSS_STYLES)],
    )
    print(f"PDF saved: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    out_file = OUT_DIR / "nonairesumes-seo-strategy.pdf"
    generate_pdf(out_file)
    print(str(out_file))
