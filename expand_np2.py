import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# EXPANDED INDEXING
make_page("numpy/indexing.html","Indexing &amp; Slicing","NumPy","&#x1F522;","intermediate","NumPy &rarr; Indexing &amp; Slicing",
"NumPy arrays support powerful indexing beyond Python lists: basic integer indexing, negative indexing, multi-dimensional indexing, slicing with start:stop:step, boolean masking, and fancy (integer array) indexing. Understanding views vs copies is critical for performance and avoiding bugs.",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Basic &amp; Negative Indexing</a></li>
<li><a href="#s2">Slicing (Start:Stop:Step)</a></li>
<li><a href="#s3">Multidimensional Indexing</a></li>
<li><a href="#s4">Boolean Indexing &amp; Masking</a></li>
<li><a href="#s5">Fancy (Integer Array) Indexing</a></li>
<li><a href="#s6">Views vs Copies</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Basic &amp; Negative Indexing</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

a = np.array([<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>, <span class="nm">40</span>, <span class="nm">50</span>, <span class="nm">60</span>])

<span class="cm"># Integer indexing (0-based)</span>
<span class="bi">print</span>(a[<span class="nm">0</span>])     <span class="cm"># 10  (first element)</span>
<span class="bi">print</span>(a[<span class="nm">3</span>])     <span class="cm"># 40</span>
<span class="bi">print</span>(a[<span class="nm">5</span>])     <span class="cm"># 60  (last element)</span>

<span class="cm"># Negative indexing (count from end)</span>
<span class="bi">print</span>(a[-<span class="nm">1</span>])    <span class="cm"># 60  (last)</span>
<span class="bi">print</span>(a[-<span class="nm">2</span>])    <span class="cm"># 50  (second from end)</span>
<span class="bi">print</span>(a[-<span class="nm">6</span>])    <span class="cm"># 10  (first via negative)</span>

<span class="cm"># Modify via index</span>
a[<span class="nm">0</span>] = <span class="nm">99</span>
<span class="bi">print</span>(a)  <span class="cm"># [99 20 30 40 50 60]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>10 &middot; 40 &middot; 60 &middot; 60 &middot; 50 &middot; 10<br>[99 20 30 40 50 60]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Slicing (Start:Stop:Step)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.arange(<span class="nm">10</span>)  <span class="cm"># [0 1 2 3 4 5 6 7 8 9]</span>

<span class="cm"># Basic slicing: a[start:stop]  (stop is EXCLUSIVE)</span>
<span class="bi">print</span>(a[<span class="nm">2</span>:<span class="nm">7</span>])       <span class="cm"># [2 3 4 5 6]</span>
<span class="bi">print</span>(a[:<span class="nm">5</span>])        <span class="cm"># [0 1 2 3 4]  (first 5)</span>
<span class="bi">print</span>(a[<span class="nm">5</span>:])        <span class="cm"># [5 6 7 8 9]  (from index 5)</span>
<span class="bi">print</span>(a[:])          <span class="cm"># [0 1 2 3 4 5 6 7 8 9]  (full copy-ish)</span>

<span class="cm"># Step slicing: a[start:stop:step]</span>
<span class="bi">print</span>(a[::<span class="nm">2</span>])        <span class="cm"># [0 2 4 6 8]  (every 2nd)</span>
<span class="bi">print</span>(a[::<span class="nm">3</span>])        <span class="cm"># [0 3 6 9]   (every 3rd)</span>
<span class="bi">print</span>(a[<span class="nm">1</span>::<span class="nm">2</span>])       <span class="cm"># [1 3 5 7 9]  (odd indices)</span>

<span class="cm"># Reverse slicing</span>
<span class="bi">print</span>(a[::-<span class="nm">1</span>])       <span class="cm"># [9 8 7 6 5 4 3 2 1 0]  (reversed)</span>
<span class="bi">print</span>(a[::-<span class="nm">2</span>])       <span class="cm"># [9 7 5 3 1]  (reversed, every 2nd)</span>
<span class="bi">print</span>(a[<span class="nm">7</span>:<span class="nm">2</span>:-<span class="nm">1</span>])     <span class="cm"># [7 6 5 4 3]  (reverse sub-range)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[2 3 4 5 6] &middot; [0 1 2 3 4] &middot; [5 6 7 8 9]<br>[0 2 4 6 8] &middot; [0 3 6 9] &middot; [1 3 5 7 9]<br>[9 8 7 6 5 4 3 2 1 0]</div></div>

<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>Slices are VIEWS!</strong><p>Unlike Python lists, NumPy slices share memory with the original array. Modifying a slice modifies the original. Use <code>.copy()</code> if you need an independent copy.</p></div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Multidimensional Indexing &amp; Slicing</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">M = np.array([[<span class="nm">1</span>,  <span class="nm">2</span>,  <span class="nm">3</span>,  <span class="nm">4</span>],
              [<span class="nm">5</span>,  <span class="nm">6</span>,  <span class="nm">7</span>,  <span class="nm">8</span>],
              [<span class="nm">9</span>, <span class="nm">10</span>, <span class="nm">11</span>, <span class="nm">12</span>]])

