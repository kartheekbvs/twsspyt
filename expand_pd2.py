import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# READING DATA
make_page("pandas/reading-data.html","Reading &amp; Writing Data","Pandas","&#x1F43C;","beginner","Pandas &rarr; Reading Data",
"Pandas provides robust functions to read data from various formats including CSV, Excel, and SQL. This section details formal textbook patterns and return value analysis.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">CSV &amp; Text Files</a></li>
<li><a href="#s2">Return Values in I/O</a></li>
<li><a href="#s3">Chunking for Large Data</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; CSV &amp; Text Files</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"The <code>read_csv</code> and <code>read_table</code> are part of the 'Parsing functions' that convert text data into a DataFrame." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Values in I/O</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: pd.read_csv()</div>
    <p>By default, <code>pd.read_csv()</code> returns a <strong>DataFrame</strong>. However, if the <code>chunksize</code> parameter is passed, it returns a <strong>TextFileReader</strong> object, which is an <em>iterator</em> that yields DataFrames of the specified size.</p>
</div>
</section>''',
("series-dataframe.html","Series &amp; DataFrame"),("selection.html","Selection &amp; Filtering"),
[("series-dataframe.html", "Core Objects"), ("../python/file-io.html", "Python File I/O")])

# SELECTION & FILTERING
make_page("pandas/selection.html","Selection &amp; Filtering","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Selection",
"Mastering selection with .loc and .iloc is crucial for robust data manipulation. This section covers textbook definitions and return value differences between Series and DataFrames.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Label-Based (.loc)</a></li>
<li><a href="#s2">Integer-Based (.iloc)</a></li>
<li><a href="#s3">Return Value Complexity</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Label-Based Selection (.loc)</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"The <code>loc</code> attribute allows for label-based indexing. It is inclusive of both the start and end labels." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s3"><h2>2 &middot; Return Value Complexity</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: Indexing</div>
    <p>Selection behavior varies by input:
    <ul>
        <li><strong>Single Label:</strong> Returns a <strong>Series</strong> representing the row/column.</li>
        <li><strong>List of Labels:</strong> Returns a <strong>DataFrame</strong>.</li>
        <li><strong>Slice:</strong> Returns a <strong>DataFrame</strong> (inclusive for <code>.loc</code>).</li>
    </ul></p>
</div>
</section>''',
("reading-data.html","Reading Data"),("cleaning.html","Data Cleaning"),
[("reading-data.html", "Loading Data"), ("../numpy/indexing.html", "NumPy Indexing")])

print("reading-data.html + selection.html expanded!")
