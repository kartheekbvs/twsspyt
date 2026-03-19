import os
extracted_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted"
with open("extracted_files.log", "w", encoding="utf-8") as f_out:
    for f in os.listdir(extracted_dir):
        f_out.write(os.path.join(extracted_dir, f) + "\n")
print("Log written to extracted_files.log")
