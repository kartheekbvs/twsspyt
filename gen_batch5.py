
import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# ===== NUMPY =====
make_page("numpy/operations.html","Array Operations","NumPy","&#x1F522;","intermediate","NumPy &rarr; Array Operations",
"NumPy operations are vectorized — they apply element-wise without Python loops, making them 10-100x faster. This covers arithmetic, broadcasting, universal functions (ufuncs), aggregation, and boolean masking.",
"numpy-user manual, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Element-wise Operations</a></li><li><a href="#s2">Broadcasting</a></li><li><a href="#s3">Aggregation Functions</a></li><li><a href="#s4">Boolean Masking</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Element-wise Operations</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

a = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>])
b = np.array([<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">30</span>,<span class="nm">40</span>])

<span class="bi">print</span>(a + b)     <span class="cm"># [11 22 33 44]</span>
<span class="bi">print</span>(a * b)     <span class="cm"># [10 40 90 160]</span>
<span class="bi">print</span>(a ** <span class="nm">2</span>)    <span class="cm"># [1 4 9 16]</span>
<span class="bi">print</span>(a > <span class="nm">2</span>)     <span class="cm"># [False False True True]</span>
<span class="bi">print</span>(np.sqrt(a)) <span class="cm"># [1. 1.414 1.732 2.]</span>
<span class="bi">print</span>(np.exp(a))  <span class="cm"># [2.718 7.389 20.086 54.598]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[11 22 33 44] &middot; [10 40 90 160] &middot; [1 4 9 16]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Broadcasting</h2>
<p>NumPy automatically expands smaller arrays to match shapes for element-wise ops.</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">A = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]])  <span class="cm"># shape (2,3)</span>
b = np.array([<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">30</span>])          <span class="cm"># shape (3,)</span>

<span class="bi">print</span>(A + b)     <span class="cm"># [[11,22,33],[14,25,36]] — b broadcast to (2,3)</span>
<span class="bi">print</span>(A * <span class="nm">2</span>)     <span class="cm"># scalar broadcast</span>
<span class="bi">print</span>(A - A.mean(axis=<span class="nm">0</span>))  <span class="cm"># center columns</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[11 22 33]<br> [14 25 36]]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Aggregation Functions</h2>
<table class="data-table"><thead><tr><th>Function</th><th>Description</th><th>axis=0</th><th>axis=1</th></tr></thead><tbody>
<tr><td><code>np.sum()</code></td><td>Sum</td><td>Column sums</td><td>Row sums</td></tr>
<tr><td><code>np.mean()</code></td><td>Mean</td><td>Column means</td><td>Row means</td></tr>
<tr><td><code>np.std()</code></td><td>Std deviation</td><td>Per column</td><td>Per row</td></tr>
<tr><td><code>np.min/max()</code></td><td>Min/Max</td><td>Column</td><td>Row</td></tr>
<tr><td><code>np.argmin/argmax()</code></td><td>Index of min/max</td><td>Column</td><td>Row</td></tr>
<tr><td><code>np.cumsum()</code></td><td>Cumulative sum</td><td>Column</td><td>Row</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]])
<span class="bi">print</span>(M.sum())          <span class="cm"># 21 (all elements)</span>
<span class="bi">print</span>(M.sum(axis=<span class="nm">0</span>))    <span class="cm"># [5, 7, 9] (column sums)</span>
<span class="bi">print</span>(M.sum(axis=<span class="nm">1</span>))    <span class="cm"># [6, 15] (row sums)</span>
<span class="bi">print</span>(M.mean())         <span class="cm"># 3.5</span>
<span class="bi">print</span>(M.argmax())       <span class="cm"># 5 (flat index of max)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>21 &middot; [5 7 9] &middot; [6 15] &middot; 3.5 &middot; 5</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Boolean Masking (Fancy Indexing)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">data = np.array([<span class="nm">12</span>,<span class="nm">5</span>,<span class="nm">18</span>,<span class="nm">3</span>,<span class="nm">25</span>,<span class="nm">7</span>,<span class="nm">30</span>])
mask = data > <span class="nm">10</span>
<span class="bi">print</span>(mask)         <span class="cm"># [True False True False True False True]</span>
<span class="bi">print</span>(data[mask])   <span class="cm"># [12, 18, 25, 30]</span>
<span class="bi">print</span>(data[(data > <span class="nm">5</span>) &amp; (data < <span class="nm">20</span>)])  <span class="cm"># [12, 18, 7]</span>

<span class="cm"># Replace values using mask</span>
data[data > <span class="nm">20</span>] = <span class="nm">20</span>   <span class="cm"># cap at 20</span>
<span class="bi">print</span>(data)   <span class="cm"># [12, 5, 18, 3, 20, 7, 20]</span>

<span class="cm"># np.where — conditional</span>
result = np.where(data > <span class="nm">10</span>, <span class="st">"high"</span>, <span class="st">"low"</span>)
<span class="bi">print</span>(result)  <span class="cm"># ['high','low','high','low','high','low','high']</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[True False True False True False True]<br>[12 18 25 30]<br>[12 18 7]<br>[12 5 18 3 20 7 20]</div></div></section>''',
("arrays.html","Arrays &amp; ndarray"),("indexing.html","Indexing &amp; Slicing"))

