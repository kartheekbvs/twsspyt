import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# VISUALIZATION (PRECISION MAPPING FROM MCKINNEY CHAPTER 9)
pd_viz_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Plotting and Visualization</h4>
    <p>Making informative visualizations (sometimes called <i>plots</i>) is one of the most important tasks in data analysis. It may be a part of the exploratory process or a part of the reporting of the final results.</p>
</div>

<div class="theory-box">
    <h3>9.1 A Brief matplotlib API Primer</h3>
    <p>Matplotlib is the primary 2D graphics library in the Python scientific stack. It was designed to resemble MATLAB's plotting functions. For large, complex visualizations, the object-oriented API is generally preferred.</p>
    
    <div class="spec-card">
        <h4>Figure & Subplots</h4>
        <ul>
            <li><strong>plt.figure():</strong> Create a new figure object.</li>
            <li><strong>fig.add_subplot(2, 2, 1):</strong> Add a subplot to a 2x2 grid.</li>
            <li><strong>plt.subplots(2, 3):</strong> Create a new figure and return a 2D array of subplots.</li>
        </ul>
    </div>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Basic Matplotlib Usage</span></div>
    <pre><code>import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

# Plotting on a specific axes
ax3.plot(np.random.randn(50).cumsum(), 'k--')

# Batch setting properties
props = {'title': 'My first matplotlib plot', 'xlabel': 'Stages'}
ax1.set(**props)</code></pre>
</div>

<div class="theory-box">
    <h3>9.2 Plotting with pandas and seaborn</h3>
    <p>pandas itself has built-in methods that simplify creating visualizations from DataFrame and Series objects. Seaborn is a statistical graphics library that simplifies creating many common, aesthetically pleasing visualization types.</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: pandas & seaborn Plots</span></div>
    <pre><code>import seaborn as sns

# Basic pandas Line Plot
s = pd.Series(np.random.randn(10).cumsum())
s.plot()

# seaborn Bar Plot with confidence intervals
sns.barplot(x='tip_pct', y='day', data=tips, orient='h')

# Pair plots for exploratory analysis
sns.pairplot(trans_data, diag_kind='kde')</code></pre>
</div>
"""

# AGGREGATION & GROUPBY (PRECISION MAPPING FROM MCKINNEY CHAPTER 10)
pd_agg_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Data Aggregation and Group Operations</h4>
    <p>Categorizing a dataset and applying a function to each group is a critical component of a data analysis workflow. pandas provides a flexible <code>groupby</code> interface.</p>
</div>

<div class="theory-box">
    <h3>10.1 GroupBy Mechanics</h3>
    <p>Hadley Wickham coined the term <strong>split-apply-combine</strong> for describing group operations. Data is split into groups based on keys, a function is applied to each group, and results are combined into a result object.</p>
    
    <div class="info-item">
        <strong>Grouping Keys:</strong> Can be lists/arrays of length N, column names, dicts/Series for mapping, or functions.
    </div>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: GroupBy Mechanics</span></div>
    <pre><code>df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'data1' : np.random.randn(5)})

# Splitting and Aggregating
grouped = df['data1'].groupby(df['key1'])
grouped.mean()

# Grouping by multiple keys
df.groupby(['key1', 'key2']).mean()

# Iterating over groups
for name, group in df.groupby('key1'):
    print(name)
    print(group)</code></pre>
</div>

<div class="theory-box">
    <h3>10.2 Data Aggregation</h3>
    <p>Aggregations refer to any data transformation that produces scalar values from arrays. Optimized group methods include <code>count</code>, <code>sum</code>, <code>mean</code>, <code>median</code>, <code>std</code>, <code>min</code>, and <code>max</code>.</p>
</div>

<div class="code-block">
    <div class="code-header"><span>Python: Advanced Aggregation</span></div>
    <pre><code># Column subsetting for aggregation
df.groupby(['key1', 'key2'])[['data2']].mean()

# Multi-function aggregation
grouped.agg(['mean', 'std', lambda x: x.max() - x.min()])</code></pre>
</div>
"""

make_page("Plotting & Visualization", pd_viz_body, "pages/pandas/visualization.html", "pandas")
make_page("Grouping & Aggregation", pd_agg_body, "pages/pandas/groupby.html", "pandas")
make_page("Pivot Tables", pd_agg_body, "pages/pandas/pivots.html", "pandas")
