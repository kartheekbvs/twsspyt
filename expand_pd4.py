import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# VISUALIZATION
make_page("pandas/visualization.html","Visualization","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Visualization",
"Pandas integrates with Matplotlib to provide built-in plotting for DataFrames and Series. Supports line plots, bar charts, histograms, scatter plots, box plots, pie charts, area plots, and more. Also covers customization, subplots, and styling.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Basic Plotting</a></li>
<li><a href="#s2">Plot Types</a></li>
<li><a href="#s3">Customization &amp; Styling</a></li>
<li><a href="#s4">Subplots &amp; Multiple Plots</a></li>
<li><a href="#s5">Statistical Plots</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Basic Plotting with Pandas</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Series plot</span>
s = pd.Series([<span class="nm">3</span>, <span class="nm">7</span>, <span class="nm">2</span>, <span class="nm">8</span>, <span class="nm">5</span>], index=[<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"C"</span>,<span class="st">"D"</span>,<span class="st">"E"</span>])
s.plot()                 <span class="cm"># line plot (default)</span>
plt.title(<span class="st">"Series Plot"</span>)
plt.show()

<span class="cm"># DataFrame plot</span>
df = pd.DataFrame({
    <span class="st">"Sales"</span>: [<span class="nm">100</span>,<span class="nm">150</span>,<span class="nm">200</span>,<span class="nm">180</span>],
    <span class="st">"Costs"</span>: [<span class="nm">80</span>,<span class="nm">100</span>,<span class="nm">120</span>,<span class="nm">110</span>]
}, index=[<span class="st">"Q1"</span>,<span class="st">"Q2"</span>,<span class="st">"Q3"</span>,<span class="st">"Q4"</span>])
df.plot()                <span class="cm"># plots all numeric columns</span>
plt.ylabel(<span class="st">"Amount ($)"</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Line plots displayed]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Plot Types</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Bar chart</span>
df.plot(kind=<span class="st">"bar"</span>)
df.plot.bar()                     <span class="cm"># same</span>
df.plot.bar(stacked=<span class="kw">True</span>)         <span class="cm"># stacked bars</span>
df.plot.barh()                    <span class="cm"># horizontal bars</span>

<span class="cm"># Histogram</span>
data = pd.Series(np.random.randn(<span class="nm">1000</span>))
data.plot.hist(bins=<span class="nm">30</span>, alpha=<span class="nm">0.7</span>)

<span class="cm"># Scatter plot</span>
df2 = pd.DataFrame({<span class="st">"x"</span>: np.random.randn(<span class="nm">100</span>), <span class="st">"y"</span>: np.random.randn(<span class="nm">100</span>)})
df2.plot.scatter(x=<span class="st">"x"</span>, y=<span class="st">"y"</span>, alpha=<span class="nm">0.5</span>)

<span class="cm"># Box plot</span>
df.plot.box()

<span class="cm"># Pie chart</span>
pd.Series([<span class="nm">30</span>,<span class="nm">20</span>,<span class="nm">50</span>], index=[<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"C"</span>]).plot.pie(autopct=<span class="st">"%.0f%%"</span>)

<span class="cm"># Area plot</span>
df.plot.area(alpha=<span class="nm">0.5</span>)

<span class="cm"># KDE (Kernel Density Estimation)</span>
data.plot.kde()

plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Various plot types displayed]</div></div>
<table class="data-table"><thead><tr><th>Kind</th><th>Method</th><th>Use Case</th></tr></thead><tbody>
<tr><td><code>"line"</code></td><td><code>df.plot.line()</code></td><td>Trends over time</td></tr>
<tr><td><code>"bar"</code></td><td><code>df.plot.bar()</code></td><td>Categorical comparisons</td></tr>
<tr><td><code>"barh"</code></td><td><code>df.plot.barh()</code></td><td>Horizontal bar chart</td></tr>
<tr><td><code>"hist"</code></td><td><code>df.plot.hist()</code></td><td>Distributions</td></tr>
<tr><td><code>"scatter"</code></td><td><code>df.plot.scatter()</code></td><td>Relationships</td></tr>
<tr><td><code>"box"</code></td><td><code>df.plot.box()</code></td><td>Distributions &amp; outliers</td></tr>
<tr><td><code>"pie"</code></td><td><code>df.plot.pie()</code></td><td>Proportions</td></tr>
<tr><td><code>"area"</code></td><td><code>df.plot.area()</code></td><td>Cumulative quantities</td></tr>
<tr><td><code>"kde"</code></td><td><code>df.plot.kde()</code></td><td>Smooth distributions</td></tr>
<tr><td><code>"hexbin"</code></td><td><code>df.plot.hexbin()</code></td><td>Dense scatter plots</td></tr>
</tbody></table></section>