<span class="cm"># Single element: M[row, col]</span>
<span class="bi">print</span>(M[<span class="nm">0</span>, <span class="nm">2</span>])         <span class="cm"># 3</span>
<span class="bi">print</span>(M[<span class="nm">2</span>, -<span class="nm">1</span>])        <span class="cm"># 12</span>

<span class="cm"># Entire row</span>
<span class="bi">print</span>(M[<span class="nm">1</span>])             <span class="cm"># [5 6 7 8]</span>
<span class="bi">print</span>(M[<span class="nm">1</span>, :])          <span class="cm"># same: [5 6 7 8]</span>

<span class="cm"># Entire column</span>
<span class="bi">print</span>(M[:, <span class="nm">1</span>])          <span class="cm"># [2 6 10]</span>
<span class="bi">print</span>(M[:, -<span class="nm">1</span>])         <span class="cm"># [4 8 12] (last column)</span>

<span class="cm"># Sub-matrix (row slicing + column slicing)</span>
<span class="bi">print</span>(M[:<span class="nm">2</span>, <span class="nm">1</span>:<span class="nm">3</span>])      <span class="cm"># [[2, 3], [6, 7]]</span>
<span class="bi">print</span>(M[<span class="nm">1</span>:, ::<span class="nm">2</span>])      <span class="cm"># [[5, 7], [9, 11]] (rows 1+, every 2nd col)</span>

<span class="cm"># Select specific rows</span>
<span class="bi">print</span>(M[[<span class="nm">0</span>, <span class="nm">2</span>], :])     <span class="cm"># [[1,2,3,4], [9,10,11,12]]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>3 &middot; 12<br>[5 6 7 8]<br>[2 6 10] &middot; [4 8 12]<br>[[2 3] [6 7]]<br>[[5 7] [9 11]]</div></div>

<h3>3D Array Indexing</h3>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">cube = np.arange(<span class="nm">24</span>).reshape(<span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>)
<span class="bi">print</span>(cube.shape)        <span class="cm"># (2, 3, 4)</span>
<span class="bi">print</span>(cube[<span class="nm">0</span>])            <span class="cm"># first "layer" (3x4)</span>
<span class="bi">print</span>(cube[<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>])     <span class="cm"># element at layer 1, row 2, col 3 = 23</span>
<span class="bi">print</span>(cube[:, <span class="nm">0</span>, :])     <span class="cm"># first row from each layer</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>(2, 3, 4)<br>23</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Boolean Indexing &amp; Masking</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">data = np.array([<span class="nm">15</span>, <span class="nm">3</span>, <span class="nm">22</span>, <span class="nm">8</span>, <span class="nm">35</span>, <span class="nm">12</span>, <span class="nm">41</span>, <span class="nm">7</span>])

<span class="cm"># Boolean mask (comparison creates bool array)</span>
mask = data > <span class="nm">10</span>
<span class="bi">print</span>(mask)           <span class="cm"># [True False True False True True True False]</span>
<span class="bi">print</span>(data[mask])     <span class="cm"># [15 22 35 12 41]</span>

<span class="cm"># Combine conditions with &amp; (and), | (or), ~ (not)</span>
<span class="bi">print</span>(data[(data > <span class="nm">10</span>) &amp; (data < <span class="nm">30</span>)])  <span class="cm"># [15 22 12]</span>
<span class="bi">print</span>(data[(data < <span class="nm">5</span>) | (data > <span class="nm">40</span>)])   <span class="cm"># [3 41]</span>
<span class="bi">print</span>(data[~(data > <span class="nm">20</span>)])                <span class="cm"># [15 3 8 12 7]</span>

<span class="cm"># Modify via boolean index</span>
data[data > <span class="nm">30</span>] = <span class="nm">30</span>    <span class="cm"># cap at 30</span>
<span class="bi">print</span>(data)  <span class="cm"># [15 3 22 8 30 12 30 7]</span>

<span class="cm"># np.where(condition, if_true, if_false)</span>
labels = np.where(data > <span class="nm">15</span>, <span class="st">"high"</span>, <span class="st">"low"</span>)
<span class="bi">print</span>(labels)  <span class="cm"># ['low' 'low' 'high' 'low' 'high' 'low' 'high' 'low']</span>

<span class="cm"># 2D boolean masking</span>
M = np.arange(<span class="nm">12</span>).reshape(<span class="nm">3</span>,<span class="nm">4</span>)
<span class="bi">print</span>(M[M % <span class="nm">3</span> == <span class="nm">0</span>])   <span class="cm"># [0 3 6 9] (divisible by 3)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[True False True False True True True False]<br>[15 22 35 12 41]<br>[15 22 12] &middot; [3 41]<br>[15 3 22 8 30 12 30 7]</div></div>