make_page("numpy/indexing.html","Indexing &amp; Slicing","NumPy","&#x1F522;","intermediate","NumPy &rarr; Indexing &amp; Slicing",
"NumPy arrays support powerful indexing: basic slicing, boolean masking, fancy (integer array) indexing, and multidimensional selection. Understanding views vs copies is crucial for performance.",
"numpy-user manual, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Basic Indexing &amp; Slicing</a></li><li><a href="#s2">2D Array Indexing</a></li><li><a href="#s3">Fancy Indexing</a></li><li><a href="#s4">Views vs Copies</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Basic Indexing &amp; Slicing</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np
a = np.arange(<span class="nm">10</span>)  <span class="cm"># [0,1,2,3,4,5,6,7,8,9]</span>

<span class="bi">print</span>(a[<span class="nm">3</span>])       <span class="cm"># 3</span>
<span class="bi">print</span>(a[<span class="nm">2</span>:<span class="nm">7</span>])     <span class="cm"># [2,3,4,5,6]</span>
<span class="bi">print</span>(a[::<span class="nm">2</span>])      <span class="cm"># [0,2,4,6,8] (every 2nd)</span>
<span class="bi">print</span>(a[::-<span class="nm">1</span>])     <span class="cm"># [9,8,7,...,0] (reversed)</span>

<span class="cm"># Slices are VIEWS (no copy!)</span>
s = a[<span class="nm">3</span>:<span class="nm">6</span>]
s[<span class="nm">0</span>] = <span class="nm">99</span>
<span class="bi">print</span>(a)  <span class="cm"># [0,1,2,99,4,5,...] original modified!</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>3 &middot; [2 3 4 5 6] &middot; [0 2 4 6 8] &middot; [0 1 2 99 4 5 6 7 8 9]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; 2D Array Indexing</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],
              [<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>],
              [<span class="nm">7</span>,<span class="nm">8</span>,<span class="nm">9</span>]])