<section class="content-section" id="s3"><h2>3 &middot; Customization &amp; Styling</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Common plot parameters</span>
df.plot(
    kind=<span class="st">"bar"</span>,
    figsize=(<span class="nm">10</span>, <span class="nm">6</span>),        <span class="cm"># figure size</span>
    title=<span class="st">"Quarterly Report"</span>,
    xlabel=<span class="st">"Quarter"</span>,
    ylabel=<span class="st">"Amount"</span>,
    color=[<span class="st">"#2ecc71"</span>, <span class="st">"#e74c3c"</span>],
    alpha=<span class="nm">0.8</span>,               <span class="cm"># transparency</span>
    rot=<span class="nm">0</span>,                   <span class="cm"># x-label rotation</span>
    grid=<span class="kw">True</span>,               <span class="cm"># show grid</span>
    legend=<span class="kw">True</span>,             <span class="cm"># show legend</span>
    edgecolor=<span class="st">"black"</span>,
)

<span class="cm"># Style context</span>
<span class="kw">with</span> plt.style.context(<span class="st">"seaborn-v0_8"</span>):
    df.plot()
    plt.show()

<span class="cm"># Available styles:</span>
<span class="cm"># 'ggplot', 'seaborn-v0_8', 'dark_background', 'bmh', 'fivethirtyeight'</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Styled bar chart displayed]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Subplots &amp; Multiple Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Each column in separate subplot</span>
df.plot(subplots=<span class="kw">True</span>, figsize=(<span class="nm">8</span>,<span class="nm">6</span>), layout=(<span class="nm">1</span>,<span class="nm">2</span>))
plt.tight_layout()
plt.show()

<span class="cm"># Manual subplots with matplotlib</span>
fig, axes = plt.subplots(<span class="nm">2</span>, <span class="nm">2</span>, figsize=(<span class="nm">12</span>, <span class="nm">8</span>))
df[<span class="st">"Sales"</span>].plot.bar(ax=axes[<span class="nm">0</span>,<span class="nm">0</span>], title=<span class="st">"Sales Bar"</span>)
df[<span class="st">"Costs"</span>].plot.line(ax=axes[<span class="nm">0</span>,<span class="nm">1</span>], title=<span class="st">"Costs Line"</span>)
df.plot.box(ax=axes[<span class="nm">1</span>,<span class="nm">0</span>], title=<span class="st">"Box Plot"</span>)
df.plot.area(ax=axes[<span class="nm">1</span>,<span class="nm">1</span>], title=<span class="st">"Area"</span>, alpha=<span class="nm">0.5</span>)
plt.tight_layout()
plt.show()

<span class="cm"># Save figure</span>
<span class="cm"># fig.savefig("report.png", dpi=300, bbox_inches="tight")</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[2x2 subplot grid displayed]</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Statistical Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Scatter matrix (pairs plot)</span>
<span class="kw">from</span> pandas.plotting <span class="kw">import</span> scatter_matrix
df_num = pd.DataFrame(np.random.randn(<span class="nm">100</span>,<span class="nm">4</span>), columns=[<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"C"</span>,<span class="st">"D"</span>])
scatter_matrix(df_num, figsize=(<span class="nm">10</span>,<span class="nm">10</span>), diagonal=<span class="st">"hist"</span>)
plt.show()

<span class="cm"># Correlation heatmap (with Pandas + Matplotlib)</span>
corr = df_num.corr()
fig, ax = plt.subplots(figsize=(<span class="nm">8</span>,<span class="nm">6</span>))
im = ax.imshow(corr, cmap=<span class="st">"coolwarm"</span>, aspect=<span class="st">"auto"</span>)
ax.set_xticks(<span class="bi">range</span>(<span class="bi">len</span>(corr)))
ax.set_xticklabels(corr.columns, rotation=<span class="nm">45</span>)
ax.set_yticks(<span class="bi">range</span>(<span class="bi">len</span>(corr)))
ax.set_yticklabels(corr.index)
plt.colorbar(im)
plt.title(<span class="st">"Correlation Heatmap"</span>)
plt.show()

