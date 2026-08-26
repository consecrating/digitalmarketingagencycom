#!/usr/bin/env python3
"""Modernize the 'Talk To Us' sidebar contact card on all blog posts."""
import re, glob, os

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODERN = '''<div class="side-card side-contact-card" style="padding:0;overflow:hidden;border:0;background:#0f172a;">
                    <div style="padding:24px 24px 20px;">
                      <h4 style="color:#fff;border:0;margin:0 0 4px;padding:0;font-size:19px;">Talk To Us</h4>
                      <p style="color:#94a3b8;font-size:13.5px;margin:0 0 18px;">We reply within 24 hours.</p>
                      <a href="tel:+919923352923" style="display:flex;align-items:center;gap:12px;text-decoration:none;margin-bottom:12px;">
                        <span style="width:40px;height:40px;flex:0 0 40px;display:flex;align-items:center;justify-content:center;background:rgba(102,126,234,.18);border-radius:11px;color:#8b9dff;font-size:16px;"><i class="fa-solid fa-phone"></i></span>
                        <span><span style="display:block;color:#64748b;font-size:11px;text-transform:uppercase;letter-spacing:.5px;">Call us</span><span style="color:#e2e8f0;font-weight:600;font-size:14.5px;">+91 99233-52923</span></span>
                      </a>
                      <a href="mailto:help@digitalmarketingagencygoa.com" style="display:flex;align-items:center;gap:12px;text-decoration:none;margin-bottom:12px;">
                        <span style="width:40px;height:40px;flex:0 0 40px;display:flex;align-items:center;justify-content:center;background:rgba(102,126,234,.18);border-radius:11px;color:#8b9dff;font-size:16px;"><i class="fa-solid fa-envelope"></i></span>
                        <span style="min-width:0;"><span style="display:block;color:#64748b;font-size:11px;text-transform:uppercase;letter-spacing:.5px;">Email</span><span style="color:#e2e8f0;font-weight:600;font-size:13px;word-break:break-all;">help@digitalmarketingagencygoa.com</span></span>
                      </a>
                      <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                        <span style="width:40px;height:40px;flex:0 0 40px;display:flex;align-items:center;justify-content:center;background:rgba(102,126,234,.18);border-radius:11px;color:#8b9dff;font-size:16px;"><i class="fa-solid fa-location-dot"></i></span>
                        <span><span style="display:block;color:#64748b;font-size:11px;text-transform:uppercase;letter-spacing:.5px;">Visit</span><span style="color:#e2e8f0;font-weight:600;font-size:14.5px;">Vasco da Gama, Goa</span></span>
                      </div>
                      <a href="https://wa.me/919923352923?text=Hi%2C%20I%20have%20a%20question%20about%20digital%20marketing" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:9px;background:#25D366;color:#fff;font-weight:700;padding:14px;border-radius:12px;text-decoration:none;font-size:15px;margin-bottom:10px;"><i class="fa-brands fa-whatsapp" style="font-size:18px;"></i> Chat on WhatsApp</a>
                      <a href="/contact" style="display:flex;align-items:center;justify-content:center;gap:8px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);color:#fff;font-weight:600;padding:13px;border-radius:12px;text-decoration:none;font-size:14.5px;">Contact Form <i class="tji-greater-than"></i></a>
                    </div>
                  </div>'''

# match the whole 'Talk To Us' side-card (no nested divs inside the original)
CARD_RE = re.compile(r'<div class="side-card">\s*<h4>Talk To Us</h4>.*?</div>(?=\s*</aside>)', re.S)

def main():
    done = 0; miss = 0
    for f in glob.glob(os.path.join(WS, "blog", "*.html")):
        if f.endswith("index.html"):
            continue
        s = open(f, encoding="utf-8").read()
        if not CARD_RE.search(s):
            miss += 1; continue
        new = CARD_RE.sub(lambda _: MODERN, s, count=1)
        bal = new.count("<div") - new.count("</div>")
        if bal != 0:
            print(f"  unbalanced ({bal}): {os.path.basename(f)}"); continue
        open(f, "w", encoding="utf-8").write(new)
        done += 1
    print(f"Modernized contact card on {done} posts | no-match {miss}")

if __name__ == "__main__":
    main()
