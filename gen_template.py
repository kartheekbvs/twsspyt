
import os, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")

NAV = '''<div class="nav-items" id="navItems">
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F40D; Python Fundamentals</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}python/introduction.html" class="nav-item">Introduction</a>
<a href="{P}python/variables-datatypes.html" class="nav-item">Variables &amp; Data Types</a>
<a href="{P}python/operators.html" class="nav-item">Operators</a>
<a href="{P}python/control-flow.html" class="nav-item">Control Flow</a>
<a href="{P}python/loops.html" class="nav-item">Loops</a>
<a href="{P}python/functions.html" class="nav-item">Functions</a>
<a href="{P}python/strings.html" class="nav-item">Strings</a>
<a href="{P}python/lists.html" class="nav-item">Lists</a>
<a href="{P}python/tuples.html" class="nav-item">Tuples</a>
<a href="{P}python/dictionaries.html" class="nav-item">Dictionaries</a>
<a href="{P}python/sets.html" class="nav-item">Sets</a>
<a href="{P}python/file-io.html" class="nav-item">File I/O</a>
<a href="{P}python/exceptions.html" class="nav-item">Exception Handling</a>
<a href="{P}python/modules.html" class="nav-item">Modules &amp; Packages</a>
</div></div>
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F3D7;&#xFE0F; OOP</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}oop/classes-objects.html" class="nav-item">Classes &amp; Objects</a>
<a href="{P}oop/inheritance.html" class="nav-item">Inheritance</a>
<a href="{P}oop/polymorphism.html" class="nav-item">Polymorphism</a>
<a href="{P}oop/encapsulation.html" class="nav-item">Encapsulation</a>
<a href="{P}oop/magic-methods.html" class="nav-item">Magic Methods</a>
<a href="{P}oop/decorators.html" class="nav-item">Decorators</a>
</div></div>
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x26A1; Advanced Python</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}advanced/generators.html" class="nav-item">Generators &amp; Iterators</a>
<a href="{P}advanced/comprehensions.html" class="nav-item">Comprehensions</a>
<a href="{P}advanced/lambda.html" class="nav-item">Lambda &amp; Functional</a>
<a href="{P}advanced/context-managers.html" class="nav-item">Context Managers</a>
<a href="{P}advanced/async.html" class="nav-item">Async &amp; Await</a>
</div></div>
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F522; NumPy</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}numpy/arrays.html" class="nav-item">Arrays &amp; ndarray</a>
<a href="{P}numpy/operations.html" class="nav-item">Array Operations</a>
<a href="{P}numpy/indexing.html" class="nav-item">Indexing &amp; Slicing</a>
<a href="{P}numpy/reshaping.html" class="nav-item">Reshaping &amp; Stacking</a>
<a href="{P}numpy/math-functions.html" class="nav-item">Math Functions</a>
<a href="{P}numpy/linear-algebra.html" class="nav-item">Linear Algebra</a>
<a href="{P}numpy/random.html" class="nav-item">Random Module</a>
</div></div>
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F43C; Pandas</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}pandas/series-dataframe.html" class="nav-item">Series &amp; DataFrame</a>
<a href="{P}pandas/reading-data.html" class="nav-item">Reading Data</a>
<a href="{P}pandas/selection.html" class="nav-item">Selection &amp; Filtering</a>
<a href="{P}pandas/cleaning.html" class="nav-item">Data Cleaning</a>
<a href="{P}pandas/groupby.html" class="nav-item">GroupBy &amp; Aggregation</a>
<a href="{P}pandas/merging.html" class="nav-item">Merging &amp; Joining</a>
<a href="{P}pandas/visualization.html" class="nav-item">Visualization</a>
</div></div>
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F916; Machine Learning</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}ml/intro-ml.html" class="nav-item">Introduction to ML</a>
<a href="{P}ml/linear-regression.html" class="nav-item">Linear Regression</a>
<a href="{P}ml/logistic-regression.html" class="nav-item">Logistic Regression</a>
<a href="{P}ml/decision-trees.html" class="nav-item">Decision Trees</a>
<a href="{P}ml/random-forest.html" class="nav-item">Random Forest</a>
<a href="{P}ml/svm.html" class="nav-item">Support Vector Machine</a>
<a href="{P}ml/knn.html" class="nav-item">K-Nearest Neighbors</a>
<a href="{P}ml/clustering.html" class="nav-item">K-Means Clustering</a>
<a href="{P}ml/model-evaluation.html" class="nav-item">Model Evaluation</a>
<a href="{P}ml/preprocessing.html" class="nav-item">Data Preprocessing</a>
</div></div>
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F9E0; Deep Learning</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}dl/neural-networks.html" class="nav-item">Neural Networks</a>
<a href="{P}dl/backpropagation.html" class="nav-item">Backpropagation</a>
<a href="{P}dl/cnn.html" class="nav-item">CNN</a>
<a href="{P}dl/rnn-lstm.html" class="nav-item">RNN &amp; LSTM</a>
<a href="{P}dl/transformers.html" class="nav-item">Transformers</a>
</div></div>
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F4CA; Data Analysis</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}data/exploratory.html" class="nav-item">Exploratory Data Analysis</a>
<a href="{P}data/feature-engineering.html" class="nav-item">Feature Engineering</a>
<a href="{P}data/matplotlib.html" class="nav-item">Matplotlib</a>
<a href="{P}data/seaborn.html" class="nav-item">Seaborn</a>
<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F4DA; Resources</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}resources/python-programs.html" class="nav-item">140+ Python Programs</a>
</div></div></div></div></div>'''

def make_page(rel_path, title, section, emoji, diff, bc, intro, books, body, prev, next_):
    fp = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    nav = NAV.replace("{P}", "../")
    css = "../../css/style.css"
    js = "../../js/main.js"
    home = "../../index.html"
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
{nav}
</nav>
<main class="main-content" id="mainContent">
<header class="topbar"><button class="mobile-toggle" id="mobileToggle">&#x2630;</button>
<div class="topbar-breadcrumb"><a href="{home}" style="color:var(--accent);text-decoration:none;">Home</a> &rarr; {bc}</div>
<div class="topbar-progress"><span class="progress-text">Reading</span><div class="progress-bar-wrap"><div class="progress-bar-fill" id="progressFill"></div></div><span id="progressPercent">0%</span></div>
</header>
<div class="page-content">
<div class="page-header">
<span class="topic-badge">{emoji} {section}</span>
<h1>{title}</h1>
<p class="page-intro">{intro}</p>
<div style="display:flex;gap:.75rem;margin-top:1rem;flex-wrap:wrap;">
<span class="difficulty-badge {diff}">&#x25CF; {diff.capitalize()}</span>
<span style="font-size:.8rem;color:var(--text-muted);align-self:center;">&#x1F4D6; Based on: <em>{books}</em></span>
</div></div>
{body}
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
    print("Template module loaded. Use make_page() to generate pages.")
