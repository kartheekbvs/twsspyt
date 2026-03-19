# DECISION TREES (MASSIVE EXPANSION)
ml_tree_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 4 &middot; Decision Trees: Interpretable Learning</h4>
    <ol>
        <li><a href="#intro">1. The Hierarchy of Decisions</a></li>
        <li><a href="#interpretable">2. The Explainability Advantage</a></li>
        <li><a href="#titanic">3. Case Study: Predicting Titanic Survival</a></li>
        <li><a href="#preprocess">4. Preprocessing: Encoding Categorical Data</a></li>
        <li><a href="#onehot">5. One Hot Encoding vs Label Encoding</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Interpretable Learning</h2>
    <p>A common argument against linear classifiers is that it is difficult to explain how the build model decides its predictions. If you have a high-dimensional SVM, visualizing the hyperplane is impossible. <strong>Decision Trees</strong> solve this by constructing a flowchart-like model that a human can easily understand and reproduce.</p>
</section>

<section class="content-section" id="titanic">
    <h2>3 &middot; Case Study: Titanic Survival</h2>
    <p>Using the Titanic dataset, we determine if a passenger would have survived given their age, passenger class, and sex. This demonstrates how trees handle mixed data types and missing values.</p>
    <div class="callout note">
        <div class="callout-icon">🚢</div>
        <div class="callout-content">
            <strong>The Titanic Hypothesis</strong>
            <p>Each instance in the dataset (from Vanderbilt Biostat) contains attributes like Name, Age, Pclass, and Survived. We manually select <code>'pclass'</code>, <code>'age'</code>, and <code>'sex'</code> as the primary influencers of survival.</p>
        </div>
    </div>
</section>

<section class="content-section" id="preprocess">
    <h2>4 &middot; Preprocessing Categorical Data</h2>
    <p>Decision Trees in Scikit-Learn expect real-valued features. Categorical data (like <code>male/female</code>) must be converted:</p>
    <ul>
        <li><strong>LabelEncoder:</strong> Converts categorical sets into <code>0..K-1</code> integers. Useful for ordinal data.</li>
        <li><strong>OneHotEncoder:</strong> Creates binary columns (indicator variables) for each class. This avoids introducing an artificial ordering between classes like '1st', '2nd', and '3rd'.</li>
    </ul>
    <div class="code-block">
        <div class="code-header"><span>Python</span><button class="copy-btn">Copy</button></div>
        <pre><code>from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

# Encode Sex as 0 or 1
enc = LabelEncoder()
titanic_X[:, 2] = enc.fit_transform(titanic_X[:, 2])

# Handle Missing Values (Imputation)
mean_age = np.mean(titanic_X[titanic_X[:, 1] != 'NA', 1].astype(float))
titanic_X[titanic_X[:, 1] == 'NA', 1] = mean_age</code></pre>
    </div>
</section>
"""

make_page("ml/decision-trees.html","Decision Trees & Interpretable ML","Machine Learning","&#x1F916;","intermediate","ML &rarr; Decision Trees",
"Massive textbook expansion of Decision Trees using the Titanic survival case study, covering explainability, preprocessing, and one-hot encoding.",
"Learning scikit-learn &mdash; Raúl Garreta", ml_tree_body, ("naive-bayes.html","Naive Bayes"), ("random-forest.html","Random Forest"),
[("random-forest.html", "Ensembles"), ("model-evaluation.html", "Pruning")])

# RANDOM FOREST (MASSIVE EXPANSION remains placeholder for now)
ml_rf_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Random Forests: Wisdom of the Crowd</h4>
    <ol>
        <li><a href="#intro">1. Ensemble Learning & Bagging</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Ensemble Learning</h2>
    <p>A Random Forest is a meta estimator that fits a number of decision tree classifiers... (More textbook content being mapped)</p>
</section>
"""

make_page("ml/random-forest.html","Random Forest","Machine Learning","&#x1F916;","intermediate","ML &rarr; Random Forest",
"In-depth analysis of Random Forest ensembles, including bagging strategy, feature randomness, and OOB evaluation methods.",
"Hands-On Machine Learning &mdash; Aurélien Géron", ml_rf_body, ("decision-trees.html","Decision Trees"), ("svm.html","SVM"),
[("decision-trees.html", "Base Trees"), ("model-evaluation.html", "Ensemble Metrics")])

print("decision-trees.html expanded with Titanic example!")

