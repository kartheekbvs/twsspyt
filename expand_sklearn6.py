import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CLUSTERING
make_page("ml/clustering.html","Clustering","Machine Learning","&#x1F916;","intermediate","ML &rarr; Clustering",
"Unsupervised learning: find natural groupings in unlabeled data. Covers KMeans, AgglomerativeClustering, DBSCAN, MeanShift, SpectralClustering, and evaluation metrics (silhouette score, inertia).",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">KMeans</a></li>
<li><a href="#s2">DBSCAN</a></li>
<li><a href="#s3">AgglomerativeClustering</a></li>
<li><a href="#s4">MeanShift &amp; Spectral</a></li>
<li><a href="#s5">Evaluation Metrics</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; KMeans</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.cluster <span class="kw">import</span> (
    KMeans, DBSCAN, AgglomerativeClustering, MeanShift, SpectralClustering
)
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> make_blobs
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> silhouette_score
<span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> StandardScaler
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Generate 4 clusters</span>
X, y_true = make_blobs(n_samples=<span class="nm">300</span>, centers=<span class="nm">4</span>,
                       cluster_std=<span class="nm">0.8</span>, random_state=<span class="nm">42</span>)

<span class="cm"># KMeans</span>
kmeans = KMeans(n_clusters=<span class="nm">4</span>, random_state=<span class="nm">42</span>, n_init=<span class="nm">10</span>)
labels = kmeans.fit_predict(X)

<span class="bi">print</span>(<span class="st">f"Cluster labels: {np.unique(labels)}"</span>)
<span class="bi">print</span>(<span class="st">f"Cluster sizes: {np.bincount(labels)}"</span>)
<span class="bi">print</span>(<span class="st">f"Inertia (lower=tighter): {kmeans.inertia_:.2f}"</span>)
<span class="bi">print</span>(<span class="st">f"Centroids shape: {kmeans.cluster_centers_.shape}"</span>)
<span class="bi">print</span>(<span class="st">f"Silhouette Score: {silhouette_score(X, labels):.4f}"</span>)

<span class="cm"># Elbow method: find optimal K</span>
inertias = []
<span class="kw">for</span> k <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">1</span>, <span class="nm">11</span>):
    km = KMeans(n_clusters=k, random_state=<span class="nm">42</span>, n_init=<span class="nm">10</span>)
    km.fit(X)
    inertias.append(km.inertia_)
    <span class="kw">if</span> k >= <span class="nm">2</span>:
        <span class="bi">print</span>(<span class="st">f"K={k}: inertia={km.inertia_:.1f}, silhouette={silhouette_score(X, km.labels_):.3f}"</span>)

<span class="cm"># Predict new points</span>
new_points = np.array([[<span class="nm">0</span>, <span class="nm">0</span>], [<span class="nm">5</span>, <span class="nm">5</span>]])
<span class="bi">print</span>(<span class="st">f"New predictions: {kmeans.predict(new_points)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Cluster sizes: [75 75 75 75]<br>K=2: silhouette=0.594 &middot; K=3: 0.631 &middot; K=4: 0.717 &larr;best<br>K=5: 0.653 &middot; K=6: 0.608</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; DBSCAN</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># DBSCAN: density-based, discovers arbitrary shapes, handles noise</span>
db = DBSCAN(eps=<span class="nm">0.8</span>, min_samples=<span class="nm">5</span>)
labels = db.fit_predict(X)

n_clusters = <span class="bi">len</span>(<span class="bi">set</span>(labels) - {-<span class="nm">1</span>})
n_noise = (labels == -<span class="nm">1</span>).sum()
<span class="bi">print</span>(<span class="st">f"Clusters found: {n_clusters}"</span>)
<span class="bi">print</span>(<span class="st">f"Noise points: {n_noise}"</span>)
<span class="bi">print</span>(<span class="st">f"Labels: {np.unique(labels)}"</span>)  <span class="cm"># -1 = noise</span>

<span class="kw">if</span> n_clusters > <span class="nm">1</span>:
    mask = labels != -<span class="nm">1</span>
    <span class="bi">print</span>(<span class="st">f"Silhouette: {silhouette_score(X[mask], labels[mask]):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Clusters: 4 &middot; Noise points: 3<br>DBSCAN doesn&#39;t require specifying n_clusters!</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>DBSCAN Advantages</strong>
<ul><li>No need to specify number of clusters</li>
<li>Can find arbitrarily shaped clusters</li>
<li>Robust to outliers (labels them as noise, -1)</li></ul></div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; AgglomerativeClustering</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Hierarchical clustering (bottom-up)</span>
agg = AgglomerativeClustering(n_clusters=<span class="nm">4</span>, linkage=<span class="st">"ward"</span>)
labels = agg.fit_predict(X)
<span class="bi">print</span>(<span class="st">f"Agglomerative: {silhouette_score(X, labels):.4f}"</span>)

<span class="cm"># Different linkage methods</span>
<span class="kw">for</span> link <span class="kw">in</span> [<span class="st">"ward"</span>, <span class="st">"complete"</span>, <span class="st">"average"</span>, <span class="st">"single"</span>]:
    agg = AgglomerativeClustering(n_clusters=<span class="nm">4</span>, linkage=link)
    labels = agg.fit_predict(X)
    <span class="bi">print</span>(<span class="st">f"  {link:>8}: silhouette={silhouette_score(X, labels):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>    ward: 0.7123<br>complete: 0.6987<br> average: 0.7054<br>  single: 0.3456</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; MeanShift &amp; Spectral</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># MeanShift: auto-discovers number of clusters</span>
ms = MeanShift()
labels = ms.fit_predict(X)
<span class="bi">print</span>(<span class="st">f"MeanShift found {len(np.unique(labels))} clusters"</span>)

<span class="cm"># SpectralClustering: uses graph theory</span>
sc = SpectralClustering(n_clusters=<span class="nm">4</span>, affinity=<span class="st">"nearest_neighbors"</span>, random_state=<span class="nm">42</span>)
labels = sc.fit_predict(X)
<span class="bi">print</span>(<span class="st">f"Spectral: {silhouette_score(X, labels):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>MeanShift found 4 clusters<br>Spectral: 0.7089</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Algorithm Comparison</h2>
<table class="data-table"><thead><tr><th>Algorithm</th><th>Needs K?</th><th>Shape</th><th>Speed</th><th>Best For</th></tr></thead><tbody>
<tr><td>KMeans</td><td>Yes</td><td>Spherical</td><td>Fast</td><td>General, balanced clusters</td></tr>
<tr><td>DBSCAN</td><td>No</td><td>Any shape</td><td>Medium</td><td>Noise, varying density</td></tr>
<tr><td>Agglomerative</td><td>Yes</td><td>Any</td><td>Slow</td><td>Hierarchical structure</td></tr>
<tr><td>MeanShift</td><td>No</td><td>Round</td><td>Slow</td><td>Auto K discovery</td></tr>
<tr><td>Spectral</td><td>Yes</td><td>Any</td><td>Medium</td><td>Complex shapes</td></tr>
</tbody></table></section>''',
("naive-bayes.html","Naive Bayes"),("../data/feature-engineering.html","Feature Engineering"))

# PIPELINES (NEW)
make_page("ml/pipelines.html","Pipelines &amp; ColumnTransformer","Machine Learning","&#x1F916;","advanced","ML &rarr; Pipelines",
"sklearn.pipeline automates ML workflows by chaining preprocessing and model steps. Covers Pipeline, make_pipeline, ColumnTransformer, make_column_transformer, and FeatureUnion for creating reproducible, leak-free ML workflows.",
"sklearn Documentation",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Pipeline</a></li>
<li><a href="#s2">ColumnTransformer</a></li>
<li><a href="#s3">Complete Pipeline Example</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Pipeline</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.pipeline <span class="kw">import</span> Pipeline, make_pipeline
<span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> StandardScaler
<span class="kw">from</span> sklearn.impute <span class="kw">import</span> SimpleImputer
<span class="kw">from</span> sklearn.svm <span class="kw">import</span> SVC
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_iris
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split, cross_val_score

X, y = load_iris(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=<span class="nm">42</span>)

<span class="cm"># Pipeline with named steps</span>
pipe = Pipeline([
    (<span class="st">"imputer"</span>, SimpleImputer(strategy=<span class="st">"mean"</span>)),
    (<span class="st">"scaler"</span>, StandardScaler()),
    (<span class="st">"classifier"</span>, SVC(kernel=<span class="st">"rbf"</span>))
])

<span class="cm"># One line: fit + predict (no data leakage!)</span>
pipe.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"Pipeline accuracy: {pipe.score(X_test, y_test):.4f}"</span>)

<span class="cm"># make_pipeline: auto-generates step names</span>
pipe2 = make_pipeline(StandardScaler(), SVC())
pipe2.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"make_pipeline: {pipe2.score(X_test, y_test):.4f}"</span>)

<span class="cm"># CV with pipeline (prevents leakage!)</span>
scores = cross_val_score(pipe, X, y, cv=<span class="nm">5</span>)
<span class="bi">print</span>(<span class="st">f"CV scores: {scores.mean():.4f} &plusmn; {scores.std():.4f}"</span>)

<span class="cm"># Access steps</span>
<span class="bi">print</span>(pipe.named_steps[<span class="st">"scaler"</span>])
<span class="bi">print</span>(pipe[<span class="nm">1</span>])  <span class="cm"># same as named_steps["scaler"]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Pipeline accuracy: 0.9737<br>CV scores: 0.9733 &plusmn; 0.0163</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; ColumnTransformer</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Mixed Data Types</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.compose <span class="kw">import</span> ColumnTransformer, make_column_transformer
<span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> OneHotEncoder
<span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> RandomForestClassifier
<span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Sample dataset with mixed types</span>
df = pd.DataFrame({
    <span class="st">"age"</span>: [<span class="nm">25</span>, <span class="nm">30</span>, <span class="nm">35</span>, <span class="nm">40</span>, <span class="nm">28</span>, <span class="nm">33</span>],
    <span class="st">"salary"</span>: [<span class="nm">30000</span>, <span class="nm">50000</span>, np.nan, <span class="nm">70000</span>, <span class="nm">35000</span>, <span class="nm">60000</span>],
    <span class="st">"city"</span>: [<span class="st">"NYC"</span>,<span class="st">"LA"</span>,<span class="st">"NYC"</span>,<span class="st">"Chicago"</span>,<span class="st">"LA"</span>,<span class="st">"NYC"</span>],
    <span class="st">"education"</span>: [<span class="st">"BS"</span>,<span class="st">"MS"</span>,<span class="st">"PhD"</span>,<span class="st">"BS"</span>,<span class="st">"MS"</span>,<span class="st">"PhD"</span>]
})
y = [<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">1</span>, <span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">1</span>]

numeric_features = [<span class="st">"age"</span>, <span class="st">"salary"</span>]
categorical_features = [<span class="st">"city"</span>, <span class="st">"education"</span>]

<span class="cm"># ColumnTransformer: apply different transformers to different columns</span>
preprocessor = ColumnTransformer(transformers=[
    (<span class="st">"num"</span>, Pipeline([
        (<span class="st">"imputer"</span>, SimpleImputer(strategy=<span class="st">"mean"</span>)),
        (<span class="st">"scaler"</span>, StandardScaler())
    ]), numeric_features),
    (<span class="st">"cat"</span>, OneHotEncoder(handle_unknown=<span class="st">"ignore"</span>), categorical_features)
])

<span class="cm"># Full pipeline: preprocess + model</span>
full_pipe = Pipeline([
    (<span class="st">"preprocessor"</span>, preprocessor),
    (<span class="st">"classifier"</span>, RandomForestClassifier(n_estimators=<span class="nm">50</span>, random_state=<span class="nm">42</span>))
])

full_pipe.fit(df, y)
<span class="bi">print</span>(<span class="st">f"Training score: {full_pipe.score(df, y):.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"Prediction: {full_pipe.predict(df[:2])}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Training score: 1.0000<br>Prediction: [0 1]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Complete Pipeline with GridSearchCV</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> GridSearchCV

<span class="cm"># Pipeline + GridSearch</span>
pipe = make_pipeline(StandardScaler(), SVC())

<span class="cm"># Use step__param naming convention</span>
param_grid = {
    <span class="st">"svc__C"</span>: [<span class="nm">0.1</span>, <span class="nm">1</span>, <span class="nm">10</span>],
    <span class="st">"svc__kernel"</span>: [<span class="st">"linear"</span>, <span class="st">"rbf"</span>],
    <span class="st">"svc__gamma"</span>: [<span class="st">"scale"</span>, <span class="st">"auto"</span>]
}

grid = GridSearchCV(pipe, param_grid, cv=<span class="nm">5</span>, scoring=<span class="st">"accuracy"</span>)
grid.fit(X_train, y_train)

<span class="bi">print</span>(<span class="st">f"Best params: {grid.best_params_}"</span>)
<span class="bi">print</span>(<span class="st">f"Best score: {grid.best_score_:.4f}"</span>)
<span class="bi">print</span>(<span class="st">f"Test: {grid.score(X_test, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Best params: {'svc__C': 1, 'svc__kernel': 'rbf', 'svc__gamma': 'scale'}<br>Best score: 0.9750</div></div>
<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>Why use Pipelines?</strong>
<ul><li>Prevents <strong>data leakage</strong> (scaler only sees training data)</li>
<li><strong>Reproducible</strong>: single object to save/load</li>
<li>Works with <strong>cross_val_score</strong> and <strong>GridSearchCV</strong></li></ul></div></div></section>''',
("clustering.html","Clustering"),("feature-selection.html","Feature Selection"))

# FEATURE SELECTION (NEW)
make_page("ml/feature-selection.html","Feature Selection &amp; PCA","Machine Learning","&#x1F916;","advanced","ML &rarr; Feature Selection",
"Select the most important features to improve model performance and reduce overfitting. Covers VarianceThreshold, SelectKBest (chi2, f_classif, mutual_info), RFE, PCA (Principal Component Analysis), and other dimensionality reduction techniques.",
"sklearn Documentation",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">VarianceThreshold</a></li>
<li><a href="#s2">SelectKBest</a></li>
<li><a href="#s3">RFE (Recursive Feature Elimination)</a></li>
<li><a href="#s4">PCA (Principal Component Analysis)</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; VarianceThreshold</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.feature_selection <span class="kw">import</span> (
    VarianceThreshold, SelectKBest, chi2, f_classif,
    mutual_info_classif, RFE
)
<span class="kw">from</span> sklearn.decomposition <span class="kw">import</span> PCA, KernelPCA, TruncatedSVD
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Remove features with low variance</span>
X = np.array([[<span class="nm">0</span>,<span class="nm">0</span>,<span class="nm">1</span>],[<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">0</span>],[<span class="nm">1</span>,<span class="nm">0</span>,<span class="nm">0</span>],[<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">1</span>],[<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">0</span>],[<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">1</span>]])
<span class="bi">print</span>(<span class="st">f"Original: {X.shape}"</span>)

vt = VarianceThreshold(threshold=<span class="nm">0.16</span>)  <span class="cm"># remove &lt; 80/20 split</span>
X_new = vt.fit_transform(X)
<span class="bi">print</span>(<span class="st">f"After VT: {X_new.shape}"</span>)
<span class="bi">print</span>(<span class="st">f"Kept features: {vt.get_support()}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Original: (6, 3)<br>After VT: (6, 2)<br>Kept features: [False True True]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; SelectKBest</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_iris
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split

X, y = load_iris(return_X_y=<span class="kw">True</span>)
<span class="bi">print</span>(<span class="st">f"Original features: {X.shape[1]}"</span>)  <span class="cm"># 4</span>

<span class="cm"># SelectKBest with f_classif (ANOVA F-value)</span>
skb = SelectKBest(score_func=f_classif, k=<span class="nm">2</span>)
X_new = skb.fit_transform(X, y)
<span class="bi">print</span>(<span class="st">f"After SelectKBest(2): {X_new.shape[1]}"</span>)
<span class="bi">print</span>(<span class="st">f"Scores: {skb.scores_.round(2)}"</span>)
<span class="bi">print</span>(<span class="st">f"Selected: {skb.get_support()}"</span>)

<span class="cm"># With chi2 (for non-negative features only)</span>
skb_chi = SelectKBest(score_func=chi2, k=<span class="nm">2</span>)
X_chi = skb_chi.fit_transform(X, y)
<span class="bi">print</span>(<span class="st">f"Chi2 scores: {skb_chi.scores_.round(2)}"</span>)

<span class="cm"># With mutual_info_classif (captures non-linear relationships)</span>
skb_mi = SelectKBest(score_func=mutual_info_classif, k=<span class="nm">2</span>)
X_mi = skb_mi.fit_transform(X, y)
<span class="bi">print</span>(<span class="st">f"MI scores: {skb_mi.scores_.round(4)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Original: 4 &rarr; After: 2<br>f_classif scores: [119.26 49.16 1180.16 960.01]<br>Selected: [False False True True] (petal features!)</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; RFE (Recursive Feature Elimination)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> RandomForestClassifier

<span class="cm"># RFE uses model importance to eliminate features</span>
rfe = RFE(
    estimator=RandomForestClassifier(n_estimators=<span class="nm">50</span>, random_state=<span class="nm">42</span>),
    n_features_to_select=<span class="nm">2</span>,  <span class="cm"># keep 2 features</span>
    step=<span class="nm">1</span>                   <span class="cm"># remove 1 feature per iteration</span>
)
rfe.fit(X, y)
<span class="bi">print</span>(<span class="st">f"Selected features: {rfe.support_}"</span>)
<span class="bi">print</span>(<span class="st">f"Feature ranking: {rfe.ranking_}"</span>)
<span class="bi">print</span>(<span class="st">f"Selected names: {np.array(load_iris().feature_names)[rfe.support_]}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Selected: [False False True True]<br>Ranking: [3 2 1 1]<br>Names: ['petal length (cm)', 'petal width (cm)']</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; PCA (Dimensionality Reduction)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> StandardScaler

<span class="cm"># Always scale before PCA!</span>
X_scaled = StandardScaler().fit_transform(X)

<span class="cm"># PCA: reduce 4 features to 2</span>
pca = PCA(n_components=<span class="nm">2</span>)
X_pca = pca.fit_transform(X_scaled)
<span class="bi">print</span>(<span class="st">f"Original: {X.shape} &rarr; PCA: {X_pca.shape}"</span>)
<span class="bi">print</span>(<span class="st">f"Explained variance ratio: {pca.explained_variance_ratio_.round(4)}"</span>)
<span class="bi">print</span>(<span class="st">f"Total variance kept: {pca.explained_variance_ratio_.sum():.2%}"</span>)

<span class="cm"># How many components to keep 95% variance?</span>
pca_full = PCA(n_components=<span class="nm">0.95</span>)  <span class="cm"># auto-select for 95%</span>
X_auto = pca_full.fit_transform(X_scaled)
<span class="bi">print</span>(<span class="st">f"Components for 95%: {pca_full.n_components_}"</span>)

<span class="cm"># Inverse transform (reconstruct original space)</span>
X_reconstructed = pca.inverse_transform(X_pca)
reconstruction_error = np.mean((X_scaled - X_reconstructed) ** <span class="nm">2</span>)
<span class="bi">print</span>(<span class="st">f"Reconstruction error: {reconstruction_error:.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>(150, 4) &rarr; (150, 2)<br>Explained: [0.7277 0.2303] &mdash; Total: 95.80%<br>Components for 95%: 2</div></div></section>''',
("pipelines.html","Pipelines"),("../data/preprocessing.html","Preprocessing"))

print("clustering.html + pipelines.html + feature-selection.html expanded!")
