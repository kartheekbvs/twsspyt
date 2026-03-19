import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# READING DATA (PRECISION MAPPING FROM MCKINNEY CHAPTER 6)
pd_io_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Data Loading, Storage, and File Formats</h4>
    <p>This module provides a definitive reference for pandas' parsing functions, based on the primary technical documentation of Wes McKinney's <i>Python for Data Analysis</i>.</p>
</div>

<div class="theory-box">
    <h3>6.1 Reading and Writing Data in Text Format</h3>
    <p>Pandas features a number of functions for reading tabular data as a DataFrame object. The most frequently used are <code>read_csv</code> and <code>read_table</code>. These functions have many additional arguments to help you handle the wide variety of exception file formats that occur.</p>
    
    <div class="spec-card">
        <h4>Table 6-1: Parsing Functions</h4>
        <ul>
            <li><strong>read_csv:</strong> Load delimited data from a file, URL, or file-like object; uses comma as default delimiter.</li>
            <li><strong>read_table:</strong> Load delimited data from a file, URL, or file-like object; uses tab ('\t') as default delimiter.</li>
            <li><strong>read_fwf:</strong> Read data in fixed-width column format (i.e., no delimiters).</li>
            <li><strong>read_clipboard:</strong> Variant of read_table that reads data from the clipboard; useful for converting tables from web pages.</li>
            <li><strong>read_excel:</strong> Read tabular data from an Excel XLS or XLSX file.</li>
            <li><strong>read_hdf:</strong> Read HDF5 files written by pandas.</li>
            <li><strong>read_json:</strong> Read data from a JSON (JavaScript Object Notation) string representation.</li>
        </ul>
    </div>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Basic Data Loading</span></div>
    <pre><code>import pandas as pd

# Basic reading without header
pd.read_csv('examples/ex2.csv', header=None)

# Specifying column names
pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])

# Using a specific column as the row index
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('examples/ex2.csv', names=names, index_col='message')</code></pre>
</div>

<div class="theory-box">
    <h3>Handling Missing Values</h3>
    <p>Handling missing values is an important and frequently nuanced part of the file parsing process. Missing data is usually either not present (empty string) or marked by some sentinel value. By default, pandas uses a set of commonly occurring sentinels, such as <code>NA</code> and <code>NULL</code>.</p>
    <div class="info-item">
        <strong>The na_values option:</strong> Can take either a list or set of strings to consider missing values.
    </div>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Custom Missing Values</span></div>
    <pre><code># Specify global sentinels
result = pd.read_csv('examples/ex5.csv', na_values=['NULL'])

# Different NA sentinels for each column
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('examples/ex5.csv', na_values=sentinels)</code></pre>
</div>

<div class="theory-box">
    <h3>Reading Text Files in Pieces</h3>
    <p>When processing very large files, you may only want to read in a small piece or iterate through smaller chunks. The <code>TextParser</code> object returned by <code>read_csv</code> allows you to iterate over the parts of the file according to the <code>chunksize</code>.</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Chunked Loading</span></div>
    <pre><code># Read only a small number of rows
pd.read_csv('examples/ex6.csv', nrows=5)

# Iterating over chunks
chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)</code></pre>
</div>

<div class="theory-box">
    <h3>Binary Data Formats</h3>
    <p>Pandas supports several binary formats for efficient storage. One of the easiest is Python's built-in <code>pickle</code> serialization. For large quantities of scientific array data, <code>HDF5</code> is a well-regarded format. It is available as a C library and supports on-the-fly compression.</p>
</div>
"""

# SELECTION & FILTERING (PRECISION MAPPING FROM MCKINNEY CHAPTER 5.2)
pd_selection_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Indexing, Selection, and Filtering</h4>
    <p>This module covers the fundamental mechanics of interacting with the data contained in a Series or DataFrame, following the 'Essential Functionality' section of the McKinney textbook.</p>
</div>

<div class="theory-box">
    <h3>Series Indexing</h3>
    <p>Series indexing (<code>obj[...]</code>) works analogously to NumPy array indexing, except you can use the Series’s index values instead of only integers. Note that slicing with labels behaves differently than normal Python slicing in that the endpoint is <strong>inclusive</strong>.</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Series Selection</span></div>
    <pre><code>import pandas as pd
import numpy as np

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

# Label indexing
obj['b'] # Returns 1.0

# Positional indexing
obj[1] # Returns 1.0

# Slicing with labels (Inclusive!)
obj['b':'c'] # Returns 'b' and 'c' values</code></pre>
</div>

<div class="theory-box">
    <h3>Selection with loc and iloc</h3>
    <p>For DataFrame label-indexing on the rows, pandas provides the special indexing operators <code>loc</code> and <code>iloc</code>. They enable you to select a subset of the rows and columns with NumPy-like notation using either axis labels (<code>loc</code>) or integers (<code>iloc</code>).</p>
    
    <div class="spec-card">
        <h4>Indexing Option Summary</h4>
        <ul>
            <li><strong>df[val]:</strong> Select single column or sequence of columns. Special cases: boolean array (filter rows), slice (slice rows).</li>
            <li><strong>df.loc[val]:</strong> Selects single row or subset of rows by label.</li>
            <li><strong>df.iloc[where]:</strong> Selects single row or subset of rows by integer position.</li>
            <li><strong>df.at[r, c]:</strong> Select a single scalar value by row and column label.</li>
            <li><strong>df.iat[i, j]:</strong> Select a single scalar value by row and column position.</li>
        </ul>
    </div>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: loc and iloc Usage</span></div>
    <pre><code>data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

# Select single row and multiple columns by label
data.loc['Colorado', ['two', 'three']]

# Select multiple rows and specific columns by integer position
data.iloc[[1, 2], [3, 0, 1]]

# Slicing with loc (Inclusive)
data.loc[:'Utah', 'two']

# Slicing with iloc (Exclusive at end)
data.iloc[:, :3][data.three > 5]</code></pre>
</div>

<div class="theory-box">
    <h3>Integer Indexes and Ambiguity</h3>
    <p>Working with pandas objects indexed by integers can be confusing. If you have an axis index containing integers, data selection will always be <strong>label-oriented</strong> to avoid ambiguity. For precise handling, always use <code>loc</code> (for labels) or <code>iloc</code> (for integers).</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Avoiding Integer Ambiguity</span></div>
    <pre><code>ser = pd.Series(np.arange(3.))

# This will fail if index is [0, 1, 2] because -1 is not a label
# ser[-1] # Generates KeyError

# Use iloc for consistent positional access
ser.iloc[-1] # Returns 2.0</code></pre>
</div>
"""

make_page("Reading Data", pd_io_body, "pages/pandas/reading-data.html", "pandas")
make_page("Selection & Filtering", pd_selection_body, "pages/pandas/selection.html", "pandas")
