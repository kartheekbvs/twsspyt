import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# LINEAR REGRESSION
make_page("ml/linear-regression.html","Linear Regression","Machine Learning","&#x1F916;","intermediate","ML &rarr; Linear Regression",
"Linear models are the workhorses of statistics and ML. This section covers textbook definitions for OLS and regularization.",
"Hands-On Machine Learning &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Normal Equation vs GD</a></li>
<li><a href="#s2">Return Value: .predict()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Normal Equation vs GD</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Linear Regression models can be trained using either a direct closed-form solution (the <em>Normal Equation</em>) or using an iterative optimization approach called <em>Gradient Descent</em>." &mdash; <em>Aur&eacute;lien G&eacute;ron</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: .predict()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>.predict()</code> method returns a <strong>NumPy Array</strong> of continuous values (floats). If you passed a 2D array of samples, you get a 1D array of predictions.</p>
</div>
</section>''',
("model-evaluation.html","Model Evaluation"),("logistic-regression.html","Logistic Regression"),
[("model-evaluation.html", "Regression Metrics"), ("../numpy/arrays.html", "NumPy Arrays")])

# LOGISTIC REGRESSION
make_page("ml/logistic-regression.html","Logistic Regression","Machine Learning","&#x1F916;","intermediate","ML &rarr; Logistic Regression",
"Logistic Regression is a classifier that estimates probabilities. This section provides textbook precision on the sigmoid function and decision logic.",
"Hands-On Machine Learning &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Estimating Probabilities</a></li>
<li><a href="#s2">Return Value: predict_proba()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Estimating Probabilities</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Just like Linear Regression, a Logistic Regression model computes a weighted sum of input features, but it outputs the <em>logistic</em> (or sigmoid) of this result." &mdash; <em>Aur&eacute;lien G&eacute;ron</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: predict_proba()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>While <code>.predict()</code> returns the class label (0 or 1), <code>.predict_proba()</code> returns a <strong>2D NumPy Array</strong> where each row contains the probabilities for all classes (e.g., <code>[P(class=0), P(class=1)]</code>).</p>
</div>
</section>''',
("linear-regression.html","Linear Regression"),("decision-trees.html","Decision Trees"),
[("model-evaluation.html", "Precision & Recall"), ("logistic-regression.html", "Classification Logic")])

print("linear-regression.html + logistic-regression.html expanded!")
