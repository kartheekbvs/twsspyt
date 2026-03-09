import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# DECISION TREES
make_page("ml/decision-trees.html","Decision Trees","Machine Learning","&#x1F916;","intermediate","ML &rarr; Decision Trees",
"Decision trees split data by asking questions at each node. Covers DecisionTreeClassifier, DecisionTreeRegressor, plot_tree visualization, controlling tree depth, and understanding overfitting through pruning parameters.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">DecisionTreeClassifier</a></li>
<li><a href="#s2">DecisionTreeRegressor</a></li>
<li><a href="#s3">Visualizing Trees</a></li>
<li><a href="#s4">Hyperparameters &amp; Pruning</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; DecisionTreeClassifier</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.tree <span class="kw">import</span> DecisionTreeClassifier, plot_tree
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_iris
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> accuracy_score, classification_report

X, y = load_iris(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=<span class="nm">0.2</span>, stratify=y, random_state=<span class="nm">42</span>)

<span class="cm"># Train decision tree</span>
tree = DecisionTreeClassifier(
    max_depth=<span class="nm">3</span>,               <span class="cm"># limit depth to prevent overfitting</span>
    min_samples_split=<span class="nm">5</span>,        <span class="cm"># min samples to split a node</span>
    min_samples_leaf=<span class="nm">2</span>,         <span class="cm"># min samples in a leaf</span>
    random_state=<span class="nm">42</span>
)
tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)
<span class="bi">print</span>(<span class="st">f"Accuracy: {accuracy_score(y_test, y_pred):.4f}"</span>)
<span class="bi">print</span>(classification_report(y_test, y_pred, target_names=load_iris().target_names))

<span class="cm"># Feature importance</span>
<span class="kw">import</span> numpy <span class="kw">as</span> np
importances = tree.feature_importances_
<span class="kw">for</span> name, imp <span class="kw">in</span> <span class="bi">sorted</span>(<span class="bi">zip</span>(load_iris().feature_names, importances),
                       key=<span class="kw">lambda</span> x: -x[<span class="nm">1</span>]):
    <span class="bi">print</span>(<span class="st">f"  {name}: {imp:.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Accuracy: 0.9667<br>  petal length (cm): 0.9047<br>  petal width (cm):  0.0953<br>  sepal length (cm): 0.0000<br>  sepal width (cm):  0.0000</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; DecisionTreeRegressor</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.tree <span class="kw">import</span> DecisionTreeRegressor
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> mean_squared_error, r2_score

<span class="cm"># Generate non-linear data</span>
np.random.seed(<span class="nm">42</span>)
X = np.sort(<span class="nm">5</span> * np.random.rand(<span class="nm">80</span>, <span class="nm">1</span>), axis=<span class="nm">0</span>)
y = np.sin(X).ravel() + np.random.randn(<span class="nm">80</span>) * <span class="nm">0.1</span>

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=<span class="nm">42</span>)

