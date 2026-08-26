#!/usr/bin/env python3
"""
Build a REAL paginated blog listing across all 121 posts.
- 12 posts per page
- Root pages: blog.html (page 1), blog-2.html ... blog-N.html
- Working pagination (prev / numbers / next)
- Preserves the existing blog.html layout, sidebar, header, footer
- Absolute URLs so it works at /blog, /blog-2, and /blog/
"""
import os, re

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(WORKSPACE, "blog")
PER_PAGE = 12
SITE = "https://www.digitalmarketingagencygoa.com"

DATES = ["05 JAN 2025","12 JAN 2025","20 JAN 2025","02 FEB 2025","14 FEB 2025",
         "25 FEB 2025","08 MAR 2025","19 MAR 2025","01 APR 2025","15 APR 2025",
         "28 APR 2025","10 MAY 2025","22 MAY 2025","03 JUN 2025","16 JUN 2025"]

# Featured posts first (the 3 originals + comprehensive guide)
FEATURED = [
    "why-seo-important-for-business-growth",
    "top-seo-strategies-for-businesses-in-goa",
    "how-to-attract-more-customers-with-seo",
    "complete-seo-guide-goa-businesses-2025",
]


def extract(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    title = (m.group(1) if m else "Blog Post").split("|")[0].split(" – Rankify")[0].strip()
    m = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    desc = m.group(1).strip() if m else ""
    m = re.search(r"assets/img/banners/([a-z0-9-]+\.png)", s)
    banner = m.group(1) if m else "digital-marketing.png"
    # category from breadcrumb subtitle
    m = re.search(r'section-heading__sub-title">(.*?)</h6>', s, re.S)
    cat = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "Marketing"
    if not cat or len(cat) > 24:
        cat = "Marketing"
    return {"title": title, "desc": desc[:150], "banner": banner, "cat": cat}


def collect():
    posts = {}
    for fn in os.listdir(BLOG_DIR):
        if fn.endswith(".html") and fn != "index.html":
            slug = fn[:-5]
            posts[slug] = extract(os.path.join(BLOG_DIR, fn))
    # order: featured first, then the rest alphabetical
    ordered = []
    for slug in FEATURED:
        if slug in posts:
            ordered.append((slug, posts.pop(slug)))
    for slug in sorted(posts):
        ordered.append((slug, posts[slug]))
    return ordered


def card(slug, p, i):
    delay = [".3s", ".4s", ".5s"][i % 3]
    return f'''                  <div class="blog__single wow fadeInUp" data-wow-delay="{delay}">
                    <div class="blog__single__banner">
                      <a href="{SITE}/blog/{slug}">
                        <img src="{SITE}/assets/img/banners/{p['banner']}" alt="{p['title']}" loading="lazy">
                      </a>
                    </div>
                    <div class="blog__single__content">
                      <ul class="blog__single__content__list">
                        <li><a href="{SITE}/blog" class="blog__single__content__tag">{p['cat']}</a></li>
                        <li class="portfolio__single__content__date"><a href="{SITE}/blog/{slug}">{DATES[i % len(DATES)]}</a></li>
                      </ul>
                      <h4 class="blog__single__title"><a href="{SITE}/blog/{slug}">{p['title']}</a></h4>
                      <p class="blog__single__desc">{p['desc']}</p>
                      <a class="tj-btn-2" href="{SITE}/blog/{slug}">Read More <i class="tji-arrow-right"></i></a>
                    </div>
                  </div>'''


def page_url(n):
    return f"{SITE}/blog" if n == 1 else f"{SITE}/blog-{n}"


def pagination(cur, total):
    li = []
    if cur > 1:
        li.append(f'<li><a class="prev page-numbers" href="{page_url(cur-1)}"><i class="tji-arrow-left"></i></a></li>')
    for n in range(1, total + 1):
        # show first, last, and neighbors
        if n == 1 or n == total or abs(n - cur) <= 2:
            if n == cur:
                li.append(f'<li><span aria-current="page" class="page-numbers current">{n}</span></li>')
            else:
                li.append(f'<li><a class="page-numbers" href="{page_url(n)}">{n}</a></li>')
        elif abs(n - cur) == 3:
            li.append('<li><span class="page-numbers dots">…</span></li>')
    if cur < total:
        li.append(f'<li><a class="next page-numbers" href="{page_url(cur+1)}"><i class="tji-arrow-right"></i></a></li>')
    return ('                <div class="tj-pagination tj-pagination--left d-flex">\n                  <ul>\n'
            + "\n".join("                    " + x for x in li)
            + "\n                  </ul>\n                </div>")


def build():
    posts = collect()
    total_pages = (len(posts) + PER_PAGE - 1) // PER_PAGE
    print(f"{len(posts)} posts -> {total_pages} pages")

    template = open(os.path.join(WORKSPACE, "blog.html"), encoding="utf-8").read()
    # Make all asset + nav links absolute so pages work anywhere
    template = template.replace('href="./assets/', f'href="{SITE}/assets/').replace('src="./assets/', f'src="{SITE}/assets/')
    template = template.replace('href="assets/', f'href="{SITE}/assets/').replace('src="assets/', f'src="{SITE}/assets/')
    for nav in ["index.html","about.html","services.html","contact.html","clients.html","faq.html","terms.html","blog.html",
                "digital-marketing.html","seo-optimization.html","social-media-marketing.html","ppc-advertising.html",
                "content-marketing.html","website-design.html","branding-strategy.html","graphic-designing.html","local-seo.html","sitemap.xml"]:
        clean = "/" if nav == "index.html" else "/" + nav.replace(".html","")
        if nav == "sitemap.xml": clean = "/sitemap.xml"
        template = template.replace(f'href="{nav}"', f'href="{SITE}{clean}"')

    # Pagination block only (NOT the following col-lg-8 close div)
    pag_re = re.compile(r'<div class="tj-pagination tj-pagination--left d-flex">.*?</ul>\s*</div>', re.S)

    for pg in range(1, total_pages + 1):
        chunk = posts[(pg-1)*PER_PAGE: pg*PER_PAGE]
        cards = "\n".join(card(slug, p, i) for i, (slug, p) in enumerate(chunk))
        html = template

        # Replace the cards inside wrapper
        html = re.sub(
            r'<div class="blog__single__wrapper">.*?</div>\s*\n\s*</div>\s*\n\s*<div class="tj-pagination',
            f'<div class="blog__single__wrapper">\n{cards}\n                </div>\n\n                <div class="tj-pagination',
            html, count=1, flags=re.S)

        # Replace pagination
        html = pag_re.sub(pagination(pg, total_pages), html, count=1)

        # Canonical + title per page
        canon = page_url(pg)
        html = re.sub(r'<link rel="canonical"[^>]*>', f'<link rel="canonical" href="{canon}">', html, count=1)
        if pg > 1:
            html = re.sub(r"<title>.*?</title>",
                          f"<title>Digital Marketing Blog – Page {pg} | Rankify Goa</title>", html, count=1, flags=re.S)

        out = "blog.html" if pg == 1 else f"blog-{pg}.html"
        open(os.path.join(WORKSPACE, out), "w", encoding="utf-8").write(html)
        print(f"  ✓ {out} ({len(chunk)} posts)")

    # blog/index.html mirrors page 1
    p1 = open(os.path.join(WORKSPACE, "blog.html"), encoding="utf-8").read()
    open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8").write(p1)
    print("  ✓ blog/index.html (mirror of page 1)")

    return total_pages


if __name__ == "__main__":
    build()