<span class="bi">print</span>(M[<span class="nm">0</span>, <span class="nm">2</span>])        <span class="cm"># 3 (row 0, col 2)</span>
<span class="bi">print</span>(M[<span class="nm">1</span>])            <span class="cm"># [4,5,6] (entire row 1)</span>
<span class="bi">print</span>(M[:, <span class="nm">1</span>])         <span class="cm"># [2,5,8] (entire column 1)</span>
<span class="bi">print</span>(M[:<span class="nm">2</span>, <span class="nm">1</span>:])      <span class="cm"># [[2,3],[5,6]] (subarray)</span>
<span class="bi">print</span>(M[[<span class="nm">0</span>,<span class="nm">2</span>], :])     <span class="cm"># [[1,2,3],[7,8,9]] (rows 0 &amp; 2)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>3 &middot; [4 5 6] &middot; [2 5 8] &middot; [[2 3] [5 6]]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Fancy Indexing</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Integer array indexing</span>
a = np.array([<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">30</span>,<span class="nm">40</span>,<span class="nm">50</span>])
idx = np.array([<span class="nm">0</span>,<span class="nm">3</span>,<span class="nm">4</span>])
<span class="bi">print</span>(a[idx])   <span class="cm"># [10, 40, 50]</span>

<span class="cm"># Boolean indexing</span>
mask = a > <span class="nm">25</span>
<span class="bi">print</span>(a[mask])   <span class="cm"># [30, 40, 50]</span>

<span class="cm"># np.ix_ for cross-product indexing</span>
M = np.arange(<span class="nm">12</span>).reshape(<span class="nm">3</span>,<span class="nm">4</span>)
<span class="bi">print</span>(M[np.ix_([<span class="nm">0</span>,<span class="nm">2</span>],[<span class="nm">1</span>,<span class="nm">3</span>])])  <span class="cm"># [[1,3],[9,11]]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[10 40 50] &middot; [30 40 50] &middot; [[1 3] [9 11]]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Views vs Copies</h2>
<table class="data-table"><thead><tr><th>Operation</th><th>Returns</th><th>Modifies Original?</th></tr></thead><tbody>
<tr><td><code>a[2:5]</code> (slice)</td><td>View</td><td>Yes</td></tr>
<tr><td><code>a[[0,3]]</code> (fancy index)</td><td>Copy</td><td>No</td></tr>
<tr><td><code>a[mask]</code> (boolean)</td><td>Copy</td><td>No</td></tr>
<tr><td><code>a.copy()</code></td><td>Copy</td><td>No</td></tr>
<tr><td><code>a.reshape()</code></td><td>View (usually)</td><td>Yes</td></tr>
</tbody></table>
<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>Gotcha</strong><p>Basic slicing returns a <em>view</em> (shared memory). Use <code>.copy()</code> if you need an independent array.</p></div></div></section>''',
("operations.html","Array Operations"),("reshaping.html","Reshaping &amp; Stacking"))

make_page("numpy/reshaping.html","Reshaping &amp; Stacking","NumPy","&#x1F522;","intermediate","NumPy &rarr; Reshaping",
"Reshaping changes array dimensions without copying data. Stacking combines arrays. These operations are fundamental to data preparation for machine learning and deep learning.",
"numpy-user manual",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">reshape &amp; resize</a></li><li><a href="#s2">Stacking &amp; Splitting</a></li><li><a href="#s3">Transpose &amp; Flatten</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; reshape</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np
a = np.arange(<span class="nm">12</span>)
<span class="bi">print</span>(a.reshape(<span class="nm">3</span>,<span class="nm">4</span>))    <span class="cm"># 3 rows, 4 cols</span>
<span class="bi">print</span>(a.reshape(<span class="nm">2</span>,-<span class="nm">1</span>))   <span class="cm"># -1 infers: (2,6)</span>
<span class="bi">print</span>(a.reshape(-<span class="nm">1</span>,<span class="nm">1</span>))   <span class="cm"># column vector (12,1)</span>

<span class="cm"># newaxis for adding dimensions</span>
v = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>])
<span class="bi">print</span>(v[:, np.newaxis].shape)    <span class="cm"># (3,1)</span>
<span class="bi">print</span>(v[np.newaxis, :].shape)    <span class="cm"># (1,3)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[ 0 1 2 3]<br> [ 4 5 6 7]<br> [ 8 9 10 11]]<br>(3, 1) &middot; (1, 3)</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Stacking &amp; Splitting</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>])
b = np.array([<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>])

<span class="bi">print</span>(np.vstack([a,b]))    <span class="cm"># [[1,2,3],[4,5,6]]</span>
<span class="bi">print</span>(np.hstack([a,b]))    <span class="cm"># [1,2,3,4,5,6]</span>
<span class="bi">print</span>(np.concatenate([a,b]))       <span class="cm"># [1,2,3,4,5,6]</span>
<span class="bi">print</span>(np.column_stack([a,b]))      <span class="cm"># [[1,4],[2,5],[3,6]]</span>

<span class="cm"># Splitting</span>
c = np.arange(<span class="nm">12</span>)
<span class="bi">print</span>(np.split(c, <span class="nm">3</span>))     <span class="cm"># [array([0,1,2,3]), ...]</span>
<span class="bi">print</span>(np.array_split(c, <span class="nm">5</span>)) <span class="cm"># uneven splits OK</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[1 2 3] [4 5 6]]<br>[1 2 3 4 5 6]<br>[[1 4] [2 5] [3 6]]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Transpose &amp; Flatten</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]])
<span class="bi">print</span>(M.T)          <span class="cm"># transpose (3,2)</span>
<span class="bi">print</span>(M.flatten())  <span class="cm"># [1,2,3,4,5,6] (copy)</span>
<span class="bi">print</span>(M.ravel())    <span class="cm"># [1,2,3,4,5,6] (view if possible)</span>
<span class="bi">print</span>(M.swapaxes(<span class="nm">0</span>,<span class="nm">1</span>))  <span class="cm"># same as .T for 2D</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[1 4]<br> [2 5]<br> [3 6]]<br>[1 2 3 4 5 6]</div></div></section>''',
("indexing.html","Indexing &amp; Slicing"),("math-functions.html","Math Functions"))

make_page("numpy/math-functions.html","Math Functions","NumPy","&#x1F522;","intermediate","NumPy &rarr; Math Functions",
"NumPy provides optimized mathematical functions (ufuncs) for trigonometry, logarithms, rounding, and statistics. These operate element-wise on arrays and are orders of magnitude faster than Python loops.",
"numpy-user manual",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Universal Functions (ufuncs)</a></li><li><a href="#s2">Statistical Functions</a></li><li><a href="#s3">Rounding &amp; Comparison</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Universal Functions</h2>
<table class="data-table"><thead><tr><th>Category</th><th>Functions</th></tr></thead><tbody>
<tr><td>Trigonometric</td><td><code>np.sin, cos, tan, arcsin, arccos, arctan</code></td></tr>
<tr><td>Exponential</td><td><code>np.exp, exp2, log, log2, log10</code></td></tr>
<tr><td>Power</td><td><code>np.sqrt, square, power, cbrt</code></td></tr>
<tr><td>Arithmetic</td><td><code>np.add, subtract, multiply, divide, mod</code></td></tr>
<tr><td>Absolute</td><td><code>np.abs, fabs, sign</code></td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np
x = np.array([<span class="nm">0</span>, np.pi/<span class="nm">4</span>, np.pi/<span class="nm">2</span>, np.pi])
<span class="bi">print</span>(np.sin(x))      <span class="cm"># [0, 0.707, 1, 0]</span>
<span class="bi">print</span>(np.exp([<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">2</span>]))  <span class="cm"># [1, 2.718, 7.389]</span>
<span class="bi">print</span>(np.log([<span class="nm">1</span>, np.e, np.e**<span class="nm">2</span>]))  <span class="cm"># [0, 1, 2]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0. 0.707 1. 0.]<br>[1. 2.718 7.389]<br>[0. 1. 2.]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Statistical Functions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">data = np.array([<span class="nm">14</span>,<span class="nm">18</span>,<span class="nm">11</span>,<span class="nm">13</span>,<span class="nm">16</span>,<span class="nm">15</span>,<span class="nm">12</span>,<span class="nm">17</span>])
<span class="bi">print</span>(<span class="st">f"Mean:   {np.mean(data):.2f}"</span>)      <span class="cm"># 14.50</span>
<span class="bi">print</span>(<span class="st">f"Median: {np.median(data):.2f}"</span>)    <span class="cm"># 14.50</span>
<span class="bi">print</span>(<span class="st">f"Std:    {np.std(data):.2f}"</span>)       <span class="cm"># 2.29</span>
<span class="bi">print</span>(<span class="st">f"Var:    {np.var(data):.2f}"</span>)       <span class="cm"># 5.25</span>
<span class="bi">print</span>(<span class="st">f"25th %: {np.percentile(data, 25)}"</span>) <span class="cm"># 12.25</span>
<span class="bi">print</span>(<span class="st">f"Corr:   {np.corrcoef([1,2,3],[2,4,6])}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Mean: 14.50<br>Median: 14.50<br>Std: 2.29<br>Var: 5.25</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Rounding &amp; Comparison</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">x = np.array([<span class="nm">1.23</span>, <span class="nm">2.78</span>, <span class="nm">3.45</span>])
<span class="bi">print</span>(np.round(x, <span class="nm">1</span>))   <span class="cm"># [1.2, 2.8, 3.5]</span>
<span class="bi">print</span>(np.floor(x))     <span class="cm"># [1., 2., 3.]</span>
<span class="bi">print</span>(np.ceil(x))      <span class="cm"># [2., 3., 4.]</span>
<span class="bi">print</span>(np.clip(x, <span class="nm">2</span>, <span class="nm">3</span>))  <span class="cm"># [2., 2.78, 3.] (clamp)</span>

<span class="cm"># Float comparison (avoid == for floats)</span>
a = np.array([<span class="nm">0.1</span>+<span class="nm">0.2</span>])
<span class="bi">print</span>(np.isclose(a, <span class="nm">0.3</span>))  <span class="cm"># [True]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1.2 2.8 3.5] &middot; [1. 2. 3.] &middot; [2. 3. 4.] &middot; [True]</div></div></section>''',
("reshaping.html","Reshaping &amp; Stacking"),("linear-algebra.html","Linear Algebra"))

make_page("numpy/linear-algebra.html","Linear Algebra","NumPy","&#x1F522;","advanced","NumPy &rarr; Linear Algebra",
"NumPy's linalg module provides optimized linear algebra operations: matrix multiplication, determinants, eigenvalues, SVD, solving linear systems. These are foundations for machine learning and deep learning.",
"numpy-user manual, Deep Learning &mdash; Ian Goodfellow",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Matrix Multiplication</a></li><li><a href="#s2">Determinant &amp; Inverse</a></li><li><a href="#s3">Eigenvalues &amp; SVD</a></li><li><a href="#s4">Solving Linear Systems</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Matrix Multiplication</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np
A = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]])
B = np.array([[<span class="nm">5</span>,<span class="nm">6</span>],[<span class="nm">7</span>,<span class="nm">8</span>]])

<span class="bi">print</span>(A @ B)          <span class="cm"># matrix multiply (recommended)</span>
<span class="bi">print</span>(np.dot(A, B))   <span class="cm"># same as @</span>
<span class="bi">print</span>(A * B)          <span class="cm"># element-wise (NOT matrix mul!)</span>

v = np.array([<span class="nm">1</span>, <span class="nm">2</span>])
<span class="bi">print</span>(A @ v)          <span class="cm"># [5, 11] matrix-vector</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[19 22]<br> [43 50]]<br>[5 11]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Determinant &amp; Inverse</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">A = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]])
<span class="bi">print</span>(np.linalg.det(A))       <span class="cm"># -2.0</span>
<span class="bi">print</span>(np.linalg.inv(A))       <span class="cm"># [[-2, 1],[1.5,-0.5]]</span>
<span class="bi">print</span>(A @ np.linalg.inv(A))   <span class="cm"># identity (verify)</span>
<span class="bi">print</span>(np.linalg.matrix_rank(A))  <span class="cm"># 2</span>
<span class="bi">print</span>(np.trace(A))            <span class="cm"># 5 (sum of diagonal)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>-2.0<br>[[-2. 1.] [1.5 -0.5]]<br>2 &middot; 5</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Eigenvalues &amp; SVD</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Eigendecomposition</span>
vals, vecs = np.linalg.eig(A)
<span class="bi">print</span>(<span class="st">f"Eigenvalues: {vals}"</span>)   <span class="cm"># [-0.372, 5.372]</span>
<span class="bi">print</span>(<span class="st">f"Eigenvectors:\\n{vecs}"</span>)

<span class="cm"># SVD (used in PCA, recommendation systems)</span>
M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>],[<span class="nm">5</span>,<span class="nm">6</span>]])
U, S, Vt = np.linalg.svd(M, full_matrices=<span class="kw">False</span>)
<span class="bi">print</span>(<span class="st">f"U shape: {U.shape}"</span>)    <span class="cm"># (3,2)</span>
<span class="bi">print</span>(<span class="st">f"S: {S}"</span>)                <span class="cm"># singular values</span>
<span class="bi">print</span>(<span class="st">f"Vt shape: {Vt.shape}"</span>)  <span class="cm"># (2,2)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Eigenvalues: [-0.372 5.372]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Solving Linear Systems</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Solve Ax = b</span>
A = np.array([[<span class="nm">2</span>,<span class="nm">1</span>],[<span class="nm">5</span>,<span class="nm">7</span>]])
b = np.array([<span class="nm">11</span>, <span class="nm">13</span>])