<span class="cm"># Andrews curves (multivariate visualization)</span>
<span class="kw">from</span> pandas.plotting <span class="kw">import</span> andrews_curves
<span class="cm"># andrews_curves(iris_df, "species")</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Scatter matrix and heatmap displayed]</div></div></section>''',
("cleaning.html","Data Cleaning"),("../data-analysis/exploratory.html","Exploratory Analysis"))

# GROUPBY 
make_page("pandas/groupby.html","GroupBy &amp; Aggregation","Pandas","&#x1F43C;","intermediate","Pandas &rarr; GroupBy",
"GroupBy implements the split-apply-combine pattern: split data by groups, apply a function to each group, and combine results. Pandas supports single/multi-column grouping, built-in and custom aggregation, transformation, filtering, and agg().",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Split-Apply-Combine</a></li>
<li><a href="#s2">Aggregation Functions</a></li>
<li><a href="#s3">agg() &amp; Named Aggregation</a></li>
<li><a href="#s4">Transform &amp; Apply</a></li>
<li><a href="#s5">Filter &amp; Advanced GroupBy</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Split-Apply-Combine</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd

df = pd.DataFrame({
    <span class="st">"Dept"</span>: [<span class="st">"Eng"</span>,<span class="st">"Eng"</span>,<span class="st">"Mkt"</span>,<span class="st">"Mkt"</span>,<span class="st">"Eng"</span>,<span class="st">"Mkt"</span>],
    <span class="st">"Level"</span>: [<span class="st">"Jr"</span>,<span class="st">"Sr"</span>,<span class="st">"Jr"</span>,<span class="st">"Sr"</span>,<span class="st">"Sr"</span>,<span class="st">"Jr"</span>],
    <span class="st">"Salary"</span>: [<span class="nm">50</span>,<span class="nm">80</span>,<span class="nm">45</span>,<span class="nm">70</span>,<span class="nm">85</span>,<span class="nm">42</span>],
    <span class="st">"Bonus"</span>: [<span class="nm">5</span>,<span class="nm">10</span>,<span class="nm">4</span>,<span class="nm">8</span>,<span class="nm">12</span>,<span class="nm">3</span>]
})

<span class="cm"># Basic groupby</span>
grouped = df.groupby(<span class="st">"Dept"</span>)
<span class="bi">print</span>(<span class="bi">type</span>(grouped))  <span class="cm"># DataFrameGroupBy</span>

<span class="cm"># Inspect groups</span>
<span class="bi">print</span>(grouped.groups)        <span class="cm"># {'Eng': [0,1,4], 'Mkt': [2,3,5]}</span>
<span class="bi">print</span>(grouped.ngroups)       <span class="cm"># 2</span>
<span class="bi">print</span>(grouped.size())        <span class="cm"># Eng=3, Mkt=3</span>
<span class="bi">print</span>(grouped.get_group(<span class="st">"Eng"</span>))  <span class="cm"># rows where Dept=Eng</span>

<span class="cm"># Iterate over groups</span>
<span class="kw">for</span> name, group <span class="kw">in</span> grouped:
    <span class="bi">print</span>(<span class="st">f"\\n{name}: {len(group)} rows"</span>)
    <span class="bi">print</span>(group)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Eng: 3 rows, Mkt: 3 rows</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Aggregation Functions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Built-in aggregations</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].mean())   <span class="cm"># avg salary per dept</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].sum())    <span class="cm"># total</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].min())    <span class="cm"># minimum</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].max())    <span class="cm"># maximum</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].count())  <span class="cm"># count</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].std())    <span class="cm"># std deviation</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>).describe())           <span class="cm"># all stats</span>

<span class="cm"># Multi-column groupby</span>
<span class="bi">print</span>(df.groupby([<span class="st">"Dept"</span>, <span class="st">"Level"</span>])[<span class="st">"Salary"</span>].mean())

<span class="cm"># Aggregate multiple columns differently</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>).agg({
    <span class="st">"Salary"</span>: <span class="st">"mean"</span>,
    <span class="st">"Bonus"</span>: <span class="st">"sum"</span>
}))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Dept<br>Eng    71.67<br>Mkt    52.33<br>Name: Salary, dtype: float64</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; agg() &amp; Named Aggregation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Multiple aggs per column</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].agg([<span class="st">"mean"</span>,<span class="st">"min"</span>,<span class="st">"max"</span>,<span class="st">"count"</span>]))

