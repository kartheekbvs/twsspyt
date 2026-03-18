import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# LOGIC & COMPARISONS
make_page("numpy/logic.html","Logic, Comparisons &amp; Search","NumPy","&#x1F522;","intermediate","NumPy &rarr; Logic",
"NumPy logic functions enable high-speed boolean operations. This section provides textbook precision on boolean masking and 'where' logic.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Vectorized Logic</a></li>
<li><a href="#s2">Return Value: np.where()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Vectorized Logic</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"NumPy allows you to express many kinds of data processing tasks as concise array expressions that might otherwise require loops. Choosing elements based on a condition is a core pattern." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: np.where()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>In its three-argument form, <code>np.where(condition, x, y)</code> returns a <strong>new Array</strong> whose elements are taken from <code>x</code> where the condition is True, and from <code>y</code> otherwise. It is a vectorized version of the ternary expression <code>x if condition else y</code>.</p>
</div>
</section>''',
("indexing.html","Indexing"),("operations.html","Operations"),
[("indexing.html", "Boolean Indexing"), ("operations.html", "Mathematical Filters")])

print("logic.html expanded!")
