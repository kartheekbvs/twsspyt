import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# CLEANING
make_page("pandas/cleaning.html","Data Cleaning","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Data Cleaning",
"Data cleaning is the most time-consuming part of data analysis (~80%). Pandas provides comprehensive tools for handling missing values (NaN), duplicates, type conversions, string cleaning, outlier detection, and data validation. Master these to prepare real-world data for analysis and machine learning.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Handling Missing Values</a></li>
<li><a href="#s2">Filling Missing Values</a></li>
<li><a href="#s3">Duplicates</a></li>
<li><a href="#s4">Type Conversion</a></li>
<li><a href="#s5">String Cleaning</a></li>
<li><a href="#s6">Renaming &amp; Replacing</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Handling Missing Values (NaN)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np

df = pd.DataFrame({
    <span class="st">"A"</span>: [<span class="nm">1</span>, <span class="nm">2</span>, np.nan, <span class="nm">4</span>, <span class="nm">5</span>],
    <span class="st">"B"</span>: [np.nan, <span class="nm">2</span>, <span class="nm">3</span>, np.nan, <span class="nm">5</span>],
    <span class="st">"C"</span>: [<span class="st">"x"</span>, <span class="kw">None</span>, <span class="st">"z"</span>, <span class="st">"w"</span>, np.nan]
})
<span class="bi">print</span>(df)

<span class="cm"># Detect missing values</span>
<span class="bi">print</span>(df.isnull())           <span class="cm"># True where NaN</span>
<span class="bi">print</span>(df.isna())             <span class="cm"># same as isnull()</span>
<span class="bi">print</span>(df.notna())            <span class="cm"># opposite</span>
<span class="bi">print</span>(df.isnull().sum())      <span class="cm"># count NaNs per column</span>
<span class="bi">print</span>(df.isnull().sum().sum()) <span class="cm"># total NaNs</span>
<span class="bi">print</span>(df.isnull().mean())    <span class="cm"># fraction missing per col</span>

<span class="cm"># Drop rows with ANY NaN</span>
<span class="bi">print</span>(df.dropna())           <span class="cm"># only row 1 &amp; 4 remain</span>

<span class="cm"># Drop rows where ALL values are NaN</span>
<span class="bi">print</span>(df.dropna(how=<span class="st">"all"</span>))

<span class="cm"># Drop columns with any NaN</span>
<span class="bi">print</span>(df.dropna(axis=<span class="nm">1</span>))

<span class="cm"># Require minimum non-NaN values</span>
<span class="bi">print</span>(df.dropna(thresh=<span class="nm">2</span>))   <span class="cm"># keep rows with &ge;2 non-NaN</span>

<span class="cm"># Drop based on specific columns</span>
<span class="bi">print</span>(df.dropna(subset=[<span class="st">"A"</span>, <span class="st">"C"</span>]))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>     A    B     C<br>0  1.0  NaN     x<br>1  2.0  2.0  None<br>2  NaN  3.0     z<br>3  4.0  NaN     w<br>4  5.0  5.0   NaN<br>NaN counts: A=1, B=2, C=2</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Filling Missing Values</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Fill with constant</span>
<span class="bi">print</span>(df.fillna(<span class="nm">0</span>))              <span class="cm"># all NaN &rarr; 0</span>
<span class="bi">print</span>(df.fillna(<span class="st">"MISSING"</span>))     <span class="cm"># all NaN &rarr; "MISSING"</span>

<span class="cm"># Fill with column-specific values</span>
<span class="bi">print</span>(df.fillna({<span class="st">"A"</span>: <span class="nm">0</span>, <span class="st">"B"</span>: df[<span class="st">"B"</span>].mean(), <span class="st">"C"</span>: <span class="st">"unknown"</span>}))

<span class="cm"># Forward fill (use previous value)</span>
<span class="bi">print</span>(df.fillna(method=<span class="st">"ffill"</span>))   <span class="cm"># or df.ffill()</span>

<span class="cm"># Backward fill (use next value)</span>
<span class="bi">print</span>(df.fillna(method=<span class="st">"bfill"</span>))   <span class="cm"># or df.bfill()</span>

<span class="cm"># Limit fills</span>
<span class="bi">print</span>(df.fillna(method=<span class="st">"ffill"</span>, limit=<span class="nm">1</span>))  <span class="cm"># max 1 consecutive fill</span>

<span class="cm"># Interpolate (linear by default)</span>
<span class="bi">print</span>(df[<span class="st">"A"</span>].interpolate())     <span class="cm"># [1, 2, 3, 4, 5]</span>
<span class="bi">print</span>(df[<span class="st">"A"</span>].interpolate(method=<span class="st">"polynomial"</span>, order=<span class="nm">2</span>))

<span class="cm"># Replace specific values with NaN</span>
df2 = df.replace(<span class="nm">0</span>, np.nan)
df2 = df.replace([<span class="nm">999</span>, -<span class="nm">1</span>, <span class="st">"?"</span>], np.nan)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>fillna(0): A=[1,2,0,4,5] B=[0,2,3,0,5]<br>ffill A: [1,2,2,4,5] &middot; interpolate A: [1,2,3,4,5]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Duplicates</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df = pd.DataFrame({
    <span class="st">"name"</span>: [<span class="st">"Alice"</span>,<span class="st">"Bob"</span>,<span class="st">"Alice"</span>,<span class="st">"Charlie"</span>,<span class="st">"Bob"</span>],
    <span class="st">"age"</span>: [<span class="nm">25</span>, <span class="nm">30</span>, <span class="nm">25</span>, <span class="nm">35</span>, <span class="nm">30</span>]
})

<span class="cm"># Detect duplicates</span>
<span class="bi">print</span>(df.duplicated())           <span class="cm"># [F, F, T, F, T]</span>
<span class="bi">print</span>(df.duplicated().sum())     <span class="cm"># 2 duplicates</span>

<span class="cm"># Check specific columns</span>
<span class="bi">print</span>(df.duplicated(subset=[<span class="st">"name"</span>]))

<span class="cm"># keep='first' (default), 'last', or False (mark ALL)</span>
<span class="bi">print</span>(df.duplicated(keep=<span class="kw">False</span>))  <span class="cm"># True for all duplicated rows</span>

<span class="cm"># Remove duplicates</span>
<span class="bi">print</span>(df.drop_duplicates())
<span class="bi">print</span>(df.drop_duplicates(subset=[<span class="st">"name"</span>], keep=<span class="st">"last"</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>duplicated: [False False True False True]<br>After drop: Alice(25), Bob(30), Charlie(35)</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Type Conversion</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df = pd.DataFrame({
    <span class="st">"price"</span>: [<span class="st">"10.5"</span>, <span class="st">"20.3"</span>, <span class="st">"30.1"</span>],
    <span class="st">"qty"</span>: [<span class="st">"1"</span>, <span class="st">"2"</span>, <span class="st">"3"</span>],
    <span class="st">"date"</span>: [<span class="st">"2024-01-01"</span>, <span class="st">"2024-02-01"</span>, <span class="st">"2024-03-01"</span>]
})
<span class="bi">print</span>(df.dtypes)  <span class="cm"># all object (string)</span>

<span class="cm"># .astype() &mdash; convert types</span>
df[<span class="st">"price"</span>] = df[<span class="st">"price"</span>].astype(<span class="bi">float</span>)
df[<span class="st">"qty"</span>] = df[<span class="st">"qty"</span>].astype(<span class="bi">int</span>)
<span class="bi">print</span>(df.dtypes)

<span class="cm"># pd.to_numeric() &mdash; with error handling</span>
s = pd.Series([<span class="st">"1"</span>, <span class="st">"2"</span>, <span class="st">"bad"</span>, <span class="st">"4"</span>])
<span class="bi">print</span>(pd.to_numeric(s, errors=<span class="st">"coerce"</span>))  <span class="cm"># "bad" &rarr; NaN</span>

<span class="cm"># pd.to_datetime()</span>
df[<span class="st">"date"</span>] = pd.to_datetime(df[<span class="st">"date"</span>])
<span class="bi">print</span>(df.dtypes)

<span class="cm"># Category type (saves memory)</span>
df[<span class="st">"grade"</span>] = pd.Categorical([<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"A"</span>], ordered=<span class="kw">True</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>price: float64, qty: int64<br>to_numeric: [1, 2, NaN, 4]<br>date: datetime64[ns]</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; String Cleaning (.str accessor)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">s = pd.Series([<span class="st">"  Alice  "</span>, <span class="st">"BOB"</span>, <span class="st">"charlie"</span>, <span class="st">"  Diana K."</span>])

<span class="bi">print</span>(s.str.strip())       <span class="cm"># remove whitespace</span>
<span class="bi">print</span>(s.str.lower())       <span class="cm"># lowercase</span>
<span class="bi">print</span>(s.str.upper())       <span class="cm"># UPPERCASE</span>
<span class="bi">print</span>(s.str.title())       <span class="cm"># Title Case</span>
<span class="bi">print</span>(s.str.replace(<span class="st">"."</span>, <span class="st">""</span>, regex=<span class="kw">False</span>))  <span class="cm"># remove dots</span>

<span class="bi">print</span>(s.str.len())         <span class="cm"># string lengths</span>
<span class="bi">print</span>(s.str.contains(<span class="st">"a"</span>, case=<span class="kw">False</span>))  <span class="cm"># boolean</span>
<span class="bi">print</span>(s.str.startswith(<span class="st">"A"</span>))
<span class="bi">print</span>(s.str.split())       <span class="cm"># split by whitespace</span>

<span class="cm"># Extract with regex</span>
emails = pd.Series([<span class="st">"user@gmail.com"</span>, <span class="st">"admin@yahoo.com"</span>])
<span class="bi">print</span>(emails.str.extract(<span class="st">r"@(\w+)\."</span>))  <span class="cm"># domain</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>strip: ['Alice', 'BOB', 'charlie', 'Diana K.']<br>lower: ['alice', 'bob', 'charlie', 'diana k.']</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Renaming &amp; Replacing</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df = pd.DataFrame({<span class="st">"old_name"</span>:[<span class="nm">1</span>,<span class="nm">2</span>], <span class="st">"old_val"</span>:[<span class="nm">3</span>,<span class="nm">4</span>]})

<span class="cm"># Rename columns</span>
df = df.rename(columns={<span class="st">"old_name"</span>:<span class="st">"name"</span>, <span class="st">"old_val"</span>:<span class="st">"value"</span>})

<span class="cm"># Rename with function</span>
df.columns = df.columns.str.upper()   <span class="cm"># all uppercase</span>
df = df.rename(columns=<span class="bi">str</span>.lower)     <span class="cm"># all lowercase</span>

<span class="cm"># Replace values</span>
df = pd.DataFrame({<span class="st">"grade"</span>: [<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"C"</span>,<span class="st">"F"</span>]})
df[<span class="st">"grade"</span>] = df[<span class="st">"grade"</span>].replace({<span class="st">"A"</span>:<span class="st">"Excellent"</span>, <span class="st">"B"</span>:<span class="st">"Good"</span>, <span class="st">"C"</span>:<span class="st">"Average"</span>, <span class="st">"F"</span>:<span class="st">"Fail"</span>})
<span class="bi">print</span>(df)

<span class="cm"># Map (same as replace for Series)</span>
df[<span class="st">"numeric"</span>] = df[<span class="st">"grade"</span>].map({<span class="st">"Excellent"</span>:<span class="nm">4</span>, <span class="st">"Good"</span>:<span class="nm">3</span>, <span class="st">"Average"</span>:<span class="nm">2</span>, <span class="st">"Fail"</span>:<span class="nm">0</span>})</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>      grade  numeric<br>0  Excellent        4<br>1      Good        3<br>2   Average        2<br>3      Fail        0</div></div></section>''',
("selection.html","Selection"),("merging.html","Merging &amp; Joining"))

# MERGING / COMBINING
make_page("pandas/merging.html","Merging &amp; Combining","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Merging",
"Pandas provides powerful functions for combining DataFrames: merge (SQL-like joins), concat (stacking), and join. Also covers append, combine_first, and update for various data combination scenarios.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">pd.merge() (SQL-Style Joins)</a></li>
<li><a href="#s2">pd.concat() (Stacking)</a></li>
<li><a href="#s3">df.join() &amp; combine_first()</a></li>
<li><a href="#s4">Pivot Tables &amp; Cross Tabulation</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; pd.merge() &mdash; SQL-Style Joins</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd

employees = pd.DataFrame({
    <span class="st">"emp_id"</span>: [<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>],
    <span class="st">"name"</span>: [<span class="st">"Alice"</span>,<span class="st">"Bob"</span>,<span class="st">"Charlie"</span>,<span class="st">"Diana"</span>],
    <span class="st">"dept_id"</span>: [<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">10</span>,<span class="nm">30</span>]
})
departments = pd.DataFrame({
    <span class="st">"dept_id"</span>: [<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">40</span>],
    <span class="st">"dept_name"</span>: [<span class="st">"Engineering"</span>,<span class="st">"Marketing"</span>,<span class="st">"Sales"</span>]
})

<span class="cm"># Inner join (default) &mdash; only matching rows</span>
<span class="bi">print</span>(pd.merge(employees, departments, on=<span class="st">"dept_id"</span>))

<span class="cm"># Left join &mdash; all from left, matched from right</span>
<span class="bi">print</span>(pd.merge(employees, departments, on=<span class="st">"dept_id"</span>, how=<span class="st">"left"</span>))

<span class="cm"># Right join &mdash; all from right, matched from left</span>
<span class="bi">print</span>(pd.merge(employees, departments, on=<span class="st">"dept_id"</span>, how=<span class="st">"right"</span>))

<span class="cm"># Outer join &mdash; all from both</span>
<span class="bi">print</span>(pd.merge(employees, departments, on=<span class="st">"dept_id"</span>, how=<span class="st">"outer"</span>))

<span class="cm"># Different column names</span>
<span class="cm"># pd.merge(df1, df2, left_on="id", right_on="emp_id")</span>

<span class="cm"># Merge on index</span>
<span class="cm"># pd.merge(df1, df2, left_index=True, right_index=True)</span>

<span class="cm"># Indicator column (shows which side matched)</span>
<span class="bi">print</span>(pd.merge(employees, departments, on=<span class="st">"dept_id"</span>, how=<span class="st">"outer"</span>, indicator=<span class="kw">True</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Inner: Alice/Eng, Bob/Mkt, Charlie/Eng (3 rows)<br>Left: + Diana/NaN (4 rows)<br>Outer: + Diana/NaN + Sales/NaN (5 rows)</div></div>
<table class="data-table"><thead><tr><th>Join Type</th><th>SQL Equivalent</th><th>Result</th></tr></thead><tbody>
<tr><td><code>inner</code></td><td>INNER JOIN</td><td>Only matching keys</td></tr>
<tr><td><code>left</code></td><td>LEFT OUTER JOIN</td><td>All left + matching right</td></tr>
<tr><td><code>right</code></td><td>RIGHT OUTER JOIN</td><td>All right + matching left</td></tr>
<tr><td><code>outer</code></td><td>FULL OUTER JOIN</td><td>All from both sides</td></tr>
<tr><td><code>cross</code></td><td>CROSS JOIN</td><td>Cartesian product</td></tr>
</tbody></table></section>

<section class="content-section" id="s2"><h2>2 &middot; pd.concat() &mdash; Stacking</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df1 = pd.DataFrame({<span class="st">"A"</span>: [<span class="nm">1</span>,<span class="nm">2</span>], <span class="st">"B"</span>: [<span class="nm">3</span>,<span class="nm">4</span>]})
df2 = pd.DataFrame({<span class="st">"A"</span>: [<span class="nm">5</span>,<span class="nm">6</span>], <span class="st">"B"</span>: [<span class="nm">7</span>,<span class="nm">8</span>]})

<span class="cm"># Vertical stack (append rows)</span>
<span class="bi">print</span>(pd.concat([df1, df2], ignore_index=<span class="kw">True</span>))

<span class="cm"># Horizontal stack (add columns)</span>
<span class="bi">print</span>(pd.concat([df1, df2], axis=<span class="nm">1</span>))

<span class="cm"># With keys (hierarchical index)</span>
<span class="bi">print</span>(pd.concat([df1, df2], keys=[<span class="st">"first"</span>, <span class="st">"second"</span>]))

<span class="cm"># Handle mismatched columns</span>
df3 = pd.DataFrame({<span class="st">"A"</span>: [<span class="nm">1</span>], <span class="st">"C"</span>: [<span class="nm">9</span>]})
<span class="bi">print</span>(pd.concat([df1, df3]))  <span class="cm"># B and C filled with NaN</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>   A  B<br>0  1  3<br>1  2  4<br>2  5  7<br>3  6  8</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; df.join() &amp; combine_first()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># .join() &mdash; join on index (simpler than merge)</span>
df1 = pd.DataFrame({<span class="st">"a"</span>:[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>]}, index=[<span class="st">"x"</span>,<span class="st">"y"</span>,<span class="st">"z"</span>])
df2 = pd.DataFrame({<span class="st">"b"</span>:[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]}, index=[<span class="st">"x"</span>,<span class="st">"y"</span>,<span class="st">"w"</span>])
<span class="bi">print</span>(df1.join(df2, how=<span class="st">"outer"</span>))

<span class="cm"># combine_first() &mdash; fill NaN in df1 with values from df2</span>
s1 = pd.Series([<span class="nm">1</span>, np.nan, <span class="nm">3</span>, np.nan])
s2 = pd.Series([np.nan, <span class="nm">2</span>, np.nan, <span class="nm">4</span>])
<span class="bi">print</span>(s1.combine_first(s2))  <span class="cm"># [1, 2, 3, 4]</span>

<span class="cm"># update() &mdash; modify in-place with non-NaN values</span>
df1 = pd.DataFrame({<span class="st">"A"</span>:[<span class="nm">1</span>,np.nan,<span class="nm">3</span>]})
df2 = pd.DataFrame({<span class="st">"A"</span>:[np.nan,<span class="nm">2</span>,<span class="nm">99</span>]})
df1.update(df2)
<span class="bi">print</span>(df1)  <span class="cm"># [1, 2, 99]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>combine_first: [1.0, 2.0, 3.0, 4.0]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Pivot Tables &amp; Cross Tabulation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df = pd.DataFrame({
    <span class="st">"Dept"</span>: [<span class="st">"Eng"</span>,<span class="st">"Eng"</span>,<span class="st">"Mkt"</span>,<span class="st">"Mkt"</span>,<span class="st">"Eng"</span>],
    <span class="st">"Level"</span>: [<span class="st">"Jr"</span>,<span class="st">"Sr"</span>,<span class="st">"Jr"</span>,<span class="st">"Sr"</span>,<span class="st">"Sr"</span>],
    <span class="st">"Salary"</span>: [<span class="nm">50</span>,<span class="nm">80</span>,<span class="nm">45</span>,<span class="nm">70</span>,<span class="nm">85</span>]
})

<span class="cm"># Pivot table</span>
<span class="bi">print</span>(pd.pivot_table(df, values=<span class="st">"Salary"</span>, index=<span class="st">"Dept"</span>,
                     columns=<span class="st">"Level"</span>, aggfunc=<span class="st">"mean"</span>))

<span class="cm"># Cross tabulation (frequency table)</span>
<span class="bi">print</span>(pd.crosstab(df[<span class="st">"Dept"</span>], df[<span class="st">"Level"</span>]))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Level    Jr    Sr<br>Dept<br>Eng    50.0  82.5<br>Mkt    45.0  70.0</div></div></section>''',
("cleaning.html","Data Cleaning"),("visualization.html","Visualization"))

print("cleaning.html + merging.html expanded!")
