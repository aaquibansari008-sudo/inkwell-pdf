# Inkwell Launch Checklist

## 1. Create the repository (GitHub, free)

1. Go to github.com, sign up if you don't have an account (free).
2. Click **New repository**. Name it e.g. `inkwell-pdf`. Set it to **Public**
   (required for free GitHub Pages). Don't add a README/license from
   GitHub's template — you already have your own.
3. Click **Add file → Upload files**, drag in: `index.html`, `robots.txt`,
   `sitemap.xml`, `LICENSE`, `README.md`. Commit.

## 2. Turn on GitHub Pages (free hosting)

1. In the repo, go to **Settings → Pages**.
2. Under "Build and deployment", set **Source: Deploy from a branch**,
   **Branch: main**, folder `/ (root)`. Save.
3. Wait 1–2 minutes. GitHub shows you the live URL, something like:
   `https://yourusername.github.io/inkwell-pdf/`
4. Visit that URL — you should see the Inkwell landing page.

## 3. (Optional) Connect a real domain

1. Buy a domain (Namecheap, Porkbun, ~$8–12/year) — e.g. `useinkwell.com`.
2. In the domain's DNS settings, add a `CNAME` record pointing to
   `yourusername.github.io`.
3. Back in GitHub repo **Settings → Pages → Custom domain**, enter your
   domain and save. Check "Enforce HTTPS" once it's available (may take a
   few hours for the certificate).
4. Update the placeholder domain in `index.html`, `robots.txt`, and
   `sitemap.xml` to match (see README step 1), then re-upload those files.

## 4. Test the live site before promoting it

Go through this on the **live URL**, not just locally — on both a desktop
browser and your phone:

- [ ] Landing page loads, no broken images/fonts.
- [ ] Click "Open Inkwell" → the editor opens in the overlay correctly.
- [ ] Upload a real PDF → it renders.
- [ ] Add a text box, type in it, change font/size/color — all apply.
- [ ] Drag a text box, a signature box, and a tick box to new positions.
- [ ] Resize a box using its handle.
- [ ] Draw a signature and place it.
- [ ] Add a tick mark.
- [ ] Add 2–3 blank pages at once.
- [ ] Merge in a second PDF.
- [ ] Set a custom file name and download — open the downloaded file and
      confirm everything you added is actually in it.
- [ ] On your phone: tap to select/drag a box, double-tap to type, confirm
      the keyboard stays open while typing and the page doesn't jump.
- [ ] Test in at least two browsers (e.g. Chrome + Safari) since PDF
      rendering can behave slightly differently between them.

## 5. Submit to Google (free)

1. Go to **Google Search Console** (search.google.com/search-console), sign
   in with a Google account.
2. Add your property (the domain or GitHub Pages URL).
3. Verify ownership (Search Console gives you a few methods — for GitHub
   Pages, the HTML file upload or DNS TXT record methods both work).
4. Once verified, use **URL inspection** → paste your homepage URL →
   **Request indexing**.
5. Under **Sitemaps**, submit `sitemap.xml`.
6. Indexing typically takes anywhere from a few hours to a couple of weeks
   — there's no way to force it faster for free.

## 6. Promote it (free channels, low effort)

See `LAUNCH-POSTS.md` for ready-to-use copy for:
- Product Hunt
- Reddit (r/software, r/productivity, r/InternetIsBeautiful)
- Indie Hackers

Post each once, space them out over a few days rather than all at once, and
reply to comments — that's what actually drives the follow-on traffic, not
the post itself.