<h3>Masked Arrays (np.ma)</h3>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Masked arrays: ignore invalid values in computations</span>
data = np.array([<span class="nm">1</span>, <span class="nm">2</span>, -<span class="nm">999</span>, <span class="nm">4</span>, <span class="nm">5</span>, -<span class="nm">999</span>])
masked = np.ma.masked_equal(data, -<span class="nm">999</span>)
<span class="bi">print</span>(masked)         <span class="cm"># [1 2 -- 4 5 --]</span>
<span class="bi">print</span>(masked.mean())  <span class="cm"># 3.0  (ignoring -999!)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1 2 -- 4 5 --]<br>3.0</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Fancy (Integer Array) Indexing</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.array([<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>, <span class="nm">40</span>, <span class="nm">50</span>])

<span class="cm"># Index with array of integers</span>
idx = np.array([<span class="nm">0</span>, <span class="nm">3</span>, <span class="nm">4</span>])
<span class="bi">print</span>(a[idx])          <span class="cm"># [10 40 50]</span>

<span class="cm"># Can repeat indices</span>
<span class="bi">print</span>(a[[<span class="nm">0</span>, <span class="nm">0</span>, <span class="nm">2</span>, <span class="nm">2</span>]])  <span class="cm"># [10 10 30 30]</span>

<span class="cm"># 2D fancy indexing</span>
M = np.arange(<span class="nm">12</span>).reshape(<span class="nm">3</span>, <span class="nm">4</span>)
<span class="cm"># Select elements at (0,1), (1,2), (2,3)</span>
<span class="bi">print</span>(M[[<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">2</span>], [<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>]])  <span class="cm"># [1 6 11]</span>

<span class="cm"># np.ix_ for cross-product selection</span>
<span class="bi">print</span>(M[np.ix_([<span class="nm">0</span>,<span class="nm">2</span>], [<span class="nm">1</span>,<span class="nm">3</span>])])
<span class="cm"># [[ 1  3]</span>
<span class="cm">#  [ 9 11]]  (rows 0&amp;2 x cols 1&amp;3)</span>

<span class="cm"># np.take and np.put</span>
<span class="bi">print</span>(np.take(a, [<span class="nm">1</span>,<span class="nm">3</span>]))  <span class="cm"># [20 40]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[10 40 50]<br>[10 10 30 30]<br>[1 6 11]<br>[[ 1 3] [ 9 11]]</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Views vs Copies</h2>
<table class="data-table"><thead><tr><th>Operation</th><th>Returns</th><th>Modifies Original?</th></tr></thead><tbody>
<tr><td><code>a[2:5]</code> (basic slice)</td><td>View</td><td>Yes</td></tr>
<tr><td><code>a[[0,3]]</code> (fancy index)</td><td>Copy</td><td>No</td></tr>
<tr><td><code>a[mask]</code> (boolean)</td><td>Copy</td><td>No</td></tr>
<tr><td><code>a.reshape()</code></td><td>View (usually)</td><td>Yes</td></tr>
<tr><td><code>a.T</code> (transpose)</td><td>View</td><td>Yes</td></tr>
<tr><td><code>a.ravel()</code></td><td>View (if possible)</td><td>Yes</td></tr>
<tr><td><code>a.flatten()</code></td><td>Copy (always)</td><td>No</td></tr>
<tr><td><code>a.copy()</code></td><td>Copy (always)</td><td>No</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">original = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>])

<span class="cm"># Slice = VIEW (shared memory)</span>
view = original[<span class="nm">1</span>:<span class="nm">4</span>]
view[<span class="nm">0</span>] = <span class="nm">999</span>
<span class="bi">print</span>(original)  <span class="cm"># [1 999 3 4 5] &mdash; original changed!</span>

<span class="cm"># Fancy index = COPY (independent)</span>
original = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>])
copy = original[[<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>]]
copy[<span class="nm">0</span>] = <span class="nm">999</span>
<span class="bi">print</span>(original)  <span class="cm"># [1 2 3 4 5] &mdash; original unchanged!</span>

<span class="cm"># Check if view: np.shares_memory()</span>
a = np.arange(<span class="nm">10</span>)
<span class="bi">print</span>(np.shares_memory(a, a[<span class="nm">2</span>:<span class="nm">5</span>]))   <span class="cm"># True (view)</span>
<span class="bi">print</span>(np.shares_memory(a, a.copy()))  <span class="cm"># False (copy)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1 999 3 4 5]<br>[1 2 3 4 5]<br>True &middot; False</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Best Practice</strong><p>Use <code>np.shares_memory(a, b)</code> to check if two arrays share data. Always use <code>.copy()</code> when you need to modify a slice without affecting the original.</p></div></div></section>''',
("arrays.html","Arrays &amp; ndarray"),("operations.html","Array Operations"))

print("indexing.html expanded!")
