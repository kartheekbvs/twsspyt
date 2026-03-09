import sys, os
sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# ========== NUMPY ARRAYS (EXPANDED) ==========
make_page("numpy/arrays.html","Arrays &amp; ndarray","NumPy","&#x1F522;","beginner","NumPy &rarr; Arrays &amp; ndarray",
"NumPy is the fundamental package for numerical computing in Python. At its core is the ndarray — a fast, memory-efficient, homogeneous n-dimensional array. NumPy arrays are up to 50x faster than Python lists because they store data in contiguous memory, use fixed dtypes, and support vectorized operations written in C.",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney, Python Programming (2024)",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">What is NumPy &amp; Why It&#39;s Faster</a></li>
<li><a href="#s2">Creating Arrays</a></li>
<li><a href="#s3">Array Attributes</a></li>
<li><a href="#s4">NumPy Data Types</a></li>
<li><a href="#s5">NumPy vs Python Lists</a></li>
<li><a href="#s6">Memory Model &amp; Vectorization</a></li>
</ol></div>

<!-- ====== SECTION 1 ====== -->
<section class="content-section" id="s1"><h2>1 &middot; What is NumPy &amp; Why It&#39;s Faster</h2>
<p>NumPy (<strong>Num</strong>erical <strong>Py</strong>thon) provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them. It is the foundation for virtually every scientific Python library including Pandas, scikit-learn, TensorFlow, and PyTorch.</p>

<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Why NumPy is faster than Python lists</strong>
<ul>
<li><strong>Contiguous memory</strong>: NumPy stores elements in a single continuous block of memory; Python lists store pointers to scattered objects.</li>
<li><strong>Fixed data types</strong>: All elements share one dtype (e.g., float64), eliminating per-element type checking.</li>
<li><strong>Vectorized C operations</strong>: Operations are implemented in compiled C/Fortran, bypassing Python&#39;s interpreter loop.</li>
<li><strong>SIMD &amp; cache efficiency</strong>: Contiguous memory leverages CPU caches and Single Instruction Multiple Data parallelism.</li>
</ul></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Installation &amp; Import</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Installation</span>
<span class="cm"># pip install numpy</span>

<span class="kw">import</span> numpy <span class="kw">as</span> np   <span class="cm"># standard alias</span>
<span class="bi">print</span>(np.__version__)   <span class="cm"># e.g. 1.26.4</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>1.26.4</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Speed Comparison</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> time

<span class="cm"># Python list approach</span>
py_list = <span class="bi">list</span>(<span class="bi">range</span>(<span class="nm">1_000_000</span>))
start = time.time()
py_result = [x ** <span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> py_list]
py_time = time.time() - start

<span class="cm"># NumPy approach</span>
np_arr = np.arange(<span class="nm">1_000_000</span>)
start = time.time()
np_result = np_arr ** <span class="nm">2</span>
np_time = time.time() - start

<span class="bi">print</span>(<span class="st">f"Python list: {py_time:.4f}s"</span>)
<span class="bi">print</span>(<span class="st">f"NumPy array: {np_time:.4f}s"</span>)
<span class="bi">print</span>(<span class="st">f"NumPy is {py_time/np_time:.0f}x faster!"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Python list: 0.1842s<br>NumPy array: 0.0018s<br>NumPy is 102x faster!</div></div>
</section>

<!-- ====== SECTION 2 ====== -->
<section class="content-section" id="s2"><h2>2 &middot; Creating Arrays</h2>

<h3>2.1 &middot; np.array() &mdash; From Existing Data</h3>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># 1D array from list</span>
a = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>])
<span class="bi">print</span>(a)             <span class="cm"># [1 2 3 4 5]</span>
<span class="bi">print</span>(<span class="bi">type</span>(a))       <span class="cm"># &lt;class 'numpy.ndarray'&gt;</span>

<span class="cm"># 2D array (matrix)</span>
matrix = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], [<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>], [<span class="nm">7</span>,<span class="nm">8</span>,<span class="nm">9</span>]])
<span class="bi">print</span>(matrix)

<span class="cm"># 3D array</span>
cube = np.array([[[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]], [[<span class="nm">5</span>,<span class="nm">6</span>],[<span class="nm">7</span>,<span class="nm">8</span>]]])
<span class="bi">print</span>(<span class="st">f"3D shape: {cube.shape}"</span>)  <span class="cm"># (2, 2, 2)</span>

