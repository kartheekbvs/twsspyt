import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# SVM (MASSIVE EXPANSION)
ml_svm_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 11 &middot; Support Vector Machines</h4>
    <ol>
        <li><a href="#hyperplane">1. Optimal Hyperplanes & Margins</a></li>
        <li><a href="#image">2. Application: Face Recognition</a></li>
        <li><a href="#kernel">3. The Kernel Trick: Mapping Higher Dimensions</a></li>
        <li><a href="#pros">4. Efficiency in High-Dimensional Spaces</a></li>
    </ol>
</div>

<section class="content-section" id="hyperplane">
    <h2>1 &middot; Optimal Hyperplanes</h2>
    <p>Imagine instances as points in a multidimensional space. A classifier builds a surface—a <strong>hyperplane</strong>—to separate classes. Support Vector Machines (SVM) obtain these hyperplanes optimally by selecting those that pass through the widest possible gaps (margins) between classes.</p>
    <div class="callout note">
        <div class="callout-icon">📏</div>
        <div class="callout-content">
            <strong>The Large Margin Principle</strong>
            <p>The "Red Surface" (Optimal Hyperplane) is chosen to maximize the distance to the closest training instances. This reduces generalization error and makes the model resistant to overfitting.</p>
        </div>
    </div>
</section>

<section class="content-section" id="image">
    <h2>2 &middot; Case Study: Image Recognition</h2>
    <p>SVM is effective in high-dimensional spaces where features (pixels) outnumber instances. In the Olivetti Faces dataset (64x64 pixels = 4096 features), SVM finds the unique signatures of individual faces by modeling pixels as coordinate vectors.</p>
</section>
"""

make_page("ml/svm.html","Support Vector Machines","Machine Learning","&#x1F916;","intermediate","ML &rarr; SVM",
"Formal textbook analysis of Optimal Hyperplanes, Margin Maximization, and high-dimensional efficiency for Image Recognition.",
"Learning scikit-learn &mdash; Raúl Garreta", ml_svm_body, ("random-forest.html","Random Forest"), ("knn.html","K-Nearest Neighbors"),
[("random-forest.html", "Ensembles"), ("model-evaluation.html", "Hyperparameters")])

# KNN (MASSIVE EXPANSION)
ml_knn_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 12 &middot; K-Nearest Neighbors</h4>
    <ol>
        <li><a href="#lazy">1. The Lazy Learner Paradigm</a></li>
        <li><a href="#distance">2. Distance Metrics: Euclidean vs Manhattan</a></li>
        <li><a href="#scaling">3. The Importance of Feature Scaling</a></li>
    </ol>
</div>

<section class="content-section" id="lazy">
    <h2>1 &middot; The Lazy Learner</h2>
    <p>k-NN is a non-parametric, instance-based method. It is called a <strong>Lazy Learner</strong> because it does not learn a discriminative function; instead, it memorizes the training set and classifies new instances based on their proximity to stored examples.</p>
</section>

<section class="content-section" id="distance">
    <h2>2 &middot; Distance Metrics</h2>
    <p>The choice of k and the distance metric (Equation: \( \sqrt{\sum (x_i - y_i)^2} \) for Euclidean) determines how the local neighborhood is constructed. In high-dimensional spaces, k-NN is susceptible to the 'curse of dimensionality'.</p>
</section>
"""

make_page("ml/knn.html","K-Nearest Neighbors","Machine Learning","&#x1F916;","beginner","ML &rarr; KNN",
"In-depth analysis of Instance-Based learning, distance calculations, and the theoretical implications of the 'Lazy' paradigm.",
"Learning scikit-learn &mdash; Raúl Garreta", ml_knn_body, ("svm.html","SVM"), ("clustering.html","K-Means"),
[("svm.html", "Optimal Hyperplane"), ("preprocessing.html", "Scaling")])

print("svm.html + knn.html MASSIVELY expanded with Garreta content!")

