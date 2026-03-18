import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# LINEAR ALGEBRA
make_page("numpy/linalg.html","Linear Algebra &amp; Matrices","NumPy","&#x1F522;","advanced","NumPy &rarr; LinAlg",
"Linear algebra is the foundation of machine learning. This section provides textbook precision on matrix products and decomposition.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">The dot Product</a></li>
<li><a href="#s2">Return Value: linalg.solve()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; The dot Product</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"There is a distinction between element-wise multiplication (<code>*</code>) and matrix multiplication (<code>@</code> or <code>.dot()</code>). Matrix multiplication follows the standard rules of linear algebra." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: linalg.solve()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>np.linalg.solve(A, b)</code> function returns a <strong>1D or 2D NumPy Array</strong> which is the solution to the linear matrix equation <code>Ax = b</code>. It raises a <code>LinAlgError</code> if the matrix <code>A</code> is singular.</p>
</div>
</section>''',
("random.html","Random"),("indexing.html","Indexing"),
[("random.html", "Generating Matrices"), ("indexing.html", "Slicing Arrays")])

print("linalg.html expanded!")
