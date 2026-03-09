import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# READING DATA
make_page("pandas/reading-data.html","Reading &amp; Writing Data","Pandas","&#x1F43C;","beginner","Pandas &rarr; Reading Data",
"Pandas can read data from CSV, Excel, JSON, SQL, HTML, parquet and more using pd.read_*() functions. It also writes to all these formats. This covers all major I/O operations with practical examples for handling headers, dtypes, encoding, and chunked reading for large files.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">CSV Files</a></li>
<li><a href="#s2">Excel Files</a></li>
<li><a href="#s3">JSON, SQL &amp; Other Formats</a></li>
<li><a href="#s4">Writing Data</a></li>
<li><a href="#s5">Large File Strategies</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; CSV Files (pd.read_csv)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd

<span class="cm"># Basic CSV read</span>
<span class="cm"># df = pd.read_csv("data.csv")</span>

<span class="cm"># Common parameters:</span>
<span class="cm"># df = pd.read_csv("data.csv",</span>
<span class="cm">#     sep=",",              # delimiter (default comma)</span>
<span class="cm">#     header=0,             # row number for headers (None = no header)</span>
<span class="cm">#     names=["A","B","C"],  # custom column names</span>
<span class="cm">#     index_col=0,          # column to use as index</span>
<span class="cm">#     usecols=["A","C"],    # load only certain columns</span>
<span class="cm">#     dtype={"A": int},     # specify dtypes</span>
<span class="cm">#     parse_dates=["date"], # parse date columns</span>
<span class="cm">#     na_values=["NA","?"], # additional NaN markers</span>
<span class="cm">#     skiprows=2,           # skip first N rows</span>
<span class="cm">#     nrows=100,            # read only first 100 rows</span>
<span class="cm">#     encoding="utf-8",     # file encoding</span>
<span class="cm">#     skipfooter=1,         # skip last N rows</span>
<span class="cm"># )</span>

<span class="cm"># From string (for demo)</span>
<span class="kw">from</span> io <span class="kw">import</span> StringIO
csv_text = <span class="st">"""name,age,salary
Alice,25,50000
Bob,30,60000
Charlie,35,70000"""</span>

df = pd.read_csv(StringIO(csv_text))
<span class="bi">print</span>(df)
<span class="bi">print</span>(df.dtypes)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>      name  age  salary<br>0    Alice   25   50000<br>1      Bob   30   60000<br>2  Charlie   35   70000<br>name: object, age: int64, salary: int64</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; TSV &amp; Custom Delimiters</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Tab-separated values</span>
<span class="cm"># df = pd.read_csv("data.tsv", sep="\\t")</span>

<span class="cm"># Pipe-separated</span>
<span class="cm"># df = pd.read_csv("data.txt", sep="|")</span>

<span class="cm"># No header</span>
<span class="cm"># df = pd.read_csv("data.csv", header=None, names=["col1","col2"])</span></pre></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Excel Files</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># pip install openpyxl</span>

<span class="cm"># Read Excel</span>
<span class="cm"># df = pd.read_excel("data.xlsx")</span>
<span class="cm"># df = pd.read_excel("data.xlsx", sheet_name="Sheet2")</span>
<span class="cm"># df = pd.read_excel("data.xlsx", sheet_name=0)  # first sheet</span>

<span class="cm"># Read ALL sheets (returns dict of DataFrames)</span>
<span class="cm"># all_sheets = pd.read_excel("data.xlsx", sheet_name=None)</span>
<span class="cm"># for name, df in all_sheets.items():</span>
<span class="cm">#     print(f"Sheet: {name}, Shape: {df.shape}")</span>

<span class="cm"># Write Excel</span>
<span class="cm"># df.to_excel("output.xlsx", sheet_name="Results", index=False)</span>

<span class="cm"># Multiple sheets to one file</span>
<span class="cm"># with pd.ExcelWriter("output.xlsx") as writer:</span>
<span class="cm">#     df1.to_excel(writer, sheet_name="Data")</span>
<span class="cm">#     df2.to_excel(writer, sheet_name="Summary")</span></pre></div></section>

<section class="content-section" id="s3"><h2>3 &middot; JSON, SQL &amp; Other Formats</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># JSON</span>
<span class="cm"># df = pd.read_json("data.json")</span>
<span class="cm"># df = pd.read_json("data.json", orient="records")</span>

<span class="cm"># SQL Database</span>
<span class="cm"># import sqlite3</span>
<span class="cm"># conn = sqlite3.connect("database.db")</span>
<span class="cm"># df = pd.read_sql("SELECT * FROM users WHERE age > 20", conn)</span>
<span class="cm"># df = pd.read_sql_table("users", conn)  # entire table</span>
<span class="cm"># df.to_sql("results", conn, if_exists="replace", index=False)</span>

<span class="cm"># HTML tables (scraping)</span>
<span class="cm"># tables = pd.read_html("https://example.com/table-page")</span>
<span class="cm"># df = tables[0]  # first table on page</span>

<span class="cm"># Parquet (fast columnar format)</span>
<span class="cm"># df = pd.read_parquet("data.parquet")</span>
<span class="cm"># df.to_parquet("output.parquet", compression="snappy")</span>

<span class="cm"># Clipboard</span>
<span class="cm"># df = pd.read_clipboard()  # paste from spreadsheet!</span></pre></div>
<table class="data-table"><thead><tr><th>Format</th><th>Read Function</th><th>Write Method</th><th>Install</th></tr></thead><tbody>
<tr><td>CSV</td><td><code>pd.read_csv()</code></td><td><code>df.to_csv()</code></td><td>built-in</td></tr>
<tr><td>Excel</td><td><code>pd.read_excel()</code></td><td><code>df.to_excel()</code></td><td>openpyxl</td></tr>
<tr><td>JSON</td><td><code>pd.read_json()</code></td><td><code>df.to_json()</code></td><td>built-in</td></tr>
<tr><td>SQL</td><td><code>pd.read_sql()</code></td><td><code>df.to_sql()</code></td><td>sqlalchemy</td></tr>
<tr><td>Parquet</td><td><code>pd.read_parquet()</code></td><td><code>df.to_parquet()</code></td><td>pyarrow</td></tr>
<tr><td>HTML</td><td><code>pd.read_html()</code></td><td><code>df.to_html()</code></td><td>lxml</td></tr>
<tr><td>Clipboard</td><td><code>pd.read_clipboard()</code></td><td><code>df.to_clipboard()</code></td><td>built-in</td></tr>
</tbody></table></section>

<section class="content-section" id="s4"><h2>4 &middot; Writing Data</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> io <span class="kw">import</span> StringIO
df = pd.DataFrame({<span class="st">"a"</span>:[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], <span class="st">"b"</span>:[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]})

<span class="cm"># CSV</span>
<span class="cm"># df.to_csv("output.csv", index=False)</span>
<span class="bi">print</span>(df.to_csv(index=<span class="kw">False</span>))  <span class="cm"># to string</span>

<span class="cm"># JSON</span>
<span class="bi">print</span>(df.to_json(orient=<span class="st">"records"</span>, indent=<span class="nm">2</span>))

<span class="cm"># HTML</span>
<span class="bi">print</span>(df.to_html(index=<span class="kw">False</span>))

<span class="cm"># Markdown</span>
<span class="bi">print</span>(df.to_markdown())

<span class="cm"># String representation</span>
<span class="bi">print</span>(df.to_string())</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>a,b<br>1,4<br>2,5<br>3,6</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Large File Strategies</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Chunk processing (for files larger than RAM)</span>
<span class="cm"># chunks = pd.read_csv("huge.csv", chunksize=10000)</span>
<span class="cm"># for chunk in chunks:</span>
<span class="cm">#     process(chunk)  # process 10K rows at a time</span>

<span class="cm"># Read only needed columns</span>
<span class="cm"># df = pd.read_csv("big.csv", usecols=["id", "value"])</span>

<span class="cm"># Optimize dtypes on load</span>
<span class="cm"># df = pd.read_csv("big.csv", dtype={"id": "int32", "cat": "category"})</span>

<span class="cm"># First N rows only</span>
<span class="cm"># df = pd.read_csv("big.csv", nrows=1000)</span></pre></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Memory Tip</strong><p>Use <code>dtype={{"col": "category"}}</code> for string columns with few unique values (like gender, country). This can reduce memory by 90%+. Use <code>int32</code> instead of <code>int64</code> for smaller integers.</p></div></div></section>''',
("series-dataframe.html","Series &amp; DataFrame"),("selection.html","Selection &amp; Filtering"))

