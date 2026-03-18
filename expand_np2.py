import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# EXPANDED INDEXING
make_page("numpy/indexing.html","Indexing &amp; Slicing","NumPy","&#x1F522;","intermediate","NumPy &rarr; Indexing &amp; Slicing",
"NumPy indexing is a powerful mechanism for data access. This section covers textbook definitions for views vs copies and return value analysis.",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Basic Slicing</a></li>
<li><a href="#s2">Views vs Copies</a></li>
<li><a href="#s3">Fancy Indexing</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Basic Slicing</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"NumPy's array slicing is an extension of Python's list slicing, but with a critical difference: slices are views on the original array." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Views vs Copies</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: Slicing</div>
    <p>Basic slicing (e.g., <code>arr[1:5]</code>) returns a <strong>View</strong>. This means modifying the slice will modify the original array. This is done for memory efficiency in large datasets.</p>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: Fancy Indexing</div>
    <p>Fancy indexing (e.g., <code>arr[[0, 2, 4]]</code>) always returns a <strong>Copy</strong> of the data into a new array. Modifying this result does not affect the original array.</p>
</div>
</section>''',
("arrays.html","Arrays &amp; ndarray"),("operations.html","Array Operations"),
[("arrays.html", "Creating Arrays"), ("../pandas/selection.html", "Pandas Selection")])

print("indexing.html expanded!")
