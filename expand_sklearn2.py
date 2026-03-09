import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# MODEL EVALUATION: train_test_split, cross_val, GridSearchCV
make_page("ml/model-evaluation.html","Model Evaluation &amp; Selection","Machine Learning","&#x1F916;","intermediate","ML &rarr; Model Evaluation",
"sklearn.model_selection provides tools for splitting data, cross-validation, and hyperparameter tuning. Covers train_test_split, cross_val_score, KFold, StratifiedKFold, LeaveOneOut, GridSearchCV, and RandomizedSearchCV.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron, sklearn docs",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">train_test_split</a></li>
<li><a href="#s2">Cross-Validation</a></li>
<li><a href="#s3">KFold &amp; StratifiedKFold</a></li>
<li><a href="#s4">GridSearchCV</a></li>
<li><a href="#s5">RandomizedSearchCV</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; train_test_split</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_iris
<span class="kw">import</span> numpy <span class="kw">as</span> np

X, y = load_iris(return_X_y=<span class="kw">True</span>)
<span class="bi">print</span>(<span class="st">f"Full dataset: {X.shape}"</span>)     <span class="cm"># (150, 4)</span>

<span class="cm"># Basic 80/20 split</span>
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=<span class="nm">0.2</span>, random_state=<span class="nm">42</span>
)
<span class="bi">print</span>(<span class="st">f"Train: {X_train.shape}, Test: {X_test.shape}"</span>)

<span class="cm"># Stratified split (preserves class proportions)</span>
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=<span class="nm">0.2</span>, random_state=<span class="nm">42</span>, stratify=y
)
<span class="bi">print</span>(<span class="st">f"Train class counts: {np.bincount(y_train)}"</span>)
<span class="bi">print</span>(<span class="st">f"Test  class counts: {np.bincount(y_test)}"</span>)

<span class="cm"># Different split ratios</span>
<span class="cm"># test_size=0.3   &rarr; 70/30 split</span>
<span class="cm"># test_size=0.1   &rarr; 90/10 split</span>
<span class="cm"># test_size=30    &rarr; 30 samples in test set</span>
<span class="cm"># train_size=0.7  &rarr; same as test_size=0.3</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Full: (150, 4)<br>Train: (120, 4), Test: (30, 4)<br>Train counts: [40 40 40] &mdash; perfectly balanced!</div></div>
<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>Always use <code>stratify=y</code> for classification!</strong><p>Without stratification, classes may be unevenly distributed between train and test sets, leading to misleading accuracy scores.</p></div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Cross-Validation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> cross_val_score, cross_validate
<span class="kw">from</span> sklearn.tree <span class="kw">import</span> DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=<span class="nm">42</span>)

<span class="cm"># cross_val_score &mdash; simple K-fold CV</span>
scores = cross_val_score(model, X, y, cv=<span class="nm">5</span>, scoring=<span class="st">"accuracy"</span>)
<span class="bi">print</span>(<span class="st">f"Fold scores: {scores.round(3)}"</span>)
<span class="bi">print</span>(<span class="st">f"Mean &plusmn; Std: {scores.mean():.3f} &plusmn; {scores.std():.3f}"</span>)

