import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CLEANING
make_page("pandas/cleaning.html","Data Cleaning","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Data Cleaning",
"Data cleaning is essential for quality analysis. This section provides textbook definitions for handling missing data and return value analysis for inplace operations.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Missing Data</a></li>
<li><a href="#s2">Return Values &amp; Inplace</a></li>
<li><a href="#s3">Duplicates</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Missing Data</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Missing data is common in most data analysis applications. pandas uses the floating-point value <code>NaN</code> to represent missing data." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Values &amp; Inplace</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: dropna/fillna</div>
    <p>By default, functions like <code>dropna()</code> and <code>fillna()</code> return a <strong>new DataFrame</strong>. If <code>inplace=True</code> is used, they return <strong>None</strong> and modify the original object.</p>
</div>
</section>''',
("selection.html","Selection"),("merging.html","Merging &amp; Joining"),
[("selection.html", "Filtering"), ("../numpy/indexing.html", "NumPy Indexing")])

# MERGING / COMBINING
make_page("pandas/merging.html","Merging &amp; Combining","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Merging",
"Combining datasets is a core task in data science. This section covers SQL-style joins and concatenations with textbook precision.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Database-Style Joins</a></li>
<li><a href="#s2">Return Values in Merging</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Database-Style Joins (merge)</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Merge or join operations combine datasets by linking rows using one or more keys. These are central to relational databases." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Values</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: pd.merge()</div>
    <p>The <code>pd.merge()</code> function returns a <strong>new DataFrame</strong> containing the combined columns from both input DataFrames based on the join logic.</p>
</div>
</section>''',
("cleaning.html","Data Cleaning"),("visualization.html","Visualization"),
[("cleaning.html", "Preparing Data"), ("../ml/intro-ml.html", "ML Pipeline")])

print("cleaning.html + merging.html expanded!")
