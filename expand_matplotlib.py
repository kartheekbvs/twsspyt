import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# MATPLOTLIB
make_page("data/matplotlib.html","Matplotlib Visualization","Data Analysis","&#x1F4CA;","intermediate","Data &rarr; Matplotlib",
"Matplotlib is the foundation of Python visualization. This section explores the anatomy of a figure with textbook definitions and return value analysis.",
"Python for Data Analysis &mdash; Wes McKinney, Matplotlib Documentation",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Anatomy of a Figure</a></li>
<li><a href="#s2">Return Value: plt.subplots()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Anatomy of a Figure</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"A Matplotlib <code>Figure</code> is the whole window in the user interface. Within the figure can be one or more <code>Axes</code> (an actual plot with x and y axes, title, etc.)." &mdash; <em>Matplotlib Docs</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: plt.subplots()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>plt.subplots()</code> function returns a <strong>Tuple</strong>: <code>(fig, ax)</code>. <code>fig</code> is the Figure object, and <code>ax</code> is either a single Axes object or a NumPy array of Axes objects (if multiple rows/cols are requested).</p>
</div>
</section>''',
("../ml/preprocessing.html","Preprocessing"),("seaborn.html","Seaborn"),
[("../pandas/visualization.html", "Pandas Plotting"), ("numpy/arrays.html", "NumPy for Data")])

print("matplotlib.html expanded!")
