import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# INTRO TO ML (MASSIVE EXPANSION)
ml_intro_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Machine Learning: The Scikit-Learn Pipeline</h4>
    <ol>
        <li><a href="#intro">1. The Formal Definition of Learning</a></li>
        <li><a href="#types">2. Supervised vs Unsupervised Learning</a></li>
        <li><a href="#api">3. The Estimator API Philosophy</a></li>
        <li><a href="#workflow">4. The End-to-End Workflow</a></li>
        <li><a href="#scaling">5. Scaling & Preprocessing</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Formal Definition of Learning</h2>
    <p>Machine Learning is the study of algorithms that improve through experience. As Tom Mitchell formally defines it, a computer program is said to learn from experience <em>E</em> with respect to some task <em>T</em> and performance measure <em>P</em>, if its performance at tasks in <em>T</em> improves with experience <em>E</em>.</p>
</section>

<section class="content-section" id="api">
    <h2>3 &middot; The Estimator API Philosophy</h2>
    <div class="callout note">
        <div class="callout-icon">🛠️</div>
        <div class="callout-content">
            <strong>The Consistency Principle</strong>
            <p>Every object in Scikit-Learn follows a strict interface. <strong>Estimators</strong> use <code>.fit()</code>, <strong>Transformers</strong> use <code>.transform()</code>, and <strong>Predictors</strong> use <code>.predict()</code>. This design allows for the creation of complex <strong>Pipelines</strong>.</p>
        </div>
    </div>
</section>

<section class="content-section" id="workflow">
    <h2>4 &middot; The End-to-End Workflow</h2>
    <p>A typical ML project sequence: 1. Data Selection &rarr; 2. Data Preprocessing &rarr; 3. Feature Selection &rarr; 4. Model Selection &rarr; 5. Training &rarr; 6. Evaluation.</p>
    <div class="return-value-box">
        <div class="rv-label">🔁 Return Value: .fit()</div>
        <p>The <code>model.fit()</code> method returns <strong>self</strong>. This enables method chaining: <code>model = LogisticRegression().fit(X, y)</code>.</p>
    </div>
</section>
"""

make_page("ml/intro-ml.html","Introduction to Machine Learning","Machine Learning","&#x1F916;","beginner","ML &rarr; Introduction",
"Formal textbook introduction to Machine Learning, the Scikit-Learn API philosophy, and the end-to-end data science workflow.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_intro_body, ("../pandas/visualization.html","Pandas Visualization"), ("linear-regression.html","Linear Regression"),
[("../pandas/series-dataframe.html", "Data Structures"), ("model-evaluation.html", "Metrics")])

# LINEAR REGRESSION (MASSIVE EXPANSION)
ml_lin_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Linear Regression: Ordinary Least Squares</h4>
    <ol>
        <li><a href="#intro">1. The Statistical Hypothesis</a></li>
        <li><a href="#math">2. The Normal Equation vs Gradient Descent</a></li>
        <li><a href="#metrics">3. Evaluating Regression: MSE, RMSE, R²</a></li>
        <li><a href="#regular">4. Regularization: Ridge, Lasso, Elastic Net</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Statistical Hypothesis</h2>
    <p>Linear Regression models the relationship between a dependent variable and one or more independent variables using a linear function.</p>
</section>

<section class="content-section" id="math">
    <h2>2 &middot; The Mathematics of Fitting</h2>
    <div class="callout note">
        <div class="callout-icon">📐</div>
        <div class="callout-content">
            <strong>Ordinary Least Squares (OLS)</strong>
            <p>OLS minimizes the sum of squared residuals between the observed targets and the predictions. This can be solved analytically using the <strong>Normal Equation</strong> or iteratively using <strong>Gradient Descent</strong>.</p>
        </div>
    </div>
</section>
"""

make_page("ml/linear-regression.html","Linear Regression","Machine Learning","&#x1F916;","intermediate","ML &rarr; Regression",
"In-depth analysis of Linear Regression, covering the Normal Equation, Gradient Descent, and regularization techniques like Ridge and Lasso.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_lin_body, ("intro-ml.html","Introduction"), ("logistic-regression.html","Logistic Regression"),
[("intro-ml.html", "ML Workflow"), ("model-evaluation.html", "Regression Metrics")])

print("intro-ml.html + linear-regression.html MASSIVELY expanded!")