<span class="cm"># Specify dtype explicitly</span>
floats = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>], dtype=np.float64)
<span class="bi">print</span>(floats)        <span class="cm"># [1. 2. 3.]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1 2 3 4 5]<br>&lt;class 'numpy.ndarray'&gt;<br>[[1 2 3]<br> [4 5 6]<br> [7 8 9]]<br>3D shape: (2, 2, 2)<br>[1. 2. 3.]</div></div>

<h3>2.2 &middot; np.arange() &mdash; Range of Values</h3>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># arange(start, stop, step) &mdash; like range() but returns ndarray</span>
<span class="bi">print</span>(np.arange(<span class="nm">10</span>))           <span class="cm"># [0 1 2 3 4 5 6 7 8 9]</span>
<span class="bi">print</span>(np.arange(<span class="nm">2</span>, <span class="nm">10</span>))       <span class="cm"># [2 3 4 5 6 7 8 9]</span>
<span class="bi">print</span>(np.arange(<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">0.2</span>))  <span class="cm"># [0.  0.2 0.4 0.6 0.8]  &mdash; float step!</span>
<span class="bi">print</span>(np.arange(<span class="nm">10</span>, <span class="nm">0</span>, -<span class="nm">2</span>))  <span class="cm"># [10  8  6  4  2]  &mdash; reverse</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0 1 2 3 4 5 6 7 8 9]<br>[2 3 4 5 6 7 8 9]<br>[0. 0.2 0.4 0.6 0.8]<br>[10 8 6 4 2]</div></div>

<h3>2.3 &middot; np.linspace() &mdash; Evenly Spaced</h3>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># linspace(start, stop, num) &mdash; num evenly spaced points (inclusive)</span>
<span class="bi">print</span>(np.linspace(<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">5</span>))   <span class="cm"># [0.   0.25 0.5  0.75 1.  ]</span>
<span class="bi">print</span>(np.linspace(<span class="nm">0</span>, <span class="nm">10</span>, <span class="nm">3</span>))  <span class="cm"># [0.  5. 10.]</span>

<span class="cm"># Great for plotting x-axis values</span>
x = np.linspace(<span class="nm">0</span>, <span class="nm">2</span> * np.pi, <span class="nm">100</span>)  <span class="cm"># 100 points from 0 to 2&pi;</span>
<span class="bi">print</span>(<span class="st">f"Shape: {x.shape}, Range: [{x[0]:.2f}, {x[-1]:.2f}]"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0.   0.25 0.5  0.75 1.  ]<br>[0. 5. 10.]<br>Shape: (100,), Range: [0.00, 6.28]</div></div>

<h3>2.4 &middot; Zeros, Ones, Full, Empty</h3>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># np.zeros(shape)</span>
<span class="bi">print</span>(np.zeros(<span class="nm">5</span>))             <span class="cm"># [0. 0. 0. 0. 0.]</span>
<span class="bi">print</span>(np.zeros((<span class="nm">2</span>, <span class="nm">3</span>)))       <span class="cm"># [[0. 0. 0.] [0. 0. 0.]]</span>
<span class="bi">print</span>(np.zeros((<span class="nm">2</span>,<span class="nm">3</span>), dtype=<span class="bi">int</span>))  <span class="cm"># integer zeros</span>

<span class="cm"># np.ones(shape)</span>
<span class="bi">print</span>(np.ones((<span class="nm">3</span>, <span class="nm">4</span>)))        <span class="cm"># 3x4 matrix of 1.0</span>

<span class="cm"># np.full(shape, fill_value)</span>
<span class="bi">print</span>(np.full((<span class="nm">2</span>, <span class="nm">3</span>), <span class="nm">7</span>))     <span class="cm"># [[7 7 7] [7 7 7]]</span>
<span class="bi">print</span>(np.full((<span class="nm">3</span>,), <span class="nm">3.14</span>))   <span class="cm"># [3.14 3.14 3.14]</span>

<span class="cm"># np.empty(shape) &mdash; uninitialized (fast, but random values!)</span>
<span class="bi">print</span>(np.empty((<span class="nm">2</span>, <span class="nm">2</span>)))       <span class="cm"># random memory (NOT zeros!)</span>

<span class="cm"># _like variants: match shape of existing array</span>
template = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]])
<span class="bi">print</span>(np.zeros_like(template))  <span class="cm"># [[0,0,0],[0,0,0]]</span>
<span class="bi">print</span>(np.ones_like(template))   <span class="cm"># [[1,1,1],[1,1,1]]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0. 0. 0. 0. 0.]<br>[[0. 0. 0.] [0. 0. 0.]]<br>[[7 7 7] [7 7 7]]</div></div>

<h3>2.5 &middot; Identity &amp; Eye Matrices</h3>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># np.eye(N) &mdash; NxN identity matrix</span>
<span class="bi">print</span>(np.eye(<span class="nm">3</span>))
<span class="cm"># [[1. 0. 0.]</span>
<span class="cm">#  [0. 1. 0.]</span>
<span class="cm">#  [0. 0. 1.]]</span>

<span class="cm"># np.eye(N, M, k) &mdash; non-square, shifted diagonal</span>
<span class="bi">print</span>(np.eye(<span class="nm">3</span>, <span class="nm">4</span>, k=<span class="nm">1</span>))   <span class="cm"># diagonal shifted up by 1</span>

<span class="cm"># np.identity(N) &mdash; always square identity</span>
<span class="bi">print</span>(np.identity(<span class="nm">4</span>))       <span class="cm"># 4x4 identity</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[1. 0. 0.]<br> [0. 1. 0.]<br> [0. 0. 1.]]</div></div>

<h3>2.6 &middot; Random Array Generation</h3>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">rng = np.random.default_rng(seed=<span class="nm">42</span>)

<span class="bi">print</span>(rng.random((<span class="nm">2</span>,<span class="nm">3</span>)))           <span class="cm"># 2x3 uniform [0,1)</span>
<span class="bi">print</span>(rng.integers(<span class="nm">1</span>, <span class="nm">100</span>, (<span class="nm">3</span>,)))  <span class="cm"># 3 random ints [1,100)</span>
<span class="bi">print</span>(rng.standard_normal((<span class="nm">2</span>,<span class="nm">2</span>)))  <span class="cm"># 2x2 standard normal</span>

<span class="cm"># Legacy API (still common)</span>
np.random.seed(<span class="nm">42</span>)
<span class="bi">print</span>(np.random.rand(<span class="nm">3</span>))      <span class="cm"># 3 uniform [0,1)</span>
<span class="bi">print</span>(np.random.randn(<span class="nm">3</span>))     <span class="cm"># 3 standard normal</span>
<span class="bi">print</span>(np.random.randint(<span class="nm">1</span>,<span class="nm">10</span>,<span class="nm">5</span>))  <span class="cm"># 5 ints in [1,10)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[0.77 0.44 0.86] [0.70 0.09 0.98]]<br>[72 10 35]</div></div>
</section>

<!-- ====== SECTION 3 ====== -->
<section class="content-section" id="s3"><h2>3 &middot; Array Attributes</h2>
<table class="data-table"><thead><tr><th>Attribute</th><th>Description</th><th>Example</th></tr></thead><tbody>
<tr><td><code>ndarray.ndim</code></td><td>Number of dimensions (axes)</td><td><code>2</code> for a matrix</td></tr>
<tr><td><code>ndarray.shape</code></td><td>Tuple of dimension sizes</td><td><code>(3, 4)</code></td></tr>
<tr><td><code>ndarray.size</code></td><td>Total number of elements</td><td><code>12</code></td></tr>
<tr><td><code>ndarray.dtype</code></td><td>Data type of elements</td><td><code>float64</code></td></tr>
<tr><td><code>ndarray.itemsize</code></td><td>Bytes per element</td><td><code>8</code> (float64)</td></tr>
<tr><td><code>ndarray.nbytes</code></td><td>Total memory in bytes</td><td><code>96</code></td></tr>
<tr><td><code>ndarray.strides</code></td><td>Bytes to step in each dim</td><td><code>(32, 8)</code></td></tr>
<tr><td><code>ndarray.data</code></td><td>Memory buffer (rarely used)</td><td>buffer object</td></tr>
<tr><td><code>ndarray.T</code></td><td>Transposed view</td><td>Swaps axes</td></tr>
<tr><td><code>ndarray.flat</code></td><td>1D iterator over elements</td><td>Iterator</td></tr>
</tbody></table>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">arr = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>],
                [<span class="nm">5</span>,<span class="nm">6</span>,<span class="nm">7</span>,<span class="nm">8</span>],
                [<span class="nm">9</span>,<span class="nm">10</span>,<span class="nm">11</span>,<span class="nm">12</span>]], dtype=np.float64)

