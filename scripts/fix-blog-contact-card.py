#!/usr/bin/env python3
"""Modernize the sidebar contact card — ON-THEME (light/white with brand accents)."""
import re, glob, os

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODERN = '''<div class="side-card side-contact-card">
                    <h4>Talk To Us</h4>
                    <p style="color:#7a869a;font-size:13.5px;margin:-6px 0 18px;">We reply within 24 hours.</p>
                    <a href="tel:+919923352923" style="display:flex;align-items:center;gap:12px;text-decoration:none;margin-bottom:12px;">
                      <span style="width:40px;height:40px;flex:0 0 40px;display:flex;align-items:center;justify-content:center;background:#eef1ff;border-radius:11px;color:#5a63d6;font-size:15px;"><i class="fa-solid fa-phone"></i></span>
                      <span><span style="display:block;color:#9aa3b5;font-size:11px;text-transform:uppercase;letter-spacing:.5px;">Call us</span><span style="color:#1f2937;font-weight:700;font-size:14.5px;">+91 99233-52923</span></span>
                    </a>
                    <a href="mailto:help@digitalmarketingagencygoa.com" style="display:flex;align-items:center;gap:12px;text-decoration:none;margin-bottom:12px;">
                      <span style="width:40px;height:40px;flex:0 0 40px;display:flex;align-items:center;justify-content:center;background:#eef1ff;border-radius:11px;color:#5a63d6;font-size:15px;"><i class="fa-solid fa-envelope"></i></span>
                      <span style="min-width:0;"><span style="display:block;color:#9aa3b5;font-size:11px;text-transform:uppercase;letter-spacing:.5px;">Email</span><span style="color:#1f2937;font-weight:700;font-size:12.5px;word-break:break-all;">help@digitalmarketingagencygoa.com</span></span>
                    </a>
                    <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                      <span style="width:40px;height:40px;flex:0 0 40px;display:flex;align-items:center;justify-content:center;background:#eef1ff;border-radius:11px;color:#5a63d6;font-size:15px;"><i class="fa-solid fa-location-dot"></i></span>
                      <span><span style="display:block;color:#9aa3b5;font-size:11px;text-transform:uppercase;letter-spacing:.5px;">Visit</span><span style="color:#1f2937;font-weight:700;font-size:14.5px;">Vasco da Gama, Goa</span></span>
                    </div>
                    <a href="https://wa.me/919923352923?text=Hi%2C%20I%20have%20a%20question%20about%20digital%20marketing" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:9px;background:#25D366;color:#fff;font-weight:700;padding:14px;border-radius:12px;text-decoration:none;font-size:15px;margin-bottom:10px;"><i class="fa-brands fa-whatsapp" style="font-size:18px;"></i> Chat on WhatsApp</a>
                    <a href="/contact" style="display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;font-weight:700;padding:13px;border-radius:12px;text-decoration:none;font-size:14.5px;">Contact Form <i class="tji-greater-than"></i></a>
                  </div>'''

# Match the current (dark) side-contact-card OR the earlier plain 'Talk To Us' card
CARD_RE = re.compile(
    r'<div class="side-card side-contact-card"[^>]*>.*?</div>(?=\s*</aside>)'
    r'|<div class="side-card">\s*<h4>Talk To Us</h4>.*?</div>(?=\s*</aside>)', re.S)

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
    print(f"Re-themed contact card on {done} posts | no-match {miss}")

if __name__ == "__main__":
    main()
