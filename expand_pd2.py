import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# READING DATA (MASSIVE EXPANSION)
pd_io_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Data I/O: The Textbook Reference</h4>
    <ol>
        <li><a href="#intro">1. The Parsing Pipeline</a></li>
        <li><a href="#csv">2. Delimited Formats (CSV/TSV)</a></li>
        <li><a href="#excel">3. Microsoft Excel Integration</a></li>
        <li><a href="#sql">4. SQL Databases & SQLAlchemy</a></li>
        <li><a href="#json">5. JSON & Semi-Structured Data</a></li>
        <li><a href="#performance">6. Performance: Binary Formats (Parquet/HDF5)</a></li>
        <li><a href="#chunking">7. Memory Management: Chunking Large Files</a></li>
        <li><a href="#summary">8. Summary</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Parsing Pipeline</h2>
    <p>Data I/O is often the most time-consuming part of a data scientist's workflow. Pandas addresses this with a suite of "reader" functions. As Wes McKinney explains, these functions do more than just read bytes; they perform <strong>Type Inference</strong>, <strong>Header Identification</strong>, and <strong>Missing Value Handling</strong> automatically.</p>
</section>

<section class="content-section" id="csv">
    <h2>2 &middot; Delimited Formats (CSV/TSV)</h2>
    <p>The most common data format is the Commma-Separated Value (CSV). Pandas' <code>read_csv()</code> is a highly optimized engine written in C/Cython for maximum speed.</p>
    <div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df = pd.read_csv('data.csv', 
                 sep=',', 
                 header=0, 
                 index_col='ID',
                 parse_dates=['Date'],
                 na_values=['NA', 'None'])</pre>
    </div>
</section>

<section class="content-section" id="performance">
    <h2>6 &middot; Performance: Binary Formats</h2>
    <p>For large-scale data, text-based formats like CSV are inefficient. <strong>Parquet</strong> and <strong>HDF5</strong> provide columnar storage and compression, reducing disk I/O significantly.</p>
    <div class="callout note">
        <div class="callout-icon">🚀</div>
        <div class="callout-content">
            <strong>Pro Tip: Parquet</strong>
            <p>Use <code>df.to_parquet()</code> for saving large datasets. It preserves data types and is natively supported by Spark and BigQuery.</p>
        </div>
    </div>
</section>

<section class="content-section" id="chunking">
    <h2>7 &middot; Memory Management: Chunking</h2>
    <p>When a file exceeds available RAM, you must read it in <em>Chunks</em>. This returns an iterator rather than a full DataFrame.</p>
    <div class="return-value-box">
        <div class="rv-label">🔁 Return Value: Chunking</div>
        <p><code>pd.read_csv(..., chunksize=10000)</code> returns a <strong>TextFileReader</strong>. Iterating over it yields blocks of 10,000 rows as <strong>DataFrames</strong>.</p>
    </div>
</section>
"""

make_page("pandas/reading-data.html","Reading & Writing Data","Pandas","&#x1F43C;","beginner","Pandas &rarr; Reading Data",
"Comprehensive guide to Pandas I/O operations, covering CSV, SQL, and memory-safe chunking techniques.",
"Python for Data Analysis &mdash; Wes McKinney", pd_io_body, ("series-dataframe.html","Series & DataFrame"), ("selection.html","Selection & Filtering"),
[("series-dataframe.html", "Core Objects"), ("../python/file-io.html", "Python File I/O"), ("selection.html", "Accessing Data")])

# SELECTION & FILTERING (MASSIVE EXPANSION)
pd_sel_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Selection & Filtering: The Deep Dive</h4>
    <ol>
        <li><a href="#theory">1. Indexing Theory</a></li>
        <li><a href="#loc">2. Label-Based Selection (.loc)</a></li>
        <li><a href="#iloc">3. Integer-Based Selection (.iloc)</a></li>
        <li><a href="#boolean">4. Boolean Indexing & Masking</a></li>
        <li><a href="#at">5. High-Performance Access (.at/.iat)</a></li>
        <li><a href="#setting">6. Setting Values & Views vs Copies</a></li>
    </ol>
</div>

<section class="content-section" id="theory">
    <h2>1 &middot; Indexing Theory</h2>
    <p>Indexing in Pandas is more complex than in NumPy because of the <strong>Index Object</strong>. We must distinguish between <em>Label-based</em> (the name of the row) and <em>Position-based</em> (the numeric order) selection.</p>
</section>

<section class="content-section" id="loc">
    <h2>2 &middot; Label-Based Selection (.loc)</h2>
    <p>The <code>.loc</code> property is the primary way to access data by label. <strong>Crucially:</strong> It is inclusive of the end label.</p>
    <div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"># Returns a Series
row = df.loc['2023-01-01']

# Returns a Scalar
value = df.loc['2023-01-01', 'Price']</pre>
    </div>
</section>

<section class="content-section" id="setting">
    <h2>6 &middot; Setting Values & The SettingWithCopyWarning</h2>
    <div class="callout warning">
        <div class="callout-icon">⚠️</div>
        <div class="callout-content">
            <strong>SettingWithCopyWarning</strong>
            <p>This occurs when you try to modify a SLICE of a DataFrame. Always use <code>.loc[row, col] = val</code> to ensure you are modifying the original object.</p>
        </div>
    </div>
</section>
"""

make_page("pandas/selection.html","Selection & Filtering","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Selection",
"Mastering label and integer-based selection, boolean masking, and high-performance scalar access.",
"Python for Data Analysis &mdash; Wes McKinney", pd_sel_body, ("reading-data.html","Reading Data"), ("cleaning.html","Data Cleaning"),
[("reading-data.html", "Loading Data"), ("../numpy/indexing.html", "NumPy Indexing"), ("cleaning.html", "Data Wrangling")])

print("reading-data.html + selection.html MASSIVELY expanded!")
