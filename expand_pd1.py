import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# ========== EXPANDED SERIES & DATAFRAME ==========
make_page("pandas/series-dataframe.html","Series &amp; DataFrame","Pandas","&#x1F43C;","beginner","Pandas &rarr; Series &amp; DataFrame",
"Pandas provides two primary data structures: Series (1D labeled array) and DataFrame (2D labeled table). Built on NumPy, they support heterogeneous data types, automatic alignment, and powerful indexing. This covers creating, inspecting, and understanding both structures along with Index and MultiIndex.",
"Python for Data Analysis &mdash; Wes McKinney, Data Science and Analytics with Python",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">What is Pandas &amp; Why Use It</a></li>
<li><a href="#s2">Series</a></li>
<li><a href="#s3">DataFrame</a></li>
<li><a href="#s4">Creating DataFrames</a></li>
<li><a href="#s5">DataFrame Attributes</a></li>
<li><a href="#s6">Index &amp; MultiIndex</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; What is Pandas &amp; Why Use It</h2>
<p>Pandas is the most popular Python library for data manipulation and analysis. It provides fast, flexible data structures designed to work with <em>relational</em> or <em>labeled</em> data &mdash; think spreadsheets, SQL tables, or CSV files.</p>
<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Pandas vs NumPy</strong>
<table style="width:100%;font-size:.85rem">
<tr><th>Feature</th><th>NumPy</th><th>Pandas</th></tr>
<tr><td>Data types</td><td>Homogeneous (one dtype)</td><td>Heterogeneous (mixed)</td></tr>
<tr><td>Labels</td><td>Integer indices only</td><td>Custom labels (strings, dates)</td></tr>
<tr><td>Missing data</td><td>No built-in NaN handling</td><td>First-class NaN support</td></tr>
<tr><td>Data loading</td><td>Basic (loadtxt)</td><td>Rich (CSV, Excel, SQL, JSON)</td></tr>
<tr><td>Best for</td><td>Numerical computation</td><td>Data wrangling &amp; analysis</td></tr>
</table></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Installation &amp; Import</span>
<span class="cm"># pip install pandas</span>
<span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np
<span class="bi">print</span>(pd.__version__)  <span class="cm"># e.g., 2.2.1</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>2.2.1</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Series (1D Labeled Array)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># From list</span>
s = pd.Series([<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>, <span class="nm">40</span>])
<span class="bi">print</span>(s)
<span class="cm"># 0    10</span>
<span class="cm"># 1    20</span>
<span class="cm"># 2    30</span>
<span class="cm"># 3    40</span>
<span class="cm"># dtype: int64</span>

<span class="cm"># With custom index</span>
s = pd.Series([<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>], index=[<span class="st">"a"</span>, <span class="st">"b"</span>, <span class="st">"c"</span>])
<span class="bi">print</span>(s[<span class="st">"b"</span>])   <span class="cm"># 20</span>

<span class="cm"># From dictionary</span>
d = {<span class="st">"apples"</span>: <span class="nm">5</span>, <span class="st">"bananas"</span>: <span class="nm">3</span>, <span class="st">"oranges"</span>: <span class="nm">8</span>}
s = pd.Series(d)
<span class="bi">print</span>(s)

<span class="cm"># From NumPy array</span>
s = pd.Series(np.arange(<span class="nm">5</span>), index=[<span class="st">"a"</span>,<span class="st">"b"</span>,<span class="st">"c"</span>,<span class="st">"d"</span>,<span class="st">"e"</span>])

<span class="cm"># Series attributes</span>
<span class="bi">print</span>(<span class="st">f"values: {s.values}"</span>)      <span class="cm"># underlying NumPy array</span>
<span class="bi">print</span>(<span class="st">f"index:  {s.index.tolist()}"</span>)
<span class="bi">print</span>(<span class="st">f"dtype:  {s.dtype}"</span>)
<span class="bi">print</span>(<span class="st">f"name:   {s.name}"</span>)        <span class="cm"># None (can be set)</span>
<span class="bi">print</span>(<span class="st">f"shape:  {s.shape}"</span>)       <span class="cm"># (5,)</span>

<span class="cm"># Vectorized operations</span>
<span class="bi">print</span>(s * <span class="nm">2</span>)        <span class="cm"># multiply all by 2</span>
<span class="bi">print</span>(s[s > <span class="nm">2</span>])     <span class="cm"># boolean filter</span>
<span class="bi">print</span>(s.mean())     <span class="cm"># 2.0</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>a    0<br>b    1<br>c    2<br>d    3<br>e    4<br>dtype: int64</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; DataFrame (2D Labeled Table)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># From dictionary of lists</span>
df = pd.DataFrame({
    <span class="st">"Name"</span>:    [<span class="st">"Alice"</span>, <span class="st">"Bob"</span>, <span class="st">"Charlie"</span>, <span class="st">"Diana"</span>],
    <span class="st">"Age"</span>:     [<span class="nm">25</span>, <span class="nm">30</span>, <span class="nm">35</span>, <span class="nm">28</span>],
    <span class="st">"Salary"</span>:  [<span class="nm">50000</span>, <span class="nm">60000</span>, <span class="nm">70000</span>, <span class="nm">55000</span>],
    <span class="st">"Dept"</span>:    [<span class="st">"Eng"</span>, <span class="st">"Mkt"</span>, <span class="st">"Eng"</span>, <span class="st">"Mkt"</span>]
})
<span class="bi">print</span>(df)
<span class="cm">#       Name  Age  Salary Dept</span>
<span class="cm"># 0    Alice   25   50000  Eng</span>
<span class="cm"># 1      Bob   30   60000  Mkt</span>
<span class="cm"># 2  Charlie   35   70000  Eng</span>
<span class="cm"># 3    Diana   28   55000  Mkt</span>

<span class="cm"># Quick inspection</span>
<span class="bi">print</span>(df.head(<span class="nm">2</span>))     <span class="cm"># first 2 rows</span>
<span class="bi">print</span>(df.tail(<span class="nm">2</span>))     <span class="cm"># last 2 rows</span>
<span class="bi">print</span>(df.info())      <span class="cm"># dtypes, non-null counts, memory</span>
<span class="bi">print</span>(df.describe())  <span class="cm"># stats for numeric columns</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>      Name  Age  Salary Dept<br>0    Alice   25   50000  Eng<br>1      Bob   30   60000  Mkt<br>2  Charlie   35   70000  Eng<br>3    Diana   28   55000  Mkt</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Creating DataFrames (All Methods)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># 1. From dictionary of lists</span>
df1 = pd.DataFrame({<span class="st">"a"</span>: [<span class="nm">1</span>,<span class="nm">2</span>], <span class="st">"b"</span>: [<span class="nm">3</span>,<span class="nm">4</span>]})

<span class="cm"># 2. From list of dictionaries</span>
df2 = pd.DataFrame([{<span class="st">"a"</span>:<span class="nm">1</span>,<span class="st">"b"</span>:<span class="nm">2</span>}, {<span class="st">"a"</span>:<span class="nm">3</span>,<span class="st">"b"</span>:<span class="nm">4</span>}])

<span class="cm"># 3. From list of lists</span>
df3 = pd.DataFrame([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]], columns=[<span class="st">"a"</span>,<span class="st">"b"</span>])

