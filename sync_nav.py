import os
import re
from gen_template import NAV

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(BASE_DIR, "pages")

def sync_nav():
    print("Starting navigation synchronization...")
    count = 0
    for root, dirs, files in os.walk(PAGES_DIR):
        for file in files:
            if file.endswith(".html"):
                fp = os.path.join(root, file)
                
                # Determine depth for {P} prefix
                rel_to_pages = os.path.relpath(root, PAGES_DIR)
                depth = 0 if rel_to_pages == "." else len(rel_to_pages.split(os.sep))
                prefix = "../" * depth
                
                # Prepare the nav html
                current_nav = NAV.replace("{P}", prefix)
                
                with open(fp, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Regex to find the nav items div and replace its content
                # We look for the start tag and replace everything until the end of the sidebar
                # In this template, the sidebar ends just before <main or </nav>
                pattern = re.compile(r'(<div class="nav-items" id="navItems">).*?(</nav>)', re.DOTALL)
                
                if pattern.search(content):
                    # The current_nav already includes the start tag, so don't add group 1 again
                    new_content = pattern.sub(rf'{current_nav}\n    \2', content)
                    if new_content != content:
                        with open(fp, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"  Updated: {os.path.relpath(fp, BASE_DIR)}")
                        count += 1
                else:
                    print(f"  Warning: Could not find nav pattern in {os.path.relpath(fp, BASE_DIR)}")

    print(f"Navigation sync complete. {count} files updated.")

if __name__ == "__main__":
    sync_nav()
