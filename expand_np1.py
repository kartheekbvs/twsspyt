import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# ========== NUMPY ARRAYS (EXPANDED) ==========
make_page("numpy/arrays.html","Arrays &amp; ndarray","NumPy","&#x1F522;","beginner","NumPy &rarr; Arrays &amp; ndarray",
"NumPy is the fundamental package for scientific computing in Python. This section explains the ndarray, memory layout, and formal textbook definitions of numerical arrays.",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">What is an ndarray?</a></li>
<li><a href="#s2">Creating Arrays</a></li>
<li><a href="#s3">Memory Layout &amp; Strides</a></li>
<li><a href="#s4">Vectorization</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; What is an ndarray?</h2>
<p>NumPy's main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers.</p>

<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"An ndarray is a generic multidimensional container for homogeneous data; that is, all of the elements must be the same type. Every array has a <code>shape</code> and a <code>dtype</code>." &mdash; <em>Learning NumPy</em></p>
    </div>
</div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np
data = np.array([[<span class="nm">1.5</span>, -<span class="nm">0.1</span>, <span class="nm">3</span>], [<span class="nm">0</span>, -<span class="nm">3</span>, <span class="nm">6.5</span>]])
<span class="bi">print</span>(data.shape)  <span class="cm"># (2, 3)</span>
<span class="bi">print</span>(data.dtype)  <span class="cm"># float64</span></pre>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>np.array()</code> function returns a <strong>numpy.ndarray object</strong>. Unlike Python lists, the return value of slicing (e.g., <code>arr[1:3]</code>) is a <strong>view</strong> on the original data, not a copy. Changing the slice changes the original array!</p>
</div>
</section>''',
("../advanced/async.html","Async &amp; Await"),("operations.html","Array Operations"),
[("../pandas/series-dataframe.html", "Pandas Data Structures"), ("operations.html", "Vectorized Math"), ("broadcasting.html", "Broadcasting Rules")])

print("arrays.html expanded with enriched content!")

