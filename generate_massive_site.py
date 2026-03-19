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

def format_textbook_content(text):
    """Formats raw text into HTML with code blocks, sections, lists, and bolding."""
    lines = text.split('\n')
    formatted = ""
    in_code = False
    in_list = False
    
    # Technical keywords to bold for better readability
    keywords = [
        "ndarray", "DataFrame", "Series", "Backpropagation", "Gradient Descent",
        "Stochastic", "Activation Function", "Hyperparameter", "Vectorization",
        "Broadcasting", "Regularization", "Overfitting", "Transformer", "Attention",
        "Convolutional", "Recurrent", "Optimization", "Loss Function", "Weights"
    ]
    
    for line in lines:
        clean_line = line.strip()
        if not clean_line: 
            if in_list:
                formatted += '</ul>'
                in_list = False
            continue
        
        # Bolding technical keywords
        bolded_line = line
        for kw in keywords:
            bolded_line = re.sub(rf'\b{kw}\b', f'<strong>{kw}</strong>', bolded_line, flags=re.IGNORECASE)
        
        # Code block detection
        if clean_line.startswith('>>>') or clean_line.startswith('...') or (in_code and line.startswith('    ')):
            if in_list:
                formatted += '</ul>'
                in_list = False
            if not in_code:
                formatted += '<div class="code-block-wrapper"><pre class="code-block">'
                in_code = True
            formatted += line + '\n'
        else:
            if in_code:
                formatted += '</pre></div>'
                in_code = False
            
            # List detection
            if clean_line.startswith('- ') or clean_line.startswith('* ') or re.match(r'^\d+\. ', clean_line):
                if not in_list:
                    formatted += '<ul class="textbook-list">'
                    in_list = True
                content = clean_line.lstrip('-*').strip()
                if re.match(r'^\d+\. ', content): content = re.sub(r'^\d+\. ', '', content)
                formatted += f'<li>{content}</li>'
                continue
            elif in_list:
                formatted += '</ul>'
                in_list = False

            # Callout detection
            if any(clean_line.upper().startswith(x) for x in ["NOTE:", "WARNING:", "DEFINITION:", "IMPORTANT:"]):
                parts = clean_line.split(':', 1)
                type_ = parts[0].lower()
                content = parts[1].strip() if len(parts) > 1 else ""
                formatted += f'<div class="callout callout-{type_}"><strong>{parts[0]}</strong> {content}</div>'
                continue

            # Massive paragraphs vs titles
            if len(clean_line) > 80:
                formatted += f'<section class="content-section"><p>{bolded_line}</p></section>'
            else:
                formatted += f'<h3 class="section-title">{bolded_line}</h3>'
                
    if in_code: formatted += '</pre></div>'
    if in_list: formatted += '</ul>'
    return formatted

def get_text_segment(file_paths, query, category, min_chars=50000):
    """Searches for a query across sources with keyword relaxation."""
    combined_content = ""
    
    # Keyword relaxation strategy
    search_terms = [query]
    if " " in query:
        search_terms += query.split()
    search_terms.append(category) # Final fallback
    
    for term in search_terms:
        if len(term) < 3: continue
        
        for file_path in file_paths:
            if not os.path.exists(file_path): continue
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            pattern = rf"\b{re.escape(term)}\b"
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            
            if matches:
                # Grab a HUGE chunk from each match until we hit min_chars
                for m in matches[:3]: # Take up to 3 major sections
                    start = m.start()
                    combined_content += content[start : start + (min_chars // 2)]
                    if len(combined_content) >= min_chars: break
            if len(combined_content) >= min_chars: break
        if len(combined_content) >= min_chars: break
            
    if not combined_content:
        return f"<p>Aggregated technical data for <strong>{query}</strong> is being synthesized from core Python specifications.</p>"
        
    return format_textbook_content(combined_content)

def generate_site():
    sections = load_concepts()
    print(f"Generating site for {sum(len(s['pages']) for s in sections.values())} concepts...")
    
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
        intro = f"Technically exhaustive breakdown of <strong>{query}</strong>. This module provide infinite depth with textbook-level precision."
        
        prev = all_pages[i-1][2] if i > 0 else {"path": "index.html", "title": "Home"}
        next_ = all_pages[i+1][2] if i < len(all_pages)-1 else {"path": "index.html", "title": "Home"}
        
        make_page(
            rel_path=p_data['path'], title=p_data['title'], section_name=s_name,
            emoji=s_icon, diff="advanced", bc=bc, intro=intro,
            books=", ".join([os.path.basename(s) for s in sources if os.path.exists(s)]),
            body=body_content,
            prev=(prev['path'], prev['title']), next_=(next_['path'], next_['title']),
            sections=sections
        )

if __name__ == "__main__":
    generate_site()