<span class="cm"># 4. From NumPy array</span>
df4 = pd.DataFrame(np.random.randn(<span class="nm">3</span>,<span class="nm">4</span>), columns=[<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"C"</span>,<span class="st">"D"</span>])

<span class="cm"># 5. From CSV file</span>
<span class="cm"># df5 = pd.read_csv("data.csv")</span>

<span class="cm"># 6. From Excel file</span>
<span class="cm"># df6 = pd.read_excel("data.xlsx", sheet_name="Sheet1")</span>

<span class="cm"># 7. From JSON</span>
<span class="cm"># df7 = pd.read_json("data.json")</span>

<span class="cm"># 8. From SQL database</span>
<span class="cm"># import sqlite3</span>
<span class="cm"># conn = sqlite3.connect("database.db")</span>
<span class="cm"># df8 = pd.read_sql("SELECT * FROM table", conn)</span>

<span class="cm"># 9. From Series</span>
s1 = pd.Series([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], name=<span class="st">"x"</span>)
s2 = pd.Series([<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>], name=<span class="st">"y"</span>)
df9 = pd.concat([s1, s2], axis=<span class="nm">1</span>)
<span class="bi">print</span>(df9)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>   x  y<br>0  1  4<br>1  2  5<br>2  3  6</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; DataFrame Attributes</h2>
<table class="data-table"><thead><tr><th>Attribute</th><th>Returns</th><th>Example</th></tr></thead><tbody>
<tr><td><code>df.shape</code></td><td>(rows, cols) tuple</td><td><code>(4, 4)</code></td></tr>
<tr><td><code>df.columns</code></td><td>Column labels</td><td><code>Index(['Name','Age',...])</code></td></tr>
<tr><td><code>df.index</code></td><td>Row labels</td><td><code>RangeIndex(start=0,...)</code></td></tr>
<tr><td><code>df.dtypes</code></td><td>Column data types</td><td><code>Name: object, Age: int64</code></td></tr>
<tr><td><code>df.values</code></td><td>NumPy array of data</td><td><code>ndarray</code></td></tr>
<tr><td><code>df.axes</code></td><td>[index, columns]</td><td>List of 2 Index objects</td></tr>
<tr><td><code>df.ndim</code></td><td>Number of dimensions</td><td><code>2</code></td></tr>
<tr><td><code>df.size</code></td><td>Total element count</td><td><code>16</code></td></tr>
<tr><td><code>df.empty</code></td><td>Boolean if empty</td><td><code>False</code></td></tr>
<tr><td><code>df.T</code></td><td>Transposed DataFrame</td><td>Rows &harr; Columns</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df = pd.DataFrame({<span class="st">"Name"</span>:[<span class="st">"Alice"</span>,<span class="st">"Bob"</span>], <span class="st">"Age"</span>:[<span class="nm">25</span>,<span class="nm">30</span>], <span class="st">"Sal"</span>:[<span class="nm">50000</span>,<span class="nm">60000</span>]})