<span class="cm"># Named aggregation (Pandas 0.25+) &mdash; cleaner syntax</span>
result = df.groupby(<span class="st">"Dept"</span>).agg(
    avg_salary=(<span class="st">"Salary"</span>, <span class="st">"mean"</span>),
    total_bonus=(<span class="st">"Bonus"</span>, <span class="st">"sum"</span>),
    headcount=(<span class="st">"Salary"</span>, <span class="st">"count"</span>),
    max_salary=(<span class="st">"Salary"</span>, <span class="st">"max"</span>)
)
<span class="bi">print</span>(result)

<span class="cm"># Custom aggregation function</span>
<span class="kw">def</span> salary_range(x):
    <span class="kw">return</span> x.max() - x.min()

<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].agg(salary_range))

<span class="cm"># Lambda in agg</span>
<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].agg(<span class="kw">lambda</span> x: x.quantile(<span class="nm">0.75</span>)))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>     avg_salary  total_bonus  headcount  max_salary<br>Eng       71.67           27          3          85<br>Mkt       52.33           15          3          70</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; transform() &amp; apply()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># transform() &mdash; returns same-shape result</span>
<span class="cm"># Great for broadcasting group stats back to original size</span>
df[<span class="st">"dept_avg"</span>] = df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].transform(<span class="st">"mean"</span>)
df[<span class="st">"z_score"</span>] = df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].transform(
    <span class="kw">lambda</span> x: (x - x.mean()) / x.std()
)
<span class="bi">print</span>(df)

<span class="cm"># apply() &mdash; most flexible (any function on each group)</span>
<span class="kw">def</span> top_earner(group):
    <span class="kw">return</span> group.nlargest(<span class="nm">1</span>, <span class="st">"Salary"</span>)

<span class="bi">print</span>(df.groupby(<span class="st">"Dept"</span>).apply(top_earner))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[DataFrame with dept_avg and z_score columns added]</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; filter() &amp; Advanced GroupBy</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># filter() &mdash; keep/drop entire groups</span>
<span class="cm"># Keep only departments with avg salary > 60</span>
result = df.groupby(<span class="st">"Dept"</span>).filter(<span class="kw">lambda</span> x: x[<span class="st">"Salary"</span>].mean() > <span class="nm">60</span>)
<span class="bi">print</span>(result)

<span class="cm"># Group by with time resampling</span>
<span class="cm"># dates = pd.date_range("2024-01-01", periods=100, freq="D")</span>
<span class="cm"># ts = pd.DataFrame({"val": np.random.randn(100)}, index=dates)</span>
<span class="cm"># ts.resample("M").mean()  # monthly average</span>

