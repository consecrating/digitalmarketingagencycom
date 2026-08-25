#!/usr/bin/env python3
"""Transform all blog posts into a full-width 2-column magazine layout with sticky sidebar."""
import os, glob

BLOG = "blog"

OPEN_OLD = '<div class="row justify-content-center"><div class="col-lg-10"><div class="post-details-wrapper">'
OPEN_NEW = '<div class="row g-4 g-lg-5 blog-layout"><div class="col-lg-8"><div class="post-details-wrapper">'

CLOSE_OLD = '    </div></div></div></div></section>'

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

def main():
    changed = 0
    skipped = 0
    for f in glob.glob(f"{BLOG}/*.html"):
        if f.endswith("index.html"):
            continue
        s = open(f, encoding="utf-8").read()
        if 'blog-layout' in s:
            skipped += 1
            continue
        if OPEN_OLD not in s or CLOSE_OLD not in s:
            print(f"  ! pattern not found: {f}")
            continue
        s = s.replace(OPEN_OLD, OPEN_NEW, 1)
        s = s.replace(CLOSE_OLD, SIDEBAR, 1)
        open(f, "w", encoding="utf-8").write(s)
        # balance check
        bal = s.count("<div") - s.count("</div>")
        if bal != 0:
            print(f"  ⚠ UNBALANCED ({bal}): {f}")
        changed += 1
    print(f"Transformed {changed} posts, skipped {skipped} (already done)")

if __name__ == "__main__":
    main()