x = np.linalg.solve(A, b)
<span class="bi">print</span>(<span class="st">f"Solution: {x}"</span>)  <span class="cm"># [7.111, -3.222]</span>
<span class="bi">print</span>(np.allclose(A @ x, b))  <span class="cm"># True (verify)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Solution: [ 7.111 -3.222]<br>True</div></div></section>''',
("math-functions.html","Math Functions"),("random.html","Random Module"))

make_page("numpy/random.html","Random Module","NumPy","&#x1F522;","intermediate","NumPy &rarr; Random Module",
"NumPy's random module generates arrays of random numbers from various distributions. Essential for simulations, data augmentation, train/test splits, and initializing neural network weights.",
"numpy-user manual",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Basic Random Generation</a></li><li><a href="#s2">Distributions</a></li><li><a href="#s3">Shuffling &amp; Sampling</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Basic Random Generation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np
rng = np.random.default_rng(seed=<span class="nm">42</span>)  <span class="cm"># recommended</span>

<span class="bi">print</span>(rng.random(<span class="nm">5</span>))              <span class="cm"># 5 uniform [0,1)</span>
<span class="bi">print</span>(rng.integers(<span class="nm">0</span>, <span class="nm">10</span>, size=<span class="nm">5</span>)) <span class="cm"># 5 random ints [0,10)</span>
<span class="bi">print</span>(rng.standard_normal((<span class="nm">2</span>,<span class="nm">3</span>)))  <span class="cm"># 2x3 standard normal</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0.773 0.438 0.859 0.697 0.094]<br>[8 6 9 0 1]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Distributions</h2>
<table class="data-table"><thead><tr><th>Distribution</th><th>Method</th><th>Use Case</th></tr></thead><tbody>
<tr><td>Uniform</td><td><code>rng.uniform(low, high, size)</code></td><td>Random initialization</td></tr>
<tr><td>Normal</td><td><code>rng.normal(mean, std, size)</code></td><td>Data simulation</td></tr>
<tr><td>Binomial</td><td><code>rng.binomial(n, p, size)</code></td><td>Coin flips</td></tr>
<tr><td>Poisson</td><td><code>rng.poisson(lam, size)</code></td><td>Event counting</td></tr>
<tr><td>Exponential</td><td><code>rng.exponential(scale, size)</code></td><td>Wait times</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Normal distribution (mean=0, std=1)</span>
samples = rng.normal(<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">1000</span>)
<span class="bi">print</span>(<span class="st">f"Mean: {samples.mean():.3f}, Std: {samples.std():.3f}"</span>)
<span class="cm"># Mean: -0.005, Std: 0.993</span>

<span class="cm"># Binomial (coin flips)</span>
flips = rng.binomial(<span class="nm">10</span>, <span class="nm">0.5</span>, <span class="nm">5</span>)  <span class="cm"># 10 flips, 5 experiments</span>
<span class="bi">print</span>(<span class="st">f"Heads in each: {flips}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Mean: -0.005, Std: 0.993</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Shuffling &amp; Sampling</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">arr = np.arange(<span class="nm">10</span>)
rng.shuffle(arr)       <span class="cm"># in-place shuffle</span>
<span class="bi">print</span>(arr)

<span class="cm"># Random choice (with/without replacement)</span>
<span class="bi">print</span>(rng.choice([<span class="st">"a"</span>,<span class="st">"b"</span>,<span class="st">"c"</span>], size=<span class="nm">5</span>, replace=<span class="kw">True</span>))
<span class="bi">print</span>(rng.choice(<span class="nm">100</span>, size=<span class="nm">5</span>, replace=<span class="kw">False</span>))  <span class="cm"># no repeat</span>

<span class="cm"># Permutation (returns new array, doesn't modify)</span>
<span class="bi">print</span>(rng.permutation(<span class="nm">5</span>))  <span class="cm"># [3,0,4,1,2] etc.</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[shuffled array]</div></div></section>''',
("linear-algebra.html","Linear Algebra"),("../pandas/series-dataframe.html","Pandas Series"))

print("Batch 5: NumPy pages done (operations, indexing, reshaping, math-functions, linear-algebra, random).")
