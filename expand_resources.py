import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# RESOURCES
make_page("resources/python-cheat-sheet.html","Python &amp; Data Science Cheat Sheet","Resources","&#x1F4DA;","intermediate","Resources &rarr; Cheat Sheet",
"Cheat sheets are essential for rapid development. This section provides textbook definitions for API references and introspection tools.",
"Python Official Documentation &mdash; Built-in Functions",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Introspection Tools</a></li>
<li><a href="#s2">Return Value: help()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Introspection Tools</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Introspection is the ability to determine the type or attributes of an object at runtime. Python provides several built-in functions like <code>dir()</code>, <code>type()</code>, and <code>help()</code> for this purpose." &mdash; <em>Python Docs</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: help()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>help()</code> function is unique: it returns <strong>None</strong>, but it prints an interactive help page to the console or standard output. In contrast, <code>dir()</code> returns a <strong>List of strings</strong> containing the attributes and methods of the object.</p>
</div>
</section>''',
("../index.html","Home"),("math-for-ml.html","Math for ML"),
[("../index.html", "Quick Start"), ("math-for-ml.html", "Foundational Math")])

print("python-cheat-sheet.html expanded!")