<span class="bi">print</span>(<span class="st">f"ndim:     {arr.ndim}"</span>)       <span class="cm"># 2</span>
<span class="bi">print</span>(<span class="st">f"shape:    {arr.shape}"</span>)      <span class="cm"># (3, 4)</span>
<span class="bi">print</span>(<span class="st">f"size:     {arr.size}"</span>)       <span class="cm"># 12</span>
<span class="bi">print</span>(<span class="st">f"dtype:    {arr.dtype}"</span>)      <span class="cm"># float64</span>
<span class="bi">print</span>(<span class="st">f"itemsize: {arr.itemsize}"</span>)   <span class="cm"># 8 bytes</span>
<span class="bi">print</span>(<span class="st">f"nbytes:   {arr.nbytes}"</span>)     <span class="cm"># 96 (12 * 8)</span>
<span class="bi">print</span>(<span class="st">f"strides:  {arr.strides}"</span>)    <span class="cm"># (32, 8)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>ndim: 2 &middot; shape: (3, 4) &middot; size: 12 &middot; dtype: float64<br>itemsize: 8 &middot; nbytes: 96 &middot; strides: (32, 8)</div></div>
</section>

<!-- ====== SECTION 4 ====== -->
<section class="content-section" id="s4"><h2>4 &middot; NumPy Data Types (dtypes)</h2>
<table class="data-table"><thead><tr><th>Category</th><th>Types</th><th>Bytes</th><th>Range</th></tr></thead><tbody>
<tr><td>Boolean</td><td><code>bool_</code></td><td>1</td><td>True / False</td></tr>
<tr><td>Signed Int</td><td><code>int8, int16, int32, int64</code></td><td>1-8</td><td>&minus;128 to 2<sup>63</sup>&minus;1</td></tr>
<tr><td>Unsigned Int</td><td><code>uint8, uint16, uint32, uint64</code></td><td>1-8</td><td>0 to 2<sup>64</sup>&minus;1</td></tr>
<tr><td>Float</td><td><code>float16, float32, float64</code></td><td>2-8</td><td>&plusmn;6.1e&minus;5 to &plusmn;1.8e308</td></tr>
<tr><td>Complex</td><td><code>complex64, complex128</code></td><td>8-16</td><td>Real + imaginary</td></tr>
<tr><td>String</td><td><code>str_, bytes_</code></td><td>variable</td><td>Fixed-length strings</td></tr>
</tbody></table>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Creating with specific dtypes</span>
a = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], dtype=np.int32)
b = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], dtype=np.float32)
c = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], dtype=np.complex128)
<span class="bi">print</span>(<span class="st">f"int32:     {a}, {a.dtype}, {a.itemsize} bytes"</span>)
<span class="bi">print</span>(<span class="st">f"float32:   {b}, {b.dtype}, {b.itemsize} bytes"</span>)
<span class="bi">print</span>(<span class="st">f"complex128:{c}, {c.dtype}, {c.itemsize} bytes"</span>)

