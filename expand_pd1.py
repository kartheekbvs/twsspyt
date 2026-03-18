# ========== EXPANDED SERIES & DATAFRAME ==========
make_page("pandas/series-dataframe.html","Series &amp; DataFrame","Pandas","&#x1F43C;","beginner","Pandas &rarr; Series &amp; DataFrame",
"Pandas provides two primary data structures: Series (1D labeled array) and DataFrame (2D labeled table). This section covers their formal definitions, attributes, and relationship with NumPy.",
"Python for Data Analysis &mdash; Wes McKinney, Pandas Documentation",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">What is Pandas?</a></li>
<li><a href="#s2">Series (1D Labeled Array)</a></li>
<li><a href="#s3">DataFrame (2D Labeled Table)</a></li>
<li><a href="#s4">Attributes & Internal Structure</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; What is Pandas?</h2>
<p>Pandas is a fast, powerful, and flexible open-source data analysis and manipulation tool built on top of the Python programming language.</p>

<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with 'relational' or 'labeled' data both easy and intuitive." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Series: The 1D Building Block</h2>
<p>A <strong>Series</strong> is a one-dimensional array-like object containing a sequence of values and an associated array of data labels, called its <em>index</em>.</p>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
s = pd.Series([<span class="nm">4</span>, <span class="nm">7</span>, -<span class="nm">5</span>, <span class="nm">3</span>])
<span class="bi">print</span>(s)</pre>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Creating a Series returns a <strong>pandas.Series object</strong>. Accessing <code>s.values</code> returns a <strong>NumPy ndarray</strong>, while <code>s.index</code> returns a <strong>RangeIndex</strong> (or custom Index object).</p>
</div>
</section>

<section class="content-section" id="s3"><h2>3 &middot; DataFrame: The SQL Table of Python</h2>
<p>A <strong>DataFrame</strong> represents a rectangular table of data and contains an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.).</p>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df = pd.DataFrame({
    <span class="st">'state'</span>: [<span class="st">'Ohio'</span>, <span class="st">'Ohio'</span>, <span class="st">'Nevada'</span>],
    <span class="st">'year'</span>: [<span class="nm">2000</span>, <span class="nm">2001</span>, <span class="nm">2002</span>],
    <span class="st">'pop'</span>: [<span class="nm">1.5</span>, <span class="nm">1.7</span>, <span class="nm">3.2</span>]
})
<span class="bi">print</span>(df.head())</pre>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Accessing a single column (e.g., <code>df['state']</code>) returns a <strong>Series object</strong>. Operations like <code>df.head()</code> return a <strong>new DataFrame object</strong> containing a slice of the original data.</p>
</div>
</section>''',
("../numpy/arrays.html","NumPy Arrays"),("reading-data.html","Reading Data"),
[("../numpy/arrays.html", "NumPy Fundamentals"), ("reading-data.html", "Importing Data"), ("selection.html", "Indexing & Slicing")])

print("series-dataframe.html expanded with enriched content!")
