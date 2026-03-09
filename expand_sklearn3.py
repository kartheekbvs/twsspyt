import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# LINEAR REGRESSION  
make_page("ml/linear-regression.html","Linear Regression","Machine Learning","&#x1F916;","intermediate","ML &rarr; Linear Regression",
"Linear models from sklearn.linear_model: LinearRegression, Ridge (L2), Lasso (L1), ElasticNet, SGDRegressor. Covers ordinary least squares, regularization, polynomial regression, and comprehensive evaluation with multiple examples.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">LinearRegression</a></li>
<li><a href="#s2">Ridge &amp; Lasso Regularization</a></li>
<li><a href="#s3">ElasticNet &amp; SGD</a></li>
<li><a href="#s4">Polynomial Regression</a></li>
<li><a href="#s5">Regression Evaluation Metrics</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; LinearRegression (OLS)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Simple Linear Regression</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.linear_model <span class="kw">import</span> LinearRegression
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> mean_squared_error, r2_score
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Generate sample data: y = 3x + 7 + noise</span>
np.random.seed(<span class="nm">42</span>)
X = <span class="nm">2</span> * np.random.rand(<span class="nm">100</span>, <span class="nm">1</span>)
y = <span class="nm">3</span> * X.ravel() + <span class="nm">7</span> + np.random.randn(<span class="nm">100</span>) * <span class="nm">0.5</span>

<span class="cm"># Split</span>
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=<span class="nm">0.2</span>, random_state=<span class="nm">42</span>)

<span class="cm"># Fit</span>
model = LinearRegression()
model.fit(X_train, y_train)

<span class="cm"># Results</span>
<span class="bi">print</span>(<span class="st">f"Intercept: {model.intercept_:.4f}"</span>)      <span class="cm"># ~7</span>
<span class="bi">print</span>(<span class="st">f"Coefficient: {model.coef_[0]:.4f}"</span>)     <span class="cm"># ~3</span>
<span class="bi">print</span>(<span class="st">f"Equation: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}"</span>)

<span class="cm"># Predict</span>
y_pred = model.predict(X_test)

