#!/usr/bin/env python3
"""Standardize the footer across all blog posts using the rich main-site footer (absolute paths)."""
import re, glob, os

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Extract the full footer element from clients.html
src = open(os.path.join(WS, "clients.html"), encoding="utf-8").read()
m = re.search(r'<footer class="footer[^>]*>.*?</footer>', src, re.S)
footer = m.group(0)

# 2. Convert all relative paths to absolute so it works from /blog/
# assets
footer = re.sub(r'(href|src|action)="\./assets/', r'\1="/assets/', footer)
footer = re.sub(r'(href|src|action)="assets/', r'\1="/assets/', footer)
# subscribe.php
footer = footer.replace('action="subscribe.php"', 'action="/subscribe.php"')
# page links: index.html -> /, name.html -> /name
footer = footer.replace('href="index.html"', 'href="/"')
footer = re.sub(r'href="([a-z0-9][a-z0-9-]*)\.html"', r'href="/\1"', footer)
# sitemap -> human page
footer = footer.replace('href="/sitemap.xml"', 'href="/html-sitemap"')
footer = footer.replace('href="sitemap.xml"', 'href="/html-sitemap"')
# tel/mailto/social/sanctify links are already absolute; leave them

# sanity
bal = footer.count("<div") - footer.count("</div>")
assert bal == 0, f"footer div balance {bal}"

# 3. Replace footer in every blog post
FOOTER_RE = re.compile(r'<footer[^>]*>.*?</footer>', re.S)
done = 0; errs = 0
for f in glob.glob(os.path.join(WS, "blog", "*.html")):
    if f.endswith("index.html"):
        continue
    s = open(f, encoding="utf-8").read()
    if not FOOTER_RE.search(s):
        print(f"  ! no footer: {os.path.basename(f)}"); errs += 1; continue
    new = FOOTER_RE.sub(lambda _: footer, s, count=1)
    fb = new.count("<div") - new.count("</div>")
    if fb != 0:
        print(f"  ⚠ unbalanced ({fb}): {os.path.basename(f)}"); errs += 1; continue
    open(f, "w", encoding="utf-8").write(new)
    done += 1

print(f"Standardized footer on {done} blog posts | errors {errs}")
widgets = re.findall(r'footer__title">([^<]+)', footer)
print("Footer widgets: " + ", ".join(widgets))
