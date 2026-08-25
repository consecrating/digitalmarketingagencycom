#!/usr/bin/env python3
"""Replace the broken 'Expert X Services' sidebar widget on all service pages
with a modern lead-magnet CTA card."""
import re, glob

# service label per file (for the lead magnet copy)
LABELS = {
    "digital-marketing.html": "Digital Marketing",
    "olddigital-marketing.html": "Digital Marketing",
    "seo-optimization.html": "SEO",
    "social-media-marketing.html": "Social Media",
    "ppc-advertising.html": "PPC & Google Ads",
    "content-marketing.html": "Content Marketing",
    "website-design.html": "Website",
    "branding-strategy.html": "Branding",
    "graphic-designing.html": "Graphic Design",
    "local-seo.html": "Local SEO",
}

# Match the whole widget-feature-item block
WIDGET_RE = re.compile(
    r'<div class="tj-sidebar-widget widget-feature-item[^"]*">.*?</div>\s*</div>\s*</div>',
    re.S)

def card(label):
    slug = label.replace(" & ", " ").replace(" ", "%20")
    return f'''<div class="tj-sidebar-widget service-leadmagnet" style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border-radius:18px;padding:30px 26px;color:#fff;box-shadow:0 16px 44px rgba(118,75,162,.30);">
                  <span style="display:inline-block;background:rgba(255,255,255,.20);color:#fff;font-size:11px;font-weight:800;letter-spacing:.6px;padding:6px 13px;border-radius:20px;margin-bottom:16px;">&#127873; FREE LEAD MAGNET</span>
                  <h3 style="color:#fff;font-size:22px;font-weight:800;margin:0 0 10px;line-height:1.3;">Free {label} Audit &amp; Strategy Session</h3>
                  <p style="color:rgba(255,255,255,.92);font-size:14.5px;line-height:1.7;margin:0 0 22px;">Get a free {label.lower()} audit for your Goa business. We&rsquo;ll show you exactly what&rsquo;s holding you back &mdash; and how to fix it. No cost, no obligation.</p>
                  <a href="https://wa.me/919923352923?text=Hi%2C%20I%20want%20a%20free%20{slug}%20audit%20for%20my%20business" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:9px;background:#25D366;color:#fff;font-weight:700;padding:15px;border-radius:12px;text-decoration:none;margin-bottom:12px;font-size:15px;"><i class="fa-brands fa-whatsapp" style="font-size:19px;"></i> Get Free Audit on WhatsApp</a>
                  <a href="tel:+919923352923" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#fff;color:#764ba2;font-weight:700;padding:14px;border-radius:12px;text-decoration:none;font-size:15px;"><i class="fa-solid fa-phone"></i> +91 99233-52923</a>
                  <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.22);font-size:13px;color:rgba(255,255,255,.88);text-align:center;">&#11088; Trusted by 600+ businesses across Goa</div>
                </div>'''

def main():
    done = 0
    for f, label in LABELS.items():
        try:
            s = open(f, encoding="utf-8").read()
        except FileNotFoundError:
            print(f"  ! missing: {f}"); continue
        if "widget-feature-item" not in s:
            print(f"  - no widget: {f}"); continue
        new = WIDGET_RE.sub(card(label), s, count=1)
        if new == s:
            print(f"  ! regex no match: {f}"); continue
        bal = new.count("<div") - new.count("</div>")
        if bal != 0:
            print(f"  ⚠ UNBALANCED ({bal}): {f} — skipped"); continue
        open(f, "w", encoding="utf-8").write(new)
        print(f"  ✓ {f} (div balance {bal})")
        done += 1
    print(f"\nUpdated {done} service pages")

if __name__ == "__main__":
    main()
