import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# ========== INTRO TO ML / SKLEARN OVERVIEW ==========
make_page("ml/intro-ml.html","Introduction to Machine Learning","Machine Learning","&#x1F916;","beginner","ML &rarr; Introduction",
"Scikit-learn is Python&#39;s most popular machine learning library. This page covers the complete ML workflow with formal textbook definitions and API deep dives.",
"Hands-On Machine Learning with Scikit-Learn &mdash; Aur&eacute;lien G&eacute;ron, Tom Mitchell &mdash; Machine Learning",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">What is Machine Learning?</a></li>
<li><a href="#s2">The ML Workflow</a></li>
<li><a href="#s3">Scikit-Learn API</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; What is Machine Learning?</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"A computer program is said to learn from experience <em>E</em> with respect to some class of tasks <em>T</em> and performance measure <em>P</em>, if its performance at tasks in <em>T</em>, as measured by <em>P</em>, improves with experience <em>E</em>." &mdash; <em>Tom Mitchell</em></p>
    </div>
</div>
<p>In Scikit-learn, this "experience" is your training data (<code>X_train</code>, <code>y_train</code>), the "task" is prediction (<code>.predict()</code>), and the "performance" is your metric (e.g., <code>accuracy_score</code>).</p>
</section>

<section class="content-section" id="s3"><h2>2 &middot; Scikit-Learn API</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: .fit()</div>
    <p>The <code>model.fit()</code> method returns <strong>self</strong> (the estimator instance itself). This allows for <strong>method chaining</strong>: <code>model = LogisticRegression().fit(X, y)</code>. After fitting, the model object is updated with learned parameters (identifiable by a trailing underscore, like <code>model.coef_</code>).</p>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: .predict()</div>
    <p>The <code>model.predict()</code> method returns a <strong>NumPy ndarray</strong> or a <strong>Pandas Series</strong> containing the predicted labels or values for each input sample.</p>
</div>
</section>''',
("model-evaluation.html","Model Evaluation"),("linear-regression.html","Linear Regression"),
[("../numpy/arrays.html", "NumPy ndarray"), ("../pandas/series-dataframe.html", "Pandas DataFrames")])

print("intro-ml.html expanded with enriched content!")

print("intro-ml.html expanded!")
