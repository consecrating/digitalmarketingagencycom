#!/usr/bin/env python3
"""
Integrate the 22 banner images across all landing/blog pages by topic.
Inserts a hero banner image into pages that currently lack one, and
swaps blog placeholder images for category-matched banners.
"""
import os, re

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(WORKSPACE, "blog")

# keyword -> banner filename (order matters: most specific first)
RULES = [
    (("local-seo", "google-maps", "google-business", "google-my-business", "citation", "near-me", "multi-location"), "local-seo.png"),
    (("restaurant", "hotel", "resort", "hospitality", "tourism", "travel"), "restaurant-marketing.png"),
    (("ecommerce", "shopify", "amazon"), "ecommerce.png"),
    (("ppc", "google-ads", "google-shopping", "facebook-ads", "remarketing", "paid"), "ppc.png"),
    (("social-media", "instagram", "facebook", "linkedin", "influencer", "whatsapp", "user-generated"), "social-media-marketing.png"),
    (("video", "youtube"), "video-marketing.png"),
    (("content", "blog-writing", "content-writing", "seo-content"), "content-marketing.png"),
    (("website", "web-development", "web-design", "wordpress", "landing-page", "conversion", "mobile-first", "website-speed", "website-security", "website-redesign"), "website-design.png"),
    (("branding", "brand-identity", "logo"), "branding.png"),
    (("graphic", "social-media-creatives"), "graphic-design.png"),
    (("email",), "email-marketing.png"),
    (("analytics", "reporting", "roi", "google-analytics", "kpi"), "analytics.png"),
    (("lead-generation", "lead"), "lead-generation.png"),
    (("faq",), "faq-support.png"),
    (("technical-seo", "on-page-seo", "off-page-seo", "keyword-research", "link-building", "backlink", "seo-audit", "schema", "core-web-vitals", "featured-snippet", "eeat", "algorithm", "seo-vs", "seo-services", "seo-company", "seo-agency", "seo-expert", "seo-consultant", "seo-packages", "seo-panaji", "seo-margao", "seo-mapusa", "seo-vasco", "seo-calangute", "voice-search", "image-seo", "answer-engine", "geo-seo", "ai-overviews", "zero-click", "international-seo", "seo-trends", "internal-linking", "competitor-analysis"), "seo.png"),
    (("real-estate", "healthcare", "education", "fitness", "wellness", "legal", "finance", "automotive", "salon", "beauty", "construction", "manufacturing", "startup", "small-business"), "business-growth.png"),
    (("digital-marketing", "marketing-agency", "marketing-company", "marketing-agencies", "advertising", "creative-agency", "growth", "internet-marketing", "search-engine-marketing", "performance-marketing", "data-driven", "ai-marketing", "omnichannel", "marketing-funnel", "budget", "personal-branding", "reputation", "crisis", "chatgpt", "sem", "b2b", "app-marketing", "franchise", "event", "wedding", "ngo", "political"), "digital-marketing.png"),
]

DEFAULT = "digital-marketing.png"

# Pages to SKIP (they already have rich custom design)
SKIP = {
    "index.html", "about.html", "services.html", "contact.html", "blog.html",
    "clients.html", "faq.html", "terms.html", "404.html", "thank-you.html",
    "olddigital-marketing.html", "html-sitemap.html",
    "digital-marketing.html", "seo-optimization.html", "social-media-marketing.html",
    "ppc-advertising.html", "content-marketing.html", "website-design.html",
    "branding-strategy.html", "graphic-designing.html", "local-seo.html",
    "why-seo-important-for-business-growth.html", "top-seo-strategies-for-businesses-in-goa.html",
    "how-to-attract-more-customers-with-seo.html",
}

def pick_banner(name):
    n = name.lower()
    for keys, banner in RULES:
        for k in keys:
            if k in n:
                return banner
    return DEFAULT

def alt_for(name):
    base = name.replace(".html", "").replace("-", " ").replace("/", " ").strip()
    return base[:110].capitalize() + " – Rankify Goa"

def integrate_landing(path, name, prefix="assets"):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    if 'assets/img/banners/' in s:
        return False  # already has a banner
    banner = pick_banner(name)
    alt = alt_for(name)
    img_html = (f'\n      <div class="blog-images" style="margin-bottom:28px;">'
                f'<img src="{prefix}/img/banners/{banner}" alt="{alt}" '
                f'style="width:100%;height:auto;border-radius:14px;" loading="lazy"></div>')
    # Insert right after the post-details-wrapper opening div
    marker = '<div class="post-details-wrapper">'
    idx = s.find(marker)
    if idx == -1:
        return False
    insert_at = idx + len(marker)
    s = s[:insert_at] + img_html + s[insert_at:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    return True

def integrate_blog(path, name):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    banner = pick_banner(name)
    alt = alt_for(name)
    # Blog posts reference ../assets/img/blog/blog-1.png as hero; swap to banner
    new = re.sub(r'src="\.\./assets/img/blog/blog-[0-9]\.png"',
                 f'src="../assets/img/banners/{banner}"', s)
    # also handle already-updated featured banners (leave them)
    if new != s:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        return True
    return False

def main():
    root_done = 0
    for fn in sorted(os.listdir(WORKSPACE)):
        if not fn.endswith(".html") or fn in SKIP:
            continue
        if integrate_landing(os.path.join(WORKSPACE, fn), fn, prefix="assets"):
            root_done += 1
    print(f"Landing pages updated: {root_done}")

    blog_done = 0
    for fn in sorted(os.listdir(BLOG_DIR)):
        if not fn.endswith(".html") or fn == "index.html":
            continue
        if integrate_blog(os.path.join(BLOG_DIR, fn), fn):
            blog_done += 1
    print(f"Blog posts updated: {blog_done}")
    print(f"TOTAL: {root_done + blog_done} pages now have banner images")

if __name__ == "__main__":
    main()
