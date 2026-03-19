import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")

def get_nav(current_path, sections):
    """Generates the dynamic sidebar HTML based on the concept tree."""
    nav_html = '<div class="nav-items" id="navItems">'
    
    # Prefix for links based on depth (assuming all pages are in sections/file.html)
    p = "../"
    
    for section_name, items in sections.items():
        icon = items.get("icon", "&#x1F4DA;")
        nav_html += f'<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>{icon} {section_name}</span><span class="chevron">&#x25BC;</span></div>'
        nav_html += '<div class="nav-section-items">'
        
        for item in items.get("pages", []):
            item_path = item["path"]
            item_title = item["title"]
            is_master = "masterclass" in item_path
            style = ' style="color:var(--accent);font-weight:700;"' if is_master else ''
            active_class = " active" if item_path == current_path else ""
            
            nav_html += f'<a href="{p}{item_path}" class="nav-item{active_class}"{style}>{item_title}</a>'
            
        nav_html += '</div></div>'
    
    nav_html += '</div>'
    return nav_html

def make_page(rel_path, title, section_name, emoji, diff, bc, intro, books, body, prev, next_, sections, see_also=None):
    fp = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    
    nav_html = get_nav(rel_path, sections)
    css = "../../css/style.css"
    js = "../../js/main.js"
    home = "../../index.html"
    
    # Generate See Also HTML if provided
    see_also_html = ""
    if see_also:
        see_also_html = '<section class="see-also-section"><h3>📚 See Also</h3><div class="see-also-links">'
        for sa_link, sa_title in see_also:
            see_also_html += f'<a href="{sa_link}" class="sa-link">{sa_title}</a>'
        see_also_html += '</div></section>'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - Python Learning Hub</title>
<meta name="description" content="{title} - comprehensive textbook reference with code examples.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
</head>
<body>
<nav class="sidebar" id="sidebar">
<div class="sidebar-header"><a href="{home}" class="logo"><div class="logo-icon">&#x1F40D;</div><div class="logo-text"><span class="logo-title">PyTextbook</span><span class="logo-sub">Complete Reference</span></div></a><button class="sidebar-toggle" id="sidebarToggle">&#x2630;</button></div>
<div class="search-box"><input type="text" id="searchInput" placeholder="&#x1F50D; Search topics..." class="search-input"></div>
{nav_html}
</nav>
<main class="main-content" id="mainContent">
<header class="topbar"><button class="mobile-toggle" id="mobileToggle">&#x2630;</button>
<div class="topbar-breadcrumb"><a href="{home}" style="color:var(--accent);text-decoration:none;">Home</a> &rarr; {bc}</div>
<div class="topbar-progress"><span class="progress-text">Reading</span><div class="progress-bar-wrap"><div class="progress-bar-fill" id="progressFill"></div></div><span id="progressPercent">0%</span></div>
</header>
<div class="page-content">
<div class="page-header">
<span class="topic-badge">{emoji} {section_name}</span>
<h1>{title}</h1>
<p class="page-intro">{intro}</p>
<div style="display:flex;gap:.75rem;margin-top:1rem;flex-wrap:wrap;">
<span class="difficulty-badge {diff}">&#x25CF; {diff.capitalize()}</span>
<span style="font-size:.8rem;color:var(--text-muted);align-self:center;">&#x1F4D6; Based on: <em>{books}</em></span>
</div></div>
{body}
{see_also_html}
</div>
<div class="page-nav">
<a href="{prev[0]}"><span class="nav-direction">&larr; Previous</span><span class="nav-topic">{prev[1]}</span></a>
<a href="{next_[0]}" class="next"><span class="nav-direction">Next &rarr;</span><span class="nav-topic">{next_[1]}</span></a>
</div>
<footer class="footer"><p>&#x1F40D; Python Learning Hub &mdash; Built from leading textbooks for deep understanding</p></footer>
</main>
<script src="{js}"></script>
</body></html>'''
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Created: {rel_path}")

if __name__ == "__main__":
    print("Template module loaded. Dynamic nav ready.")