<span class="cm"># cross_validate &mdash; multiple metrics + timing</span>
result = cross_validate(
    model, X, y, cv=<span class="nm">5</span>,
    scoring=[<span class="st">"accuracy"</span>, <span class="st">"f1_macro"</span>],
    return_train_score=<span class="kw">True</span>
)
<span class="bi">print</span>(<span class="st">f"Test accuracy:  {result['test_accuracy'].mean():.3f}"</span>)
<span class="bi">print</span>(<span class="st">f"Train accuracy: {result['train_accuracy'].mean():.3f}"</span>)
<span class="bi">print</span>(<span class="st">f"Test F1 macro:  {result['test_f1_macro'].mean():.3f}"</span>)
<span class="bi">print</span>(<span class="st">f"Fit time:       {result['fit_time'].mean():.4f}s"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Fold scores: [0.967 0.967 0.900 0.933 1.0]<br>Mean: 0.953 ± 0.033</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; KFold &amp; StratifiedKFold</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> (
    KFold, StratifiedKFold, LeaveOneOut, ShuffleSplit
)

<span class="cm"># KFold &mdash; standard K-fold</span>
kf = KFold(n_splits=<span class="nm">5</span>, shuffle=<span class="kw">True</span>, random_state=<span class="nm">42</span>)
<span class="kw">for</span> fold, (train_idx, val_idx) <span class="kw">in</span> <span class="bi">enumerate</span>(kf.split(X)):
    <span class="bi">print</span>(<span class="st">f"Fold {fold}: train={len(train_idx)}, val={len(val_idx)}"</span>)

<span class="cm"># StratifiedKFold &mdash; preserves class ratios in each fold</span>
skf = StratifiedKFold(n_splits=<span class="nm">5</span>, shuffle=<span class="kw">True</span>, random_state=<span class="nm">42</span>)
scores = cross_val_score(model, X, y, cv=skf)
<span class="bi">print</span>(<span class="st">f"StratifiedKFold: {scores.mean():.3f}"</span>)

<span class="cm"># LeaveOneOut &mdash; N folds (one sample as test each time)</span>
loo = LeaveOneOut()
scores = cross_val_score(model, X, y, cv=loo)
<span class="bi">print</span>(<span class="st">f"LOOCV: {scores.mean():.3f} ({len(scores)} folds)"</span>)

<span class="cm"># ShuffleSplit &mdash; random splits (not exhaustive)</span>
ss = ShuffleSplit(n_splits=<span class="nm">10</span>, test_size=<span class="nm">0.2</span>, random_state=<span class="nm">42</span>)
scores = cross_val_score(model, X, y, cv=ss)
<span class="bi">print</span>(<span class="st">f"ShuffleSplit: {scores.mean():.3f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Fold 0: train=120, val=30<br>StratifiedKFold: 0.953<br>LOOCV: 0.953 (150 folds)</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; GridSearchCV</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> GridSearchCV
<span class="kw">from</span> sklearn.svm <span class="kw">import</span> SVC

<span class="cm"># Define parameter grid</span>
param_grid = {
    <span class="st">"C"</span>: [<span class="nm">0.1</span>, <span class="nm">1</span>, <span class="nm">10</span>, <span class="nm">100</span>],
    <span class="st">"kernel"</span>: [<span class="st">"linear"</span>, <span class="st">"rbf"</span>, <span class="st">"poly"</span>],
    <span class="st">"gamma"</span>: [<span class="st">"scale"</span>, <span class="st">"auto"</span>]
}

<span class="cm"># GridSearchCV tests ALL combinations</span>
grid = GridSearchCV(
    SVC(), param_grid,
    cv=<span class="nm">5</span>, scoring=<span class="st">"accuracy"</span>,
    verbose=<span class="nm">0</span>, refit=<span class="kw">True</span>  <span class="cm"># refit on full train with best params</span>
)
grid.fit(X_train, y_train)

<span class="bi">print</span>(<span class="st">f"Best params: {grid.best_params_}"</span>)
<span class="bi">print</span>(<span class="st">f"Best CV score: {grid.best_score_:.3f}"</span>)
<span class="bi">print</span>(<span class="st">f"Test score: {grid.score(X_test, y_test):.3f}"</span>)
<span class="bi">print</span>(<span class="st">f"Best estimator: {grid.best_estimator_}"</span>)

<span class="cm"># Total combinations tested: 4 * 3 * 2 = 24</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Best params: {'C': 1, 'gamma': 'scale', 'kernel': 'rbf'}<br>Best CV score: 0.975<br>Test score: 0.967</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; RandomizedSearchCV</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> RandomizedSearchCV
<span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> RandomForestClassifier
<span class="kw">from</span> scipy.stats <span class="kw">import</span> randint, uniform

<span class="cm"># Define distributions (not fixed values)</span>
param_dist = {
    <span class="st">"n_estimators"</span>: randint(<span class="nm">50</span>, <span class="nm">500</span>),
    <span class="st">"max_depth"</span>: [<span class="nm">3</span>, <span class="nm">5</span>, <span class="nm">10</span>, <span class="nm">20</span>, <span class="kw">None</span>],
    <span class="st">"min_samples_split"</span>: randint(<span class="nm">2</span>, <span class="nm">20</span>),
    <span class="st">"min_samples_leaf"</span>: randint(<span class="nm">1</span>, <span class="nm">10</span>),
    <span class="st">"max_features"</span>: [<span class="st">"sqrt"</span>, <span class="st">"log2"</span>, <span class="kw">None</span>]
}

<span class="cm"># RandomizedSearch samples n_iter random combinations</span>
random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=<span class="nm">42</span>),
    param_dist, n_iter=<span class="nm">50</span>,
    cv=<span class="nm">5</span>, scoring=<span class="st">"accuracy"</span>,
    random_state=<span class="nm">42</span>, n_jobs=-<span class="nm">1</span>
)
random_search.fit(X_train, y_train)