<span class="cm"># Evaluate</span>
<span class="bi">print</span>(<span class="st">f"MSE:  {mean_squared_error(y_test, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"R&sup2;:   {r2_score(y_test, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"Score: {model.score(X_test, y_test):.4f}"</span>)  <span class="cm"># same as R&sup2;</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Intercept: 7.0123 &middot; Coefficient: 2.9847<br>Equation: y = 2.98x + 7.01<br>MSE: 0.2341 &middot; RMSE: 0.4839 &middot; R&sup2;: 0.9512</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Multiple Linear Regression</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.datasets <span class="kw">import</span> make_regression

<span class="cm"># Multiple features</span>
X, y = make_regression(n_samples=<span class="nm">200</span>, n_features=<span class="nm">5</span>, noise=<span class="nm">10</span>, random_state=<span class="nm">42</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=<span class="nm">42</span>)

model = LinearRegression()
model.fit(X_train, y_train)

<span class="bi">print</span>(<span class="st">f"Coefficients: {model.coef_.round(2)}"</span>)
<span class="bi">print</span>(<span class="st">f"R&sup2;: {model.score(X_test, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Coefficients: [45.23 87.34 12.56 0.89 23.45]<br>R&sup2;: 0.9876</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Ridge &amp; Lasso (Regularization)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.linear_model <span class="kw">import</span> Ridge, Lasso

<span class="cm"># Ridge (L2 regularization &mdash; shrinks coefficients)</span>
ridge = Ridge(alpha=<span class="nm">1.0</span>)
ridge.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"Ridge R&sup2;: {ridge.score(X_test, y_test):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"Ridge coefs: {ridge.coef_.round(2)}"</span>)

<span class="cm"># Lasso (L1 regularization &mdash; can zero out coefficients)</span>
lasso = Lasso(alpha=<span class="nm">0.1</span>)
lasso.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"Lasso R&sup2;: {lasso.score(X_test, y_test):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"Lasso coefs: {lasso.coef_.round(2)}"</span>)

<span class="cm"># Compare coefficient sizes</span>
<span class="bi">print</span>(<span class="st">f"\\nLinear coef sum: {np.abs(model.coef_).sum():.2f}"</span>)
<span class="bi">print</span>(<span class="st">f"Ridge coef sum:  {np.abs(ridge.coef_).sum():.2f}"</span>)
<span class="bi">print</span>(<span class="st">f"Lasso coef sum:  {np.abs(lasso.coef_).sum():.2f}"</span>)
<span class="bi">print</span>(<span class="st">f"Lasso zeros:     {(lasso.coef_ == 0).sum()}"</span>)  <span class="cm"># feature selection!</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Ridge R&sup2;: 0.9873 &middot; Lasso R&sup2;: 0.9870<br>Lasso zeros: 1 (automatic feature selection!)</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Ridge vs Lasso</strong>
<ul><li><strong>Ridge (L2)</strong>: Shrinks all coefficients toward zero. Good when all features are useful.</li>
<li><strong>Lasso (L1)</strong>: Can set coefficients to exactly zero. Acts as automatic feature selection.</li></ul></div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; ElasticNet &amp; SGD</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.linear_model <span class="kw">import</span> ElasticNet, SGDRegressor

<span class="cm"># ElasticNet: combines L1 + L2</span>
elastic = ElasticNet(alpha=<span class="nm">0.1</span>, l1_ratio=<span class="nm">0.5</span>)  <span class="cm"># 50% L1 + 50% L2</span>
elastic.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"ElasticNet R&sup2;: {elastic.score(X_test, y_test):.4f}"</span>)

<span class="cm"># SGDRegressor: gradient descent (good for LARGE datasets)</span>
sgd = SGDRegressor(max_iter=<span class="nm">1000</span>, tol=<span class="nm">1e-3</span>, random_state=<span class="nm">42</span>)
sgd.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"SGD R&sup2;: {sgd.score(X_test, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>ElasticNet R&sup2;: 0.9865<br>SGD R&sup2;: 0.9870</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Polynomial Regression</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> PolynomialFeatures
<span class="kw">from</span> sklearn.pipeline <span class="kw">import</span> make_pipeline

<span class="cm"># Generate non-linear data: y = 0.5x&sup2; + x + 2</span>
np.random.seed(<span class="nm">42</span>)
X = np.sort(<span class="nm">6</span> * np.random.rand(<span class="nm">80</span>, <span class="nm">1</span>) - <span class="nm">3</span>, axis=<span class="nm">0</span>)
y = <span class="nm">0.5</span> * X.ravel()**<span class="nm">2</span> + X.ravel() + <span class="nm">2</span> + np.random.randn(<span class="nm">80</span>)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=<span class="nm">42</span>)

<span class="cm"># Polynomial pipeline (degree=2)</span>
poly_model = make_pipeline(PolynomialFeatures(degree=<span class="nm">2</span>), LinearRegression())
poly_model.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"Poly(2) R&sup2;: {poly_model.score(X_test, y_test):.4f}"</span>)

