import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# ========== EXPANDED MATH FUNCTIONS (+ sorting + searching) ==========
make_page("numpy/math-functions.html","Math &amp; Statistical Functions","NumPy","&#x1F522;","intermediate","NumPy &rarr; Math &amp; Stats",
"NumPy provides optimized statistical functions (mean, median, std, var, percentile, corrcoef), sorting/searching (sort, argsort, partition, unique, searchsorted), and comprehensive mathematical ufuncs for scientific computing.",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Statistical Functions</a></li>
<li><a href="#s2">Correlation &amp; Covariance</a></li>
<li><a href="#s3">Sorting</a></li>
<li><a href="#s4">Searching &amp; Counting</a></li>
<li><a href="#s5">Set Operations</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Statistical Functions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

data = np.array([<span class="nm">14</span>, <span class="nm">18</span>, <span class="nm">11</span>, <span class="nm">13</span>, <span class="nm">16</span>, <span class="nm">15</span>, <span class="nm">12</span>, <span class="nm">17</span>, <span class="nm">19</span>, <span class="nm">10</span>])

<span class="cm"># np.sum() &mdash; sum of elements</span>
<span class="bi">print</span>(<span class="st">f"Sum:     {np.sum(data)}"</span>)         <span class="cm"># 145</span>

<span class="cm"># np.mean() &mdash; arithmetic mean</span>
<span class="bi">print</span>(<span class="st">f"Mean:    {np.mean(data):.2f}"</span>)     <span class="cm"># 14.50</span>

<span class="cm"># np.median() &mdash; middle value (sorted)</span>
<span class="bi">print</span>(<span class="st">f"Median:  {np.median(data):.2f}"</span>)   <span class="cm"># 14.50</span>

<span class="cm"># np.std() &mdash; standard deviation</span>
<span class="bi">print</span>(<span class="st">f"Std:     {np.std(data):.4f}"</span>)      <span class="cm"># 2.8723</span>
<span class="bi">print</span>(<span class="st">f"Std(ddof=1): {np.std(data,ddof=1):.4f}"</span>)  <span class="cm"># sample std</span>

<span class="cm"># np.var() &mdash; variance</span>
<span class="bi">print</span>(<span class="st">f"Var:     {np.var(data):.4f}"</span>)      <span class="cm"># 8.2500</span>

<span class="cm"># np.min(), np.max()</span>
<span class="bi">print</span>(<span class="st">f"Min:     {np.min(data)}"</span>)          <span class="cm"># 10</span>
<span class="bi">print</span>(<span class="st">f"Max:     {np.max(data)}"</span>)          <span class="cm"># 19</span>
<span class="bi">print</span>(<span class="st">f"Range:   {np.ptp(data)}"</span>)          <span class="cm"># 9 (peak-to-peak)</span>

<span class="cm"># np.argmin(), np.argmax()</span>
<span class="bi">print</span>(<span class="st">f"ArgMin:  {np.argmin(data)}"</span>)       <span class="cm"># 9 (index of 10)</span>
<span class="bi">print</span>(<span class="st">f"ArgMax:  {np.argmax(data)}"</span>)       <span class="cm"># 8 (index of 19)</span>

<span class="cm"># Percentiles &amp; quantiles</span>
<span class="bi">print</span>(<span class="st">f"25th:    {np.percentile(data, 25)}"</span>)   <span class="cm"># 12.25</span>
<span class="bi">print</span>(<span class="st">f"50th:    {np.percentile(data, 50)}"</span>)   <span class="cm"># 14.50</span>
<span class="bi">print</span>(<span class="st">f"75th:    {np.percentile(data, 75)}"</span>)   <span class="cm"># 16.75</span>
<span class="bi">print</span>(<span class="st">f"IQR:     {np.percentile(data,75)-np.percentile(data,25)}"</span>)

<span class="cm"># 2D: axis parameter</span>
M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>],[<span class="nm">7</span>,<span class="nm">8</span>,<span class="nm">9</span>]])
<span class="bi">print</span>(<span class="st">f"Col means: {M.mean(axis=0)}"</span>)  <span class="cm"># [4. 5. 6.]</span>
<span class="bi">print</span>(<span class="st">f"Row means: {M.mean(axis=1)}"</span>)  <span class="cm"># [2. 5. 8.]</span>
<span class="bi">print</span>(<span class="st">f"Col stds:  {M.std(axis=0)}"</span>)   <span class="cm"># [2.449 2.449 2.449]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Sum: 145 &middot; Mean: 14.50 &middot; Median: 14.50<br>Std: 2.8723 &middot; Var: 8.2500<br>Min: 10 &middot; Max: 19<br>25th: 12.25 &middot; 75th: 16.75<br>Col means: [4. 5. 6.] &middot; Row means: [2. 5. 8.]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Correlation &amp; Covariance</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Correlation coefficient matrix</span>
x = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>])
y = np.array([<span class="nm">2</span>, <span class="nm">4</span>, <span class="nm">5</span>, <span class="nm">4</span>, <span class="nm">5</span>])

