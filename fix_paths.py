import os
import re

root = os.path.dirname(os.path.abspath(__file__))
windows_path = r"C:\Users\DELL\.\gemini\antigravity\scratch\python-textbook-site".replace(".", "") # dodge the regex escape issue

# Simple replacement for the sys.path.insert line
pattern = re.compile(r'import sys; sys\.path\.insert\(0, r?"C:\\Users\\DELL\\.gemini\\antigravity\\scratch\\python-textbook-site"\)')
replacement = 'import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))'

# Also handle cases where sys.path.insert is on its own line
pattern2 = re.compile(r'sys\.path\.insert\(0, r?"C:\\Users\\DELL\\.gemini\\antigravity\\scratch\\python-textbook-site"\)')
replacement2 = 'import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))'

for filename in os.listdir(root):
    if filename.endswith(".py") and filename != "fix_paths.py":
        filepath = os.path.join(root, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = pattern.sub(replacement, content)
        new_content = pattern2.sub(replacement2, new_content)
        
        # Also fix specific open() calls with hardcoded paths
        new_content = new_content.replace(r'C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site', '.')
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed: {filename}")

print("Path fixing complete.")
