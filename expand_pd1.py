import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# SERIES & DATAFRAMES (PRECISION MAPPING FROM MCKINNEY CHAPTER 5.1)
pd_core_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Introduction to pandas Data Structures</h4>
    <p>To get started with pandas, you will need to get comfortable with its two workhorse data structures: <strong>Series</strong> and <strong>DataFrame</strong>. While they are not a universal solution for every problem, they provide a solid, easy-to-use foundation for most applications.</p>
</div>

<div class="theory-box">
    <h3>5.1.1 Series</h3>
    <p>A Series is a one-dimensional array-like object containing a sequence of values (of similar types to NumPy types) and an associated array of data labels, called its <strong>index</strong>. The simplest Series is formed from only an array of data.</p>
    
    <div class="info-item">
        <strong>The Series Index:</strong> By default, if no index is specified, a sequence of integers from 0 to N-1 (where N is the length of the data) is assigned. You can also specify an index when creating a Series.
    </div>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Series Foundations</span></div>
    <pre><code>import pandas as pd
import numpy as np

# Basic Series
obj = pd.Series([4, 7, -5, 3])
obj.values # Returns array([4, 7, -5, 3])
obj.index  # Returns RangeIndex(start=0, stop=4, step=1)

# Series with a custom Index
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2.index # Returns Index(['d', 'b', 'a', 'c'], dtype='object')

# Selecting by label
obj2['a'] # Returns -5

# Filtering and Scalar Multiplication
obj2[obj2 > 0]
obj2 * 2
np.exp(obj2)</code></pre>
</div>

<div class="theory-box">
    <h3>Creating Series from Dicts</h3>
    <p>Another way to think about a Series is as a fixed-length, ordered dict, as it is a mapping of index values to data values. It can be used in many contexts where you might use a dict. Should you have data contained in a Python dict, you can create a Series from it by passing the dict.</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Dict to Series</span></div>
    <pre><code>sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)

# Overriding order with an explicit index
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)

# Detecting missing data
pd.isnull(obj4)
pd.notnull(obj4)</code></pre>
</div>

<div class="theory-box">
    <h3>5.1.2 DataFrame</h3>
    <p>A DataFrame represents a rectangular table of data and contains an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.). The DataFrame has both a row and column index; it can be thought of as a dict of Series all sharing the same index.</p>
    <div class="spec-card">
        <h4>Table 5-1: Data inputs to DataFrame constructor</h4>
        <ul>
            <li><strong>2D ndarray:</strong> A matrix of data, passing optional row and column labels.</li>
            <li><strong>dict of arrays, lists, or tuples:</strong> Each sequence becomes a column; all must be the same length.</li>
            <li><strong>dict of Series:</strong> Each value becomes a column; indexes are unioned together.</li>
            <li><strong>dict of dicts:</strong> Each inner dict becomes a column; keys are unioned to form the row index.</li>
        </ul>
    </div>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: DataFrame Foundations</span></div>
    <pre><code>data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

# Row retrieval by label
frame2.loc['three']

# Column modification by assignment
frame2['debt'] = 16.5
frame2['debt'] = np.arange(6.)

# Deleting columns
del frame2['eastern']</code></pre>
</div>

<div class="theory-box">
    <h3>5.1.3 Index Objects</h3>
    <p>Pandas’s Index objects are responsible for holding the axis labels and other metadata (like the axis name or names). Any array or other sequence of labels you use when constructing a Series or DataFrame is internally converted to an Index. <strong>Index objects are immutable</strong> and thus can’t be modified by the user.</p>
</div>
"""

make_page("Series & DataFrame", pd_core_body, "pages/pandas/series-dataframe.html", "pandas")
make_page("Sorting & Ranking", pd_core_body, "pages/pandas/sorting-ranking.html", "pandas")