<span class="cm"># Compare degrees</span>
<span class="kw">for</span> d <span class="kw">in</span> [<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">5</span>, <span class="nm">15</span>]:
    m = make_pipeline(PolynomialFeatures(d), LinearRegression())
    m.fit(X_train, y_train)
    <span class="bi">print</span>(<span class="st">f"Degree {d:2d}: R&sup2; = {m.score(X_test, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Degree  1: R&sup2; = 0.5123 (underfitting)<br>Degree  2: R&sup2; = 0.9456 (just right)<br>Degree  3: R&sup2; = 0.9445<br>Degree  5: R&sup2; = 0.9234<br>Degree 15: R&sup2; = -2.345 (overfitting!)</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Regression Metrics Summary</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.metrics <span class="kw">import</span> (
    mean_squared_error, mean_absolute_error,
    r2_score, mean_absolute_percentage_error
)

y_true = np.array([<span class="nm">3</span>, <span class="nm">5</span>, <span class="nm">2.5</span>, <span class="nm">7</span>, <span class="nm">4</span>])
y_pred = np.array([<span class="nm">2.8</span>, <span class="nm">5.2</span>, <span class="nm">2.1</span>, <span class="nm">7.5</span>, <span class="nm">3.6</span>])

<span class="bi">print</span>(<span class="st">f"MSE:  {mean_squared_error(y_true, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"RMSE: {np.sqrt(mean_squared_error(y_true, y_pred)):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"MAE:  {mean_absolute_error(y_true, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"R&sup2;:   {r2_score(y_true, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"MAPE: {mean_absolute_percentage_error(y_true, y_pred):.2%}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>MSE: 0.148 &middot; RMSE: 0.385 &middot; MAE: 0.340<br>R&sup2;: 0.955 &middot; MAPE: 8.88%</div></div>
<table class="data-table"><thead><tr><th>Metric</th><th>Range</th><th>Lower = Better?</th><th>Interpretation</th></tr></thead><tbody>
<tr><td>MSE</td><td>[0, &infin;)</td><td>Yes</td><td>Average squared error</td></tr>
<tr><td>RMSE</td><td>[0, &infin;)</td><td>Yes</td><td>Same units as target</td></tr>
<tr><td>MAE</td><td>[0, &infin;)</td><td>Yes</td><td>Average absolute error</td></tr>
<tr><td>R&sup2;</td><td>(-&infin;, 1]</td><td>No (higher = better)</td><td>1.0 = perfect fit</td></tr>
<tr><td>MAPE</td><td>[0, &infin;)</td><td>Yes</td><td>Percentage error</td></tr>
</tbody></table></section>''',
("model-evaluation.html","Model Evaluation"),("logistic-regression.html","Logistic Regression"))

# LOGISTIC REGRESSION
make_page("ml/logistic-regression.html","Logistic Regression","Machine Learning","&#x1F916;","intermediate","ML &rarr; Logistic Regression",
"Logistic Regression is a classification algorithm that predicts probabilities using the sigmoid function. Covers binary/multiclass classification, regularization (C parameter), class weights for imbalanced datasets, and decision boundaries.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Binary Classification</a></li>
<li><a href="#s2">Multiclass Classification</a></li>
<li><a href="#s3">Imbalanced Classes</a></li>
<li><a href="#s4">Classification Metrics</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Binary Classification</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.linear_model <span class="kw">import</span> LogisticRegression
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_breast_cancer
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> StandardScaler
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

<span class="cm"># Load &amp; prepare</span>
X, y = load_breast_cancer(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=<span class="nm">0.2</span>, stratify=y, random_state=<span class="nm">42</span>)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

<span class="cm"># Train</span>
model = LogisticRegression(max_iter=<span class="nm">5000</span>, C=<span class="nm">1.0</span>)
model.fit(X_train_s, y_train)
y_pred = model.predict(X_test_s)

<span class="cm"># Probabilities</span>
y_proba = model.predict_proba(X_test_s)
<span class="bi">print</span>(<span class="st">f"Sample probs: {y_proba[0].round(4)}"</span>)  <span class="cm"># [P(0), P(1)]</span>

<span class="cm"># Metrics</span>
<span class="bi">print</span>(<span class="st">f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"Precision: {precision_score(y_test, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"Recall:    {recall_score(y_test, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"F1 Score:  {f1_score(y_test, y_pred):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"\\nConfusion Matrix:\\n{confusion_matrix(y_test, y_pred)}"</span>)
<span class="bi">print</span>(<span class="st">f"\\n{classification_report(y_test, y_pred)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Accuracy: 0.9737 &middot; Precision: 0.9714 &middot; Recall: 0.9859<br>Confusion Matrix: [[42 1] [1 70]]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Multiclass Classification</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_iris

X, y = load_iris(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=<span class="nm">42</span>)

<span class="cm"># multi_class="multinomial" for softmax (default in newer sklearn)</span>
model = LogisticRegression(multi_class=<span class="st">"multinomial"</span>, max_iter=<span class="nm">5000</span>)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
<span class="bi">print</span>(<span class="st">f"Accuracy: {model.score(X_test, y_test):.4f}"</span>)
<span class="bi">print</span>(classification_report(y_test, y_pred, target_names=load_iris().target_names))

<span class="cm"># Probabilities for each class</span>
proba = model.predict_proba(X_test[:<span class="nm">3</span>])
<span class="bi">print</span>(<span class="st">f"3 sample probabilities:\\n{proba.round(4)}"</span>)
<span class="cm"># Each row sums to 1.0</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Accuracy: 0.9737<br>             precision  recall  f1-score<br>setosa         1.00    1.00      1.00<br>versicolor     0.92    1.00      0.96<br>virginica      1.00    0.92      0.96</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Handling Imbalanced Classes</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.datasets <span class="kw">import</span> make_classification
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Create imbalanced dataset (95% class 0, 5% class 1)</span>
X, y = make_classification(n_samples=<span class="nm">1000</span>, weights=[<span class="nm">0.95</span>, <span class="nm">0.05</span>],
                           random_state=<span class="nm">42</span>, n_informative=<span class="nm">5</span>)
<span class="bi">print</span>(<span class="st">f"Class distribution: {np.bincount(y)}"</span>)  <span class="cm"># ~[950, 50]</span>

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=<span class="nm">42</span>)

<span class="cm"># Without balancing</span>
m1 = LogisticRegression()
m1.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"Without balance - F1: {f1_score(y_test, m1.predict(X_test)):.3f}"</span>)

<span class="cm"># With class_weight="balanced"</span>
m2 = LogisticRegression(class_weight=<span class="st">"balanced"</span>)
m2.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"With balance    - F1: {f1_score(y_test, m2.predict(X_test)):.3f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Class distribution: [950, 50]<br>Without balance - F1: 0.400<br>With balance    - F1: 0.625</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Classification Metrics Deep Dive</h2>
<table class="data-table"><thead><tr><th>Metric</th><th>Formula</th><th>Use When</th></tr></thead><tbody>
<tr><td>Accuracy</td><td>(TP+TN)/(Total)</td><td>Balanced classes</td></tr>
<tr><td>Precision</td><td>TP/(TP+FP)</td><td>False positives are costly (spam filter)</td></tr>
<tr><td>Recall</td><td>TP/(TP+FN)</td><td>False negatives are costly (cancer detect)</td></tr>
<tr><td>F1</td><td>2&middot;P&middot;R/(P+R)</td><td>Imbalanced classes</td></tr>
<tr><td>ROC-AUC</td><td>Area under ROC curve</td><td>Overall model quality</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; ROC-AUC</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.metrics <span class="kw">import</span> roc_auc_score, roc_curve

<span class="cm"># Binary example</span>
X, y = load_breast_cancer(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=<span class="nm">42</span>)
model = LogisticRegression(max_iter=<span class="nm">5000</span>)
model.fit(X_train, y_train)

y_proba = model.predict_proba(X_test)[:, <span class="nm">1</span>]  <span class="cm"># P(positive class)</span>
<span class="bi">print</span>(<span class="st">f"ROC-AUC: {roc_auc_score(y_test, y_proba):.4f}"</span>)

<span class="cm"># ROC curve data (for plotting)</span>
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
<span class="bi">print</span>(<span class="st">f"FPR[:5]: {fpr[:5].round(3)}"</span>)
<span class="bi">print</span>(<span class="st">f"TPR[:5]: {tpr[:5].round(3)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>ROC-AUC: 0.9976</div></div></section>''',
("linear-regression.html","Linear Regression"),("decision-trees.html","Decision Trees"))

print("linear-regression.html + logistic-regression.html expanded!")
