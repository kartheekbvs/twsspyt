import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# DATA CLEANING (PRECISION MAPPING FROM MCKINNEY CHAPTER 7)
pd_cleaning_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Data Cleaning and Preparation</h4>
    <p>During the course of doing data analysis and modeling, a significant amount of time is spent on data preparation: loading, cleaning, transforming, and rearranging.</p>
</div>

<div class="theory-box">
    <h3>7.1 Handling Missing Data</h3>
    <p>Missing data occurs commonly in many data analysis applications. One of the goals of pandas is to make working with missing data as painless as possible. For example, all of the descriptive statistics on pandas objects exclude missing data by default.</p>
    
    <div class="spec-card">
        <h4>Table 7-2: fillna function arguments</h4>
        <ul>
            <li><strong>value:</strong> Scalar value or dict-like object to use to fill missing values.</li>
            <li><strong>method:</strong> Interpolation; by default 'ffill' (forward fill).</li>
            <li><strong>axis:</strong> Axis to fill on; default axis=0.</li>
            <li><strong>inplace:</strong> Modify the calling object without producing a copy.</li>
        </ul>
    </div>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Cleaning & Transformation</span></div>
    <pre><code>import pandas as pd
import numpy as np

# Filling missing values
df.fillna(0, inplace=True)
df.fillna(method='ffill', limit=2)

# Removing Duplicates
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
data.duplicated()
data.drop_duplicates(['k1'])

# Element-wise Transformation
meat_to_animal = {'bacon': 'pig', 'pastrami': 'cow'}
data['animal'] = data['food'].str.lower().map(meat_to_animal)

# Replacing values (Sentinel handling)
data.replace(-999, np.nan)</code></pre>
</div>

<div class="theory-box">
    <h3>7.2 Data Transformation</h3>
    <p>Discretization and binning is another class of important operations. Continuous data is often separated into "bins" for analysis. Pandas provides <code>cut</code> for fixed-edge binning and <code>qcut</code> for quantile-based binning.</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Discretization</span></div>
    <pre><code>ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)

# Quantile-based binning
pd.qcut(data, 4) # Cut into quartiles</code></pre>
</div>
"""

# MERGING & COMBINING (PRECISION MAPPING FROM MCKINNEY CHAPTER 8)
pd_merging_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Combining and Merging Datasets</h4>
    <p>Data contained in pandas objects can be combined together in a number of ways: <strong>merge</strong>, <strong>concat</strong>, and <strong>combine_first</strong>.</p>
</div>

<div class="theory-box">
    <h3>Database-Style DataFrame Joins</h3>
    <p>Merge or join operations combine datasets by linking rows using one or more keys. These are similar to the join operations in relational databases. If no key is specified, <code>merge</code> uses the overlapping column names as the keys.</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Merging Datasets</span></div>
    <pre><code># Basic merge on overlapping column
pd.merge(df1, df2, on='key')

# Specifying different keys
pd.merge(df3, df4, left_on='lkey', right_on='rkey')

# Join types: 'inner', 'outer', 'left', 'right'
pd.merge(df1, df2, how='outer')

# Merging on Index
pd.merge(left1, right1, left_on='key', right_index=True)</code></pre>
</div>

<div class="theory-box">
    <h3>Concatenation Along an Axis</h3>
    <p>Concatenation refers to binding or stacking datasets. The <code>concat</code> function provides a consistent way to glue together values and indexes along an axis. By default, it works along <code>axis=0</code> (rows).</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Concatenation</span></div>
    <pre><code># Concatenating Series
pd.concat([s1, s2, s3])

# Concatenating along columns
pd.concat([s1, s2, s3], axis=1)

# Hierarchical Indexing with Concat
pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])</code></pre>
</div>

<div class="theory-box">
    <h3>Reshaping: Stacking and Pivoting</h3>
    <p>Hierarchical indexing provides a consistent way to rearrange data. <code>stack</code> rotates from columns to rows, and <code>unstack</code> rotates from rows to columns.</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Reshaping Format</span></div>
    <pre><code># Pivoting 'Long' to 'Wide'
pivoted = ldata.pivot('date', 'item', 'value')

# Stacking/Unstacking
result = data.stack()
result.unstack()</code></pre>
</div>
"""

make_page("Data Cleaning", pd_cleaning_body, "pages/pandas/cleaning.html", "pandas")
make_page("Merging & Combining", pd_merging_body, "pages/pandas/merging.html", "pandas")
make_page("Reshaping Data", pd_merging_body, "pages/pandas/reshaping.html", "pandas")
