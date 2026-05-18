"""
ClearLegalTips — ComfyUI Featured Image Generator
Kullanım: python comfyui_generate.py --prompt "..." --output "path/to/image.jpg" [--model ...]
"""
import argparse
import json
import random
import time
import urllib.parse
import urllib.request
import urllib.error
import os
import sys

COMFYUI_URL = "http://127.0.0.1:8000"

DEFAULT_MODEL = "juggernautXL_ragnarokBy.safetensors"
DEFAULT_NEGATIVE = (
    "text, watermark, signature, logo, words, letters, blurry, low quality, "
    "cartoon, anime, people faces, hands, distorted, ugly, bad anatomy, "
    "cluttered background, busy, overexposed, dark, grainy, noisy"
)

# SDXL uyumlu en yakın boyut (1200x630 için)
SDXL_WIDTH = 1216
SDXL_HEIGHT = 640
FINAL_WIDTH = 1200
FINAL_HEIGHT = 630


def build_workflow(prompt: str, negative: str, model: str, seed: int) -> dict:
    return {
        "3": {
            "inputs": {
                "seed": seed,
                "steps": 20,
                "cfg": 7.0,
                "sampler_name": "dpmpp_2m",
                "scheduler": "karras",
                "denoise": 1,
                "model": ["4", 0],
                "positive": ["6", 0],
                "negative": ["7", 0],
                "latent_image": ["5", 0],
            },
            "class_type": "KSampler",
        },
        "4": {
            "inputs": {"ckpt_name": model},
            "class_type": "CheckpointLoaderSimple",
        },
        "5": {
            "inputs": {
                "width": SDXL_WIDTH,
                "height": SDXL_HEIGHT,
                "batch_size": 1,
            },
            "class_type": "EmptyLatentImage",
        },
        "6": {
            "inputs": {"text": prompt, "clip": ["4", 1]},
            "class_type": "CLIPTextEncode",
        },
        "7": {
            "inputs": {"text": negative, "clip": ["4", 1]},
            "class_type": "CLIPTextEncode",
        },
        "8": {
            "inputs": {"samples": ["3", 0], "vae": ["4", 2]},
            "class_type": "VAEDecode",
        },
        "9": {
            "inputs": {
                "filename_prefix": "clt_featured",
                "images": ["8", 0],
            },
            "class_type": "SaveImage",
        },
    }


def queue_prompt(workflow: dict) -> str:
    payload = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(
        f"{COMFYUI_URL}/prompt",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        resp = json.loads(r.read())
    return resp["prompt_id"]


def wait_for_completion(prompt_id: str, timeout: int = 600) -> dict:
    start = time.time()
    dots = 0
    while time.time() - start < timeout:
        with urllib.request.urlopen(
            f"{COMFYUI_URL}/history/{prompt_id}", timeout=10
        ) as r:
            history = json.loads(r.read())
        if prompt_id in history:
            return history[prompt_id]
        dots += 1
        print(f"\rÜretiliyor{'.' * (dots % 4)}   ", end="", flush=True)
        time.sleep(3)
    raise TimeoutError(f"ComfyUI {timeout}s içinde tamamlamadı.")


def download_image(filename: str, subfolder: str = "", img_type: str = "output") -> bytes:
    params = f"filename={urllib.parse.quote(filename)}&subfolder={subfolder}&type={img_type}"
    url = f"{COMFYUI_URL}/view?{params}"
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read()


def resize_to_1200x630(img_bytes: bytes, output_path: str):
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(img_bytes))
        img = img.resize((FINAL_WIDTH, FINAL_HEIGHT), Image.LANCZOS)
        img.save(output_path, "JPEG", quality=92)
        print(f"\nKaydedildi (PIL resize): {output_path}")
    except ImportError:
        # PIL yoksa ham olarak kaydet
        with open(output_path, "wb") as f:
            f.write(img_bytes)
        print(f"\nKaydedildi (raw, PIL yok): {output_path}")
        print(f"Not: Boyut {SDXL_WIDTH}x{SDXL_HEIGHT} — Manuel {FINAL_WIDTH}x{FINAL_HEIGHT}'e yeniden boyutlandırın.")


def main():
    parser = argparse.ArgumentParser(description="ClearLegalTips ComfyUI Image Generator")
    parser.add_argument("--prompt", required=True, help="Pozitif prompt")
    parser.add_argument("--negative", default=DEFAULT_NEGATIVE, help="Negatif prompt")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model dosyası")
    parser.add_argument("--output", required=True, help="Çıktı dosya yolu (.jpg)")
    parser.add_argument("--seed", type=int, default=-1, help="Seed (-1 = rastgele)")
    args = parser.parse_args()

    seed = args.seed if args.seed >= 0 else random.randint(0, 2**32 - 1)
    print(f"Model   : {args.model}")
    print(f"Seed    : {seed}")
    print(f"Boyut   : {FINAL_WIDTH}x{FINAL_HEIGHT}px")
    print(f"Çıktı   : {args.output}")
    print(f"Prompt  : {args.prompt[:80]}...")

    # Bağlantı testi
    try:
        urllib.request.urlopen(f"{COMFYUI_URL}/system_stats", timeout=3)
    except Exception:
        print("\nHATA: ComfyUI bağlanamıyor (http://127.0.0.1:8000).")
        print("ComfyUI'yi başlatın ve tekrar deneyin.")
        sys.exit(1)

    workflow = build_workflow(args.prompt, args.negative, args.model, seed)

    print("\nComfyUI kuyruğuna gönderiliyor...")
    prompt_id = queue_prompt(workflow)
    print(f"Prompt ID: {prompt_id}")

    print("Tamamlanması bekleniyor (CPU'da 3-10 dakika sürebilir)...")
    result = wait_for_completion(prompt_id)

    # Çıktı dosyasını bul
    outputs = result.get("outputs", {})
    img_data = None
    for node_id, node_out in outputs.items():
        if "images" in node_out:
            for img_info in node_out["images"]:
                img_data = download_image(
                    img_info["filename"],
                    img_info.get("subfolder", ""),
                    img_info.get("type", "output"),
                )
                break
        if img_data:
            break

    if not img_data:
        print("\nHATA: ComfyUI çıktı görseli bulunamadı.")
        sys.exit(1)

    # Çıktı dizinini oluştur
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    resize_to_1200x630(img_data, args.output)

    print(f"\n✓ Tamamlandı: {args.output}")
    print(f"\nWordPress'e yüklemek için:")
    print(f'  wp media import "{args.output}" --featured_image --post_id=POST_ID')


if __name__ == "__main__":
    main()
