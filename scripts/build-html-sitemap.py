#!/usr/bin/env python3
"""Build a MODERN human-friendly HTML sitemap page matching the site theme."""
import os, re, json, glob

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.digitalmarketingagencygoa.com"

# Reuse header + footer from clients.html (has full theme, relative paths, works at root)
base = open(os.path.join(WORKSPACE, "clients.html"), encoding="utf-8").read()
m_open = re.search(r'<main[^>]*>', base)
head = base[:m_open.end()]
tail = base[base.index("</main>"):]

# SEO head adjustments
head = re.sub(r'<title>.*?</title>', '<title>Sitemap – All Pages & Resources | Rankify Goa</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Browse every page on Rankify Goa – our full sitemap of digital marketing services, locations we serve, industry solutions, guides and blog articles for businesses in Goa.">', head, count=1)
head = re.sub(r'<link rel="canonical"[^>]*>', f'<link rel="canonical" href="{SITE}/html-sitemap">', head, count=1)
head = re.sub(r'(<meta property="og:url" content=")[^"]*(">)', r'\1' + SITE + '/html-sitemap\2', head)
head = head.replace('<h1 class="hero-breadcrumb__title">Clients</h1>', '<h1 class="hero-breadcrumb__title">Sitemap</h1>')
head = re.sub(r'(<span>)Clients(</span>)', r'\1Sitemap\2', head)

# ---- Collect & categorize pages ----
def title_of(path):
    try:
        s = open(path, encoding="utf-8").read()
        m = re.search(r"<title>(.*?)</title>", s, re.S)
        if m:
            return m.group(1).split("|")[0].split(" – Rankify")[0].split(" - Rankify")[0].strip()
    except Exception:
        pass
    return os.path.basename(path).replace(".html", "").replace("-", " ").title()

def clean(slug):
    return "/" if slug == "index" else "/" + slug

root_files = [os.path.basename(f)[:-5] for f in glob.glob(os.path.join(WORKSPACE, "*.html"))
              if not os.path.basename(f).startswith("old")]
blog_files = [os.path.basename(f)[:-5] for f in glob.glob(os.path.join(WORKSPACE, "blog", "*.html"))
              if os.path.basename(f) != "index.html"]

cats = {
    "Main Pages": [], "Core Services": [], "Industry Solutions": [], "Locations We Serve": [],
    "Services by Location": [], "Guides & Comparisons": [], "Tools & Resources": [], "Blog Articles": [],
}
CORE = {"digital-marketing","seo-optimization","social-media-marketing","ppc-advertising","content-marketing","website-design","branding-strategy","graphic-designing","local-seo"}
MAIN = {"index","about","services","contact","clients","case-studies","blog","faq","terms","html-sitemap"}

for slug in root_files:
    if slug in ("404","thank-you","html-sitemap"): 
        if slug != "html-sitemap": continue
    if slug in MAIN:
        cats["Main Pages"].append(slug)
    elif slug in CORE:
        cats["Core Services"].append(slug)
    elif slug.endswith("-digital-marketing-goa"):
        cats["Industry Solutions"].append(slug)
    elif slug.startswith("digital-marketing-") and slug.endswith("-goa") and "for" not in slug and "services" not in slug and "company" not in slug and "packages" not in slug and "pricing" not in slug and "near" not in slug and "consultant" not in slug and "course" not in slug and "jobs" not in slug and "internship" not in slug:
        cats["Locations We Serve"].append(slug)
    elif "-services-" in slug and slug.endswith("-goa"):
        cats["Services by Location"].append(slug)
    elif "-vs-" in slug:
        cats["Guides & Comparisons"].append(slug)
    else:
        cats["Tools & Resources"].append(slug)

for slug in sorted(blog_files):
    cats["Blog Articles"].append("blog/" + slug)

# Icons per category (ranko/tji or fa)
ICONS = {
    "Main Pages": "tji-home", "Core Services": "tji-seo-strategy", "Industry Solutions": "tji-analytics-reporting",
    "Locations We Serve": "tji-location", "Services by Location": "tji-target", "Guides & Comparisons": "tji-book",
    "Tools & Resources": "tji-settings", "Blog Articles": "tji-edit",
}