<span class="bi">print</span>(<span class="st">f"Best params: {random_search.best_params_}"</span>)
<span class="bi">print</span>(<span class="st">f"Best score: {random_search.best_score_:.3f}"</span>)
<span class="bi">print</span>(<span class="st">f"Test score: {random_search.score(X_test, y_test):.3f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Best params: {'max_depth': 10, 'n_estimators': 284, ...}<br>Best score: 0.967<br>Test score: 0.967</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Grid vs Random Search</strong>
<ul>
<li><strong>GridSearchCV</strong>: Tests every combination. Use when parameter space is small (&lt;100 combos).</li>
<li><strong>RandomizedSearchCV</strong>: Samples random combos. Faster for large spaces, often finds near-optimal configs.</li>
</ul></div></div></section>''',
("intro-ml.html","Intro to ML"),("linear-regression.html","Linear Regression"))

# PREPROCESSING
make_page("data/preprocessing.html","Preprocessing &amp; Encoding","Data Analysis","&#x1F4CA;","intermediate","Data &rarr; Preprocessing",
"sklearn.preprocessing provides scalers (StandardScaler, MinMaxScaler, RobustScaler), encoders (LabelEncoder, OneHotEncoder, OrdinalEncoder), and transformers (PolynomialFeatures, PowerTransformer). Also covers sklearn.impute for missing values (SimpleImputer, KNNImputer).",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Feature Scaling</a></li>
<li><a href="#s2">Encoding Categorical Variables</a></li>
<li><a href="#s3">Data Transformation</a></li>
<li><a href="#s4">Handling Missing Values (Imputers)</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Feature Scaling</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> (
    StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler
)
<span class="kw">import</span> numpy <span class="kw">as</span> np

X = np.array([[<span class="nm">1</span>, <span class="nm">1000</span>], [<span class="nm">2</span>, <span class="nm">2000</span>], [<span class="nm">3</span>, <span class="nm">3000</span>], [<span class="nm">100</span>, <span class="nm">50000</span>]])

<span class="cm"># StandardScaler: mean=0, std=1 (Z-score normalization)</span>
ss = StandardScaler()
<span class="bi">print</span>(<span class="st">"StandardScaler:"</span>)
<span class="bi">print</span>(ss.fit_transform(X).round(<span class="nm">3</span>))
<span class="bi">print</span>(<span class="st">f"Mean: {ss.mean_}, Scale: {ss.scale_.round(2)}"</span>)

<span class="cm"># MinMaxScaler: scales to [0, 1]</span>
mms = MinMaxScaler()
<span class="bi">print</span>(<span class="st">"\\nMinMaxScaler (0 to 1):"</span>)
<span class="bi">print</span>(mms.fit_transform(X).round(<span class="nm">3</span>))

<span class="cm"># MinMaxScaler with custom range</span>
mms2 = MinMaxScaler(feature_range=(-<span class="nm">1</span>, <span class="nm">1</span>))
<span class="bi">print</span>(<span class="st">"\\nMinMaxScaler (-1 to 1):"</span>)
<span class="bi">print</span>(mms2.fit_transform(X).round(<span class="nm">3</span>))

<span class="cm"># RobustScaler: robust to OUTLIERS (uses median &amp; IQR)</span>
rs = RobustScaler()
<span class="bi">print</span>(<span class="st">"\\nRobustScaler:"</span>)
<span class="bi">print</span>(rs.fit_transform(X).round(<span class="nm">3</span>))

<span class="cm"># MaxAbsScaler: scales by max absolute value [-1, 1]</span>
mas = MaxAbsScaler()
<span class="bi">print</span>(<span class="st">"\\nMaxAbsScaler:"</span>)
<span class="bi">print</span>(mas.fit_transform(X).round(<span class="nm">3</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>StandardScaler: [[-0.63 -0.66] [-0.60 -0.61] [-0.58 -0.56] [1.81 1.83]]<br>MinMaxScaler: [[0. 0.] [0.01 0.02] [0.02 0.04] [1. 1.]]<br>RobustScaler uses median/IQR, less affected by outlier (100, 50000)</div></div>

<table class="data-table"><thead><tr><th>Scaler</th><th>Formula</th><th>Range</th><th>Best For</th></tr></thead><tbody>
<tr><td>StandardScaler</td><td>(x &minus; &mu;) / &sigma;</td><td>Unbounded</td><td>Normal-like data</td></tr>
<tr><td>MinMaxScaler</td><td>(x &minus; min) / (max &minus; min)</td><td>[0, 1]</td><td>Bounded data, neural nets</td></tr>
<tr><td>RobustScaler</td><td>(x &minus; median) / IQR</td><td>Unbounded</td><td>Outlier-heavy data</td></tr>
<tr><td>MaxAbsScaler</td><td>x / max(|x|)</td><td>[-1, 1]</td><td>Sparse data</td></tr>
</tbody></table>

<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>Critical Rule</strong><p><code>fit_transform()</code> on training data only. <code>transform()</code> on test data. Never fit on test data &mdash; this causes data leakage!</p></div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Encoding Categorical Variables</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> (
    LabelEncoder, OneHotEncoder, OrdinalEncoder
)

<span class="cm"># &#x1F3F7;&#xFE0F; LabelEncoder &mdash; converts labels to integers</span>
le = LabelEncoder()
labels = [<span class="st">"cat"</span>, <span class="st">"dog"</span>, <span class="st">"bird"</span>, <span class="st">"cat"</span>, <span class="st">"bird"</span>]
encoded = le.fit_transform(labels)
<span class="bi">print</span>(<span class="st">f"Encoded: {encoded}"</span>)             <span class="cm"># [1 2 0 1 0]</span>
<span class="bi">print</span>(<span class="st">f"Classes: {le.classes_}"</span>)           <span class="cm"># ['bird' 'cat' 'dog']</span>
<span class="bi">print</span>(<span class="st">f"Decoded: {le.inverse_transform(encoded)}"</span>)

<span class="cm"># &#x1F525; OneHotEncoder &mdash; creates binary columns</span>
ohe = OneHotEncoder(sparse_output=<span class="kw">False</span>)
colors = np.array([[<span class="st">"red"</span>],[<span class="st">"blue"</span>],[<span class="st">"green"</span>],[<span class="st">"red"</span>]])
encoded = ohe.fit_transform(colors)
<span class="bi">print</span>(<span class="st">f"One-hot:\\n{encoded}"</span>)
<span class="bi">print</span>(<span class="st">f"Categories: {ohe.categories_}"</span>)
<span class="cm"># [[0. 0. 1.]    red</span>
<span class="cm">#  [1. 0. 0.]    blue</span>
<span class="cm">#  [0. 1. 0.]    green</span>
<span class="cm">#  [0. 0. 1.]]   red</span>

<span class="cm"># Handle unknown categories at prediction time</span>
ohe = OneHotEncoder(sparse_output=<span class="kw">False</span>, handle_unknown=<span class="st">"ignore"</span>)
ohe.fit(colors)
<span class="bi">print</span>(ohe.transform([[<span class="st">"yellow"</span>]]))  <span class="cm"># [0. 0. 0.] all zeros</span>

<span class="cm"># &#x1F522; OrdinalEncoder &mdash; ordered categories</span>
oe = OrdinalEncoder(categories=[[<span class="st">"low"</span>, <span class="st">"medium"</span>, <span class="st">"high"</span>]])
sizes = np.array([[<span class="st">"high"</span>],[<span class="st">"low"</span>],[<span class="st">"medium"</span>],[<span class="st">"high"</span>]])
<span class="bi">print</span>(oe.fit_transform(sizes))
<span class="cm"># [[2.] [0.] [1.] [2.]]  low=0, medium=1, high=2</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>LabelEncoder: [1 2 0 1 0] &middot; classes: ['bird','cat','dog']<br>OneHot: [[0. 0. 1.] [1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]<br>Ordinal: [[2.] [0.] [1.] [2.]]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Data Transformation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> (
    PolynomialFeatures, Binarizer, Normalizer,
    PowerTransformer, QuantileTransformer
)

<span class="cm"># PolynomialFeatures: create polynomial &amp; interaction features</span>
X = np.array([[<span class="nm">2</span>, <span class="nm">3</span>], [<span class="nm">4</span>, <span class="nm">5</span>]])
poly = PolynomialFeatures(degree=<span class="nm">2</span>, include_bias=<span class="kw">False</span>)
<span class="bi">print</span>(poly.fit_transform(X))
<span class="cm"># [[ 2  3  4  6  9]   &rarr; [x1, x2, x1&sup2;, x1*x2, x2&sup2;]</span>
<span class="cm">#  [ 4  5 16 20 25]]</span>
<span class="bi">print</span>(poly.get_feature_names_out())

<span class="cm"># Binarizer: threshold &rarr; 0/1</span>
bz = Binarizer(threshold=<span class="nm">3.0</span>)
<span class="bi">print</span>(bz.transform(np.array([[<span class="nm">1</span>,<span class="nm">4</span>,<span class="nm">3</span>,<span class="nm">5</span>,<span class="nm">2</span>]])))
<span class="cm"># [[0 1 0 1 0]]</span>

<span class="cm"># Normalizer: scale each ROW to unit norm</span>
nm = Normalizer(norm=<span class="st">"l2"</span>)
X = np.array([[<span class="nm">3</span>, <span class="nm">4</span>], [<span class="nm">1</span>, <span class="nm">2</span>]])
<span class="bi">print</span>(nm.transform(X).round(<span class="nm">3</span>))
<span class="cm"># [[0.6 0.8]    &radic;(3&sup2;+4&sup2;)=5 &rarr; [3/5, 4/5]</span>
<span class="cm">#  [0.447 0.894]]</span>

<span class="cm"># PowerTransformer: make data ~normal</span>
pt = PowerTransformer(method=<span class="st">"yeo-johnson"</span>)
skewed = np.array([[<span class="nm">1</span>],[<span class="nm">2</span>],[<span class="nm">3</span>],[<span class="nm">50</span>],[<span class="nm">100</span>]])
<span class="bi">print</span>(pt.fit_transform(skewed).round(<span class="nm">3</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Polynomial: [[2 3 4 6 9] [4 5 16 20 25]]<br>Binarizer(3): [0 1 0 1 0]<br>Normalizer: [[0.6 0.8] [0.447 0.894]]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Handling Missing Values (Imputers)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.impute <span class="kw">import</span> SimpleImputer, KNNImputer

X = np.array([
    [<span class="nm">1</span>, <span class="nm">2</span>, np.nan],
    [<span class="nm">3</span>, np.nan, <span class="nm">6</span>],
    [<span class="nm">7</span>, <span class="nm">8</span>, <span class="nm">9</span>],
    [np.nan, <span class="nm">5</span>, <span class="nm">3</span>]
])

<span class="cm"># SimpleImputer: fill with mean (default)</span>
imp_mean = SimpleImputer(strategy=<span class="st">"mean"</span>)
<span class="bi">print</span>(<span class="st">"Mean imputed:"</span>)
<span class="bi">print</span>(imp_mean.fit_transform(X))

<span class="cm"># Other strategies</span>
imp_median = SimpleImputer(strategy=<span class="st">"median"</span>)
imp_freq = SimpleImputer(strategy=<span class="st">"most_frequent"</span>)
imp_const = SimpleImputer(strategy=<span class="st">"constant"</span>, fill_value=<span class="nm">0</span>)

<span class="bi">print</span>(<span class="st">"\\nMedian imputed:"</span>)
<span class="bi">print</span>(imp_median.fit_transform(X))

<span class="bi">print</span>(<span class="st">"\\nConstant (0) imputed:"</span>)
<span class="bi">print</span>(imp_const.fit_transform(X))

<span class="cm"># KNNImputer: uses K-nearest neighbors to impute</span>
imp_knn = KNNImputer(n_neighbors=<span class="nm">2</span>)
<span class="bi">print</span>(<span class="st">"\\nKNN imputed:"</span>)
<span class="bi">print</span>(imp_knn.fit_transform(X))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Mean imputed:<br>[[ 1.  2.  6.] [ 3.  5.  6.] [ 7.  8.  9.] [3.67 5.  3.]]<br>KNN uses neighbor similarity for smarter imputation</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Which imputer to use?</strong>
<ul>
<li><code>SimpleImputer(mean)</code> &mdash; numeric data, no outliers</li>
<li><code>SimpleImputer(median)</code> &mdash; numeric data WITH outliers</li>
<li><code>SimpleImputer(most_frequent)</code> &mdash; categorical data</li>
<li><code>KNNImputer</code> &mdash; preserves relationships between features</li>
</ul></div></div></section>''',
("../ml/model-evaluation.html","Model Evaluation"),("feature-engineering.html","Feature Engineering"))

print("model-evaluation.html + preprocessing.html expanded!")
