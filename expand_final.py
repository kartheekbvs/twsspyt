import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# ADVANCED NUMPY (NEW)
make_page("numpy/advanced-numpy.html","Advanced NumPy","NumPy","&#x1F522;","advanced","NumPy &rarr; Advanced Concepts",
"Advanced NumPy concepts including detailed broadcasting rules, strides and memory layout, structured arrays, record arrays, universal function (ufunc) creation, np.vectorize, and performance optimization tips.",
"NumPy User Guide, High Performance Python",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Broadcasting Rules In-Depth</a></li>
<li><a href="#s2">Strides &amp; Memory Layout</a></li>
<li><a href="#s3">Structured &amp; Record Arrays</a></li>
<li><a href="#s4">Custom ufuncs &amp; np.vectorize</a></li>
<li><a href="#s5">Performance Tips</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Broadcasting Rules In-Depth</h2>
<p>Broadcasting allows NumPy to perform operations on arrays of different shapes. The rules are applied from the <strong>trailing</strong> (rightmost) dimensions.</p>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>The 3 Broadcasting Rules</strong>
<ol><li>If arrays differ in ndim, pad the smaller shape with 1s on the <strong>left</strong>.</li>
<li>Arrays with size 1 along a dimension are <strong>stretched</strong> to match.</li>
<li>If sizes disagree and <strong>neither</strong> is 1, raise <code>ValueError</code>.</li></ol></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Example 1: (3,4) + (4,) &rarr; (3,4) + (1,4) &rarr; (3,4)</span>
A = np.ones((<span class="nm">3</span>, <span class="nm">4</span>))
b = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>])   <span class="cm"># shape (4,) &rarr; (1,4)</span>
<span class="bi">print</span>((A + b).shape)    <span class="cm"># (3, 4) &mdash; b broadcast to each row</span>