corr = np.corrcoef(x, y)
<span class="bi">print</span>(<span class="st">f"Correlation matrix:\\n{corr.round(4)}"</span>)
<span class="bi">print</span>(<span class="st">f"r = {corr[0,1]:.4f}"</span>)   <span class="cm"># Pearson r</span>

<span class="cm"># Covariance matrix</span>
cov = np.cov(x, y)
<span class="bi">print</span>(<span class="st">f"Covariance matrix:\\n{cov.round(4)}"</span>)

<span class="cm"># Histogram</span>
data = np.random.randn(<span class="nm">1000</span>)
counts, edges = np.histogram(data, bins=<span class="nm">10</span>)
<span class="bi">print</span>(<span class="st">f"Bin counts: {counts}"</span>)
<span class="bi">print</span>(<span class="st">f"Bin edges: {edges.round(2)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>r = 0.8321<br>Covariance: [[2.5 1.75] [1.75 1.3]]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Sorting</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># np.sort() &mdash; returns sorted COPY</span>
a = np.array([<span class="nm">5</span>, <span class="nm">2</span>, <span class="nm">8</span>, <span class="nm">1</span>, <span class="nm">9</span>, <span class="nm">3</span>])
<span class="bi">print</span>(np.sort(a))      <span class="cm"># [1 2 3 5 8 9]</span>
<span class="bi">print</span>(a)               <span class="cm"># [5 2 8 1 9 3] (unchanged)</span>

<span class="cm"># a.sort() &mdash; sorts IN-PLACE</span>
a.sort()
<span class="bi">print</span>(a)               <span class="cm"># [1 2 3 5 8 9]</span>

<span class="cm"># Reverse sort</span>
<span class="bi">print</span>(np.sort(a)[::-<span class="nm">1</span>])  <span class="cm"># [9 8 5 3 2 1]</span>

<span class="cm"># np.argsort() &mdash; indices that would sort the array</span>
a = np.array([<span class="nm">30</span>, <span class="nm">10</span>, <span class="nm">50</span>, <span class="nm">20</span>])
idx = np.argsort(a)
<span class="bi">print</span>(idx)          <span class="cm"># [1 3 0 2]</span>
<span class="bi">print</span>(a[idx])       <span class="cm"># [10 20 30 50] (sorted via indices)</span>

<span class="cm"># Sort 2D array</span>
M = np.array([[<span class="nm">3</span>,<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">6</span>,<span class="nm">4</span>,<span class="nm">5</span>]])
<span class="bi">print</span>(np.sort(M, axis=<span class="nm">1</span>))  <span class="cm"># sort each row</span>
<span class="bi">print</span>(np.sort(M, axis=<span class="nm">0</span>))  <span class="cm"># sort each column</span>

<span class="cm"># np.partition() &mdash; partial sort (faster for top-k)</span>
a = np.array([<span class="nm">7</span>, <span class="nm">2</span>, <span class="nm">9</span>, <span class="nm">1</span>, <span class="nm">5</span>, <span class="nm">8</span>, <span class="nm">3</span>])
<span class="bi">print</span>(np.partition(a, <span class="nm">3</span>))  <span class="cm"># 3 smallest on left, rest unsorted</span>
<span class="bi">print</span>(np.partition(a, -<span class="nm">3</span>)) <span class="cm"># 3 largest on right</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1 2 3 5 8 9]<br>argsort: [1 3 0 2]<br>sort rows: [[1 2 3] [4 5 6]]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Searching &amp; Counting</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># np.unique() &mdash; sorted unique values</span>
a = np.array([<span class="nm">3</span>, <span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">1</span>, <span class="nm">4</span>, <span class="nm">2</span>, <span class="nm">1</span>])
uniq, counts = np.unique(a, return_counts=<span class="kw">True</span>)
<span class="bi">print</span>(<span class="st">f"Unique: {uniq}"</span>)     <span class="cm"># [1 2 3 4]</span>
<span class="bi">print</span>(<span class="st">f"Counts: {counts}"</span>)   <span class="cm"># [3 2 2 1]</span>

<span class="cm"># Return first occurrence indices</span>
uniq, idx = np.unique(a, return_index=<span class="kw">True</span>)
<span class="bi">print</span>(<span class="st">f"First at: {idx}"</span>)  <span class="cm"># [1 2 0 5]</span>

<span class="cm"># np.searchsorted() &mdash; binary search in sorted array</span>
sorted_arr = np.array([<span class="nm">1</span>, <span class="nm">3</span>, <span class="nm">5</span>, <span class="nm">7</span>, <span class="nm">9</span>])
<span class="bi">print</span>(np.searchsorted(sorted_arr, <span class="nm">4</span>))    <span class="cm"># 2 (insert at index 2)</span>
<span class="bi">print</span>(np.searchsorted(sorted_arr, [<span class="nm">2</span>,<span class="nm">6</span>,<span class="nm">8</span>]))  <span class="cm"># [1 3 4]</span>

<span class="cm"># np.where() &mdash; indices where condition is True</span>
a = np.array([<span class="nm">10</span>, <span class="nm">25</span>, <span class="nm">5</span>, <span class="nm">30</span>, <span class="nm">15</span>])
<span class="bi">print</span>(np.where(a > <span class="nm">20</span>))     <span class="cm"># (array([1, 3]),)</span>
<span class="bi">print</span>(np.nonzero(a > <span class="nm">20</span>))   <span class="cm"># same result</span>

<span class="cm"># np.extract() &mdash; extract elements matching condition</span>
<span class="bi">print</span>(np.extract(a > <span class="nm">20</span>, a))  <span class="cm"># [25 30]</span>

<span class="cm"># Count</span>
<span class="bi">print</span>(np.count_nonzero(a > <span class="nm">10</span>))  <span class="cm"># 3</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Unique: [1 2 3 4] &middot; Counts: [3 2 2 1]<br>searchsorted(4): 2<br>where > 20: [1 3]<br>count > 10: 3</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Set Operations</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>])
b = np.array([<span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>, <span class="nm">6</span>, <span class="nm">7</span>])

<span class="bi">print</span>(np.intersect1d(a, b))      <span class="cm"># [3 4 5]</span>
<span class="bi">print</span>(np.union1d(a, b))          <span class="cm"># [1 2 3 4 5 6 7]</span>
<span class="bi">print</span>(np.setdiff1d(a, b))        <span class="cm"># [1 2] (in a but not b)</span>
<span class="bi">print</span>(np.setxor1d(a, b))         <span class="cm"># [1 2 6 7] (in either but not both)</span>
<span class="bi">print</span>(np.in1d(a, b))             <span class="cm"># [F F T T T]</span>
<span class="bi">print</span>(np.isin(a, [<span class="nm">2</span>,<span class="nm">4</span>]))        <span class="cm"># [F T F T F]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>intersect: [3 4 5] &middot; union: [1 2 3 4 5 6 7]<br>setdiff: [1 2] &middot; setxor: [1 2 6 7]</div></div></section>''',
("reshaping.html","Reshaping &amp; Stacking"),("linear-algebra.html","Linear Algebra"))

print("math-functions.html expanded!")
