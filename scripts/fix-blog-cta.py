#!/usr/bin/env python3
"""Replace the outdated bottom CTA block on all blog posts with a modern CTA."""
import re, glob, os

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WA = ("https://wa.me/919923352923?text=Hi%2C%20I%20read%20your%20blog%20and%20"
      "want%20a%20free%20digital%20marketing%20strategy%20session")

MODERN_CTA = (
'<div class="blog-cta" style="margin-top:56px;position:relative;overflow:hidden;'
'background:linear-gradient(135deg,#5b6ef5 0%,#7c3aed 55%,#9333ea 100%);border-radius:24px;'
'padding:52px 36px;text-align:center;color:#fff;box-shadow:0 24px 60px rgba(91,110,245,.35);">'
'<span style="position:absolute;top:-45px;right:-45px;width:190px;height:190px;'
'background:rgba(255,255,255,.08);border-radius:50%;"></span>'
'<span style="position:absolute;bottom:-55px;left:-35px;width:160px;height:160px;'
'background:rgba(255,255,255,.06);border-radius:50%;"></span>'
'<div style="position:relative;z-index:1;">'
'<span style="display:inline-block;background:rgba(255,255,255,.18);padding:7px 16px;'
'border-radius:30px;font-size:12.5px;font-weight:700;letter-spacing:.6px;margin-bottom:18px;">'
'&#128640; GROW WITH RANKIFY GOA</span>'
'<h3 style="color:#fff;font-size:30px;font-weight:800;line-height:1.25;margin:0 0 12px;">'
'Ready to Grow Your Business in Goa?</h3>'
'<p style="color:rgba(255,255,255,.92);font-size:16px;max-width:560px;margin:0 auto 30px;line-height:1.7;">'
'Join 600+ businesses growing with data-driven digital marketing. Get a free strategy session '
'&mdash; no cost, no commitments.</p>'
'<div style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center;">'
f'<a href="{WA}" target="_blank" rel="noopener noreferrer" '
'style="display:inline-flex;align-items:center;gap:9px;background:#25D366;color:#fff;font-weight:700;'
'font-size:16px;padding:15px 30px;border-radius:14px;text-decoration:none;box-shadow:0 8px 24px rgba(37,211,102,.4);">'
'<i class="fa-brands fa-whatsapp" style="font-size:20px;"></i> WhatsApp Us Now</a>'
'<a href="/contact" '
'style="display:inline-flex;align-items:center;gap:9px;background:rgba(255,255,255,.14);'
'border:2px solid rgba(255,255,255,.6);color:#fff;font-weight:700;font-size:16px;padding:15px 30px;'
'border-radius:14px;text-decoration:none;">Get a Free Quote</a>'
'</div>'
'<p style="color:rgba(255,255,255,.72);font-size:13px;margin:24px 0 0;">'
'&#11088; 4.9/5 rating &nbsp;&middot;&nbsp; 600+ clients &nbsp;&middot;&nbsp; 12+ years in Goa</p>'
'</div></div>')

# Matches both variants: same opening div, no nested divs inside, ends at first </div>
CTA_RE = re.compile(
    r'<div style="margin-top:50px;padding:40px;background:linear-gradient\(135deg,#667eea 0%,#764ba2 100%\);'
    r'border-radius:16px;text-align:center;color:#fff;">.*?</div>', re.S)

def main():
    done = 0; miss = 0
    for f in glob.glob(os.path.join(WS, "blog", "*.html")):
        if f.endswith("index.html"):
            continue
        s = open(f, encoding="utf-8").read()
        if not CTA_RE.search(s):
            miss += 1; continue
        new = CTA_RE.sub(lambda _: MODERN_CTA, s, count=1)
        bal = new.count("<div") - new.count("</div>")
        if bal != 0:
            print(f"  ⚠ unbalanced ({bal}): {os.path.basename(f)}"); continue
        open(f, "w", encoding="utf-8").write(new)
        done += 1
    print(f"Modernized CTA on {done} posts | no-match {miss}")

if __name__ == "__main__":
    main()
