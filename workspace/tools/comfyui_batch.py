"""
ClearLegalTips — ComfyUI Toplu Featured Image Üretici
Tüm 50 makale için 1200x630px featured image üretir.

Kullanım:
  python comfyui_batch.py --start 131 --end 180
  python comfyui_batch.py --ids 131,132,133
  python comfyui_batch.py --missing  # Sadece görseli olmayan makaleler
"""

import argparse
import json
import os
import random
import sys
import time
import urllib.parse
import urllib.request

COMFYUI_URL = "http://127.0.0.1:8000"
OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), "..", "generated-images"
)
MODEL = "juggernautXL_ragnarokBy.safetensors"

# Her makale için prompt haritası (Post ID → prompt)
ARTICLE_PROMPTS = {
    131: ("pen signing non-disclosure agreement document, confidential stamp, "
          "professional legal desk, navy blue and white", "NDA"),
    132: ("freelancer contractor working at desk with contract document, "
          "professional handshake, modern office", "Independent Contractor"),
    133: ("LLC business formation documents on desk, company seal, "
          "professional office setting", "LLC Operating Agreement"),
    134: ("commercial building exterior keys lease document, "
          "business real estate professional", "Commercial Lease"),
    135: ("house keys on rental agreement document, residential property, "
          "professional real estate setting", "Residential Lease"),
    136: ("bill of sale document with car keys and pen, transaction handshake, "
          "clean professional background", "Bill of Sale"),
    137: ("promissory note document with pen, money and professional desk, "
          "financial agreement", "Promissory Note"),
    138: ("last will and testament document with pen, estate planning, "
          "professional legal setting", "Last Will"),
    139: ("living trust document with family estate symbols, "
          "professional legal planning desk", "Living Trust"),
    140: ("power of attorney legal document with official stamp, "
          "professional law office setting", "General POA"),
    141: ("medical power of attorney document with stethoscope, "
          "healthcare legal document professional setting", "Medical POA"),
    142: ("prenuptial agreement document with wedding rings, "
          "professional legal setting", "Prenup"),
    143: ("eviction notice document with property keys, "
          "landlord tenant legal document professional", "Eviction Notice"),
    144: ("sublease agreement document with apartment keys, "
          "real estate subletting professional setting", "Sublease"),
    145: ("service agreement contract document with handshake, "
          "professional business services", "Service Agreement"),
    146: ("joint venture agreement document with two business partners, "
          "professional corporate setting", "Joint Venture"),
    147: ("partnership agreement document with two handshakes, "
          "professional business partnership", "Partnership Agreement"),
    148: ("child custody agreement document with family silhouette, "
          "professional family law setting", "Child Custody"),
    149: ("consulting agreement document with professional consultant, "
          "business meeting professional setting", "Consulting Agreement"),
    150: ("quitclaim deed property transfer document with house, "
          "real estate legal professional", "Quitclaim Deed"),
    151: ("LLC formation cost calculator on laptop screen, "
          "business startup planning professional", "LLC Cost"),
    152: ("S-Corp versus LLC comparison chart, business tax planning, "
          "financial document professional", "S-Corp vs LLC"),
    153: ("registered agent office professional with mail, "
          "business compliance service", "Registered Agent Cost"),
    154: ("DBA filing document with business name registration stamp, "
          "professional business filing", "DBA Filing"),
    155: ("EIN tax ID number document with IRS logo, "
          "business federal tax registration", "EIN Application"),
    156: ("annual report filing calendar with business documents, "
          "state compliance professional", "Annual Report Fees"),
    157: ("business license application documents with official stamps, "
          "local government professional", "Business License"),
    158: ("foreign qualification certificate document, state business "
          "registration multi-state professional", "Foreign Qualification"),
    159: ("trademark registration certificate with USPTO seal, "
          "intellectual property professional legal", "Trademark Cost"),
    160: ("estate tax calculation document with calculator and property, "
          "financial planning professional", "Estate Tax"),
    161: ("probate court documents with gavel, estate administration "
          "professional legal setting", "Probate Cost"),
    162: ("living trust versus will comparison document, estate planning "
          "decision professional", "Living Trust vs Will"),
    163: ("divorce cost calculator document with legal scales, "
          "family law financial planning", "Divorce Cost"),
    164: ("child support calculation worksheet with family court documents, "
          "professional family law", "Child Support"),
    165: ("small claims court filing documents with courthouse, "
          "affordable legal action professional", "Small Claims Fees"),
    166: ("laptop screen showing LLC online formation steps, "
          "digital business registration process", "Form LLC Online"),
    167: ("IRS EIN online application on computer screen, "
          "federal tax ID digital process", "File EIN Online"),
    168: ("registered agent online service website on laptop, "
          "professional business compliance digital", "RA Online"),
    169: ("online divorce filing on laptop screen with legal documents, "
          "digital uncontested divorce process", "Uncontested Divorce Online"),
    170: ("online legal service website on laptop, professional review "
          "rating stars, digital legal platform", "CompleteCasez Review"),
    171: ("name change legal process documents online, "
          "official identity change professional", "Name Change Online"),
    172: ("living trust creation on laptop screen, digital estate planning "
          "professional online service", "Create Living Trust Online"),
    173: ("trademark application online USPTO portal on laptop, "
          "intellectual property digital filing", "File Trademark Online"),
    174: ("DBA registration online portal on laptop screen, "
          "business name filing digital process", "DBA Online"),
    175: ("legal separation documents with family law professional, "
          "alternative to divorce document", "Legal Separation Online"),
    176: ("US state map with divorce statistics, online divorce "
          "state-specific guide professional", "Online Divorce State Guides"),
    177: ("LLC dissolution documents with closed business, "
          "business wind-down professional legal", "Dissolve LLC Online"),
    178: ("copyright registration certificate with creative work, "
          "US Copyright Office official document", "Copyright Registration"),
    179: ("small claims court eviction notice documents, "
          "landlord legal action professional", "Small Claims Evictions"),
    180: ("landlord accounting spreadsheet with rental property, "
          "financial record-keeping professional", "Landlord Accounting"),
}

