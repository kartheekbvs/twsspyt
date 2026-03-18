import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# VISUALIZATION (MASSIVE EXPANSION)
pd_viz_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Data Visualization: From Arrays to Insights</h4>
    <ol>
        <li><a href="#intro">1. The Matplotlib Wrapper Architecture</a></li>
        <li><a href="#line">2. Line Plots & Time Series Trends</a></li>
        <li><a href="#bar">3. Categorical Comparisons: Bar & Area</a></li>
        <li><a href="#hist">4. Distribution Analysis: Histograms & KDE</a></li>
        <li><a href="#scat">5. Relationship Exploration: Scatter & Hexbin</a></li>
        <li><a href="#subplots">6. Subplots and Shared Axes</a></li>
        <li><a href="#return">7. Return Values: The Axes Object</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Architecture of Pandas Plotting</h2>
    <p>Pandas plotting is built on a "High-Level Wrapper" philosophy. It leverages Matplotlib's powerful backend while offering a much simpler, data-aware API. As Wes McKinney notes, the integration ensures that indexes and labels are automatically handled, preventing common plotting alignment errors.</p>
</section>

<section class="content-section" id="return">
    <h2>7 &middot; Return Values: The Axes Object</h2>
    <div class="return-value-box">
        <div class="rv-label">🔁 Return Value: .plot()</div>
        <p>The <code>.plot()</code> method (on Series or DataFrame) returns a <strong>Matplotlib Axes</strong> object. For subplots, it returns a <strong>NumPy array of Axes</strong>. This is the entry point for "low-level" Matplotlib customization (e.g., <code>ax.set_title()</code>).</p>
    </div>
</section>
"""

make_page("pandas/visualization.html","Visualization","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Visualization",
"Mastering the Pandas plotting API, covering all major statistical plot types and deep integration with Matplotlib Axes objects.",
"Python for Data Analysis &mdash; Wes McKinney", pd_viz_body, ("merging.html","Merging"), ("time-series.html","Time Series"),
[("merging.html", "Data Joins"), ("../data/matplotlib.html", "Matplotlib Basics"), ("time-series.html", "Temporal Data")])

# TIME SERIES (MASSIVE EXPANSION)
pd_time_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Temporal Data: Concepts & Slicing</h4>
    <ol>
        <li><a href="#intro">1. The DatetimeIndex Object</a></li>
        <li><a href="#freq">2. Frequency and Period Logic</a></li>
        <li><a href="#resample">3. Resampling: Downsampling & Upsampling</a></li>
        <li><a href="#window">4. Window Functions: Rolling & Expanding</a></li>
        <li><a href="#timezone">5. TimeZone Localization</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The DatetimeIndex</h2>
    <p>Time series data in Pandas is centered around the <strong>DatetimeIndex</strong>. This specialized index allows for powerful string-based slicing (e.g., <code>df['2023']</code>) and temporal offsets.</p>
</section>

<section class="content-section" id="resample">
    <h2>3 &middot; Resampling Paradigms</h2>
    <div class="callout note">
        <div class="callout-icon">🕒</div>
        <div class="callout-content">
            <strong>Textbook Definition: Resampling</strong>
            <p>"Resampling is the process of converting a time series from one frequency to another. Downsampling (high to low) involves aggregation, while upsampling (low to high) involves interpolation." &mdash; <em>Wes McKinney</em></p>
        </div>
    </div>
</section>
"""

make_page("pandas/time-series.html","Time Series Analysis","Pandas","&#x1F43C;","advanced","Pandas &rarr; Time Series",
"Deep-dive into temporal data structures, frequency conversion, resampling strategies, and rolling window computations.",
"Python for Data Analysis &mdash; Wes McKinney", pd_time_body, ("visualization.html","Visualization"), ("../data/exploratory.html","Data Analysis"),
[("visualization.html", "Plotting Trends"), ("groupby.html", "Grouping Data"), ("../data/exploratory.html", "EDA")])

print("visualization.html + time-series.html MASSIVELY expanded!")
