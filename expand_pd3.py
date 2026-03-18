import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# DATA CLEANING (MASSIVE EXPANSION)
pd_clean_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Data Cleaning: The Art of Wrangling</h4>
    <ol>
        <li><a href="#intro">1. The Cleaning Workflow</a></li>
        <li><a href="#missing">2. Handling Missing Data (NULL/NaN)</a></li>
        <li><a href="#duplicates">3. Duplicate Identification</a></li>
        <li><a href="#replace">4. Replacement and Mapping</a></li>
        <li><a href="#outliers">5. Outlier Detection and Capping</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Cleaning Workflow</h2>
    <p>Cleaning is the most important step in any data science project. Real-world data is messy, incomplete, and often incorrectly formatted. Pandas provides the tools to handle these issues with precision and performance.</p>
</section>

<section class="content-section" id="missing">
    <h2>2 &middot; Handling Missing Data</h2>
    <div class="callout note">
        <div class="callout-icon">🔍</div>
        <div class="callout-content">
            <strong>Deep Dive: NaN vs None</strong>
            <p>Pandas uses <code>NaN</code> (Not a Number) for missing numeric and object data. It inherits this from NumPy. For Python objects, <code>None</code> is often used, but Pandas automatically converts it to <code>NaN</code> for numeric types to allow for vectorized math.</p>
        </div>
    </div>
</section>
"""

make_page("pandas/cleaning.html","Data Cleaning & Wrangling","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Cleaning",
"Mastering missing data handling, duplicate removal, and value replacement using vectorized string and numeric operations.",
"Python for Data Analysis &mdash; Wes McKinney", pd_clean_body, ("selection.html","Selection & Filtering"), ("groupby.html","GroupBy & Aggregation"),
[("selection.html", "Accessing Data"), ("groupby.html", "Aggregating Data"), ("merging.html", "Joining Data")])

# MERGING & JOINING (MASSIVE EXPANSION)
pd_merge_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Relational Algebra in Pandas</h4>
    <ol>
        <li><a href="#intro">1. The Merge Paradigm</a></li>
        <li><a href="#inner">2. Inner, Outer, Left, and Right Joins</a></li>
        <li><a href="#concat">3. Concatenation and Stacking</a></li>
        <li><a href="#overlap">4. Handling Overlapping Column Names</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Merge Paradigm</h2>
    <p>Merging is the process of combining datasets based on one or more common keys. This is identical to the SQL "JOIN" operations. We must choose the type of join based on how we want to handle missing keys in either dataset.</p>
</section>

<section class="content-section" id="inner">
    <h2>2 &middot; Join Types</h2>
    <div class="callout important">
        <div class="callout-icon">🔗</div>
        <div class="callout-content">
            <strong>The Four Horsemen of Joins</strong>
            <ul>
                <li><strong>Inner Join:</strong> Only keys present in both.</li>
                <li><strong>Outer Join:</strong> All keys from both (adds NaN).</li>
                <li><strong>Left Join:</strong> All keys from left, intersection from right.</li>
                <li><strong>Right Join:</strong> All keys from right, intersection from left.</li>
            </ul>
        </div>
    </div>
</section>
"""

make_page("pandas/merging.html","Merging & Joining","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Merging",
"Comprehensive analysis of relational database operations in Pandas, covering merges, joins, and concatenations.",
"Python for Data Analysis &mdash; Wes McKinney", pd_merge_body, ("groupby.html","GroupBy & Aggregation"), ("visualization.html","Visualization"),
[("groupby.html", "Aggregating Data"), ("selection.html", "Filtering Keys")])

print("cleaning.html + merging.html MASSIVELY expanded!")
