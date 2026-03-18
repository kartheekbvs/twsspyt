import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# FINAL PROJECT
make_page("resources/final-project.html","Final Project: End-to-End ML Workflow","Resources","&#x1F393;","advanced","Resources &rarr; Final Project",
"The final project synthesizes all concepts into a production-ready workflow. This section provides textbook precision on model persistence and deployment.",
"Hands-On Machine Learning &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Model Persistence</a></li>
<li><a href="#s2">Return Value: joblib.dump()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Model Persistence</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Once you have a high-performing model, you should save its parameters so you can use it later without retraining. This is known as <em>serialization</em> or <em>model persistence</em>." &mdash; <em>Aur&eacute;lien G&eacute;ron</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: joblib.dump()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>joblib.dump(model, filename)</code> function returns a <strong>List of filenames</strong> where the object was saved. This is useful for verifying that large models with many components have been successfully written to disk.</p>
</div>
</section>''',
("python-cheat-sheet.html","Cheat Sheet"),("../index.html","Home"),
[("python-cheat-sheet.html", "Quick Reference"), ("../index.html", "Review All Topics")])

print("final-project.html expanded!")
