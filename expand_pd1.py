import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# SERIES & DATAFRAME (MASSIVE EXPANSION)
pd_core_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Core Objects: The Internal Architecture</h4>
    <ol>
        <li><a href="#intro">1. The Philosophy of Labeled Data</a></li>
        <li><a href="#series">2. Series: 1D Homogeneous Data</a></li>
        <li><a href="#dataframe">3. DataFrame: 2D Heterogeneous Data</a></li>
        <li><a href="#index">4. The Index Object: Immutable Metadata</a></li>
        <li><a href="#dtype">5. Type Systems: NumPy dtypes vs Extension Types</a></li>
        <li><a href="#performance">6. Memory Layout and Vectorization</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Philosophy of Labeled Data</h2>
    <p>At its heart, Pandas is about <strong>Metadata</strong>. Unlike NumPy, which focuses on raw numeric arrays, Pandas attaches <em>meaning</em> to data through labels. This allows for automatic data alignment—a feature Wes McKinney describes as the 'killer feature' of the library.</p>
</section>

<section class="content-section" id="series">
    <h2>2 &middot; Series: 1D Homogeneous Data</h2>
    <p>A Series is a one-dimensional array-like object containing a sequence of values and an associated array of data labels.</p>
    <div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">import pandas as pd
s = pd.Series([7, 'Python', 3.14, -5], index=['a', 'b', 'c', 'd'])
print(s.values) # returns ndarray
print(s.index)  # returns Index object</pre>
    </div>
</section>

<section class="content-section" id="index">
    <h2>4 &middot; The Index Object</h2>
    <p>The Index object is the backbone of Pandas. It is <strong>Immutable</strong>. Once created, you cannot change a label directly. This ensures that data alignment remains consistent across operations.</p>
</section>
"""

make_page("pandas/series-dataframe.html","Series & DataFrame","Pandas","&#x1F43C;","beginner","Pandas &rarr; Series & DataFrame",
"In-depth analysis of the Series and DataFrame structures, their relationship with NumPy, and the power of the Index object.",
"Python for Data Analysis &mdash; Wes McKinney", pd_core_body, ("../numpy/arrays.html","NumPy Arrays"), ("reading-data.html","Reading Data"),
[("../numpy/arrays.html", "NumPy Fundamentals"), ("reading-data.html", "Importing Data"), ("selection.html", "Indexing & Slicing")])

# GROUPBY & AGGREGATION (MASSIVE EXPANSION)
pd_agg_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Split-Apply-Combine Pattern</h4>
    <ol>
        <li><a href="#intro">1. The Split-Apply-Combine Paradigm</a></li>
        <li><a href="#groupby">2. The GroupBy Object: Lazy Evaluation</a></li>
        <li><a href="#agg">3. Aggregation: compute summary stats</a></li>
        <li><a href="#trans">4. Transformation: broadcast back to shape</a></li>
        <li><a href="#filt">5. Filtering: dropping groups</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Split-Apply-Combine</h2>
    <p>Group operations follow the "split-apply-combine" pattern introduced by Hadley Wickham. <strong>1. Split:</strong> Breaking data into groups based on keys. <strong>2. Apply:</strong> Compute a function within each group. <strong>3. Combine:</strong> Merge results into a new object.</p>
</section>

<section class="content-section" id="groupby">
    <h2>2 &middot; The GroupBy Object</h2>
    <div class="callout note">
        <div class="callout-icon">⚡</div>
        <div class="callout-content">
            <strong>Deep Dive: Lazy Evaluation</strong>
            <p>Creating a GroupBy object (e.g., <code>df.groupby('A')</code>) does NOT perform any computation. It creates a plan. The work only happens when you call an aggregation like <code>.sum()</code> or <code>.mean()</code>.</p>
        </div>
    </div>
</section>
"""

make_page("pandas/groupby.html","GroupBy & Aggregation","Pandas","&#x1F43C;","advanced","Pandas &rarr; GroupBy",
"The definitive guide to the Split-Apply-Combine paradigm, covering custom aggregations, transformations, and group-wise filtering.",
"Pandas Documentation / Python for Data Analysis", pd_agg_body, ("cleaning.html","Data Cleaning"), ("merging.html","Merging & Joining"),
[("cleaning.html", "Data Wrangling"), ("merging.html", "Bridging Data"), ("visualization.html", "Plotting Groups")])

print("series-dataframe.html + groupby.html MASSIVELY expanded!")
