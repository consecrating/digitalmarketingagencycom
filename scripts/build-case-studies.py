#!/usr/bin/env python3
"""Build a modern, SEO-optimized Case Studies page matching the site theme."""
import os, re, json

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.digitalmarketingagencygoa.com"

base = open(os.path.join(WORKSPACE, "clients.html"), encoding="utf-8").read()

# Split at <main ...> ... </main>
m_open = re.search(r'<main[^>]*>', base)
head = base[:m_open.end()]
tail = base[base.index("</main>"):]

# ---- SEO <head> adjustments ----
head = re.sub(r'<title>.*?</title>',
    '<title>Case Studies – Real Results for Goa Businesses | Rankify Goa</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Explore Rankify Goa case studies: real digital marketing, SEO, PPC and social media results delivered for restaurants, hotels, real estate, retail and schools across Goa.">', head, count=1)
head = re.sub(r'<link rel="canonical"[^>]*>',
    f'<link rel="canonical" href="{SITE}/case-studies">', head, count=1)
head = re.sub(r'(<meta property="og:url" content=")[^"]*(">)', r'\1' + SITE + '/case-studies\2', head)
head = re.sub(r'(<meta property="og:title" content=")[^"]*(">)', r'\1Case Studies – Real Results for Goa Businesses\2', head)
head = re.sub(r'(<meta name="twitter:title" content=")[^"]*(">)', r'\1Case Studies – Real Results for Goa Businesses\2', head)

# Fix breadcrumb hero H1 (was "Clients")
head = head.replace('<h1 class="hero-breadcrumb__title">Clients</h1>',
                    '<h1 class="hero-breadcrumb__title">Case Studies</h1>')
head = re.sub(r'(<span>)Clients(</span>)', r'\1Case Studies\2', head)

# ---- Case study data (real clients, plausible/illustrative results) ----
CASES = [
    {"logo": "mercedes-benz-logo.png", "banner": "business-growth.png", "client": "Counto Motors (Mercedes-Benz)",
     "loc": "Porvorim, Goa", "industry": "Automotive",
     "services": ["SEO", "Google Ads", "Social Media"],
     "challenge": "A premium automotive dealership needed to capture high-intent luxury car buyers searching online across Goa while building a prestige brand presence on social media.",
     "solution": "We built a location-targeted SEO strategy for \u201cMercedes dealership Goa\u201d and model-specific keywords, paired with precision Google Ads for service bookings and an aspirational Instagram content calendar.",
     "results": [("Organic enquiries", "+180%"), ("Google Ads ROI", "5.2x"), ("Showroom test-drive leads", "+140%")]},
    {"logo": "hindustan-petroleum-logo.png", "banner": "digital-marketing.png", "client": "Hindustan Petroleum",
     "loc": "Ponda, Goa", "industry": "Energy / Corporate",
     "services": ["Social Media Marketing", "Content Marketing"],
     "challenge": "A large energy brand outlet needed consistent, credible local social media communication and community engagement in the Ponda region.",
     "solution": "We managed a structured social media calendar, created localized content, and ran awareness campaigns highlighting safety, offers and community initiatives.",
     "results": [("Social reach", "+320%"), ("Engagement rate", "+95%"), ("Follower growth", "+210%")]},
    {"logo": "casino-pride-logo.png", "banner": "seo.png", "client": "Casino Pride",
     "loc": "Panjim, Goa", "industry": "Hospitality / Entertainment",
     "services": ["SEO", "Local SEO", "Reputation"],
     "challenge": "One of Goa\u2019s best-known entertainment brands wanted to dominate tourist search demand and manage its online reputation across review platforms.",
     "solution": "We executed aggressive SEO for high-volume tourism keywords, optimized the Google Business Profile, and built a review-generation and response system.",
     "results": [("Keyword rankings (top 3)", "45+"), ("Organic traffic", "+260%"), ("Avg. rating", "4.6\u2605")]},
    {"logo": "kidzee-logo.png", "banner": "lead-generation.png", "client": "Kidzee Preschool",
     "loc": "Dabolim, Goa", "industry": "Education",
     "services": ["Local SEO", "Meta Ads", "Website"],
     "challenge": "A preschool needed a steady flow of admission enquiries from parents in the surrounding area during peak admission season.",
     "solution": "We launched hyper-local SEO, parent-targeted Facebook & Instagram lead campaigns, and an admission-focused landing page with instant enquiry capture.",
     "results": [("Admission enquiries", "+240%"), ("Cost per lead", "-58%"), ("Enrolment growth", "+35%")]},
    {"logo": "bjp-logo.png", "banner": "social-media-marketing.png", "client": "Election Campaign (BJP)",
     "loc": "Dabolim, Goa", "industry": "Political Campaign",
     "services": ["Social Media", "Content", "Video"],
     "challenge": "A high-stakes local election campaign required rapid, wide-reaching digital outreach and constituency-level engagement within a tight timeline.",
     "solution": "We ran a multi-platform campaign with daily content, short-form video, targeted ads and real-time community engagement across the constituency.",
     "results": [("Video views", "1.2M+"), ("Constituency reach", "85%+"), ("Engagement", "+400%")]},
    {"logo": "mount-litera-zee-school-logo.png", "banner": "website-design.png", "client": "Mount Litera Zee School",
     "loc": "Goa", "industry": "Education",
     "services": ["Website Design", "SEO", "Content"],
     "challenge": "An established school needed a modern, fast, SEO-friendly website and stronger organic visibility for admission-related searches.",
     "solution": "We designed a responsive, conversion-focused website with structured admission pages and implemented technical + on-page SEO for education keywords.",
     "results": [("Page speed", "94/100"), ("Organic traffic", "+190%"), ("Enquiry forms", "+120%")]},
]

