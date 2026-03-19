import os
extracted_dir = r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted"
for f in os.listdir(extracted_dir):
    print(os.path.join(extracted_dir, f))
