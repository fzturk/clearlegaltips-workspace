"""
ClearLegalTips — Markdown → PDF dönüştürücü
Kullanım:
  python generate_pdf.py --input workspace/templates/NDA_Template_2026.md \
                         --output workspace/pdfs/NDA_Template_ClearLegalTips.pdf \
                         --title "Free NDA Template 2026"
Gereksinim: pip install reportlab markdown
"""

import argparse
import os
import re
import sys


def md_to_plain(md_text):
    """Basit Markdown → düz metin dönüşümü (ReportLab için)."""
    text = re.sub(r"^#{1,6}\s+", "", md_text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    return text


def build_pdf_reportlab(input_path, output_path, title):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, HRFlowable
    )

    NAVY = colors.HexColor("#1C2B4A")
    GRAY = colors.HexColor("#555555")

    with open(input_path, encoding="utf-8") as f:
        raw = f.read()

    # YAML front matter'ı atla
    raw = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.DOTALL)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=1 * inch,
        rightMargin=1 * inch,
        topMargin=1 * inch,
        bottomMargin=1 * inch,
    )

    styles = getSampleStyleSheet()
    style_h1 = ParagraphStyle("H1", parent=styles["Heading1"],
                               textColor=NAVY, fontSize=20, spaceAfter=12)
    style_h2 = ParagraphStyle("H2", parent=styles["Heading2"],
                               textColor=NAVY, fontSize=14, spaceAfter=8)
    style_body = ParagraphStyle("Body", parent=styles["Normal"],
                                textColor=GRAY, fontSize=10, leading=15,
                                spaceAfter=6)
    style_disclaimer = ParagraphStyle("Disclaimer", parent=styles["Normal"],
                                      textColor=GRAY, fontSize=8,
                                      borderColor=NAVY, borderWidth=0.5,
                                      borderPadding=6, backColor=colors.HexColor("#F8F6F2"))

    story = []

    # Başlık
    story.append(Paragraph(title, style_h1))
    story.append(Paragraph("ClearLegalTips.com", style_body))
    story.append(HRFlowable(color=NAVY, thickness=1, width="100%"))
    story.append(Spacer(1, 12))

    # İçeriği satır satır işle
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            story.append(Spacer(1, 6))
        elif line.startswith("# "):
            story.append(Paragraph(line[2:], style_h1))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], style_h2))
        elif line.startswith("### "):
            story.append(Paragraph(f"<b>{line[4:]}</b>", style_body))
        else:
            clean = md_to_plain(line)
            story.append(Paragraph(clean, style_body))

    # Footer disclaimer
    story.append(Spacer(1, 24))
    story.append(HRFlowable(color=NAVY, thickness=0.5, width="100%"))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "© 2026 ClearLegalTips.com &nbsp;|&nbsp; clearlegaltips.com<br/>"
        "This document is for informational purposes only and does not constitute legal advice. "
        "Consult a licensed attorney for advice specific to your situation.",
        style_disclaimer,
    ))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.build(story)
    print(f"PDF oluşturuldu: {output_path}")


def build_pdf_fallback(input_path, output_path, title):
    """ReportLab yoksa basit HTML → PDF (weasyprint) veya düz metin."""
    try:
        import weasyprint
        with open(input_path, encoding="utf-8") as f:
            md_text = f.read()
        import markdown
        html_body = markdown.markdown(md_text)
        html = f"""<!DOCTYPE html>
<html><head><meta charset='utf-8'>
<style>
body{{font-family:Arial,sans-serif;color:#333;margin:40px;}}
h1,h2,h3{{color:#1C2B4A;}}
footer{{color:#999;font-size:11px;border-top:1px solid #ccc;margin-top:24px;padding-top:8px;}}
</style></head><body>
<h1>{title}</h1>
{html_body}
<footer>© 2026 ClearLegalTips.com — For informational purposes only. Not legal advice.</footer>
</body></html>"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        weasyprint.HTML(string=html).write_pdf(output_path)
        print(f"PDF oluşturuldu (weasyprint): {output_path}")
    except ImportError:
        txt_path = output_path.replace(".pdf", ".txt")
        with open(input_path, encoding="utf-8") as f:
            content = f.read()
        os.makedirs(os.path.dirname(txt_path), exist_ok=True)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(f"{title}\nClearLegalTips.com\n{'='*60}\n\n{content}")
        print(f"UYARI: PDF kütüphanesi bulunamadı. Metin olarak kaydedildi: {txt_path}")
        print("Kurulum: pip install reportlab")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="ClearLegalTips Document")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"HATA: Dosya bulunamadı: {args.input}")
        sys.exit(1)

    try:
        import reportlab  # noqa
        build_pdf_reportlab(args.input, args.output, args.title)
    except ImportError:
        print("ReportLab bulunamadı, alternatif deneniyor...")
        build_pdf_fallback(args.input, args.output, args.title)


if __name__ == "__main__":
    main()
