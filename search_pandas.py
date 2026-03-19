import os
file_path = r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\Python for Data Analysis_ Data Wrangling with Pandas, NumPy, and IPython ( PDFDrive ).pdf.txt"
keywords = ["Data Loading", "read_csv", "Handling Missing Values"]

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

matches = []
for i, line in enumerate(lines):
    for kw in keywords:
        if kw in line:
            matches.append((i+1, line.strip()))
            break

for m in matches[:20]:
    print(f"Line {m[0]}: {m[1]}")