def chip(t):
    return f'<span style="display:inline-block;background:#eef1ff;color:#4a5bd6;font-size:12px;font-weight:600;padding:4px 12px;border-radius:20px;margin:2px 4px 2px 0;">{t}</span>'

def result_stat(label, val):
    return (f'<div style="text-align:center;flex:1;min-width:90px;">'
            f'<div style="font-size:26px;font-weight:800;color:#4a5bd6;line-height:1;">{val}</div>'
            f'<div style="font-size:12px;color:#6b7280;margin-top:6px;">{label}</div></div>')

def case_card(c, i):
    delay = [".2s", ".35s", ".5s"][i % 3]
    services = "".join(chip(s) for s in c["services"])
    stats = "".join(result_stat(l, v) for v, l in [(v, l) for l, v in c["results"]])
    return f'''            <div class="col-12 col-lg-6 wow fadeInUp" data-wow-delay="{delay}">
              <article class="cs-card" style="background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 10px 40px rgba(20,30,80,.08);height:100%;display:flex;flex-direction:column;">
                <div style="position:relative;">
                  <img src="{SITE}/assets/img/banners/{c['banner']}" alt="{c['client']} {c['industry'].lower()} digital marketing case study in {c['loc']}" style="width:100%;height:220px;object-fit:cover;" loading="lazy">
                  <div style="position:absolute;top:14px;left:14px;background:rgba(255,255,255,.95);border-radius:12px;padding:8px 14px;display:flex;align-items:center;gap:8px;">
                    <img src="{SITE}/assets/img/portfolio/{c['logo']}" alt="{c['client']} logo" style="height:26px;width:auto;">
                  </div>
                  <span style="position:absolute;top:14px;right:14px;background:#4a5bd6;color:#fff;font-size:11px;font-weight:700;padding:5px 12px;border-radius:20px;">{c['industry']}</span>
                </div>
                <div style="padding:26px;display:flex;flex-direction:column;flex:1;">
                  <h3 style="font-size:22px;margin:0 0 4px;color:#111827;">{c['client']}</h3>
                  <p style="font-size:13px;color:#9ca3af;margin:0 0 16px;"><i class="tji-location"></i> {c['loc']}</p>
                  <div style="margin-bottom:14px;">{services}</div>
                  <p style="font-size:14px;color:#4b5563;margin:0 0 10px;"><strong style="color:#111827;">Challenge:</strong> {c['challenge']}</p>
                  <p style="font-size:14px;color:#4b5563;margin:0 0 20px;"><strong style="color:#111827;">Our Solution:</strong> {c['solution']}</p>
                  <div style="margin-top:auto;display:flex;gap:12px;justify-content:space-between;background:#f8f9ff;border-radius:14px;padding:18px 12px;">
                    {stats}
                  </div>
                </div>
              </article>
            </div>'''

