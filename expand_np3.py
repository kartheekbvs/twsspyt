import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# EXPANDED OPERATIONS (element-wise + ufuncs + logical)
make_page("numpy/operations.html","Array Operations","NumPy","&#x1F522;","intermediate","NumPy &rarr; Array Operations",
"NumPy operations are vectorized &mdash; they apply element-wise using compiled C without Python loops, making them 10-100x faster. Covers arithmetic operations, universal functions (ufuncs), comparison operations, and logical operations (any, all, where, isnan).",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Element-wise Arithmetic</a></li>
<li><a href="#s2">Universal Functions (ufuncs)</a></li>
<li><a href="#s3">Broadcasting</a></li>
<li><a href="#s4">Comparison Operations</a></li>
<li><a href="#s5">Logical Operations</a></li>
<li><a href="#s6">Aggregation &amp; Reduction</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Element-wise Arithmetic</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

a = np.array([<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>, <span class="nm">40</span>])
b = np.array([<span class="nm">1</span>,  <span class="nm">2</span>,  <span class="nm">3</span>,  <span class="nm">4</span>])

<span class="cm"># Addition</span>
<span class="bi">print</span>(a + b)         <span class="cm"># [11 22 33 44]</span>
<span class="bi">print</span>(np.add(a, b))  <span class="cm"># same</span>

<span class="cm"># Subtraction</span>
<span class="bi">print</span>(a - b)              <span class="cm"># [9 18 27 36]</span>
<span class="bi">print</span>(np.subtract(a, b))  <span class="cm"># same</span>

<span class="cm"># Multiplication</span>
<span class="bi">print</span>(a * b)              <span class="cm"># [10 40 90 160] (element-wise, NOT matrix!)</span>
<span class="bi">print</span>(np.multiply(a, b))  <span class="cm"># same</span>

<span class="cm"># Division</span>
<span class="bi">print</span>(a / b)              <span class="cm"># [10. 10. 10. 10.]</span>
<span class="bi">print</span>(a // b)             <span class="cm"># [10 10 10 10] (floor division)</span>
<span class="bi">print</span>(np.divide(a, b))    <span class="cm"># true division</span>

<span class="cm"># Power</span>
<span class="bi">print</span>(b ** <span class="nm">2</span>)             <span class="cm"># [1 4 9 16]</span>
<span class="bi">print</span>(np.power(b, <span class="nm">3</span>))     <span class="cm"># [1 8 27 64]</span>

<span class="cm"># Modulus</span>
<span class="bi">print</span>(a % <span class="nm">3</span>)              <span class="cm"># [1 2 0 1]</span>
<span class="bi">print</span>(np.mod(a, <span class="nm">7</span>))       <span class="cm"># [3 6 2 5]</span>

<span class="cm"># Scalar operations (broadcast scalar to all elements)</span>
<span class="bi">print</span>(a + <span class="nm">100</span>)   <span class="cm"># [110 120 130 140]</span>
<span class="bi">print</span>(a * <span class="nm">0.5</span>)   <span class="cm"># [5. 10. 15. 20.]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[11 22 33 44]<br>[10 40 90 160]<br>[10. 10. 10. 10.]<br>[1 4 9 16]<br>[1 2 0 1]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Universal Functions (ufuncs)</h2>
<p>Ufuncs are vectorized wrappers for element-wise operations, implemented in compiled C for speed.</p>
<table class="data-table"><thead><tr><th>Category</th><th>Functions</th></tr></thead><tbody>
<tr><td><strong>Arithmetic</strong></td><td><code>np.add, subtract, multiply, divide, power, mod, remainder</code></td></tr>
<tr><td><strong>Trigonometric</strong></td><td><code>np.sin, cos, tan, arcsin, arccos, arctan, arctan2</code></td></tr>
<tr><td><strong>Exponential</strong></td><td><code>np.exp, exp2, log, log2, log10, expm1, log1p</code></td></tr>
<tr><td><strong>Power</strong></td><td><code>np.sqrt, square, cbrt, reciprocal</code></td></tr>
<tr><td><strong>Absolute</strong></td><td><code>np.abs, fabs, sign, negative</code></td></tr>
<tr><td><strong>Rounding</strong></td><td><code>np.round, floor, ceil, trunc, rint</code></td></tr>
<tr><td><strong>Hyperbolic</strong></td><td><code>np.sinh, cosh, tanh, arcsinh</code></td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">x = np.array([<span class="nm">0</span>, np.pi/<span class="nm">6</span>, np.pi/<span class="nm">4</span>, np.pi/<span class="nm">3</span>, np.pi/<span class="nm">2</span>])

<span class="cm"># Trigonometric</span>
<span class="bi">print</span>(np.sin(x).round(<span class="nm">3</span>))  <span class="cm"># [0.  0.5  0.707 0.866 1.]</span>
<span class="bi">print</span>(np.cos(x).round(<span class="nm">3</span>))  <span class="cm"># [1.  0.866 0.707 0.5  0.]</span>

<span class="cm"># Exponential &amp; Logarithmic</span>
<span class="bi">print</span>(np.exp([<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>]))     <span class="cm"># [1.  2.718 7.389 20.086]</span>
<span class="bi">print</span>(np.log([<span class="nm">1</span>, np.e, np.e**<span class="nm">2</span>]))  <span class="cm"># [0. 1. 2.]  (natural log)</span>
<span class="bi">print</span>(np.log10([<span class="nm">1</span>, <span class="nm">10</span>, <span class="nm">100</span>]))     <span class="cm"># [0. 1. 2.]</span>
<span class="bi">print</span>(np.log2([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">4</span>, <span class="nm">8</span>]))      <span class="cm"># [0. 1. 2. 3.]</span>

<span class="cm"># Power &amp; Root</span>
<span class="bi">print</span>(np.sqrt([<span class="nm">4</span>, <span class="nm">9</span>, <span class="nm">16</span>, <span class="nm">25</span>]))  <span class="cm"># [2. 3. 4. 5.]</span>
<span class="bi">print</span>(np.cbrt([<span class="nm">8</span>, <span class="nm">27</span>, <span class="nm">64</span>]))      <span class="cm"># [2. 3. 4.]  (cube root)</span>
<span class="bi">print</span>(np.square([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>]))      <span class="cm"># [1 4 9 16]</span>

<span class="cm"># Rounding</span>
vals = np.array([<span class="nm">1.23</span>, <span class="nm">2.78</span>, -<span class="nm">3.45</span>, <span class="nm">4.50</span>])
<span class="bi">print</span>(np.round(vals, <span class="nm">1</span>))    <span class="cm"># [1.2, 2.8, -3.4, 4.5]</span>
<span class="bi">print</span>(np.floor(vals))       <span class="cm"># [1., 2., -4., 4.]</span>
<span class="bi">print</span>(np.ceil(vals))        <span class="cm"># [2., 3., -3., 5.]</span>
<span class="bi">print</span>(np.trunc(vals))       <span class="cm"># [1., 2., -3., 4.]  (towards zero)</span>

<span class="cm"># Clip (clamp values)</span>
<span class="bi">print</span>(np.clip(vals, -<span class="nm">2</span>, <span class="nm">3</span>))  <span class="cm"># [1.23, 2.78, -2., 3.]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0. 0.5 0.707 0.866 1.]<br>[1. 2.718 7.389 20.086]<br>[2. 3. 4. 5.]<br>[1.2 2.8 -3.4 4.5]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Broadcasting</h2>
<p>Broadcasting automatically expands arrays with different shapes so element-wise operations can proceed.</p>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Broadcasting Rules</strong>
<ol>
<li>If arrays differ in ndim, the smaller array is padded with 1s on the left.</li>
<li>Arrays with size 1 along an axis are stretched to match the other array.</li>
<li>If sizes disagree and neither is 1, raise an error.</li>
</ol></div></div>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Scalar broadcast</span>
a = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>])
<span class="bi">print</span>(a * <span class="nm">10</span>)    <span class="cm"># [10 20 30] &mdash; 10 broadcast to [10,10,10]</span>

<span class="cm"># 1D + 2D broadcast</span>
M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]])  <span class="cm"># (2,3)</span>
v = np.array([<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">30</span>])          <span class="cm"># (3,) &rarr; broadcast to (2,3)</span>
<span class="bi">print</span>(M + v)
<span class="cm"># [[11 22 33]</span>
<span class="cm">#  [14 25 36]]</span>

<span class="cm"># Column vector broadcast</span>
col = np.array([[<span class="nm">100</span>],[<span class="nm">200</span>]])     <span class="cm"># (2,1) &rarr; broadcast to (2,3)</span>
<span class="bi">print</span>(M + col)
<span class="cm"># [[101 102 103]</span>
<span class="cm">#  [204 205 206]]</span>

<span class="cm"># Centering data (subtract column means)</span>
data = np.array([[<span class="nm">1</span>,<span class="nm">10</span>,<span class="nm">100</span>],[<span class="nm">2</span>,<span class="nm">20</span>,<span class="nm">200</span>],[<span class="nm">3</span>,<span class="nm">30</span>,<span class="nm">300</span>]])
centered = data - data.mean(axis=<span class="nm">0</span>)
<span class="bi">print</span>(centered)
<span class="cm"># [[-1. -10. -100.]</span>
<span class="cm">#  [ 0.   0.    0.]</span>
<span class="cm">#  [ 1.  10.  100.]]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[11 22 33]<br> [14 25 36]]<br>[[101 102 103]<br> [204 205 206]]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Comparison Operations</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.array([<span class="nm">1</span>, <span class="nm">5</span>, <span class="nm">3</span>, <span class="nm">8</span>, <span class="nm">2</span>])
b = np.array([<span class="nm">2</span>, <span class="nm">5</span>, <span class="nm">1</span>, <span class="nm">7</span>, <span class="nm">3</span>])

<span class="bi">print</span>(a > b)           <span class="cm"># [False False  True  True False]</span>
<span class="bi">print</span>(a == b)          <span class="cm"># [False  True False False False]</span>
<span class="bi">print</span>(a >= b)          <span class="cm"># [False  True  True  True False]</span>
<span class="bi">print</span>(np.greater(a,b)) <span class="cm"># same as a > b</span>
<span class="bi">print</span>(np.equal(a,b))   <span class="cm"># same as a == b</span>

<span class="cm"># Float comparison (NEVER use == for floats!)</span>
x = np.array([<span class="nm">0.1</span> + <span class="nm">0.2</span>])
<span class="bi">print</span>(x == <span class="nm">0.3</span>)               <span class="cm"># [False] &mdash; floating point error!</span>
<span class="bi">print</span>(np.isclose(x, <span class="nm">0.3</span>))     <span class="cm"># [True]  &mdash; correct!</span>
<span class="bi">print</span>(np.allclose(x, [<span class="nm">0.3</span>]))  <span class="cm"># True</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[False False True True False]<br>[False True False False False]<br>[False] &middot; [True]</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Logical Operations</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.array([<span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">3</span>, <span class="nm">0</span>, <span class="nm">5</span>])
b = np.array([<span class="nm">0</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">0</span>, <span class="nm">0</span>])

<span class="cm"># np.any() &mdash; True if ANY element is True/nonzero</span>
<span class="bi">print</span>(np.any(a > <span class="nm">4</span>))      <span class="cm"># True (5 > 4)</span>
<span class="bi">print</span>(np.any(a > <span class="nm">10</span>))     <span class="cm"># False</span>

<span class="cm"># np.all() &mdash; True if ALL elements are True/nonzero</span>
<span class="bi">print</span>(np.all(a > <span class="nm">0</span>))      <span class="cm"># False (has zeros)</span>
<span class="bi">print</span>(np.all(a >= <span class="nm">0</span>))     <span class="cm"># True</span>

<span class="cm"># np.where(condition, x, y) &mdash; conditional selection</span>
result = np.where(a > <span class="nm">0</span>, <span class="st">"positive"</span>, <span class="st">"zero"</span>)
<span class="bi">print</span>(result)  <span class="cm"># ['positive' 'zero' 'positive' 'zero' 'positive']</span>

<span class="cm"># np.where(condition) &mdash; returns indices where True</span>
idx = np.where(a > <span class="nm">0</span>)
<span class="bi">print</span>(idx)     <span class="cm"># (array([0, 2, 4]),)</span>

<span class="cm"># Logical functions</span>
<span class="bi">print</span>(np.logical_and(a > <span class="nm">0</span>, a < <span class="nm">4</span>))  <span class="cm"># [True False True False False]</span>
<span class="bi">print</span>(np.logical_or(a > <span class="nm">0</span>, b > <span class="nm">0</span>))   <span class="cm"># [True True True False True]</span>
<span class="bi">print</span>(np.logical_not(a > <span class="nm">0</span>))          <span class="cm"># [False True False True False]</span>

<span class="cm"># NaN checking</span>
data = np.array([<span class="nm">1.0</span>, np.nan, <span class="nm">3.0</span>, np.nan, <span class="nm">5.0</span>])
<span class="bi">print</span>(np.isnan(data))       <span class="cm"># [False True False True False]</span>
<span class="bi">print</span>(np.isinf([<span class="nm">1</span>, np.inf, -np.inf]))  <span class="cm"># [False True True]</span>
<span class="bi">print</span>(np.isfinite(data))    <span class="cm"># [True False True False True]</span>

<span class="cm"># Count non-NaN values</span>
<span class="bi">print</span>(np.count_nonzero(~np.isnan(data)))  <span class="cm"># 3</span>
<span class="bi">print</span>(np.nanmean(data))                    <span class="cm"># 3.0 (ignores NaN)</span>
<span class="bi">print</span>(np.nansum(data))                     <span class="cm"># 9.0</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>True &middot; False &middot; False &middot; True<br>['positive' 'zero' 'positive' 'zero' 'positive']<br>[True False True False False]<br>[False True False True False]<br>3 &middot; 3.0 &middot; 9.0</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Aggregation &amp; Reduction</h2>
<table class="data-table"><thead><tr><th>Function</th><th>Description</th><th>axis=0</th><th>axis=1</th></tr></thead><tbody>
<tr><td><code>np.sum()</code></td><td>Sum of elements</td><td>Column sums</td><td>Row sums</td></tr>
<tr><td><code>np.mean()</code></td><td>Arithmetic mean</td><td>Column means</td><td>Row means</td></tr>
<tr><td><code>np.median()</code></td><td>Median value</td><td>Per column</td><td>Per row</td></tr>
<tr><td><code>np.std()</code></td><td>Standard deviation</td><td>Per column</td><td>Per row</td></tr>
<tr><td><code>np.var()</code></td><td>Variance</td><td>Per column</td><td>Per row</td></tr>
<tr><td><code>np.min/max()</code></td><td>Min/Max values</td><td>Column</td><td>Row</td></tr>
<tr><td><code>np.argmin/argmax()</code></td><td>Index of min/max</td><td>Column</td><td>Row</td></tr>
<tr><td><code>np.cumsum()</code></td><td>Cumulative sum</td><td>Along axis</td><td>Along axis</td></tr>
<tr><td><code>np.cumprod()</code></td><td>Cumulative product</td><td>Along axis</td><td>Along axis</td></tr>
<tr><td><code>np.percentile()</code></td><td>Nth percentile</td><td>Per column</td><td>Per row</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">M = np.array([[<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>],
              [<span class="nm">4</span>, <span class="nm">5</span>, <span class="nm">6</span>],
              [<span class="nm">7</span>, <span class="nm">8</span>, <span class="nm">9</span>]])

<span class="bi">print</span>(<span class="st">f"Total sum:  {M.sum()}"</span>)          <span class="cm"># 45</span>
<span class="bi">print</span>(<span class="st">f"Col sums:   {M.sum(axis=0)}"</span>)    <span class="cm"># [12 15 18]</span>
<span class="bi">print</span>(<span class="st">f"Row sums:   {M.sum(axis=1)}"</span>)    <span class="cm"># [6 15 24]</span>
<span class="bi">print</span>(<span class="st">f"Mean:       {M.mean():.2f}"</span>)      <span class="cm"># 5.00</span>
<span class="bi">print</span>(<span class="st">f"Col means:  {M.mean(axis=0)}"</span>)   <span class="cm"># [4. 5. 6.]</span>
<span class="bi">print</span>(<span class="st">f"Std:        {M.std():.4f}"</span>)       <span class="cm"># 2.5820</span>
<span class="bi">print</span>(<span class="st">f"Min:        {M.min()}"</span>)            <span class="cm"># 1</span>
<span class="bi">print</span>(<span class="st">f"Max:        {M.max()}"</span>)            <span class="cm"># 9</span>
<span class="bi">print</span>(<span class="st">f"ArgMax:     {M.argmax()}"</span>)         <span class="cm"># 8 (flat index)</span>
<span class="bi">print</span>(<span class="st">f"ArgMax cols:{M.argmax(axis=0)}"</span>)  <span class="cm"># [2 2 2]</span>

<span class="cm"># Cumulative</span>
<span class="bi">print</span>(<span class="st">f"Cumsum: {np.cumsum([1,2,3,4,5])}"</span>)   <span class="cm"># [1 3 6 10 15]</span>
<span class="bi">print</span>(<span class="st">f"Cumprod:{np.cumprod([1,2,3,4,5])}"</span>)  <span class="cm"># [1 2 6 24 120]</span>

<span class="cm"># Percentiles &amp; quantiles</span>
data = np.array([<span class="nm">2</span>, <span class="nm">5</span>, <span class="nm">8</span>, <span class="nm">12</span>, <span class="nm">15</span>, <span class="nm">20</span>, <span class="nm">25</span>])
<span class="bi">print</span>(<span class="st">f"25th percentile: {np.percentile(data, 25)}"</span>)  <span class="cm"># 6.5</span>
<span class="bi">print</span>(<span class="st">f"75th percentile: {np.percentile(data, 75)}"</span>)  <span class="cm"># 17.5</span>
<span class="bi">print</span>(<span class="st">f"Median:          {np.median(data)}"</span>)          <span class="cm"># 12.0</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Total sum: 45 &middot; Col sums: [12 15 18] &middot; Row sums: [6 15 24]<br>Mean: 5.00 &middot; Std: 2.5820<br>Cumsum: [1 3 6 10 15]<br>25th%: 6.5 &middot; 75th%: 17.5 &middot; Median: 12.0</div></div></section>''',
("indexing.html","Indexing &amp; Slicing"),("reshaping.html","Reshaping &amp; Stacking"))

print("operations.html expanded!")
