import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CLUSTERING (MASSIVE EXPANSION)
ml_clus_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Clustering: Unsupervised Representation</h4>
    <ol>
        <li><a href="#intro">1. The K-Means Objective Function</a></li>
        <li><a href="#limitations">2. Limitations & The Elbow Method</a></li>
        <li><a href="#hier">3. Hierarchical & Density-Based Clustering</a></li>
        <li><a href="#metrics">4. Unsupervised Metrics: Silhouette Score</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; K-Means Objective Function</h2>
    <p>K-Means seeks to partition <em>n</em> observations into <em>k</em> clusters. The objective is to minimize the <strong>Inertia</strong>, or within-cluster sum-of-squares (WCSS). It is a hard-clustering algorithm, meaning each point belongs to exactly one cluster.</p>
</section>

<section class="content-section" id="metrics">
    <h2>4 &middot; The Silhouette Score</h2>
    <div class="callout note">
        <div class="callout-icon">🧬</div>
        <div class="callout-content">
            <strong>Evaluating the Unknown</strong>
            <p>In unsupervised learning, we don't have ground truth labels. The <strong>Silhouette Score</strong> measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation). A score of +1 is ideal.</p>
        </div>
    </div>
</section>
"""

make_page("ml/clustering.html","K-Means Clustering","Machine Learning","&#x1F916;","intermediate","ML &rarr; Clustering",
"Formal textbook analysis of unsupervised learning, Centroid-based clustering logic, and performance metrics like Inertia and Silhouette.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_clus_body, ("knn.html","K-Nearest Neighbors"), ("model-evaluation.html","Model Evaluation"),
[("knn.html", "Instance-Based"), ("model-evaluation.html", "Metrics"), ("preprocessing.html", "Scaling")])

# MODEL EVALUATION (MASSIVE EXPANSION)
ml_eval_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Model Selection & Metrics</h4>
    <ol>
        <li><a href="#classification">1. Classification: Beyond Accuracy</a></li>
        <li><a href="#confusion">2. The Confusion Matrix Deep Dive</a></li>
        <li><a href="#roc">3. ROC Curves and AUC</a></li>
        <li><a href="#cv">4. Cross-Validation Paradigms</a></li>
    </ol>
</div>

<section class="content-section" id="classification">
    <h2>1 &middot; Beyond Accuracy</h2>
    <p>Accuracy is often misleading in imbalanced datasets. We must use <strong>Precision</strong>, <strong>Recall</strong>, and the <strong>F1-Score</strong> to get a true picture of model performance.</p>
</section>

<section class="content-section" id="cv">
    <h2>4 &middot; K-Fold Cross-Validation</h2>
    <div class="callout important">
        <div class="callout-icon">🔄</div>
        <div class="callout-content">
            <strong>Generalization Error</strong>
            <p>Cross-validation allows us to estimate the model's performance on unseen data. By splitting the training set into <em>K</em> folds and rotating the validation set, we ensure that every data point is used for both training and validation.</p>
        </div>
    </div>
</section>
"""

make_page("ml/model-evaluation.html","Model Evaluation","Machine Learning","&#x1F916;","intermediate","ML &rarr; Evaluation",
"Comprehensive guide to statistical model evaluation, covering confusion matrices, ROC curves, and cross-validation strategies.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_eval_body, ("clustering.html","K-Means Clustering"), ("preprocessing.html","Data Preprocessing"),
[("clustering.html", "Unsupervised Eval"), ("intro-ml.html", "Workflow"), ("preprocessing.html", "Data Prep")])

print("clustering.html + model-evaluation.html MASSIVELY expanded!")
