import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# VISUALIZATION
make_page("pandas/visualization.html","Visualization","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Visualization",
"Pandas plotting is a high-level wrapper around Matplotlib. This section covers textbook definitions for plot types and return value analysis for figure objects.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Pandas &amp; Matplotlib</a></li>
<li><a href="#s2">Return Values</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Pandas &amp; Matplotlib</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Pandas has many built-in methods for creating visualizations from Series and DataFrame objects. Most of these are wrappers around the Matplotlib library." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Values</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: .plot()</div>
    <p>The <code>.plot()</code> method (on Series or DataFrame) returns a <strong>Matplotlib Axes</strong> object (or an array of them if <code>subplots=True</code>). This allows for further customization using Matplotlib commands.</p>
</div>
</section>''',
("cleaning.html","Data Cleaning"),("../data-analysis/exploratory.html","Exploratory Analysis"),
[("cleaning.html", "Preparing Data"), ("../data/matplotlib.html", "Matplotlib Basics")])

# GROUPBY
make_page("pandas/groupby.html","GroupBy &amp; Aggregation","Pandas","&#x1F43C;","intermediate","Pandas &rarr; GroupBy",
"The 'split-apply-combine' pattern is the heart of data aggregation. This section provides textbook precision on grouping logic.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Split-Apply-Combine</a></li>
<li><a href="#s2">Return Value: groupby()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Split-Apply-Combine</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Group operations can be described using the term <em>split-apply-combine</em>. Data is split into groups based on keys, a function is applied, and results are combined into a new object." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: groupby()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Calling <code>df.groupby()</code> does not compute anything immediately. It returns a <strong>DataFrameGroupBy</strong> object, which is an intermediate representation ready for aggregation (like <code>.sum()</code> or <code>.mean()</code>).</p>
</div>
</section>''',
("merging.html","Merging"),("visualization.html","Visualization"),
[("merging.html", "Data Joins"), ("../numpy/operations.html", "Reductions")])

# TIME SERIES
make_page("pandas/time-series.html","Time Series Analysis","Pandas","&#x1F43C;","advanced","Pandas &rarr; Time Series",
"Time series support is a standout feature of Pandas. This section covers resampling and frequency conversion with textbook definitions.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Resampling Logic</a></li>
<li><a href="#s2">Return Value: resample()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Resampling Logic</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Resampling refers to the process of converting a time series from one frequency to another. Aggregating higher frequency data to lower frequency is called <em>downsampling</em>, while the reverse is <em>upsampling</em>." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: resample()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Similar to <code>groupby()</code>, the <code>resample()</code> method returns a <strong>Resampler</strong> object. You must call an aggregation method on it to get a DataFrame or Series.</p>
</div>
</section>''',
("visualization.html","Visualization"),("../data-analysis/exploratory.html","Data Analysis"),
[("visualization.html", "Plotting Trends"), ("groupby.html", "Grouping Data")])

print("visualization.html + groupby.html + time-series.html expanded!")