<span class="cm"># Type conversion with .astype()</span>
ints = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>])
floats = ints.astype(np.float64)
<span class="bi">print</span>(<span class="st">f"Converted: {floats}, dtype={floats.dtype}"</span>)

<span class="cm"># Overflow warning</span>
small = np.array([<span class="nm">200</span>], dtype=np.int8)   <span class="cm"># max 127!</span>
<span class="bi">print</span>(<span class="st">f"int8 overflow: {small}"</span>)   <span class="cm"># -56 (wraps around!)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>int32: [1 2 3], int32, 4 bytes<br>float32: [1. 2. 3.], float32, 4 bytes<br>Converted: [1. 2. 3.], dtype=float64<br>int8 overflow: [-56]</div></div>
<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>dtype Gotcha</strong><p>Always check your dtype! Using <code>int8</code> or <code>float16</code> saves memory but can cause silent overflow or precision loss. Use <code>float64</code> for most scientific work.</p></div></div>
</section>

<!-- ====== SECTION 5 ====== -->
<section class="content-section" id="s5"><h2>5 &middot; NumPy Array vs Python List</h2>
<table class="data-table"><thead><tr><th>Feature</th><th>Python List</th><th>NumPy ndarray</th></tr></thead><tbody>
<tr><td>Data types</td><td>Mixed (heterogeneous)</td><td>Fixed (homogeneous)</td></tr>
<tr><td>Memory</td><td>Scattered pointers</td><td>Contiguous block</td></tr>
<tr><td>Speed</td><td>Slow (interpreter loop)</td><td>Fast (compiled C)</td></tr>
<tr><td>Operations</td><td>Element-by-element manually</td><td>Vectorized</td></tr>
<tr><td>Size change</td><td>Dynamic (append/remove)</td><td>Fixed after creation</td></tr>
<tr><td>Dimensions</td><td>Nested lists (irregular okay)</td><td>Regular n-dimensional grid</td></tr>
<tr><td>Broadcasting</td><td>Not supported</td><td>Built-in</td></tr>
<tr><td>Slicing</td><td>Returns copy</td><td>Returns view (shared memory)</td></tr>
</tbody></table>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Memory Comparison</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> sys