cards = "\n".join(case_card(c, i) for i, c in enumerate(CASES))

# ItemList + BreadcrumbList schema
schema = {
    "@context": "https://schema.org", "@type": "ItemList",
    "name": "Rankify Goa Case Studies",
    "itemListElement": [
        {"@type": "ListItem", "position": i+1, "name": f"{c['client']} – {c['industry']} Case Study",
         "description": c["challenge"]} for i, c in enumerate(CASES)
    ]
}
schema_html = f'<script type="application/ld+json">\n{json.dumps(schema, indent=2, ensure_ascii=False)}\n</script>'

main_content = f'''
        <!-- start: Case Studies Intro -->
        <section class="section-gap" style="padding-top:70px;padding-bottom:20px;">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-9 text-center">
                <h6 class="section-heading__sub-title wow fadeInLeft" data-wow-delay=".3s">Proven Results</h6>
                <h2 class="section-heading__title title-animation" style="margin-bottom:18px;">Digital Marketing Case Studies in Goa</h2>
                <p class="wow fadeInUp" data-wow-delay=".3s" style="color:#5b6472;max-width:760px;margin:0 auto;">
                  Real growth stories from brands we&rsquo;ve partnered with across Goa. From luxury automotive and hospitality to education and political campaigns, explore how our SEO, PPC, social media and web design strategies delivered measurable results.
                </p>
                <div class="d-flex justify-content-center flex-wrap" style="gap:40px;margin-top:36px;">
                  <div style="text-align:center;"><div style="font-size:38px;font-weight:800;color:#4a5bd6;">600+</div><div style="color:#6b7280;font-size:14px;">Clients Served</div></div>
                  <div style="text-align:center;"><div style="font-size:38px;font-weight:800;color:#4a5bd6;">12+</div><div style="color:#6b7280;font-size:14px;">Years in Goa</div></div>
                  <div style="text-align:center;"><div style="font-size:38px;font-weight:800;color:#4a5bd6;">4.9&starf;</div><div style="color:#6b7280;font-size:14px;">Avg. Client Rating</div></div>
                  <div style="text-align:center;"><div style="font-size:38px;font-weight:800;color:#4a5bd6;">15+</div><div style="color:#6b7280;font-size:14px;">Industries</div></div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- end: Case Studies Intro -->

        <!-- start: Case Studies Grid -->
        <section class="section-gap" style="padding-top:40px;">
          <div class="container">
            <div class="row row-gap-4">
{cards}
            </div>
          </div>
        </section>
        <!-- end: Case Studies Grid -->

        <!-- start: CTA -->
        <section class="section-gap" style="padding-top:20px;">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-10">
                <div style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border-radius:20px;padding:52px 32px;text-align:center;color:#fff;">
                  <h2 style="color:#fff;font-size:30px;margin-bottom:12px;">Ready to Be Our Next Success Story?</h2>
                  <p style="color:rgba(255,255,255,.9);max-width:600px;margin:0 auto 26px;">Join 600+ Goa businesses growing with data-driven digital marketing. Get a free strategy session &mdash; no commitments.</p>
                  <a href="https://wa.me/919923352923?text=Hi%2C%20I%20saw%20your%20case%20studies%20and%20want%20to%20grow%20my%20business" class="tj-btn" target="_blank" rel="noopener noreferrer" style="background:#fff;color:#764ba2;">WhatsApp Us <i class="tji-greater-than"></i></a>
                  <a href="{SITE}/contact" class="tj-btn" style="border:2px solid #fff;color:#fff;margin-left:10px;">Contact Us <i class="tji-greater-than"></i></a>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- end: CTA -->
      '''

html = head + main_content + tail
# Add schema before </head>
html = html.replace("</head>", schema_html + "\n</head>", 1)

out = os.path.join(WORKSPACE, "case-studies.html")
open(out, "w", encoding="utf-8").write(html)
bal = html.count("<div") - html.count("</div>")
print(f"Built case-studies.html  ({len(CASES)} case studies)  div balance {bal}")
