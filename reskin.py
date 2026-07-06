#!/usr/bin/env python3
"""
reskin.py — white-label Inkwell for a client.

Produces a re-branded copy of index.html: new name, new colors, new domain,
new contact email. Use this to resell the tool to clients under their own
brand without hand-editing HTML each time.

USAGE
-----
1. Edit the CONFIG block below for the client you're building for
   (or copy this file per client and keep a folder of configs).
2. Run:  python3 reskin.py
3. Find the output in  ./output/<slug>-index.html
4. Open it once locally and check the header, hero, and footer show the new
   name and colors before you hand it off or upload it anywhere.

This only reskins index.html. Give each client their own LICENSE file too if
you're selling this as a commercial license — see LICENSE.
"""

import re
import os

# ---------------------------------------------------------------------------
# CONFIG — change this per client
# ---------------------------------------------------------------------------
CONFIG = {
    # Brand name shown in the header/hero/footer. Keep it short — it gets
    # split visually into two parts (bold + colored) like "Ink" + "well".
    "brand_first_half": "Form",
    "brand_second_half": "Flow",

    # Full brand name used in <title>, meta tags, alt text, etc.
    "brand_full": "FormFlow",

    # Live domain this client will deploy to (used in canonical/OG/sitemap
    # tags). Use the real domain once you know it.
    "domain": "https://formflow.example.com",

    # Contact email shown if you add a support link (optional — only used
    # if you wire it into the template yourself).
    "contact_email": "support@formflow.example.com",

    # Color palette — hex values. accent_dark should be a darker shade of
    # accent for hover states.
    "colors": {
        "--ink": "#1f2430",
        "--paper": "#fbfaf7",
        "--paper-deep": "#f1ece0",
        "--accent": "#2f6f5e",
        "--accent-dark": "#1c4a3d",
        "--amber": "#c9853a",
        "--line": "#dcd6c9",
        "--line-soft": "#e9e4d8",
    },

    # Output filename slug, e.g. "formflow" -> output/formflow-index.html
    "slug": "formflow",
}

# ---------------------------------------------------------------------------
SOURCE_FILE = "index.html"
OUTPUT_DIR = "output"


def reskin(config, source_path=SOURCE_FILE, output_dir=OUTPUT_DIR):
    with open(source_path, "r", encoding="utf-8") as f:
        html = f.read()

    original_len = len(html)

    # 1. Swap CSS custom properties (colors) inside every :root block, so we
    #    don't touch color values used elsewhere in the file. There are two
    #    :root blocks in this file: one for the landing page, one inside the
    #    embedded editor's own stylesheet — both need updating.
    def recolor_root_block(match):
        block = match.group(1)
        for var, value in config["colors"].items():
            block = re.sub(
                rf"({re.escape(var)}\s*:\s*)#[0-9a-fA-F]{{3,8}}",
                rf"\g<1>{value}",
                block,
            )
        return ":root{" + block + "}"

    html = re.sub(r":root\{(.*?)\}", recolor_root_block, html, flags=re.DOTALL)

    # 2. Swap the split "Ink" / "well" wordmark wherever it appears as two
    #    tags, e.g. <b>Ink</b><span ...>well</span>
    html = re.sub(
        r"(<b>)Ink(</b>)",
        rf"\g<1>{config['brand_first_half']}\g<2>",
        html,
    )
    html = re.sub(
        r"(<span[^>]*>)well(</span>)",
        rf"\g<1>{config['brand_second_half']}\g<2>",
        html,
    )

    # 3. Swap plain-text occurrences of "Inkwell" (titles, meta, alt text,
    #    JSON-LD, embedded app title) with the full brand name.
    html = html.replace("Inkwell", config["brand_full"])

    # 4. Swap the placeholder domain everywhere it appears.
    html = html.replace("https://useinkwell.com/", config["domain"].rstrip("/") + "/")
    html = html.replace("https://useinkwell.com", config["domain"].rstrip("/"))

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{config['slug']}-index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Wrote {out_path}  ({original_len} -> {len(html)} chars)")
    print("Open it in a browser and check: header wordmark, hero heading, "
          "footer, and button colors before delivering to the client.")


if __name__ == "__main__":
    reskin(CONFIG)
