#!/usr/bin/env python3
"""Generate 5 professional portraits of Indian women in modern western office outfits."""
import os, json, time, urllib.request

API_KEY = "MS570b8aa3c8c34c7d9bf9ab86402c9b47"
BASE = "https://api.freepik.com/v1/ai/text-to-image/nano-banana-pro-flash"
WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(WORKSPACE, "assets/img/team")
os.makedirs(OUT, exist_ok=True)

STYLE = ("professional corporate headshot, modern western office outfit, smart formal business attire, "
         "clean modern studio background, soft natural lighting, sharp focus, polished, "
         "confident friendly expression, high quality, photorealistic, tasteful, elegant, "
         "marketing agency team member, upper-body portrait")

PEOPLE = [
    ("team-1.png", "A poised young Indian woman in her mid-20s wearing a tailored navy western business suit with a white shirt, neat long dark hair, warm confident smile, soft blue-grey studio backdrop"),
    ("team-2.png", "A professional young Indian woman around 24 in a modern maroon western blazer and formal blouse, elegant styled hair, friendly approachable smile, light neutral studio backdrop"),
    ("team-3.png", "A confident young Indian woman in her early 20s wearing a beige western pantsuit blazer, sleek hair, subtle smile, soft warm studio backdrop"),
    ("team-4.png", "A stylish young Indian woman around 26 in a charcoal grey western formal blazer with a pastel shirt, shoulder-length hair, bright professional smile, clean light backdrop"),
    ("team-5.png", "A graceful young Indian woman in her mid-20s wearing a teal western office blazer and smart top, neat hair, warm engaging smile, soft gradient studio backdrop"),
]

def post(prompt):
    body = json.dumps({"prompt": prompt + ". " + STYLE, "aspect_ratio": "3:4", "resolution": "1K"}).encode()
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
    for _ in range(2):
        try:
            tid = post(prompt)
        except Exception as e:
            print(f"  post err {fn}: {e}"); time.sleep(3); continue
        url = poll(tid)
        if url:
            urllib.request.urlretrieve(url, out)
            print(f"  ok {fn} ({os.path.getsize(out)//1024}KB)"); return True
        print(f"  retry {fn}")
    print(f"  FAILED {fn}"); return False

if __name__ == "__main__":
    ok = 0
    for fn, p in PEOPLE:
        if gen(fn, p): ok += 1
    print(f"DONE {ok}/{len(PEOPLE)}")
