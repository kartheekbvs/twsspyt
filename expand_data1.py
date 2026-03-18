import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# EDA
make_page("data/exploratory.html","Exploratory Data Analysis","Data Analysis","&#x1F4CA;","intermediate","Data &rarr; EDA",
"EDA is the bedrock of data science. This section covers textbook patterns for understanding data distributions and relationships.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">The Goal of EDA</a></li>
<li><a href="#s2">Return Value: .describe()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; The Goal of EDA</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Exploratory Data Analysis is not a formal process with a strict set of rules. More than anything, EDA is a state of mind. You should use it to investigate the quality of your data." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: .describe()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>df.describe()</code> method returns a <strong>DataFrame</strong> where indexes are the statistics (count, mean, std, etc.) and columns are the numeric features of the original data.</p>
</div>
</section>''',
("matplotlib.html","Matplotlib"),("feature-engineering.html","Feature Engineering"),
[("../pandas/visualization.html", "Pandas Plotting"), ("../numpy/operations.html", "NumPy Stats")])

# FEATURE ENGINEERING
make_page("data/feature-engineering.html","Feature Engineering","Data Analysis","&#x1F4CA;","advanced","Data &rarr; Feature Engineering",
"Feature engineering creates new signals from raw data. This section provides textbook precision on the 'Garbage In, Garbage Out' principle.",
"Hands-On Machine Learning &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Signal vs Noise</a></li>
<li><a href="#s2">Return Value: Log Transform</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Signal vs Noise</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Feature engineering means coming up with better features to help your ML model learn the underlying structure of the data. Successful models are often 80% data preparation." &mdash; <em>Aur&eacute;lien G&eacute;ron</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: Log Transform</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Performing <code>np.log1p()</code> on a Series returns a new <strong>Series</strong> where skewed values are compressed into a more normal distribution, which is essential for many linear algorithms.</p>
</div>
</section>''',
("exploratory.html","EDA"),("../ml/preprocessing.html","Preprocessing"),
[("exploratory.html", "Understanding Data"), ("../ml/preprocessing.html", "Encoding Categoricals")])

# SEABORN
make_page("data/seaborn.html","Seaborn Visualization","Data Analysis","&#x1F4CA;","intermediate","Data &rarr; Seaborn",
"Seaborn is a high-level statistical viz library. This section provides textbook precision on visual encoding and grouping.",
"Python Data Science Handbook &mdash; Jake VanderPlas",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Statistical Aesthetics</a></li>
<li><a href="#s2">Return Value: sns.FacetGrid</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Statistical Aesthetics</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Seaborn is a library that simplifies the creation of complicated plots by working directly with Pandas DataFrames and handling the aggregation and mapping of data to visual aesthetics." &mdash; <em>Jake VanderPlas</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: sns.FacetGrid</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>High-level functions like <code>sns.relplot()</code> or <code>sns.catplot()</code> return a <strong>FacetGrid</strong> object. This object holds multiple subplots and allows for global adjustments to titles and labels across all 'facets'.</p>
</div>
</section>''',
("matplotlib.html","Matplotlib"),("feature-engineering.html","Feature Engineering"),
[("matplotlib.html", "Base Layer"), ("../pandas/visualization.html", "Pandas Wrapper")])

print("exploratory.html + feature-engineering.html + seaborn.html expanded!")
