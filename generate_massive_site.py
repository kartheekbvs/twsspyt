import os, json, re
from gen_template import make_page

TEXTBOOKS = {
    "Python Fundamentals": r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\_𝐏𝐲𝐭𝐡𝐨𝐧 ! _1706765922.pdf.txt",
    "Object Oriented Programming": r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\_𝐏𝐲𝐭𝐡𝐨𝐧 ! _1706765922.pdf.txt",
    "NumPy": r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\Python for Data Analysis_ Data Wrangling with Pandas, NumPy, and IPython ( PDFDrive ).pdf.txt",
    "Pandas": r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\Python for Data Analysis_ Data Wrangling with Pandas, NumPy, and IPython ( PDFDrive ).pdf.txt",
    "Machine Learning": r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\Learning scikit-learn Machine Learning in Python.pdf.txt",
    "Deep Learning": r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\Deep+Learning+Ian+Goodfellow.pdf.txt"
}

FALLBACKS = [
    r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\Machine Learning with Python Cookbook_ Practical Solutions from Preprocessing to Deep Learning ( PDFDrive.com ).pdf.txt",
    r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\DL DL al is well\extracted\ml_ebook.pdf.txt"
]

def load_concepts():
    with open('py_concepts.json', 'r') as f:
        return json.load(f)

def format_textbook_content(text, category):
    """Formats raw text into a premium web experience with cards, icons, and list detection."""
    # Clean up massive text before processing
    text = re.sub(r'\s+', ' ', text)
    
    # Improved List Detection: Look for ' • ', ' - ', or ' 1. ' in the big text blob
    text = re.sub(r' (•|-|\d+\.) ', r'\n- ', text)
    
    # Split into blocks (Headings vs Paragraphs)
    blocks = re.split(r'(\d+\.\d+\s+[A-Z][^.]{5,50}|[A-Z\s]{10,50}:|\n- )', text)
    
    formatted = ""
    icons = ["&#x1F4D8;", "&#x1F52C;", "&#x1F4CA;", "&#x1F527;", "&#x1F4A1;", "&#x1F4BB;"]
    icon_idx = 0
    in_list = False
    
    keywords = ["ndarray", "DataFrame", "Series", "Convolutional", "Transformer", "Attention", "Broadcasting", "Vectorization"]

    for block in blocks:
        clean_block = block.strip()
        if not clean_block or clean_block == "-": continue
        
        # Bolding
        bolded_block = clean_block
        for kw in keywords:
            bolded_block = re.sub(rf'\b{kw}\b', f'<strong>{kw}</strong>', bolded_block, flags=re.IGNORECASE)

        # List item
        if clean_block.startswith('- '):
            if not in_list:
                formatted += '<ul class="textbook-list">'
                in_list = True
            content = clean_block[2:].strip()
            if content: formatted += f'<li>{content}</li>'
            continue
        elif in_list:
            formatted += '</ul>'
            in_list = False

        # Heading
        is_page_num = re.match(r'^\d+$', clean_block) or (len(clean_block) < 5 and clean_block.isdigit())
        if len(clean_block) < 70 and not is_page_num and (re.match(r'^\d+\.', clean_block) or clean_block.isupper() or ":" in clean_block):
            icon = icons[icon_idx % len(icons)]
            icon_idx += 1
            formatted += f'<h2 class="side-heading">{icon} {bolded_block}</h2>'
            continue

        # Content
        if ">>>" in clean_block or "..." in clean_block:
            formatted += f'<div class="code-block-wrapper"><pre class="code-block">{clean_block}</pre><button class="copy-btn">&#x1F4CB; Copy</button></div>'
        else:
            sentences = re.split(r'(?<=[.!?])\s+', bolded_block)
            formatted += '<div class="content-card">'
            current_p = ""
            for i, sent in enumerate(sentences):
                current_p += sent + " "
                if (i + 1) % 4 == 0 or i == len(sentences) - 1:
                    formatted += f'<p>{current_p.strip()}</p>'
                    current_p = ""
            formatted += '</div>'
            
    if in_list: formatted += '</ul>'
    return formatted

def get_text_segment(file_paths, query, category, min_chars=50000):
    """Searches for a query across sources with exact match prioritization."""
    combined_content = ""
    
    # Strategy: Try EXACT match of query + category first
    search_queries = [f"{query} {category}", query]
    
    for sq in search_queries:
        for file_path in file_paths:
            if not os.path.exists(file_path): continue
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Use regex for whole-phrase matching
            pattern = rf"\b{re.escape(sq)}\b"
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            if matches:
                for m in matches[:5]:
                    start = max(0, m.start() - 500) # Give some context before
                    combined_content += content[start : start + (min_chars // 2)]
                    if len(combined_content) >= min_chars: break
            if len(combined_content) >= min_chars: break
        if len(combined_content) >= min_chars: break

    # Fallback to word-level if still too short
    if len(combined_content) < 5000:
        words = query.split()
        for word in words:
            if len(word) < 4: continue
            for file_path in file_paths:
                if not os.path.exists(file_path): continue
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                matches = list(re.finditer(rf"\b{re.escape(word)}\b", content, re.IGNORECASE))
                for m in matches[:2]:
                    start = m.start()
                    combined_content += content[start : start + 10000]
                if len(combined_content) >= min_chars: break
            if len(combined_content) >= min_chars: break
    
    if not combined_content:
        return f"<p>Detailed concepts for <strong>{query}</strong> are being synthesized.</p>"
    return format_textbook_content(combined_content, category)

def generate_site():
    sections = load_concepts()
    all_pages = []
    for s_name, s_data in sections.items():
        for p in s_data['pages']:
            all_pages.append((s_name, s_data['icon'], p))
            
    for i in range(len(all_pages)):
        s_name, s_icon, p_data = all_pages[i]
        query = p_data['title']
        primary_source = TEXTBOOKS.get(s_name)
        sources = [primary_source] + FALLBACKS if primary_source else FALLBACKS
        
        body_content = get_text_segment(sources, query, s_name)
        bc = f"{s_name} &rarr; {query}"
        intro = f"Premium masterclass on <strong>{query}</strong> with industrial-grade technical depth."
        
        # Navigation logic
        p_raw = all_pages[i-1][2] if i > 0 else {"path": "index.html", "title": "Home"}
        n_raw = all_pages[i+1][2] if i < len(all_pages)-1 else {"path": "index.html", "title": "Home"}
        
        def fix_path(path):
            if path == "index.html": return "../../index.html"
            return "../" + path if "/" in path else path
            
        make_page(
            rel_path=p_data['path'], title=p_data['title'], section_name=s_name,
            emoji=s_icon, diff="advanced", bc=bc, intro=intro,
            books=", ".join([os.path.basename(s) for s in sources if os.path.exists(s)]),
            body=body_content,
            prev=(fix_path(p_raw['path']), p_raw['title']), 
            next_=(fix_path(n_raw['path']), n_raw['title']),
            sections=sections
        )

if __name__ == "__main__":
    generate_site()
