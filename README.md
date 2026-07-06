# Inkwell — Free PDF Fill, Sign & Edit Tool

A free, private, browser-based PDF editor. Users can add text, tick marks,
signatures, and highlights, merge and reorder pages, and download the result
— all without uploading the file anywhere. Everything runs client-side using
`pdf.js` (rendering) and `pdf-lib` (editing/export), both loaded from a CDN.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole site: landing page **and** the editor tool in one file. Clicking "Open Inkwell" reveals the editor in an overlay — no second page, no broken links. |
| `robots.txt` | Tells search engines they're allowed to crawl the site. |
| `sitemap.xml` | Lists the site for search engines. |
| `LICENSE` | All-rights-reserved license — see note below. |

**This is a single self-contained file.** Earlier versions split the landing
page and the tool into two separate files (`index.html` + `app.html`), which
is what caused the "Open Inkwell button doesn't do anything" bug — the two
files have to sit in the exact same folder for a plain link between them to
work, and it's easy to upload one without the other. The editor is now
embedded directly inside `index.html` and opens in an overlay, so there's
nothing that can go out of sync. Just upload the one file.

Visiting `yoursite.com/#app` opens straight into the editor — useful if you
ever want to link people directly to the tool instead of the landing page.

### A note on minifying this file

I tried producing a minified `index.min.html` and caught a real bug during
testing: because the editor's entire source is embedded inside this file as
a preserved text block (so the overlay can load it), a generic HTML minifier
partially corrupted that embedded block and broke the editor. Rather than
ship something that looked smaller but was quietly broken, I left this file
unminified. In practice this costs you nothing — GitHub Pages, Cloudflare
Pages, and Netlify all serve static files with gzip/Brotli compression
automatically, which shrinks this file for visitors regardless of whether
the source is minified. If you want it minified anyway for a non-static-host
deployment, say so and I'll build a minifier that specifically skips the
embedded block.

## Before you deploy — configuration checklist

1. **Domain**: `index.html`, `robots.txt`, and `sitemap.xml` currently
   reference the placeholder domain `https://useinkwell.com/`. Once you've
   picked your real domain (or are staying on a GitHub Pages URL), replace
   every instance of that placeholder with your actual URL. (Search each
   file for `useinkwell.com`.)
2. **License**: open `LICENSE` and replace `[YOUR NAME OR BUSINESS NAME
   HERE]` and `[YOUR EMAIL HERE]` with your details.
3. **Branding** (optional): colors, fonts, and copy live in the `<style>`
   blocks and body of `index.html`. The CSS variables at the top of each
   `<style>` tag (`--ink`, `--accent`, `--paper`, etc.) re-theme the look
   without touching layout code. `reskin.py` (included) automates this for
   white-label reselling — see that file's header comment.
4. **Analytics** (optional, recommended): if you want visitor numbers, add a
   privacy-friendly analytics snippet (e.g. Plausible or Simple Analytics —
   both are paid but lightweight and don't require a cookie banner in most
   regions) or Google Analytics (free) just before `</head>` in `index.html`.

## No build step

There's nothing to compile or install. This is a plain static HTML file —
"deploying" just means uploading it to a static host. See
`LAUNCH-CHECKLIST.md` for the exact steps.
