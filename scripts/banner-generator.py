#!/usr/bin/env python3
"""
SEO Banner Generator — Nano Banana Pro Flash (Gemini 3.1 Flash) via Freepik/Magnific API
Generates topic-SPECIFIC, YouTube-thumbnail-style, 1K banner images.
Each image is unique, page-relevant, and saved with SEO keyword-rich filename.
"""
import os, sys, json, time, urllib.request, urllib.error

API_KEY = "MS570b8aa3c8c34c7d9bf9ab86402c9b47"
BASE = "https://api.freepik.com/v1/ai/text-to-image/nano-banana-pro-flash"
WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(WORKSPACE, "assets/img/blog/banners")
os.makedirs(OUT_DIR, exist_ok=True)

# Shared style suffix — YouTube thumbnail aesthetic, consistent brand look
STYLE = ("YouTube thumbnail style banner, 16:9, bold high-contrast composition, "
         "vibrant electric blue and orange brand palette, dramatic cinematic lighting, "
         "clean uncluttered background with copy space on one side, punchy 3D render, "
         "professional, eye-catching, ultra-detailed, no text overlays")


def post(prompt):
    body = json.dumps({"prompt": prompt + ". " + STYLE, "aspect_ratio": "16:9", "resolution": "1K"}).encode()
    req = urllib.request.Request(BASE, data=body, method="POST",
        headers={"x-freepik-api-key": API_KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["data"]["task_id"]


def poll(task_id, tries=25, wait=6):
    for _ in range(tries):
        time.sleep(wait)
        req = urllib.request.Request(f"{BASE}/{task_id}", headers={"x-freepik-api-key": API_KEY})
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


def download(url, path):
    urllib.request.urlretrieve(url, path)
    return os.path.getsize(path)


def generate(filename, prompt):
    """Generate one banner. Returns True on success."""
    out = os.path.join(OUT_DIR, filename)
    if os.path.exists(out) and os.path.getsize(out) > 10000:
        print(f"  ⏭  {filename} (exists)")
        return True
    try:
        tid = post(prompt)
    except urllib.error.HTTPError as e:
        print(f"  ✗ {filename} POST failed: {e.code} {e.read()[:200]}")
        return False
    except Exception as e:
        print(f"  ✗ {filename} POST error: {e}")
        return False
    url = poll(tid)
    if not url:
        print(f"  ✗ {filename} generation failed/timeout")
        return False
    try:
        size = download(url, out)
        print(f"  ✓ {filename} ({size//1024} KB)")
        return True
    except Exception as e:
        print(f"  ✗ {filename} download error: {e}")
        return False


# ── PAGE-SPECIFIC BANNER DEFINITIONS ──────────────────────────────────────────
# (filename, topic-specific prompt) — each unique to its page's actual content
BANNERS = [
    # 3 FEATURED blog posts (shown on blog listing page)
    ("why-seo-important-business-growth-goa.png",
     "A thriving Goa business storefront glowing with a giant upward SEO growth arrow made of golden light rising from a laptop, palm trees and Goa coastline in soft background, symbolizing online business growth"),
    ("top-seo-strategies-businesses-goa.png",
     "A strategic chess board transforming into Google search ranking bars climbing to number 1 position, magnifying glass over a website, Goa map subtly integrated, representing winning SEO strategy"),
    ("attract-customers-online-seo-goa.png",
     "A powerful magnet pulling in crowds of happy customer icons toward a glowing website on a smartphone, Google search bar above, Goa beach vibe, representing attracting customers with SEO"),
]


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "featured"
    print(f"── Generating banners ({which}) ──")
    ok = 0
    for filename, prompt in BANNERS:
        if generate(filename, prompt):
            ok += 1
    print(f"\n✓ {ok}/{len(BANNERS)} banners generated in {OUT_DIR}")


if __name__ == "__main__":
    main()
