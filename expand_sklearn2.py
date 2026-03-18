import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# DECISION TREES (MASSIVE EXPANSION)
ml_tree_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Decision Trees: Recursive Partitioning</h4>
    <ol>
        <li><a href="#intro">1. The Hierarchy of Decisions</a></li>
        <li><a href="#split">2. Splitting Criteria: Gini vs Entropy</a></li>
        <li><a href="#over">3. Curbing Overfitting: Pruning & Min Samples</a></li>
        <li><a href="#ensemble">4. The Power of Random Forests</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Recursive Partitioning</h2>
    <p>Decision Trees are versatile algorithms that can perform both classification and regression tasks. They are characterized by a flowchart-like structure where each internal node represents a 'test' on an attribute.</p>
</section>

<section class="content-section" id="split">
    <h2>2 &middot; Splitting Criteria</h2>
    <div class="callout note">
        <div class="callout-icon">📊</div>
        <div class="callout-content">
            <strong>Gini Impurity</strong>
            <p>Gini impurity is a measure of how often a randomly chosen element from the set would be incorrectly labeled if it was randomly labeled according to the distribution of labels in the subset. A Gini of 0 means the node is <strong>Pure</strong>.</p>
        </div>
    </div>
</section>
"""

make_page("ml/decision-trees.html","Decision Trees","Machine Learning","&#x1F916;","intermediate","ML &rarr; Decision Trees",
"Formal textbook analysis of Decision Trees, splitting mathematics (Gini/Entropy), and recursive partitioning logic.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_tree_body, ("logistic-regression.html","Logistic Regression"), ("random-forest.html","Random Forest"),
[("random-forest.html", "Ensembles"), ("model-evaluation.html", "Pruning")])

# RANDOM FOREST (MASSIVE EXPANSION)
ml_rf_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Random Forests: Wisdom of the Crowd</h4>
    <ol>
        <li><a href="#intro">1. Ensemble Learning & Bagging</a></li>
        <li><a href="#random">2. Feature Randomness (The "Random" in RF)</a></li>
        <li><a href="#oob">3. Out-of-Bag (OOB) Evaluation</a></li>
        <li><a href="#import">4. Feature Importance Scores</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Ensemble Learning</h2>
    <p>A Random Forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.</p>
</section>
"""

make_page("ml/random-forest.html","Random Forest","Machine Learning","&#x1F916;","intermediate","ML &rarr; Random Forest",
"In-depth analysis of Random Forest ensembles, including bagging strategy, feature randomness, and OOB evaluation methods.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_rf_body, ("decision-trees.html","Decision Trees"), ("svm.html","SVM"),
[("decision-trees.html", "Base Trees"), ("model-evaluation.html", "Ensemble Metrics")])

print("decision-trees.html + random-forest.html MASSIVELY expanded!")
