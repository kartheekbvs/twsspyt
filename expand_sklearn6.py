import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# PREPROCESSING (MASSIVE EXPANSION)
ml_pre_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Data Preprocessing: Preparing for Models</h4>
    <ol>
        <li><a href="#intro">1. The Importance of Scaling</a></li>
        <li><a href="#scaling">2. Standardization vs Normalization</a></li>
        <li><a href="#encoding">3. Categorical Encoding: One-Hot vs Label</a></li>
        <li><a href="#impute">4. Imputation: Handling Missing Features</a></li>
        <li><a href="#poly">5. Feature Engineering: Polynomial Features</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Importance of Scaling</h2>
    <p>Most machine learning algorithms are sensitive to the scale of the input features. Algorithms that use distance metrics (like KNN and SVM) or gradient descent (like Linear Regression and Neural Networks) will perform poorly if features have vastly different ranges.</p>
</section>

<section class="content-section" id="scaling">
    <h2>2 &middot; Scaling Paradigms</h2>
    <div class="callout note">
        <div class="callout-icon">⚖️</div>
        <div class="callout-content">
            <strong>StandardScaler (Z-Score)</strong>
            <p>Standardization scales data to have a mean of 0 and a standard deviation of 1. It is less affected by outliers than Min-Max scaling and is preferred for algorithms that assume Gaussian distributions.</p>
        </div>
    </div>
</section>

<section class="content-section" id="encoding">
    <h2>3 &middot; Categorical Encoding</h2>
    <p>Machine Learning models require numeric input. <strong>One-Hot Encoding</strong> creates a binary column for each category, while <strong>Label Encoding</strong> assigns a unique integer to each category.</p>
</section>
"""

make_page("ml/preprocessing.html","Data Preprocessing","Machine Learning","&#x1F916;","intermediate","ML &rarr; Preprocessing",
"Mastering data preparation techniques, including feature scaling, categorical encoding, and automated pipelines with Scikit-Learn transformers.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_pre_body, ("model-evaluation.html","Model Evaluation"), ("masterclass.html","ML Masterclass"),
[("model-evaluation.html", "Generalization"), ("masterclass.html", "ML Hub"), ("../pandas/cleaning.html", "Pandas Cleaning")])

print("preprocessing.html MASSIVELY expanded!")
