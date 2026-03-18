import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# MODEL EVALUATION
make_page("ml/model-evaluation.html","Model Evaluation &amp; Selection","Machine Learning","&#x1F916;","intermediate","ML &rarr; Model Evaluation",
"Model evaluation is critical for assessing generalization. This section covers textbook definitions for cross-validation and return value analysis for split operations.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron, sklearn docs",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Cross-Validation</a></li>
<li><a href="#s2">Return Value: train_test_split</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Cross-Validation</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"A great way to evaluate a model is to use <em>K-fold cross-validation</em>: it randomly splits the training set into K distinct subsets called folds." &mdash; <em>Aur&eacute;lien G&eacute;ron</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: train_test_split</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>train_test_split()</code> function returns a <strong>List</strong> of four items: <code>[X_train, X_test, y_train, y_test]</code> (assuming one X and one y input). These are typically NumPy <strong>ndarrays</strong> or Pandas <strong>DataFrames/Series</strong>.</p>
</div>
</section>''',
("intro-ml.html","Intro to ML"),("linear-regression.html","Linear Regression"),
[("intro-ml.html", "ML Basics"), ("../pandas/selection.html", "Data Selection")])

# PREPROCESSING
make_page("ml/preprocessing.html","Preprocessing &amp; Encoding","Machine Learning","&#x1F4CA;","intermediate","ML &rarr; Preprocessing",
"Data preprocessing transforms raw data into a format suitable for models. This section covers scaling and encoding with textbook definitions.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Feature Scaling</a></li>
<li><a href="#s2">Return Value: Scalers</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Feature Scaling</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Machine Learning algorithms don't perform well when the input numerical attributes have very different scales. There are two common ways to get all attributes to have the same scale: <em>min-max scaling</em> and <em>standardization</em>." &mdash; <em>Aur&eacute;lien G&eacute;ron</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: fit_transform</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Most transformer methods like <code>fit_transform()</code> return a <strong>new 2D NumPy ndarray</strong> (or sparse matrix), even if the input was a Pandas DataFrame.</p>
</div>
</section>''',
("model-evaluation.html","Model Evaluation"),("../data/feature-engineering.html","Feature Engineering"),
[("model-evaluation.html", "Evaluation"), ("../numpy/arrays.html", "NumPy Arrays")])

print("model-evaluation.html + preprocessing.html expanded!")