<span class="cm"># Cumulative operations within groups</span>
df[<span class="st">"cum_salary"</span>] = df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].cumsum()
df[<span class="st">"salary_rank"</span>] = df.groupby(<span class="st">"Dept"</span>)[<span class="st">"Salary"</span>].rank(ascending=<span class="kw">False</span>)
<span class="bi">print</span>(df[[<span class="st">"Dept"</span>,<span class="st">"Salary"</span>,<span class="st">"cum_salary"</span>,<span class="st">"salary_rank"</span>]])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>  Dept  Salary  cum_salary  salary_rank<br>0  Eng      50          50          3.0<br>1  Eng      80         130          2.0<br>4  Eng      85         215          1.0</div></div></section>''',
("merging.html","Merging"),("visualization.html","Visualization"))

# TIME SERIES (NEW PAGE)
make_page("pandas/time-series.html","Time Series Analysis","Pandas","&#x1F43C;","advanced","Pandas &rarr; Time Series",
"Pandas has excellent support for time series data: DatetimeIndex, date_range, resampling, rolling windows, shifting/lagging, period conversion, and timezone handling. Essential for financial data, sensor data, and any temporal analysis.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">DatetimeIndex &amp; date_range</a></li>
<li><a href="#s2">Resampling (Downsampling &amp; Upsampling)</a></li>
<li><a href="#s3">Rolling &amp; Expanding Windows</a></li>
<li><a href="#s4">Shifting &amp; Lagging</a></li>
<li><a href="#s5">Timedelta &amp; Period</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; DatetimeIndex &amp; date_range</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># pd.to_datetime() &mdash; convert strings to datetime</span>
dates = pd.to_datetime([<span class="st">"2024-01-01"</span>,<span class="st">"2024-02-15"</span>,<span class="st">"2024-03-30"</span>])
<span class="bi">print</span>(dates)
<span class="bi">print</span>(dates.year)      <span class="cm"># [2024, 2024, 2024]</span>
<span class="bi">print</span>(dates.month)     <span class="cm"># [1, 2, 3]</span>
<span class="bi">print</span>(dates.day_name()) <span class="cm"># ['Monday', 'Thursday', 'Saturday']</span>

<span class="cm"># pd.date_range() &mdash; generate date sequences</span>
<span class="bi">print</span>(pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">5</span>, freq=<span class="st">"D"</span>))    <span class="cm"># daily</span>
<span class="bi">print</span>(pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">4</span>, freq=<span class="st">"W"</span>))    <span class="cm"># weekly</span>
<span class="bi">print</span>(pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">12</span>, freq=<span class="st">"ME"</span>))  <span class="cm"># month-end</span>
<span class="bi">print</span>(pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">4</span>, freq=<span class="st">"QE"</span>))   <span class="cm"># quarter-end</span>
<span class="bi">print</span>(pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">8</span>, freq=<span class="st">"h"</span>))    <span class="cm"># hourly</span>

<span class="cm"># Create time series</span>
ts = pd.Series(np.random.randn(<span class="nm">365</span>),
               index=pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">365</span>, freq=<span class="st">"D"</span>))
<span class="bi">print</span>(ts.head())

<span class="cm"># Slicing by date strings</span>
<span class="bi">print</span>(ts[<span class="st">"2024-03"</span>])         <span class="cm"># all of March 2024</span>
<span class="bi">print</span>(ts[<span class="st">"2024-01"</span>:<span class="st">"2024-03"</span>])  <span class="cm"># Jan through March</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>DatetimeIndex(['2024-01-01','2024-01-02',...,'2024-01-05'])<br>ts head: date-indexed random values</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Resampling</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Downsampling: daily &rarr; monthly</span>
monthly = ts.resample(<span class="st">"ME"</span>).mean()
<span class="bi">print</span>(monthly.head())

<span class="cm"># Different aggregations</span>
<span class="bi">print</span>(ts.resample(<span class="st">"ME"</span>).sum())     <span class="cm"># monthly total</span>
<span class="bi">print</span>(ts.resample(<span class="st">"ME"</span>).std())     <span class="cm"># monthly std</span>
<span class="bi">print</span>(ts.resample(<span class="st">"ME"</span>).first())   <span class="cm"># first value per month</span>
<span class="bi">print</span>(ts.resample(<span class="st">"ME"</span>).last())    <span class="cm"># last value per month</span>

<span class="cm"># Multiple aggs</span>
<span class="bi">print</span>(ts.resample(<span class="st">"ME"</span>).agg([<span class="st">"mean"</span>,<span class="st">"min"</span>,<span class="st">"max"</span>]))

<span class="cm"># Upsampling: monthly &rarr; daily (with interpolation)</span>
daily = monthly.resample(<span class="st">"D"</span>).interpolate(method=<span class="st">"linear"</span>)
<span class="bi">print</span>(daily.head(<span class="nm">10</span>))

<span class="cm"># OHLC resampling (finance)</span>
<span class="bi">print</span>(ts.resample(<span class="st">"ME"</span>).ohlc().head())  <span class="cm"># open, high, low, close</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Monthly mean: 2024-01-31: 0.05, 2024-02-29: -0.12, ...</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Rolling &amp; Expanding Windows</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Rolling window (moving average)</span>
<span class="bi">print</span>(ts.rolling(window=<span class="nm">7</span>).mean().head(<span class="nm">10</span>))   <span class="cm"># 7-day MA</span>
<span class="bi">print</span>(ts.rolling(window=<span class="nm">30</span>).mean().head(<span class="nm">35</span>))  <span class="cm"># 30-day MA</span>

<span class="cm"># Rolling std, min, max</span>
<span class="bi">print</span>(ts.rolling(<span class="nm">7</span>).std().head(<span class="nm">10</span>))
<span class="bi">print</span>(ts.rolling(<span class="nm">7</span>).min().head(<span class="nm">10</span>))

<span class="cm"># Minimum periods (allow NaN at start)</span>
<span class="bi">print</span>(ts.rolling(<span class="nm">7</span>, min_periods=<span class="nm">1</span>).mean().head(<span class="nm">10</span>))

<span class="cm"># Centered window</span>
<span class="bi">print</span>(ts.rolling(<span class="nm">7</span>, center=<span class="kw">True</span>).mean().head(<span class="nm">10</span>))

<span class="cm"># Expanding window (cumulative from start)</span>
<span class="bi">print</span>(ts.expanding().mean().head(<span class="nm">10</span>))  <span class="cm"># cumulative mean</span>
<span class="bi">print</span>(ts.expanding().sum().head(<span class="nm">10</span>))   <span class="cm"># cumulative sum</span>

<span class="cm"># Exponentially weighted moving average</span>
<span class="bi">print</span>(ts.ewm(span=<span class="nm">7</span>).mean().head(<span class="nm">10</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Rolling averages with NaN for first (window-1) values]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Shifting &amp; Lagging</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># shift(n) &mdash; shift values by n periods</span>
<span class="bi">print</span>(ts.head())
<span class="bi">print</span>(ts.shift(<span class="nm">1</span>).head())    <span class="cm"># lag by 1 day</span>
<span class="bi">print</span>(ts.shift(-<span class="nm">1</span>).head())   <span class="cm"># lead by 1 day</span>

<span class="cm"># Percent change</span>
<span class="bi">print</span>(ts.pct_change().head())  <span class="cm"># day-over-day % change</span>

<span class="cm"># Difference</span>
<span class="bi">print</span>(ts.diff().head())        <span class="cm"># day-over-day difference</span>
<span class="bi">print</span>(ts.diff(<span class="nm">7</span>).head(<span class="nm">10</span>))    <span class="cm"># week-over-week diff</span>

<span class="cm"># Common pattern: create lag features for ML</span>
df_ts = pd.DataFrame({<span class="st">"value"</span>: ts.values[:<span class="nm">10</span>]})
df_ts[<span class="st">"lag_1"</span>] = df_ts[<span class="st">"value"</span>].shift(<span class="nm">1</span>)
df_ts[<span class="st">"lag_7"</span>] = df_ts[<span class="st">"value"</span>].shift(<span class="nm">7</span>)
df_ts[<span class="st">"diff_1"</span>] = df_ts[<span class="st">"value"</span>].diff()
<span class="bi">print</span>(df_ts)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[DataFrame with value, lag_1, lag_7, diff_1 columns]</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Timedelta &amp; Period</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Timedelta &mdash; duration</span>
td = pd.Timedelta(<span class="st">"5 days 3 hours"</span>)
<span class="bi">print</span>(td)
<span class="bi">print</span>(pd.Timestamp(<span class="st">"2024-01-01"</span>) + td)  <span class="cm"># 2024-01-06 03:00:00</span>

<span class="cm"># Timedelta arithmetic</span>
dates = pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">5</span>)
<span class="bi">print</span>(dates + pd.Timedelta(days=<span class="nm">10</span>))  <span class="cm"># shift all by 10 days</span>

<span class="cm"># Date components</span>
ts_df = pd.DataFrame({<span class="st">"date"</span>: pd.date_range(<span class="st">"2024-01-01"</span>, periods=<span class="nm">100</span>)})
ts_df[<span class="st">"year"</span>] = ts_df[<span class="st">"date"</span>].dt.year
ts_df[<span class="st">"month"</span>] = ts_df[<span class="st">"date"</span>].dt.month
ts_df[<span class="st">"day"</span>] = ts_df[<span class="st">"date"</span>].dt.day
ts_df[<span class="st">"weekday"</span>] = ts_df[<span class="st">"date"</span>].dt.day_name()
ts_df[<span class="st">"quarter"</span>] = ts_df[<span class="st">"date"</span>].dt.quarter
<span class="bi">print</span>(ts_df.head())

<span class="cm"># Timezone handling</span>
utc = pd.Timestamp(<span class="st">"2024-01-01"</span>, tz=<span class="st">"UTC"</span>)
eastern = utc.tz_convert(<span class="st">"US/Eastern"</span>)
<span class="bi">print</span>(<span class="st">f"UTC: {utc} &rarr; Eastern: {eastern}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Timedelta: 5 days 03:00:00<br>date components: year, month, day, weekday, quarter</div></div></section>''',
("visualization.html","Visualization"),("../data-analysis/exploratory.html","Data Analysis"))

print("visualization.html + groupby.html + time-series.html expanded!")