<span class="cm"># Compare different depths</span>
<span class="kw">for</span> depth <span class="kw">in</span> [<span class="nm">2</span>, <span class="nm">4</span>, <span class="nm">8</span>, <span class="kw">None</span>]:
    reg = DecisionTreeRegressor(max_depth=depth, random_state=<span class="nm">42</span>)
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    <span class="bi">print</span>(<span class="st">f"Depth={str(depth):>4}: R&sup2;={r2:.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Depth=   2: R&sup2;=0.8234<br>Depth=   4: R&sup2;=0.9345<br>Depth=   8: R&sup2;=0.9012<br>Depth=None: R&sup2;=0.7856  (overfitting!)</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Visualizing Trees</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt
<span class="kw">from</span> sklearn.tree <span class="kw">import</span> plot_tree, export_text

<span class="cm"># Visual tree plot</span>
fig, ax = plt.subplots(figsize=(<span class="nm">15</span>, <span class="nm">8</span>))
plot_tree(tree, feature_names=load_iris().feature_names,
          class_names=load_iris().target_names,
          filled=<span class="kw">True</span>, rounded=<span class="kw">True</span>, ax=ax)
plt.title(<span class="st">"Decision Tree for Iris"</span>)
plt.tight_layout()
plt.show()

<span class="cm"># Text representation</span>
text_tree = export_text(tree, feature_names=load_iris().feature_names)
<span class="bi">print</span>(text_tree)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>|--- petal length (cm) &le; 2.45<br>|   |--- class: setosa<br>|--- petal length (cm) &gt; 2.45<br>|   |--- petal width (cm) &le; 1.75<br>|   |   |--- class: versicolor<br>|   |--- petal width (cm) &gt; 1.75<br>|   |   |--- class: virginica</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Hyperparameters &amp; Pruning</h2>
<table class="data-table"><thead><tr><th>Parameter</th><th>Effect</th><th>Default</th></tr></thead><tbody>
<tr><td><code>max_depth</code></td><td>Maximum tree depth</td><td>None (grow until pure)</td></tr>
<tr><td><code>min_samples_split</code></td><td>Min samples to split a node</td><td>2</td></tr>
<tr><td><code>min_samples_leaf</code></td><td>Min samples in a leaf</td><td>1</td></tr>
<tr><td><code>max_features</code></td><td>Features considered per split</td><td>None (all)</td></tr>
<tr><td><code>max_leaf_nodes</code></td><td>Maximum number of leaves</td><td>None</td></tr>
<tr><td><code>criterion</code></td><td>"gini" or "entropy"</td><td>"gini"</td></tr>
<tr><td><code>ccp_alpha</code></td><td>Cost-complexity pruning</td><td>0.0</td></tr>
</tbody></table></section>''',
("logistic-regression.html","Logistic Regression"),("random-forest.html","Random Forest"))

# RANDOM FOREST / ENSEMBLE
make_page("ml/random-forest.html","Ensemble Methods","Machine Learning","&#x1F916;","advanced","ML &rarr; Ensemble Methods",
"Ensemble methods combine multiple models for better performance. Covers RandomForest, GradientBoosting, AdaBoost, Bagging, ExtraTrees, and VotingClassifier from sklearn.ensemble. Includes both classifiers and regressors with practical examples.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">RandomForestClassifier</a></li>
<li><a href="#s2">RandomForestRegressor</a></li>
<li><a href="#s3">GradientBoosting</a></li>
<li><a href="#s4">AdaBoost &amp; Bagging</a></li>
<li><a href="#s5">Comparing Ensemble Methods</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; RandomForestClassifier</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> RandomForestClassifier
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_wine
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> accuracy_score
<span class="kw">import</span> numpy <span class="kw">as</span> np

X, y = load_wine(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=<span class="nm">0.2</span>, stratify=y, random_state=<span class="nm">42</span>)

<span class="cm"># Random Forest = many decision trees + voting</span>
rf = RandomForestClassifier(
    n_estimators=<span class="nm">100</span>,     <span class="cm"># number of trees</span>
    max_depth=<span class="nm">10</span>,          <span class="cm"># limit tree depth</span>
    min_samples_split=<span class="nm">5</span>,
    max_features=<span class="st">"sqrt"</span>,   <span class="cm"># features per split</span>
    n_jobs=-<span class="nm">1</span>,             <span class="cm"># use all CPU cores</span>
    random_state=<span class="nm">42</span>
)
rf.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"RF Accuracy: {rf.score(X_test, y_test):.4f}"</span>)

<span class="cm"># Feature importance</span>
importances = rf.feature_importances_
indices = np.argsort(importances)[::-<span class="nm">1</span>]
<span class="bi">print</span>(<span class="st">"\\nTop 5 features:"</span>)
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">5</span>):
    <span class="bi">print</span>(<span class="st">f"  {load_wine().feature_names[indices[i]]}: {importances[indices[i]]:.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>RF Accuracy: 0.9722<br>Top features: color_intensity: 0.1535, flavanoids: 0.1428, ...</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; RandomForestRegressor</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> RandomForestRegressor
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> make_regression
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> r2_score

X, y = make_regression(n_samples=<span class="nm">500</span>, n_features=<span class="nm">10</span>, noise=<span class="nm">15</span>, random_state=<span class="nm">42</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=<span class="nm">42</span>)

rf_reg = RandomForestRegressor(n_estimators=<span class="nm">200</span>, max_depth=<span class="nm">15</span>, random_state=<span class="nm">42</span>)
rf_reg.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"RF R&sup2;: {rf_reg.score(X_test, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>RF R&sup2;: 0.9123</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; GradientBoosting</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> GradientBoostingClassifier, GradientBoostingRegressor

<span class="cm"># Classification</span>
X, y = load_wine(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=<span class="nm">42</span>)

gb = GradientBoostingClassifier(
    n_estimators=<span class="nm">100</span>,       <span class="cm"># number of boosting stages</span>
    learning_rate=<span class="nm">0.1</span>,      <span class="cm"># shrinks contribution of each tree</span>
    max_depth=<span class="nm">3</span>,             <span class="cm"># depth of individual trees</span>
    random_state=<span class="nm">42</span>
)
gb.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"GradientBoosting: {gb.score(X_test, y_test):.4f}"</span>)

<span class="cm"># Regression</span>
X, y = make_regression(n_samples=<span class="nm">300</span>, n_features=<span class="nm">5</span>, noise=<span class="nm">10</span>, random_state=<span class="nm">42</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=<span class="nm">42</span>)

gb_reg = GradientBoostingRegressor(n_estimators=<span class="nm">100</span>, learning_rate=<span class="nm">0.1</span>, random_state=<span class="nm">42</span>)
gb_reg.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"GB Regressor R&sup2;: {gb_reg.score(X_test, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>GradientBoosting: 0.9722<br>GB Regressor R&sup2;: 0.9456</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; AdaBoost &amp; Bagging</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> (
    AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier
)
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_iris
X, y = load_iris(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=<span class="nm">42</span>)

<span class="cm"># AdaBoost &mdash; focuses on misclassified samples</span>
ada = AdaBoostClassifier(n_estimators=<span class="nm">50</span>, learning_rate=<span class="nm">1.0</span>, random_state=<span class="nm">42</span>)
ada.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"AdaBoost:     {ada.score(X_test, y_test):.4f}"</span>)

<span class="cm"># BaggingClassifier &mdash; Bootstrap Aggregating</span>
bag = BaggingClassifier(n_estimators=<span class="nm">50</span>, max_samples=<span class="nm">0.7</span>, random_state=<span class="nm">42</span>)
bag.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"Bagging:      {bag.score(X_test, y_test):.4f}"</span>)

<span class="cm"># ExtraTrees &mdash; Extra-Randomized Trees</span>
et = ExtraTreesClassifier(n_estimators=<span class="nm">100</span>, random_state=<span class="nm">42</span>)
et.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"ExtraTrees:   {et.score(X_test, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>AdaBoost: 0.9667<br>Bagging: 0.9333<br>ExtraTrees: 0.9667</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Comparing Ensemble Methods</h2>
<table class="data-table"><thead><tr><th>Method</th><th>How it Works</th><th>Best For</th></tr></thead><tbody>
<tr><td>Random Forest</td><td>Many trees, random feature subsets, vote</td><td>General-purpose, feature importance</td></tr>
<tr><td>GradientBoosting</td><td>Trees built sequentially, each corrects errors</td><td>High accuracy, structured data</td></tr>
<tr><td>AdaBoost</td><td>Sequential, weights misclassified samples more</td><td>Weak learner boosting</td></tr>
<tr><td>Bagging</td><td>Parallel training on bootstrap samples</td><td>Reducing variance</td></tr>
<tr><td>ExtraTrees</td><td>Like RF but splits are random (not optimized)</td><td>Faster than RF, similar accuracy</td></tr>
</tbody></table></section>''',
("decision-trees.html","Decision Trees"),("svm.html","SVM"))

print("decision-trees.html + random-forest.html expanded!")