<span class="bi">print</span>(<span class="st">f"shape:   {df.shape}"</span>)               <span class="cm"># (2, 3)</span>
<span class="bi">print</span>(<span class="st">f"columns: {df.columns.tolist()}"</span>)    <span class="cm"># ['Name', 'Age', 'Sal']</span>
<span class="bi">print</span>(<span class="st">f"index:   {df.index.tolist()}"</span>)      <span class="cm"># [0, 1]</span>
<span class="bi">print</span>(<span class="st">f"dtypes:\\n{df.dtypes}"</span>)
<span class="bi">print</span>(<span class="st">f"ndim:    {df.ndim}"</span>)                <span class="cm"># 2</span>
<span class="bi">print</span>(<span class="st">f"size:    {df.size}"</span>)                <span class="cm"># 6</span>

<span class="cm"># Memory usage</span>
<span class="bi">print</span>(df.memory_usage(deep=<span class="kw">True</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>shape: (2, 3)<br>columns: ['Name', 'Age', 'Sal']<br>dtypes: Name-object, Age-int64, Sal-int64<br>ndim: 2 &middot; size: 6</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Index &amp; MultiIndex</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Custom index</span>
df = pd.DataFrame({<span class="st">"val"</span>: [<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">30</span>]}, index=[<span class="st">"a"</span>,<span class="st">"b"</span>,<span class="st">"c"</span>])
<span class="bi">print</span>(df.loc[<span class="st">"b"</span>])  <span class="cm"># access by label</span>

<span class="cm"># Set/reset index</span>
df = pd.DataFrame({<span class="st">"id"</span>: [<span class="nm">101</span>,<span class="nm">102</span>,<span class="nm">103</span>], <span class="st">"name"</span>: [<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"C"</span>], <span class="st">"val"</span>: [<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>]})
df = df.set_index(<span class="st">"id"</span>)
<span class="bi">print</span>(df)
df = df.reset_index()  <span class="cm"># back to default int index</span>

<span class="cm"># MultiIndex (hierarchical)</span>
arrays = [[<span class="st">"A"</span>,<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"B"</span>], [<span class="nm">2023</span>,<span class="nm">2024</span>,<span class="nm">2023</span>,<span class="nm">2024</span>]]
idx = pd.MultiIndex.from_arrays(arrays, names=[<span class="st">"Group"</span>,<span class="st">"Year"</span>])
df = pd.DataFrame({<span class="st">"Sales"</span>: [<span class="nm">100</span>,<span class="nm">150</span>,<span class="nm">200</span>,<span class="nm">250</span>]}, index=idx)
<span class="bi">print</span>(df)
<span class="bi">print</span>(df.loc[<span class="st">"A"</span>])           <span class="cm"># group A rows</span>
<span class="bi">print</span>(df.loc[(<span class="st">"B"</span>, <span class="nm">2024</span>)])   <span class="cm"># specific entry</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>            Sales<br>Group Year<br>A     2023    100<br>      2024    150<br>B     2023    200<br>      2024    250</div></div></section>''',
("../numpy/random.html","NumPy Random"),("reading-data.html","Reading Data"))

print("series-dataframe.html expanded!")