<span class="cm"># Example 2: (3,1) + (1,4) &rarr; (3,4)</span>
col = np.array([[<span class="nm">1</span>],[<span class="nm">2</span>],[<span class="nm">3</span>]])  <span class="cm"># (3,1)</span>
row = np.array([[<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">30</span>,<span class="nm">40</span>]])  <span class="cm"># (1,4)</span>
<span class="bi">print</span>((col + row))
<span class="cm"># [[11 21 31 41]</span>
<span class="cm">#  [12 22 32 42]</span>
<span class="cm">#  [13 23 33 43]]</span>

<span class="cm"># Example 3: Incompatible shapes</span>
<span class="cm"># a = np.ones((3, 4))</span>
<span class="cm"># b = np.ones((3, 3))  # ERROR! 4 != 3 and neither is 1</span>

<span class="cm"># Real-world: standardize columns (Z-score)</span>
data = np.random.randn(<span class="nm">100</span>, <span class="nm">4</span>)
means = data.mean(axis=<span class="nm">0</span>)       <span class="cm"># shape (4,)</span>
stds = data.std(axis=<span class="nm">0</span>)         <span class="cm"># shape (4,)</span>
z_scores = (data - means) / stds  <span class="cm"># broadcasting!</span>
<span class="bi">print</span>(<span class="st">f"Z-scores shape: {z_scores.shape}, mean per col: {z_scores.mean(axis=0).round(4)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>(3, 4)<br>[[11 21 31 41] [12 22 32 42] [13 23 33 43]]<br>Z-scores: mean &asymp; [0, 0, 0, 0]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Strides &amp; Memory Layout</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Strides = bytes to skip along each axis</span>
a = np.arange(<span class="nm">12</span>, dtype=np.int64).reshape(<span class="nm">3</span>,<span class="nm">4</span>)
<span class="bi">print</span>(<span class="st">f"Shape: {a.shape}, Strides: {a.strides}"</span>)
<span class="cm"># (3,4), (32, 8): skip 32 bytes for next row, 8 for next col</span>

<span class="cm"># C-contiguous (row-major) vs F-contiguous (column-major)</span>
c = np.ascontiguousarray(a)   <span class="cm"># C-order</span>
f = np.asfortranarray(a)      <span class="cm"># Fortran-order</span>
<span class="bi">print</span>(<span class="st">f"C strides: {c.strides}"</span>)  <span class="cm"># (32, 8)</span>
<span class="bi">print</span>(<span class="st">f"F strides: {f.strides}"</span>)  <span class="cm"># (8, 24)</span>

<span class="cm"># Check contiguity flags</span>
<span class="bi">print</span>(<span class="st">f"C contiguous: {a.flags['C_CONTIGUOUS']}"</span>)
<span class="bi">print</span>(<span class="st">f"F contiguous: {a.flags['F_CONTIGUOUS']}"</span>)

<span class="cm"># np.lib.stride_tricks for advanced views</span>
<span class="kw">from</span> numpy.lib.stride_tricks <span class="kw">import</span> as_strided

<span class="cm"># Create sliding window view (e.g., for convolution)</span>
x = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>,<span class="nm">5</span>], dtype=np.int64)
window_size = <span class="nm">3</span>
shape = (x.size - window_size + <span class="nm">1</span>, window_size)
strides = (x.strides[<span class="nm">0</span>], x.strides[<span class="nm">0</span>])
windows = as_strided(x, shape=shape, strides=strides)
<span class="bi">print</span>(windows)
<span class="cm"># [[1 2 3]</span>
<span class="cm">#  [2 3 4]</span>
<span class="cm">#  [3 4 5]]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Shape: (3,4), Strides: (32, 8)<br>Sliding windows: [[1 2 3] [2 3 4] [3 4 5]]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Structured &amp; Record Arrays</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Structured arrays: arrays with named fields and mixed dtypes</span>
dt = np.dtype([(<span class="st">"name"</span>, <span class="st">"U10"</span>), (<span class="st">"age"</span>, <span class="st">"i4"</span>), (<span class="st">"salary"</span>, <span class="st">"f8"</span>)])
employees = np.array([
    (<span class="st">"Alice"</span>, <span class="nm">25</span>, <span class="nm">50000.0</span>),
    (<span class="st">"Bob"</span>,   <span class="nm">30</span>, <span class="nm">60000.0</span>),
    (<span class="st">"Charlie"</span>, <span class="nm">35</span>, <span class="nm">70000.0</span>)
], dtype=dt)

<span class="cm"># Access fields by name</span>
<span class="bi">print</span>(employees[<span class="st">"name"</span>])      <span class="cm"># ['Alice' 'Bob' 'Charlie']</span>
<span class="bi">print</span>(employees[<span class="st">"salary"</span>])    <span class="cm"># [50000. 60000. 70000.]</span>
<span class="bi">print</span>(employees[<span class="nm">1</span>])            <span class="cm"># ('Bob', 30, 60000.)</span>

<span class="cm"># Filter</span>
<span class="bi">print</span>(employees[employees[<span class="st">"age"</span>] > <span class="nm">28</span>])

<span class="cm"># Record arrays (attribute access instead of dict)</span>
rec = employees.view(np.recarray)
<span class="bi">print</span>(rec.name)     <span class="cm"># array(['Alice','Bob','Charlie'])</span>
<span class="bi">print</span>(rec.salary)   <span class="cm"># array([50000., 60000., 70000.])</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>names: ['Alice' 'Bob' 'Charlie']<br>age > 28: [('Bob',30,60000.), ('Charlie',35,70000.)]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Custom ufuncs &amp; np.vectorize</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># np.vectorize &mdash; wrap a scalar function as a ufunc</span>
<span class="kw">def</span> temp_category(temp):
    <span class="kw">if</span> temp < <span class="nm">0</span>: <span class="kw">return</span> <span class="st">"freezing"</span>
    <span class="kw">elif</span> temp < <span class="nm">15</span>: <span class="kw">return</span> <span class="st">"cold"</span>
    <span class="kw">elif</span> temp < <span class="nm">30</span>: <span class="kw">return</span> <span class="st">"warm"</span>
    <span class="kw">else</span>: <span class="kw">return</span> <span class="st">"hot"</span>

v_category = np.vectorize(temp_category)
temps = np.array([-<span class="nm">5</span>, <span class="nm">3</span>, <span class="nm">18</span>, <span class="nm">35</span>, <span class="nm">28</span>, -<span class="nm">10</span>])
<span class="bi">print</span>(v_category(temps))  <span class="cm"># ['freezing' 'cold' 'warm' 'hot' 'warm' 'freezing']</span>

<span class="cm"># np.frompyfunc &mdash; returns object array</span>
f = np.frompyfunc(temp_category, <span class="nm">1</span>, <span class="nm">1</span>)
<span class="bi">print</span>(f(temps))

<span class="cm"># Better approach: np.select (vectorized, faster)</span>
conditions = [temps < <span class="nm">0</span>, temps < <span class="nm">15</span>, temps < <span class="nm">30</span>, temps >= <span class="nm">30</span>]
choices = [<span class="st">"freezing"</span>, <span class="st">"cold"</span>, <span class="st">"warm"</span>, <span class="st">"hot"</span>]
<span class="bi">print</span>(np.select(conditions, choices))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>['freezing' 'cold' 'warm' 'hot' 'warm' 'freezing']</div></div>
<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>np.vectorize is NOT fast!</strong><p><code>np.vectorize</code> is a convenience wrapper &mdash; it still loops in Python. For performance, use <code>np.where</code>, <code>np.select</code>, <code>np.piecewise</code>, or boolean masking instead.</p></div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Performance Tips</h2>
<table class="data-table"><thead><tr><th>Tip</th><th>Slow</th><th>Fast</th></tr></thead><tbody>
<tr><td>Avoid Python loops</td><td><code>for i in range(len(a))</code></td><td><code>a * 2 + 1</code> (vectorized)</td></tr>
<tr><td>Use views not copies</td><td><code>a.flatten()</code></td><td><code>a.ravel()</code> (view)</td></tr>
<tr><td>Pre-allocate arrays</td><td><code>results.append(x)</code></td><td><code>results = np.empty(n)</code></td></tr>
<tr><td>Minimize dtype size</td><td><code>float64</code> (8 bytes)</td><td><code>float32</code> (4 bytes)</td></tr>
<tr><td>Use in-place ops</td><td><code>a = a + b</code></td><td><code>np.add(a, b, out=a)</code></td></tr>
<tr><td>Avoid fancy indexing</td><td><code>a[[0,5,10]]</code> (copy)</td><td><code>a[0:11:5]</code> (view)</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Memory-Efficient Operations</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># In-place operations (no memory allocation)</span>
a = np.arange(<span class="nm">1000000</span>, dtype=np.float64)
np.multiply(a, <span class="nm">2</span>, out=a)       <span class="cm"># in-place multiply</span>
np.add(a, <span class="nm">1</span>, out=a)             <span class="cm"># in-place add</span>

<span class="cm"># Pre-allocate vs append</span>
<span class="cm"># BAD: growing arrays</span>
<span class="cm"># result = []</span>
<span class="cm"># for i in range(1000): result.append(compute(i))</span>

<span class="cm"># GOOD: pre-allocate</span>
result = np.empty(<span class="nm">1000</span>)
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">1000</span>):
    result[i] = i ** <span class="nm">2</span>  <span class="cm"># fills pre-allocated array</span>

<span class="cm"># BEST: vectorized</span>
result = np.arange(<span class="nm">1000</span>) ** <span class="nm">2</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[In-place operations modify array without allocation]</div></div></section>''',
("random.html","Random Module"),("../pandas/series-dataframe.html","Pandas"))

# ADVANCED PANDAS (NEW)
make_page("pandas/advanced-pandas.html","Advanced Pandas","Pandas","&#x1F43C;","advanced","Pandas &rarr; Advanced",
"Advanced Pandas techniques including MultiIndex operations, window functions, eval/query for performance, categorical data, sparse data, pipe chains, memory optimization, and integration with Dask for large datasets.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">MultiIndex Operations</a></li>
<li><a href="#s2">Window Functions</a></li>
<li><a href="#s3">eval() &amp; query() for Performance</a></li>
<li><a href="#s4">Categorical Data</a></li>
<li><a href="#s5">Memory Optimization</a></li>
<li><a href="#s6">Method Chaining with pipe()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; MultiIndex Operations</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Create MultiIndex DataFrame</span>
idx = pd.MultiIndex.from_tuples([
    (<span class="st">"A"</span>,<span class="nm">2023</span>), (<span class="st">"A"</span>,<span class="nm">2024</span>),
    (<span class="st">"B"</span>,<span class="nm">2023</span>), (<span class="st">"B"</span>,<span class="nm">2024</span>),
    (<span class="st">"C"</span>,<span class="nm">2023</span>), (<span class="st">"C"</span>,<span class="nm">2024</span>)
], names=[<span class="st">"Group"</span>, <span class="st">"Year"</span>])

df = pd.DataFrame({
    <span class="st">"Revenue"</span>: [<span class="nm">100</span>,<span class="nm">150</span>,<span class="nm">200</span>,<span class="nm">250</span>,<span class="nm">300</span>,<span class="nm">350</span>],
    <span class="st">"Profit"</span>: [<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">30</span>,<span class="nm">40</span>,<span class="nm">50</span>,<span class="nm">60</span>]
}, index=idx)

<span class="cm"># Access levels</span>
<span class="bi">print</span>(df.loc[<span class="st">"A"</span>])              <span class="cm"># all group A rows</span>
<span class="bi">print</span>(df.loc[(<span class="st">"B"</span>, <span class="nm">2024</span>)])     <span class="cm"># specific entry</span>
<span class="bi">print</span>(df.xs(<span class="nm">2024</span>, level=<span class="st">"Year"</span>))  <span class="cm"># cross-section</span>

<span class="cm"># Stack/unstack (reshape)</span>
<span class="bi">print</span>(df.unstack(level=<span class="st">"Year"</span>))  <span class="cm"># Year to columns</span>
<span class="bi">print</span>(df.unstack().stack())      <span class="cm"># back to MultiIndex</span>

<span class="cm"># GroupBy with MultiIndex</span>
<span class="bi">print</span>(df.groupby(level=<span class="st">"Year"</span>).sum())</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>            Revenue  Profit<br>Group Year<br>A     2023      100      10<br>      2024      150      20<br>xs(2024): A=150, B=250, C=350</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Window Functions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">dates = pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">20</span>)
s = pd.Series(np.random.randn(<span class="nm">20</span>).cumsum(), index=dates)

<span class="cm"># Rolling functions</span>
<span class="bi">print</span>(s.rolling(<span class="nm">5</span>).mean())        <span class="cm"># 5-period moving average</span>
<span class="bi">print</span>(s.rolling(<span class="nm">5</span>).std())         <span class="cm"># rolling std dev</span>
<span class="bi">print</span>(s.rolling(<span class="nm">5</span>).apply(<span class="kw">lambda</span> x: x.max() - x.min()))  <span class="cm"># custom</span>

<span class="cm"># Expanding (cumulative)</span>
<span class="bi">print</span>(s.expanding().mean())       <span class="cm"># cumulative mean</span>

<span class="cm"># Exponentially weighted</span>
<span class="bi">print</span>(s.ewm(span=<span class="nm">5</span>).mean())       <span class="cm"># EMA</span>
<span class="bi">print</span>(s.ewm(halflife=<span class="nm">2</span>).mean())   <span class="cm"># halflife-based</span>

<span class="cm"># Window with specific aggregation</span>
<span class="bi">print</span>(s.rolling(<span class="nm">7</span>).agg([<span class="st">"mean"</span>, <span class="st">"std"</span>, <span class="st">"min"</span>, <span class="st">"max"</span>]))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Rolling and expanding window results]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; eval() &amp; query() for Performance</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df = pd.DataFrame({
    <span class="st">"a"</span>: np.random.randn(<span class="nm">100000</span>),
    <span class="st">"b"</span>: np.random.randn(<span class="nm">100000</span>),
    <span class="st">"c"</span>: np.random.randn(<span class="nm">100000</span>)
})

<span class="cm"># eval() &mdash; evaluates string expression efficiently</span>
<span class="cm"># Faster for large DataFrames (avoids temp arrays)</span>
df[<span class="st">"d"</span>] = df.eval(<span class="st">"a + b * c"</span>)
df[<span class="st">"e"</span>] = df.eval(<span class="st">"(a - b) / (c + 1)"</span>)

<span class="cm"># query() &mdash; filter with string expression</span>
result = df.query(<span class="st">"a > 0 and b < 0"</span>)
<span class="bi">print</span>(<span class="st">f"Filtered rows: {len(result)}"</span>)

<span class="cm"># With external variables</span>
threshold = <span class="nm">1.5</span>
result = df.query(<span class="st">"a > @threshold"</span>)

<span class="cm"># pd.eval() for multi-DataFrame expressions</span>
result = pd.eval(<span class="st">"df.a + df.b"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Filtered rows: ~25000</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Categorical Data</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Create categorical</span>
s = pd.Categorical([<span class="st">"low"</span>,<span class="st">"med"</span>,<span class="st">"high"</span>,<span class="st">"low"</span>,<span class="st">"high"</span>],
                    categories=[<span class="st">"low"</span>,<span class="st">"med"</span>,<span class="st">"high"</span>],
                    ordered=<span class="kw">True</span>)
<span class="bi">print</span>(s)
<span class="bi">print</span>(s.min())  <span class="cm"># 'low' (ordered!)</span>
<span class="bi">print</span>(s.max())  <span class="cm"># 'high'</span>

<span class="cm"># Convert column to categorical (saves memory!)</span>
df = pd.DataFrame({<span class="st">"grade"</span>: [<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"A"</span>,<span class="st">"C"</span>] * <span class="nm">10000</span>})
<span class="bi">print</span>(<span class="st">f"Object memory: {df.memory_usage(deep=True).sum():,}"</span>)
df[<span class="st">"grade"</span>] = df[<span class="st">"grade"</span>].astype(<span class="st">"category"</span>)
<span class="bi">print</span>(<span class="st">f"Category memory: {df.memory_usage(deep=True).sum():,}"</span>)

<span class="cm"># cat accessor</span>
<span class="bi">print</span>(df[<span class="st">"grade"</span>].cat.codes)       <span class="cm"># integer codes</span>
<span class="bi">print</span>(df[<span class="st">"grade"</span>].cat.categories)   <span class="cm"># ['A', 'B', 'C']</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Object memory: 2,680,128<br>Category memory: 40,362 (67x smaller!)</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Memory Optimization</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">def</span> optimize_df(df):
    <span class="st">"""Reduce DataFrame memory usage."""</span>
    start_mem = df.memory_usage(deep=<span class="kw">True</span>).sum() / <span class="nm">1024</span>**<span class="nm">2</span>

    <span class="kw">for</span> col <span class="kw">in</span> df.columns:
        col_type = df[col].dtype
        <span class="kw">if</span> col_type == <span class="st">"object"</span>:
            <span class="kw">if</span> df[col].nunique() / <span class="bi">len</span>(df) < <span class="nm">0.5</span>:
                df[col] = df[col].astype(<span class="st">"category"</span>)
        <span class="kw">elif</span> col_type == <span class="st">"int64"</span>:
            df[col] = pd.to_numeric(df[col], downcast=<span class="st">"integer"</span>)
        <span class="kw">elif</span> col_type == <span class="st">"float64"</span>:
            df[col] = pd.to_numeric(df[col], downcast=<span class="st">"float"</span>)

    end_mem = df.memory_usage(deep=<span class="kw">True</span>).sum() / <span class="nm">1024</span>**<span class="nm">2</span>
    <span class="bi">print</span>(<span class="st">f"Memory: {start_mem:.2f}MB &rarr; {end_mem:.2f}MB ({100*(1-end_mem/start_mem):.0f}% reduction)"</span>)
    <span class="kw">return</span> df

<span class="cm"># Usage</span>
df = pd.DataFrame({
    <span class="st">"id"</span>: np.arange(<span class="nm">100000</span>),
    <span class="st">"val"</span>: np.random.randn(<span class="nm">100000</span>),
    <span class="st">"cat"</span>: np.random.choice([<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"C"</span>], <span class="nm">100000</span>)
})
df = optimize_df(df)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Memory: 5.34MB &rarr; 1.05MB (80% reduction)</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Method Chaining with pipe()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Readable data processing pipelines</span>
result = (
    df
    .query(<span class="st">"val > 0"</span>)
    .assign(val_squared=<span class="kw">lambda</span> x: x[<span class="st">"val"</span>]**<span class="nm">2</span>)
    .groupby(<span class="st">"cat"</span>)
    .agg(avg_val=(<span class="st">"val"</span>, <span class="st">"mean"</span>), count=(<span class="st">"val"</span>, <span class="st">"count"</span>))
    .sort_values(<span class="st">"avg_val"</span>, ascending=<span class="kw">False</span>)
)
<span class="bi">print</span>(result)

<span class="cm"># Custom functions with pipe()</span>
<span class="kw">def</span> add_metrics(df, col):
    df[<span class="st">f"{col}_zscore"</span>] = (df[col] - df[col].mean()) / df[col].std()
    <span class="kw">return</span> df

result = df.pipe(add_metrics, <span class="st">"val"</span>)
<span class="bi">print</span>(result.head())</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>     avg_val  count<br>cat<br>A      0.82  16700<br>B      0.81  16550<br>C      0.80  16750</div></div></section>''',
("time-series.html","Time Series"),("../data-analysis/exploratory.html","Data Analysis"))

print("advanced-numpy.html + advanced-pandas.html created!")