def link_item(slug):
    label = title_of(os.path.join(WORKSPACE, (slug + ".html")))
    href = clean(slug) if not slug.startswith("blog/") else "/" + slug
    return f'<li><a href="{href}"><span class="dot"></span>{label}</a></li>'

sections = ""
for cat, items in cats.items():
    if not items: continue
    items_sorted = sorted(items, key=lambda s: title_of(os.path.join(WORKSPACE, s + ".html")))
    lis = "\n                  ".join(link_item(s) for s in items_sorted)
    icon = ICONS.get(cat, "tji-greater-than")
    sections += f'''
            <div class="col-12 col-lg-6">
              <div class="sm-card">
                <div class="sm-card__head">
                  <span class="sm-card__icon"><i class="{icon}"></i></span>
                  <h2 class="sm-card__title">{cat}</h2>
                  <span class="sm-card__count">{len(items)}</span>
                </div>
                <ul class="sm-links">
                  {lis}
                </ul>
              </div>
            </div>'''

total = sum(len(v) for v in cats.values())

style = '''
  <style>
    .sitemap-hub{padding:60px 0 40px;}
    .sitemap-hub .lead{text-align:center;max-width:720px;margin:0 auto 44px;color:#5b6472;font-size:17px;line-height:1.7;}
    .sm-card{background:#fff;border:1px solid #eef0f5;border-radius:18px;padding:26px 26px 10px;height:100%;box-shadow:0 10px 34px rgba(20,30,80,.06);transition:box-shadow .3s,transform .3s;}
    .sm-card:hover{box-shadow:0 16px 44px rgba(102,126,234,.14);transform:translateY(-3px);}
    .sm-card__head{display:flex;align-items:center;gap:12px;margin-bottom:16px;padding-bottom:16px;border-bottom:2px solid #f2f4fa;}
    .sm-card__icon{width:44px;height:44px;flex:0 0 44px;display:flex;align-items:center;justify-content:center;border-radius:12px;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;font-size:20px;}
    .sm-card__title{font-size:19px;font-weight:800;color:#111827;margin:0;flex:1;}
    .sm-card__count{background:#eef1ff;color:#4a5bd6;font-size:13px;font-weight:700;padding:4px 12px;border-radius:20px;}
    .sm-links{list-style:none;padding:0;margin:0;column-count:1;}
    .sm-links li{margin:0;}
    .sm-links a{display:flex;align-items:center;gap:10px;color:#48505f;text-decoration:none;font-size:15px;padding:9px 8px;border-radius:9px;transition:all .2s;}
    .sm-links a .dot{width:6px;height:6px;border-radius:50%;background:#c3cae6;flex:0 0 6px;transition:all .2s;}
    .sm-links a:hover{background:#f6f7ff;color:#4a5bd6;}
    .sm-links a:hover .dot{background:#667eea;transform:scale(1.5);}
    .sm-stat{display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;font-weight:700;padding:6px 18px;border-radius:24px;font-size:14px;margin-bottom:8px;}
    @media(min-width:1200px){.sm-links{column-count:2;column-gap:22px;}}
  </style>'''

main_html = f'''
        <section class="sitemap-hub">
          <div class="container">
            <div class="text-center">
              <span class="sm-stat">{total} Pages</span>
              <p class="lead">Everything on Rankify Goa in one place. Explore our digital marketing services, the locations we serve across Goa, industry-specific solutions, in-depth guides and our full blog library.</p>
            </div>
            <div class="row g-4">
{sections}
            </div>
          </div>
        </section>
      '''

# BreadcrumbList schema
schema = {
    "@context":"https://schema.org","@type":"BreadcrumbList",
    "itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},
        {"@type":"ListItem","position":2,"name":"Sitemap","item":f"{SITE}/html-sitemap"},
    ]
}
schema_html = f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'

html = head.replace("</head>", style + "\n" + schema_html + "\n</head>") + main_html + tail
open(os.path.join(WORKSPACE, "html-sitemap.html"), "w", encoding="utf-8").write(html)
bal = html.count("<div") - html.count("</div>")
print(f"Built modern html-sitemap.html — {total} pages across {sum(1 for v in cats.values() if v)} categories | div balance {bal}")
for c,v in cats.items():
    if v: print(f"  {c}: {len(v)}")
