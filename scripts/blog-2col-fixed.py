#!/usr/bin/env python3
"""CORRECTED 2-column blog transform — anchors sidebar to the CONTENT section closing only."""
import os, glob, re

BLOG = "blog"

OPEN_OLD = '<div class="row justify-content-center"><div class="col-lg-10"><div class="post-details-wrapper">'
OPEN_NEW = '<div class="row g-4 g-lg-5 blog-layout"><div class="col-lg-8"><div class="post-details-wrapper">'

# closing pattern (allow any leading whitespace)
CLOSE_RE = re.compile(r'[ \t]*</div></div></div></div></section>')

SIDEBAR = '''    </div></div>
              <div class="col-lg-4">
                <aside class="blog-sidebar">
                  <div class="side-cta">
                    <h4>Grow Your Business in Goa</h4>
                    <p>Get a free digital marketing strategy session &mdash; no commitments, just honest advice.</p>
                    <a class="cta-wa" href="https://wa.me/919923352923?text=Hi%2C%20I%20need%20help%20growing%20my%20business%20in%20Goa" target="_blank" rel="noopener noreferrer">WhatsApp Us</a>
                  </div>
                  <div class="side-card">
                    <h4>Explore Our Services</h4>
                    <ul class="side-links">
                      <li><a href="/seo-optimization">SEO Optimization</a></li>
                      <li><a href="/local-seo">Local SEO &amp; Google Maps</a></li>
                      <li><a href="/ppc-advertising">PPC &amp; Google Ads</a></li>
                      <li><a href="/social-media-marketing">Social Media Marketing</a></li>
                      <li><a href="/website-design">Website Design</a></li>
                      <li><a href="/content-marketing">Content Marketing</a></li>
                    </ul>
                  </div>
                  <div class="side-card">
                    <h4>Popular Articles</h4>
                    <ul class="side-links">
                      <li><a href="/blog/complete-seo-guide-goa-businesses-2025">Complete SEO Guide for Goa</a></li>
                      <li><a href="/blog/google-maps-ranking-goa-business">Rank Higher on Google Maps</a></li>
                      <li><a href="/blog/instagram-marketing-goa-business">Instagram Marketing Guide</a></li>
                      <li><a href="/blog/whatsapp-marketing-guide-goa">WhatsApp Marketing Guide</a></li>
                      <li><a href="/blog/website-speed-optimization-guide">Speed Up Your Website</a></li>
                    </ul>
                  </div>
                  <div class="side-card">
                    <h4>Talk To Us</h4>
                    <p class="side-contact">
                      <i class="tji-call"></i> <a href="tel:+919923352923">+91 99233-52923</a><br>
                      <i class="tji-mail"></i> <a href="mailto:help@digitalmarketingagencygoa.com">help@digitalmarketingagencygoa.com</a><br>
                      <i class="tji-location"></i> Vasco da Gama, Goa
                    </p>
                    <a class="tj-btn tj-btn--sm" href="/contact" style="margin-top:8px;">Contact Us <i class="tji-greater-than"></i></a>
                  </div>
                </aside>
              </div>
            </div></div></section>'''

def add_css(s):
    if "blog-modern.css" in s:
        return s
    for ref in ['<link rel="stylesheet" href="../assets/css/main.css">',
                '<link rel="stylesheet" href="/assets/css/main.css">',
                '<link rel="stylesheet" href="assets/css/main.css">']:
        if ref in s:
            return s.replace(ref, ref + '\n  <link rel="stylesheet" href="/assets/css/blog-modern.css">', 1)
    return s

def main():
    done = 0; errs = 0
    for f in glob.glob(f"{BLOG}/*.html"):
        if f.endswith("index.html"):
            continue
        s = open(f, encoding="utf-8").read()
        if 'blog-layout' in s:
            continue
        if OPEN_OLD not in s:
            print(f"  ! open not found: {f}"); errs += 1; continue
        # 1. add css link
        s = add_css(s)
        # 2. open -> 2col
        s = s.replace(OPEN_OLD, OPEN_NEW, 1)
        # 3. find the FIRST closing pattern AFTER the content open position
        pos = s.index(OPEN_NEW)
        m = CLOSE_RE.search(s, pos)
        if not m:
            print(f"  ! close not found after open: {f}"); errs += 1; continue
        s = s[:m.start()] + "\n" + SIDEBAR + s[m.end():]
        # 4. balance check
        bal = s.count("<div") - s.count("</div>")
        if bal != 0:
            print(f"  ⚠ UNBALANCED ({bal}): {f}"); errs += 1; continue
        open(f, "w", encoding="utf-8").write(s)
        done += 1
    print(f"Transformed {done} posts correctly | errors {errs}")

if __name__ == "__main__":
    main()