# SELECTION & FILTERING
make_page("pandas/selection.html","Selection &amp; Filtering","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Selection",
"Pandas provides multiple powerful ways to select data: [] operator for columns, .loc for label-based selection, .iloc for integer-based selection, .at/.iat for single values, and boolean indexing for conditional filtering. Mastering these is essential for efficient data manipulation.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Column Selection</a></li>
<li><a href="#s2">.loc (Label-Based)</a></li>
<li><a href="#s3">.iloc (Integer-Based)</a></li>
<li><a href="#s4">.at &amp; .iat (Scalar Access)</a></li>
<li><a href="#s5">Boolean Indexing &amp; Filtering</a></li>
<li><a href="#s6">query() Method</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Column Selection</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
df = pd.DataFrame({
    <span class="st">"Name"</span>: [<span class="st">"Alice"</span>,<span class="st">"Bob"</span>,<span class="st">"Charlie"</span>,<span class="st">"Diana"</span>],
    <span class="st">"Age"</span>: [<span class="nm">25</span>,<span class="nm">30</span>,<span class="nm">35</span>,<span class="nm">28</span>],
    <span class="st">"Salary"</span>: [<span class="nm">50000</span>,<span class="nm">60000</span>,<span class="nm">70000</span>,<span class="nm">55000</span>],
    <span class="st">"Dept"</span>: [<span class="st">"Eng"</span>,<span class="st">"Mkt"</span>,<span class="st">"Eng"</span>,<span class="st">"Mkt"</span>]
})

<span class="cm"># Single column (returns Series)</span>
<span class="bi">print</span>(df[<span class="st">"Name"</span>])          <span class="cm"># Series</span>
<span class="bi">print</span>(df.Name)             <span class="cm"># dot notation (same, but not for all names)</span>

<span class="cm"># Multiple columns (returns DataFrame)</span>
<span class="bi">print</span>(df[[<span class="st">"Name"</span>, <span class="st">"Salary"</span>]])

<span class="cm"># Row selection with []</span>
<span class="bi">print</span>(df[<span class="nm">1</span>:<span class="nm">3</span>])  <span class="cm"># rows 1-2 (slice)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>0      Alice<br>1        Bob<br>2    Charlie<br>3      Diana<br>Name: Name, dtype: object</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; .loc (Label-Based)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># .loc[row_label, col_label] &mdash; INCLUSIVE on both ends</span>

<span class="cm"># Single row</span>
<span class="bi">print</span>(df.loc[<span class="nm">0</span>])  <span class="cm"># first row as Series</span>

<span class="cm"># Multiple rows</span>
<span class="bi">print</span>(df.loc[<span class="nm">0</span>:<span class="nm">2</span>])  <span class="cm"># rows 0,1,2 (INCLUSIVE!)</span>

<span class="cm"># Single cell</span>
<span class="bi">print</span>(df.loc[<span class="nm">1</span>, <span class="st">"Name"</span>])  <span class="cm"># "Bob"</span>

<span class="cm"># Row + column slice</span>
<span class="bi">print</span>(df.loc[<span class="nm">0</span>:<span class="nm">2</span>, <span class="st">"Name"</span>:<span class="st">"Salary"</span>])

<span class="cm"># Specific rows and columns</span>
<span class="bi">print</span>(df.loc[[<span class="nm">0</span>,<span class="nm">3</span>], [<span class="st">"Name"</span>,<span class="st">"Dept"</span>]])

<span class="cm"># With boolean mask</span>
<span class="bi">print</span>(df.loc[df[<span class="st">"Age"</span>] > <span class="nm">28</span>, [<span class="st">"Name"</span>,<span class="st">"Age"</span>]])

<span class="cm"># Set values with loc</span>
df.loc[df[<span class="st">"Dept"</span>] == <span class="st">"Eng"</span>, <span class="st">"Bonus"</span>] = <span class="nm">5000</span>
<span class="bi">print</span>(df)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>loc[1,"Name"]: Bob<br>loc with boolean: Bob(30), Charlie(35)</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; .iloc (Integer-Based)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># .iloc[row_int, col_int] &mdash; EXCLUSIVE end (like Python slicing)</span>

<span class="bi">print</span>(df.iloc[<span class="nm">0</span>])          <span class="cm"># first row</span>
<span class="bi">print</span>(df.iloc[-<span class="nm">1</span>])         <span class="cm"># last row</span>
<span class="bi">print</span>(df.iloc[<span class="nm">0</span>:<span class="nm">2</span>])        <span class="cm"># rows 0,1 (EXCLUSIVE end!)</span>
<span class="bi">print</span>(df.iloc[<span class="nm">1</span>, <span class="nm">2</span>])       <span class="cm"># row 1, col 2 = 60000</span>
<span class="bi">print</span>(df.iloc[<span class="nm">0</span>:<span class="nm">2</span>, <span class="nm">0</span>:<span class="nm">3</span>])  <span class="cm"># sub-matrix</span>
<span class="bi">print</span>(df.iloc[:, -<span class="nm">1</span>])      <span class="cm"># last column</span>

<span class="cm"># Every other row</span>
<span class="bi">print</span>(df.iloc[::<span class="nm">2</span>])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>iloc[1, 2]: 60000</div></div>

<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>.loc vs .iloc</strong>
<ul>
<li><code>.loc[0:2]</code> = rows labeled 0,1,2 (3 rows, <strong>inclusive</strong>)</li>
<li><code>.iloc[0:2]</code> = rows at positions 0,1 (2 rows, <strong>exclusive</strong>)</li>
<li>Use <code>.loc</code> for label-based, <code>.iloc</code> for integer-position-based</li>
</ul></div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; .at &amp; .iat (Fast Scalar Access)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># .at[row_label, col_label] &mdash; single value, label-based</span>
<span class="bi">print</span>(df.at[<span class="nm">0</span>, <span class="st">"Name"</span>])   <span class="cm"># "Alice" (faster than .loc for single val)</span>

<span class="cm"># .iat[row_int, col_int] &mdash; single value, integer-based</span>
<span class="bi">print</span>(df.iat[<span class="nm">1</span>, <span class="nm">2</span>])       <span class="cm"># 60000 (faster than .iloc for single val)</span>

<span class="cm"># Set single value</span>
df.at[<span class="nm">0</span>, <span class="st">"Salary"</span>] = <span class="nm">52000</span>
df.iat[<span class="nm">1</span>, <span class="nm">2</span>] = <span class="nm">62000</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>at: Alice &middot; iat: 60000</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Boolean Indexing &amp; Conditional Filtering</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Single condition</span>
<span class="bi">print</span>(df[df[<span class="st">"Age"</span>] > <span class="nm">28</span>])

<span class="cm"># Multiple conditions (&amp; = and, | = or, ~ = not)</span>
<span class="bi">print</span>(df[(df[<span class="st">"Age"</span>] > <span class="nm">25</span>) &amp; (df[<span class="st">"Dept"</span>] == <span class="st">"Eng"</span>)])
<span class="bi">print</span>(df[(df[<span class="st">"Salary"</span>] > <span class="nm">55000</span>) | (df[<span class="st">"Age"</span>] < <span class="nm">26</span>)])
<span class="bi">print</span>(df[~(df[<span class="st">"Dept"</span>] == <span class="st">"Mkt"</span>)])  <span class="cm"># NOT marketing</span>

<span class="cm"># .isin() for multiple values</span>
<span class="bi">print</span>(df[df[<span class="st">"Name"</span>].isin([<span class="st">"Alice"</span>, <span class="st">"Charlie"</span>])])

<span class="cm"># .between() for ranges</span>
<span class="bi">print</span>(df[df[<span class="st">"Age"</span>].between(<span class="nm">25</span>, <span class="nm">30</span>)])

<span class="cm"># String methods</span>
<span class="bi">print</span>(df[df[<span class="st">"Name"</span>].str.startswith(<span class="st">"A"</span>)])
<span class="bi">print</span>(df[df[<span class="st">"Name"</span>].str.contains(<span class="st">"li"</span>)])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Age > 28: Bob(30), Charlie(35)<br>Age > 25 AND Eng: Charlie(35)<br>Name starts with A: Alice</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; query() Method</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># query() uses string expressions (cleaner syntax)</span>
<span class="bi">print</span>(df.query(<span class="st">"Age > 28"</span>))
<span class="bi">print</span>(df.query(<span class="st">"Age > 25 and Dept == 'Eng'"</span>))
<span class="bi">print</span>(df.query(<span class="st">"Salary > 55000 or Age < 26"</span>))

<span class="cm"># With variables (use @ prefix)</span>
min_age = <span class="nm">28</span>
<span class="bi">print</span>(df.query(<span class="st">"Age > @min_age"</span>))

<span class="cm"># query with .isin equivalent</span>
names = [<span class="st">"Alice"</span>, <span class="st">"Bob"</span>]
<span class="bi">print</span>(df.query(<span class="st">"Name in @names"</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>query Age > 28: Bob, Charlie</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>When to use which?</strong>
<ul>
<li><code>df["col"]</code> &mdash; quick column access</li>
<li><code>df.loc[]</code> &mdash; label-based rows/cols, boolean masks</li>
<li><code>df.iloc[]</code> &mdash; integer-position rows/cols</li>
<li><code>df.at/iat</code> &mdash; single scalar value (fastest)</li>
<li><code>df.query()</code> &mdash; complex conditions (most readable)</li>
</ul></div></div></section>''',
("reading-data.html","Reading Data"),("cleaning.html","Data Cleaning"))

print("reading-data.html + selection.html expanded!")