NEGATIVE = (
    "text, watermark, signature, logo, words, letters, blurry, low quality, "
    "cartoon, anime, people faces, hands, distorted, ugly, bad anatomy, "
    "cluttered background, busy, overexposed, dark, grainy, noisy, nsfw"
)


def check_comfyui():
    try:
        urllib.request.urlopen(f"{COMFYUI_URL}/system_stats", timeout=3)
        return True
    except Exception:
        return False


def build_workflow(prompt, seed):
    return {
        "3": {"inputs": {"seed": seed, "steps": 20, "cfg": 7.0,
                         "sampler_name": "dpmpp_2m", "scheduler": "karras",
                         "denoise": 1, "model": ["4", 0],
                         "positive": ["6", 0], "negative": ["7", 0],
                         "latent_image": ["5", 0]}, "class_type": "KSampler"},
        "4": {"inputs": {"ckpt_name": MODEL}, "class_type": "CheckpointLoaderSimple"},
        "5": {"inputs": {"width": 1216, "height": 640, "batch_size": 1},
              "class_type": "EmptyLatentImage"},
        "6": {"inputs": {"text": prompt, "clip": ["4", 1]}, "class_type": "CLIPTextEncode"},
        "7": {"inputs": {"text": NEGATIVE, "clip": ["4", 1]}, "class_type": "CLIPTextEncode"},
        "8": {"inputs": {"samples": ["3", 0], "vae": ["4", 2]}, "class_type": "VAEDecode"},
        "9": {"inputs": {"filename_prefix": "clt_featured", "images": ["8", 0]},
              "class_type": "SaveImage"},
    }


