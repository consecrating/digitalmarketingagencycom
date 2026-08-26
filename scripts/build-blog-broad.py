#!/usr/bin/env python3
"""
Rebuild blog listing as a BROAD full-width 3-column grid (no sidebar),
matching sanctify.in/category style. Paginated across all 121 posts.
"""
import os, re

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(WORKSPACE, "blog")
PER_PAGE = 12
SITE = "https://www.digitalmarketingagencygoa.com"
DATES = ["05 JAN 2025","12 JAN 2025","20 JAN 2025","02 FEB 2025","14 FEB 2025",
         "25 FEB 2025","08 MAR 2025","19 MAR 2025","01 APR 2025","15 APR 2025",
         "28 APR 2025","10 MAY 2025","22 MAY 2025","03 JUN 2025","16 JUN 2025"]
FEATURED = ["why-seo-important-for-business-growth","top-seo-strategies-for-businesses-in-goa",
            "how-to-attract-more-customers-with-seo","complete-seo-guide-goa-businesses-2025"]


def extract(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    title = (m.group(1) if m else "Blog Post").split("|")[0].split(" – Rankify")[0].strip()
    m = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    desc = (m.group(1).strip() if m else "")[:150]
    m = re.search(r"assets/img/banners/([a-z0-9-]+\.png)", s)
    banner = m.group(1) if m else "digital-marketing.png"
    m = re.search(r'section-heading__sub-title">(.*?)</h6>', s, re.S)
    cat = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "Marketing"
    if not cat or len(cat) > 24:
        cat = "Marketing"
    return {"title": title, "desc": desc, "banner": banner, "cat": cat}


def collect():
    posts = {}
    for fn in os.listdir(BLOG_DIR):
        if fn.endswith(".html") and fn != "index.html":
            posts[fn[:-5]] = extract(os.path.join(BLOG_DIR, fn))
    ordered = []
    for slug in FEATURED:
        if slug in posts:
            ordered.append((slug, posts.pop(slug)))
    for slug in sorted(posts):
        ordered.append((slug, posts[slug]))
    return ordered


def card(slug, p, i):
    delay = [".2s", ".3s", ".4s"][i % 3]
    return f'''                  <div class="col-12 col-md-6 col-xl-4">
                    <div class="blog__single wow fadeInUp" data-wow-delay="{delay}">
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
                    </div>
                  </div>'''


def purl(n):
    return f"{SITE}/blog" if n == 1 else f"{SITE}/blog-{n}"


def pagination(cur, total):
    li = []
    if cur > 1:
        li.append(f'<li><a class="prev page-numbers" href="{purl(cur-1)}"><i class="tji-arrow-left"></i></a></li>')
    for n in range(1, total + 1):
        if n == 1 or n == total or abs(n - cur) <= 2:
            if n == cur:
                li.append(f'<li><span aria-current="page" class="page-numbers current">{n}</span></li>')
            else:
                li.append(f'<li><a class="page-numbers" href="{purl(n)}">{n}</a></li>')
        elif abs(n - cur) == 3:
            li.append('<li><span class="page-numbers dots">…</span></li>')
    if cur < total:
        li.append(f'<li><a class="next page-numbers" href="{purl(cur+1)}"><i class="tji-arrow-right"></i></a></li>')
    inner = "\n".join("                    " + x for x in li)
    return ('              <div class="tj-pagination d-flex justify-content-center" style="margin-top:50px;">\n'
            f'                  <ul>\n{inner}\n                  </ul>\n              </div>')


def section(cards_html, pag_html):
    return f'''        <!-- start: Blog Section -->
        <section class="blog blog--main section-gap">
          <div class="container">
            <div class="row">
              <div class="col-12">
                <div class="row row-gap-4">
{cards_html}
                </div>
{pag_html}
              </div>
            </div>
          </div>
        </section>
        <!-- end: Blog Section -->'''


def build():
    posts = collect()
    total = (len(posts) + PER_PAGE - 1) // PER_PAGE
    print(f"{len(posts)} posts -> {total} pages (broad grid)")

    base = open(os.path.join(WORKSPACE, "blog.html"), encoding="utf-8").read()
    start = base.index("<!-- start: Blog Section -->")
    end = base.index("<!-- end: Blog Section -->") + len("<!-- end: Blog Section -->")
    head, tail = base[:start], base[end:]

    for pg in range(1, total + 1):
        chunk = posts[(pg-1)*PER_PAGE: pg*PER_PAGE]
        cards = "\n".join(card(s, p, i) for i, (s, p) in enumerate(chunk))
        html = head + section(cards, pagination(pg, total)) + tail
        canon = purl(pg)
        html = re.sub(r'<link rel="canonical"[^>]*>', f'<link rel="canonical" href="{canon}">', html, count=1)
        if pg > 1:
            html = re.sub(r"<title>.*?</title>", f"<title>Digital Marketing Blog – Page {pg} | Rankify Goa</title>", html, count=1, flags=re.S)
        out = "blog.html" if pg == 1 else f"blog-{pg}.html"
        open(os.path.join(WORKSPACE, out), "w", encoding="utf-8").write(html)
        # balance check
        o, c = html.count("<div"), html.count("</div>")
        print(f"  ✓ {out} ({len(chunk)} posts) div balance {o-c}")

    open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8").write(
        open(os.path.join(WORKSPACE, "blog.html"), encoding="utf-8").read())
    print("  ✓ blog/index.html")
    return total


if __name__ == "__main__":
    build()
