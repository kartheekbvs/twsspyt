import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path, output_txt):
    doc = fitz.open(pdf_path)
    with open(output_txt, "w", encoding="utf-8") as f:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            f.write(f"--- Page {page_num + 1} ---\n")
            f.write(page.get_text())
    doc.close()

pdf_dir = r"D:\python refer"
output_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted"
os.makedirs(output_dir, exist_ok=True)

pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

for pdf in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf)
    out_path = os.path.join(output_dir, pdf + ".txt")
    print(f"Extracting: {pdf_path}")
    try:
        extract_text_from_pdf(pdf_path, out_path)
    except Exception as e:
        print(f"Error extracting {pdf}: {e}")

print("Batch extraction complete.")
