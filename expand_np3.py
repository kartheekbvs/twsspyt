import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# EXPANDED OPERATIONS
make_page("numpy/operations.html","Array Operations","NumPy","&#x1F522;","intermediate","NumPy &rarr; Array Operations",
"Vectorization and Broadcasting are the heart of NumPy performance. This section explores these concepts with textbook definitions and clear examples.",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Vectorization (ufuncs)</a></li>
<li><a href="#s2">Return Values</a></li>
<li><a href="#s3">Broadcasting Rules</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Vectorization &amp; ufuncs</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"A universal function, or ufunc, is a function that performs element-wise operations on data in ndarrays." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Values</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: arithmetic</div>
    <p>Arithmetic operations between arrays (or arrays and scalars) return a <strong>new ndarray</strong> containing the result. The original arrays remain untouched.</p>
</div>
</section>''',
("indexing.html","Indexing &amp; Slicing"),("reshaping.html","Reshaping &amp; Stacking"),
[("indexing.html", "Data Access"), ("../advanced/lambda.html", "Python Map/Filter")])

print("operations.html expanded!")
