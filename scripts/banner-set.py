#!/usr/bin/env python3
"""
Generate 16 general YouTube-thumbnail banners + 6 supplementary images
via Nano Banana Pro Flash (Freepik/Magnific), 1K, 16:9. Each unique & topic-specific.
"""
import os, json, time, urllib.request, urllib.error

API_KEY = "MS570b8aa3c8c34c7d9bf9ab86402c9b47"
BASE = "https://api.freepik.com/v1/ai/text-to-image/nano-banana-pro-flash"
WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(WORKSPACE, "assets/img/banners")
os.makedirs(OUT, exist_ok=True)

STYLE = ("YouTube thumbnail style, 16:9, bold high-contrast, vibrant electric blue and orange "
         "brand palette, dramatic cinematic lighting, clean background with copy space, punchy 3D render, "
         "professional, eye-catching, ultra-detailed, modern, no text overlays, no watermark")

# 16 GENERAL category banners + 6 supplementary
IMAGES = [
    # --- 16 general category banners ---
    ("seo.png", "Glowing golden number 1 Google search ranking with magnifying glass and upward arrows, website climbing to top of search results"),
    ("digital-marketing.png", "Central rocket launching upward surrounded by floating digital marketing icons - social media, email, search, ads, analytics charts orbiting"),
    ("social-media-marketing.png", "Smartphone bursting with colorful social media engagement - hearts, likes, shares, comments flying out, Instagram and Facebook style icons"),
    ("ppc.png", "Google Ads dashboard with money coins converting from clicks, targeting bullseye with arrow hitting center, ROI growth"),
    ("content-marketing.png", "Glowing pen writing on floating documents that transform into traffic and engagement, blog and video content icons"),
    ("website-design.png", "Modern responsive website mockup on laptop, tablet and phone floating in 3D, clean UI blocks assembling"),
    ("local-seo.png", "Giant Google Maps location pin over a stylized Goa map with glowing business markers, map-pack ranking"),
    ("branding.png", "Brand identity elements assembling - logo, color palette swatches, typography, floating around a glowing brand mark"),
    ("graphic-design.png", "Creative designer toolkit exploding with color - pen tool, shapes, gradients, artistic splashes, vibrant palette"),
    ("email-marketing.png", "Email envelope opening with a burst of engagement, inbox with automated campaign flow arrows and conversion icons"),
    ("analytics.png", "3D analytics dashboard with rising bar charts, line graphs trending up, data visualization glowing, KPI metrics"),
    ("ecommerce.png", "Online shopping cart overflowing with products, glowing buy button, sales growth arrow, e-commerce store on screen"),
    ("lead-generation.png", "Magnet attracting glowing customer leads and contact cards, funnel converting prospects into customers"),
    ("video-marketing.png", "Play button in center with video content and YouTube style engagement, film reel and view counter rising"),
    ("restaurant-marketing.png", "Appetizing gourmet dish with 5-star reviews floating, restaurant storefront glowing, food photography with Goa beach vibe"),
    ("business-growth.png", "Businessperson climbing glowing upward staircase made of growth charts toward a bright target, success and scaling"),
    # --- 6 supplementary ---
    ("about-team.png", "Diverse creative marketing team collaborating around a glowing table with holographic charts, modern office, teamwork energy"),
    ("contact-consultation.png", "Friendly customer support with glowing WhatsApp and phone icons, free consultation concept, handshake of partnership"),
    ("process-strategy.png", "Strategic roadmap with connected milestone steps glowing, chess-like planning pieces, gears turning, workflow"),
    ("cta-growth.png", "Abstract dynamic gradient background with upward motion arrows and light streaks, energetic call-to-action backdrop"),
    ("goa-business.png", "Vibrant Goa cityscape blending beach, palm trees and modern business district with digital connection lines, local business hub"),
    ("faq-support.png", "Glowing question mark surrounded by helpful answer bubbles and lightbulb ideas, knowledge and support concept"),
]


def post(prompt):
    body = json.dumps({"prompt": prompt + ". " + STYLE, "aspect_ratio": "16:9", "resolution": "1K"}).encode()
    req = urllib.request.Request(BASE, data=body, method="POST",
        headers={"x-freepik-api-key": API_KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["data"]["task_id"]


def poll(tid, tries=30, wait=6):
    for _ in range(tries):
        time.sleep(wait)
        req = urllib.request.Request(f"{BASE}/{tid}", headers={"x-freepik-api-key": API_KEY})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                d = json.load(r)["data"]
        except Exception:
            continue
        if d["status"] == "COMPLETED" and d["generated"]:
            return d["generated"][0]
        if d["status"] == "FAILED":
            return None
    return None


def gen(fn, prompt):
    out = os.path.join(OUT, fn)
    if os.path.exists(out) and os.path.getsize(out) > 10000:
        print(f"  skip {fn}")
        return True
    for attempt in range(2):
        try:
            tid = post(prompt)
        except Exception as e:
            print(f"  post-retry {fn}: {e}")
            time.sleep(3); continue
        url = poll(tid)
        if url:
            urllib.request.urlretrieve(url, out)
            print(f"  ok {fn} ({os.path.getsize(out)//1024}KB)")
            return True
        print(f"  retry {fn}")
    print(f"  FAILED {fn}")
    return False


if __name__ == "__main__":
    ok = 0
    for fn, p in IMAGES:
        if gen(fn, p):
            ok += 1
    print(f"\nDONE: {ok}/{len(IMAGES)} images in {OUT}")