def queue_and_wait(workflow, post_id, label):
    payload = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(
        f"{COMFYUI_URL}/prompt", data=payload,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        prompt_id = json.loads(r.read())["prompt_id"]

    print(f"  Post {post_id} ({label}): Kuyrukta [{prompt_id[:8]}...]", end="", flush=True)
    start = time.time()
    while time.time() - start < 900:
        with urllib.request.urlopen(f"{COMFYUI_URL}/history/{prompt_id}", timeout=10) as r:
            hist = json.loads(r.read())
        if prompt_id in hist:
            outputs = hist[prompt_id].get("outputs", {})
            for _, out in outputs.items():
                if "images" in out:
                    return out["images"][0], time.time() - start
        print(".", end="", flush=True)
        time.sleep(8)
    raise TimeoutError("Zaman aşımı")


def download_and_save(img_info, out_path):
    params = (f"filename={urllib.parse.quote(img_info['filename'])}"
              f"&subfolder={img_info.get('subfolder', '')}"
              f"&type={img_info.get('type', 'output')}")
    with urllib.request.urlopen(f"{COMFYUI_URL}/view?{params}", timeout=30) as r:
        data = r.read()

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(data))
        img = img.resize((1200, 630), Image.LANCZOS)
        img.save(out_path, "JPEG", quality=92)
    except ImportError:
        with open(out_path, "wb") as f:
            f.write(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=131)
    parser.add_argument("--end", type=int, default=180)
    parser.add_argument("--ids", help="Virgülle ayrılmış Post ID listesi")
    parser.add_argument("--missing", action="store_true",
                        help="Sadece çıktı dosyası olmayan postlar")
    args = parser.parse_args()

    if not check_comfyui():
        print("HATA: ComfyUI bağlanamıyor (http://127.0.0.1:8000)")
        print("ComfyUI'yi başlatın ve tekrar deneyin.")
        sys.exit(1)

    if args.ids:
        post_ids = [int(x.strip()) for x in args.ids.split(",")]
    else:
        post_ids = list(range(args.start, args.end + 1))

    if args.missing:
        post_ids = [
            pid for pid in post_ids
            if not os.path.exists(
                os.path.join(OUTPUT_DIR, f"post-{pid}-featured.jpg")
            )
        ]

    print(f"Toplam {len(post_ids)} görsel üretilecek.")
    print(f"Model: {MODEL}")
    print(f"Çıktı: {OUTPUT_DIR}")
    print(f"Tahmini süre: {len(post_ids) * 5}-{len(post_ids) * 10} dakika (CPU)")
    print("-" * 60)

    success, failed = [], []
    for i, pid in enumerate(post_ids, 1):
        if pid not in ARTICLE_PROMPTS:
            print(f"  Post {pid}: Prompt bulunamadı, atlanıyor.")
            continue

        prompt_text, label = ARTICLE_PROMPTS[pid]
        # Legal content için prompt zenginleştir
        full_prompt = (
            f"{prompt_text}, professional photography, "
            f"navy blue #1C2B4A color scheme, clean minimalist design, "
            f"no faces, 4K sharp, wide format"
        )
        out_path = os.path.join(OUTPUT_DIR, f"post-{pid}-featured.jpg")

        if os.path.exists(out_path) and not args.missing:
            print(f"  Post {pid} ({label}): Zaten var, atlanıyor.")
            continue

        print(f"\n[{i}/{len(post_ids)}] ", end="")
        try:
            seed = random.randint(0, 2**32 - 1)
            workflow = build_workflow(full_prompt, seed)
            img_info, elapsed = queue_and_wait(workflow, pid, label)
            download_and_save(img_info, out_path)
            elapsed_s = f"{elapsed:.0f}s"
            print(f" ✓ {elapsed_s} → {out_path}")
            success.append(pid)
        except Exception as e:
            print(f" ✗ HATA: {e}")
            failed.append(pid)

    print("\n" + "=" * 60)
    print(f"TAMAMLANDI: {len(success)}/{len(post_ids)} başarılı")
    if failed:
        print(f"BAŞARISIZ: {failed}")
        print("Yeniden denemek için:")
        print(f"  python comfyui_batch.py --ids {','.join(map(str, failed))}")

    print("\nWordPress'e toplu yüklemek için:")
    print("  wp media import workspace/generated-images/post-*.jpg "
          "--path='C:\\Users\\fatih\\Studio\\clearlegaltips'")


if __name__ == "__main__":
    main()
