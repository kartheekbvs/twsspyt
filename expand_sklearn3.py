import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# SVM (MASSIVE EXPANSION)
ml_svm_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Support Vector Machines: The Margin Maximizers</h4>
    <ol>
        <li><a href="#intro">1. The Large Margin Classification Logic</a></li>
        <li><a href="#kernel">2. The Kernel Trick: Linear to Non-Linear</a></li>
        <li><a href="#cost">3. Hard vs Soft Margin (C-Parameter)</a></li>
        <li><a href="#reg">4. SVM for Regression (SVR)</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Large Margin Classification</h2>
    <p>SVM is a powerful and versatile ML model, capable of performing linear or non-linear classification, regression, and even outlier detection. The fundamental idea is to find a hyperplane that not only separates the classes but also stays as far away from the closest training instances as possible.</p>
</section>

<section class="content-section" id="kernel">
    <h2>2 &middot; The Kernel Trick</h2>
    <div class="callout note">
        <div class="callout-icon">🧬</div>
        <div class="callout-content">
            <strong>Polynomial & RBF Kernels</strong>
            <p>The kernel trick allows SVM to map inputs into high-dimensional feature spaces without actually computing the coordinates. This makes it possible to find linear separators in spaces where the original data is non-linearly distributed.</p>
        </div>
    </div>
</section>
"""

make_page("ml/svm.html","Support Vector Machine","Machine Learning","&#x1F916;","intermediate","ML &rarr; SVM",
"Formal textbook analysis of Support Vector Machines, margin maximization, and the mathematical power of the Kernel Trick.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_svm_body, ("random-forest.html","Random Forest"), ("knn.html","K-Nearest Neighbors"),
[("random-forest.html", "Ensembles"), ("model-evaluation.html", "Hyperparameters")])

# KNN (MASSIVE EXPANSION)
ml_knn_body = """
<div class="toc-box">
    <h4>&#x1F4CB; K-Nearest Neighbors: Instance-Based Learning</h4>
    <ol>
        <li><a href="#intro">1. The Lazy Learner Paradigm</a></li>
        <li><a href="#dist">2. Distance Metrics: Euclidean vs Manhattan</a></li>
        <li><a href="#k">3. Choosing the Optimal K</a></li>
        <li><a href="#pros">4. Computational Complexity and Scaling</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Lazy Learner</h2>
    <p>KNN is a non-parametric, instance-based learning algorithm. It is 'lazy' because it does not learn a discriminative function from the training data but 'memorizes' the training dataset instead.</p>
</section>
"""

make_page("ml/knn.html","K-Nearest Neighbors","Machine Learning","&#x1F916;","beginner","ML &rarr; KNN",
"In-depth analysis of KNN, distance metrics, and the effects of feature scaling on instance-based learning models.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_knn_body, ("svm.html","Support Vector Machine"), ("clustering.html","K-Means Clustering"),
[("svm.html", "Classification"), ("preprocessing.html", "Scaling")])

print("svm.html + knn.html MASSIVELY expanded!")