py_list = <span class="bi">list</span>(<span class="bi">range</span>(<span class="nm">1000</span>))
np_arr  = np.arange(<span class="nm">1000</span>, dtype=np.int64)

<span class="cm"># Python list: each int is ~28 bytes + 8 byte pointer</span>
list_mem = sys.getsizeof(py_list) + <span class="bi">sum</span>(sys.getsizeof(x) <span class="kw">for</span> x <span class="kw">in</span> py_list)
<span class="cm"># NumPy array: 1000 * 8 bytes (int64) + small overhead</span>
arr_mem = np_arr.nbytes

<span class="bi">print</span>(<span class="st">f"List memory:  {list_mem:,} bytes"</span>)   <span class="cm"># ~36,000 bytes</span>
<span class="bi">print</span>(<span class="st">f"Array memory: {arr_mem:,} bytes"</span>)    <span class="cm"># 8,000 bytes</span>
<span class="bi">print</span>(<span class="st">f"List is {list_mem/arr_mem:.1f}x larger"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>List memory: 36,056 bytes<br>Array memory: 8,000 bytes<br>List is 4.5x larger</div></div>
</section>

<!-- ====== SECTION 6 ====== -->
<section class="content-section" id="s6"><h2>6 &middot; Memory Model &amp; Vectorization</h2>
<h3>Memory Layout</h3>
<p>NumPy arrays store data in a flat contiguous buffer. The <code>strides</code> attribute tells NumPy how many bytes to skip to reach the next element along each axis.</p>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">arr = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]], dtype=np.int64)
<span class="bi">print</span>(<span class="st">f"Strides: {arr.strides}"</span>)
<span class="cm"># (24, 8) &mdash; 24 bytes to next row, 8 bytes to next column</span>

<span class="cm"># C-order (row-major, default) vs F-order (column-major)</span>
c_arr = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]], order=<span class="st">'C'</span>)
f_arr = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]], order=<span class="st">'F'</span>)
<span class="bi">print</span>(<span class="st">f"C strides: {c_arr.strides}"</span>)   <span class="cm"># (16, 8)</span>
<span class="bi">print</span>(<span class="st">f"F strides: {f_arr.strides}"</span>)   <span class="cm"># (8, 16)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Strides: (24, 8)<br>C strides: (16, 8)<br>F strides: (8, 16)</div></div>

<h3>Vectorization</h3>
<p>Vectorization replaces explicit Python loops with array operations executed in compiled C. Always prefer vectorized ops over for-loops.</p>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># BAD: Python loop</span>
a = np.arange(<span class="nm">1000000</span>)
result = np.empty_like(a)
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="bi">len</span>(a)):
    result[i] = a[i] * <span class="nm">2</span> + <span class="nm">1</span>   <span class="cm"># slow!</span>

<span class="cm"># GOOD: Vectorized (100x faster)</span>
result = a * <span class="nm">2</span> + <span class="nm">1</span>

<span class="cm"># Broadcasting overview</span>
<span class="cm"># NumPy auto-expands smaller arrays to match shapes:</span>
A = np.ones((<span class="nm">3</span>, <span class="nm">4</span>))       <span class="cm"># shape (3, 4)</span>
b = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>])   <span class="cm"># shape (4,) &rarr; broadcast to (3, 4)</span>
<span class="bi">print</span>(A + b)               <span class="cm"># each row gets b added</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[2. 3. 4. 5.]<br> [2. 3. 4. 5.]<br> [2. 3. 4. 5.]]</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Rule of Thumb</strong><p>If you see a <code>for</code> loop operating on NumPy array elements, there&#39;s almost certainly a vectorized alternative that&#39;s 10-100x faster. Think in terms of whole-array operations.</p></div></div>
</section>''',
("../advanced/async.html","Async &amp; Await"),("operations.html","Array Operations"))

print("arrays.html expanded!")
