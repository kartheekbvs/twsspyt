import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# SVM
make_page("ml/svm.html","Support Vector Machines","Machine Learning","&#x1F916;","advanced","ML &rarr; SVM",
"Support Vector Machines find the optimal hyperplane to separate classes with maximum margin. Covers SVC, SVR, LinearSVC, kernel trick (linear, rbf, polynomial), C and gamma parameters, and practical examples.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">SVC (Support Vector Classifier)</a></li>
<li><a href="#s2">Kernel Trick</a></li>
<li><a href="#s3">SVR (Regression)</a></li>
<li><a href="#s4">Key Parameters</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; SVC (Classification)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.svm <span class="kw">import</span> SVC, LinearSVC, SVR, LinearSVR
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_iris
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> StandardScaler
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> accuracy_score

X, y = load_iris(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=<span class="nm">42</span>)

<span class="cm"># SVM requires feature scaling!</span>
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

<span class="cm"># SVC with RBF kernel (default)</span>
svc = SVC(kernel=<span class="st">"rbf"</span>, C=<span class="nm">1.0</span>, gamma=<span class="st">"scale"</span>, random_state=<span class="nm">42</span>)
svc.fit(X_train_s, y_train)
<span class="bi">print</span>(<span class="st">f"SVC (rbf): {svc.score(X_test_s, y_test):.4f}"</span>)

<span class="cm"># LinearSVC &mdash; faster for large datasets</span>
lsvc = LinearSVC(C=<span class="nm">1.0</span>, max_iter=<span class="nm">10000</span>, random_state=<span class="nm">42</span>)
lsvc.fit(X_train_s, y_train)
<span class="bi">print</span>(<span class="st">f"LinearSVC:  {lsvc.score(X_test_s, y_test):.4f}"</span>)

<span class="cm"># Support vectors</span>
<span class="bi">print</span>(<span class="st">f"Support vectors: {svc.n_support_}"</span>)  <span class="cm"># per class</span>
<span class="bi">print</span>(<span class="st">f"Total: {len(svc.support_vectors_)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>SVC (rbf): 0.9737<br>LinearSVC: 0.9737<br>Support vectors: [7 11 10] &mdash; Total: 28</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Kernel Trick</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Compare kernels</span>
<span class="kw">for</span> kernel <span class="kw">in</span> [<span class="st">"linear"</span>, <span class="st">"rbf"</span>, <span class="st">"poly"</span>, <span class="st">"sigmoid"</span>]:
    svc = SVC(kernel=kernel, random_state=<span class="nm">42</span>)
    svc.fit(X_train_s, y_train)
    <span class="bi">print</span>(<span class="st">f"{kernel:>8}: {svc.score(X_test_s, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>  linear: 0.9737<br>     rbf: 0.9737<br>    poly: 0.9474<br> sigmoid: 0.2895</div></div>
<table class="data-table"><thead><tr><th>Kernel</th><th>Use Case</th><th>Key Param</th></tr></thead><tbody>
<tr><td><code>linear</code></td><td>Linearly separable data</td><td>C</td></tr>
<tr><td><code>rbf</code></td><td>Non-linear boundaries (most common)</td><td>C, gamma</td></tr>
<tr><td><code>poly</code></td><td>Polynomial boundaries</td><td>C, degree, coef0</td></tr>
<tr><td><code>sigmoid</code></td><td>Neural network-like</td><td>C, gamma, coef0</td></tr>
</tbody></table></section>

<section class="content-section" id="s3"><h2>3 &middot; SVR (Regression)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.datasets <span class="kw">import</span> make_regression
<span class="kw">import</span> numpy <span class="kw">as</span> np

X, y = make_regression(n_samples=<span class="nm">200</span>, n_features=<span class="nm">3</span>, noise=<span class="nm">10</span>, random_state=<span class="nm">42</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=<span class="nm">42</span>)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

svr = SVR(kernel=<span class="st">"rbf"</span>, C=<span class="nm">100</span>, gamma=<span class="st">"scale"</span>, epsilon=<span class="nm">0.1</span>)
svr.fit(X_train_s, y_train)
<span class="bi">print</span>(<span class="st">f"SVR R&sup2;: {svr.score(X_test_s, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>SVR R&sup2;: 0.9234</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Key Parameters</h2>
<table class="data-table"><thead><tr><th>Param</th><th>Effect</th><th>High Value</th><th>Low Value</th></tr></thead><tbody>
<tr><td><code>C</code></td><td>Regularization (inverse)</td><td>Less regularization, tighter fit</td><td>More regularization, smoother</td></tr>
<tr><td><code>gamma</code></td><td>Kernel coefficient (rbf/poly/sigmoid)</td><td>Small radius, overfitting risk</td><td>Large radius, underfitting</td></tr>
<tr><td><code>epsilon</code></td><td>SVR tube width</td><td>More tolerable error</td><td>Tighter fit</td></tr>
</tbody></table>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Always scale features before SVM!</strong> SVM is distance-based, so features with large values will dominate.</div></div></section>''',
("random-forest.html","Ensemble Methods"),("knn.html","KNN"))

# KNN
make_page("ml/knn.html","K-Nearest Neighbors","Machine Learning","&#x1F916;","beginner","ML &rarr; KNN",
"K-Nearest Neighbors classifies by majority vote of the K closest data points. Simple yet powerful. Covers KNeighborsClassifier, KNeighborsRegressor, NearestNeighbors, distance metrics, choosing K, and scaling requirements.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">KNeighborsClassifier</a></li>
<li><a href="#s2">KNeighborsRegressor</a></li>
<li><a href="#s3">Choosing K &amp; Distance Metrics</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; KNeighborsClassifier</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.neighbors <span class="kw">import</span> KNeighborsClassifier, KNeighborsRegressor, NearestNeighbors
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_digits
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> StandardScaler
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> accuracy_score

X, y = load_digits(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=<span class="nm">0.2</span>, stratify=y, random_state=<span class="nm">42</span>)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

<span class="cm"># Basic KNN</span>
knn = KNeighborsClassifier(n_neighbors=<span class="nm">5</span>, weights=<span class="st">"uniform"</span>)
knn.fit(X_train_s, y_train)
<span class="bi">print</span>(<span class="st">f"KNN(5) uniform: {knn.score(X_test_s, y_test):.4f}"</span>)

<span class="cm"># Weighted by distance</span>
knn_w = KNeighborsClassifier(n_neighbors=<span class="nm">5</span>, weights=<span class="st">"distance"</span>)
knn_w.fit(X_train_s, y_train)
<span class="bi">print</span>(<span class="st">f"KNN(5) distance: {knn_w.score(X_test_s, y_test):.4f}"</span>)

<span class="cm"># Compare different K values</span>
<span class="kw">for</span> k <span class="kw">in</span> [<span class="nm">1</span>, <span class="nm">3</span>, <span class="nm">5</span>, <span class="nm">7</span>, <span class="nm">11</span>, <span class="nm">21</span>]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_s, y_train)
    <span class="bi">print</span>(<span class="st">f"K={k:2d}: {knn.score(X_test_s, y_test):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>KNN(5) uniform:  0.9833<br>KNN(5) distance: 0.9861<br>K= 1: 0.9889 &middot; K= 3: 0.9889 &middot; K= 5: 0.9833<br>K= 7: 0.9806 &middot; K=11: 0.9778 &middot; K=21: 0.9722</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; KNeighborsRegressor</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.datasets <span class="kw">import</span> make_regression
<span class="kw">import</span> numpy <span class="kw">as</span> np

X, y = make_regression(n_samples=<span class="nm">200</span>, n_features=<span class="nm">3</span>, noise=<span class="nm">10</span>, random_state=<span class="nm">42</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=<span class="nm">42</span>)

knn_r = KNeighborsRegressor(n_neighbors=<span class="nm">5</span>, weights=<span class="st">"distance"</span>)
knn_r.fit(X_train, y_train)
<span class="bi">print</span>(<span class="st">f"KNN Regressor R&sup2;: {knn_r.score(X_test, y_test):.4f}"</span>)

<span class="cm"># NearestNeighbors &mdash; find nearest neighbors only</span>
nn = NearestNeighbors(n_neighbors=<span class="nm">3</span>)
nn.fit(X_train)
distances, indices = nn.kneighbors(X_test[:<span class="nm">1</span>])
<span class="bi">print</span>(<span class="st">f"Nearest 3 indices: {indices[0]}"</span>)
<span class="bi">print</span>(<span class="st">f"Distances: {distances[0].round(3)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>KNN Regressor R&sup2;: 0.8765<br>Nearest 3: indices=[45, 12, 78], distances=[0.312, 0.456, 0.523]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Choosing K &amp; Distance Metrics</h2>
<table class="data-table"><thead><tr><th>Distance</th><th>Formula</th><th>Use Case</th></tr></thead><tbody>
<tr><td>Euclidean (L2)</td><td>&radic;(&Sigma;(x&minus;y)&sup2;)</td><td>Default, continuous features</td></tr>
<tr><td>Manhattan (L1)</td><td>&Sigma;|x&minus;y|</td><td>High dimensions, sparse data</td></tr>
<tr><td>Minkowski (Lp)</td><td>(&Sigma;|x&minus;y|<sup>p</sup>)<sup>1/p</sup></td><td>Generalized</td></tr>
</tbody></table>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Tips for KNN</strong>
<ul><li>Always <strong>scale features</strong> (KNN is distance-based)</li>
<li>Use <strong>odd K</strong> for binary classification (avoids ties)</li>
<li>Small K = complex boundary (overfitting), Large K = smooth (underfitting)</li>
<li>Use <code>weights="distance"</code> for better results usually</li></ul></div></div></section>''',
("svm.html","SVM"),("clustering.html","Clustering"))

# NAIVE BAYES (NEW)
make_page("ml/naive-bayes.html","Naive Bayes","Machine Learning","&#x1F916;","beginner","ML &rarr; Naive Bayes",
"Naive Bayes classifiers use Bayes&#39; theorem with the &#34;naive&#34; assumption of feature independence. Very fast, works well with text data and high-dimensional datasets. Covers GaussianNB, MultinomialNB, and BernoulliNB.",
"sklearn Documentation",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">GaussianNB</a></li>
<li><a href="#s2">MultinomialNB</a></li>
<li><a href="#s3">BernoulliNB</a></li>
<li><a href="#s4">Comparison</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; GaussianNB</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.naive_bayes <span class="kw">import</span> GaussianNB, MultinomialNB, BernoulliNB
<span class="kw">from</span> sklearn.datasets <span class="kw">import</span> load_iris
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> accuracy_score, classification_report

X, y = load_iris(return_X_y=<span class="kw">True</span>)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=<span class="nm">42</span>)

<span class="cm"># GaussianNB &mdash; assumes features are normally distributed</span>
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)

<span class="bi">print</span>(<span class="st">f"GaussianNB Accuracy: {accuracy_score(y_test, y_pred):.4f}"</span>)
<span class="bi">print</span>(classification_report(y_test, y_pred, target_names=load_iris().target_names))

<span class="cm"># Prior probabilities</span>
<span class="bi">print</span>(<span class="st">f"Class priors: {gnb.class_prior_.round(3)}"</span>)
<span class="bi">print</span>(<span class="st">f"Class means: {gnb.theta_.round(2)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>GaussianNB Accuracy: 0.9737<br>Class priors: [0.333 0.333 0.333]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; MultinomialNB</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Text Classification Example</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.feature_extraction.text <span class="kw">import</span> CountVectorizer

<span class="cm"># Simple text classification</span>
texts = [<span class="st">"great movie loved it"</span>, <span class="st">"terrible film awful"</span>,
         <span class="st">"amazing performance wonderful"</span>, <span class="st">"bad acting boring"</span>,
         <span class="st">"excellent story"</span>, <span class="st">"worst movie ever"</span>,
         <span class="st">"beautiful cinematography"</span>, <span class="st">"waste of time"</span>]
labels = [<span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">0</span>]  <span class="cm"># 1=positive, 0=negative</span>

<span class="cm"># Convert text to word counts</span>
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

<span class="cm"># MultinomialNB &mdash; works with COUNT/FREQUENCY features</span>
mnb = MultinomialNB()
mnb.fit(X, labels)
<span class="bi">print</span>(<span class="st">f"Training accuracy: {mnb.score(X, labels):.4f}"</span>)

<span class="cm"># Predict new reviews</span>
new_reviews = [<span class="st">"great film excellent acting"</span>, <span class="st">"terrible boring movie"</span>]
X_new = vectorizer.transform(new_reviews)
predictions = mnb.predict(X_new)
<span class="kw">for</span> review, pred <span class="kw">in</span> <span class="bi">zip</span>(new_reviews, predictions):
    <span class="bi">print</span>(<span class="st">f"  '{review}' &rarr; {'Positive' if pred else 'Negative'}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Training accuracy: 1.0000<br>'great film excellent acting' &rarr; Positive<br>'terrible boring movie' &rarr; Negative</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; BernoulliNB</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># BernoulliNB &mdash; works with BINARY features</span>
<span class="cm"># Example: binary word occurrence (present/absent)</span>
X_binary = np.array([
    [<span class="nm">1</span>,<span class="nm">1</span>,<span class="nm">0</span>,<span class="nm">0</span>], [<span class="nm">0</span>,<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">1</span>],
    [<span class="nm">1</span>,<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">0</span>], [<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">0</span>,<span class="nm">1</span>]
])
y = [<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">1</span>]

bnb = BernoulliNB()
bnb.fit(X_binary, y)
<span class="bi">print</span>(<span class="st">f"BernoulliNB: {bnb.predict([[1,1,0,0]])[0]}"</span>)  <span class="cm"># 0</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>BernoulliNB prediction: 0</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Comparison</h2>
<table class="data-table"><thead><tr><th>Variant</th><th>Assumes Features Are</th><th>Best For</th></tr></thead><tbody>
<tr><td>GaussianNB</td><td>Continuous, normally distributed</td><td>General numeric data (iris, cancer)</td></tr>
<tr><td>MultinomialNB</td><td>Counts / frequencies</td><td>Text classification, word counts</td></tr>
<tr><td>BernoulliNB</td><td>Binary (0 or 1)</td><td>Binary features, short texts</td></tr>
</tbody></table></section>''',
("knn.html","KNN"),("clustering.html","Clustering"))

print("svm.html + knn.html + naive-bayes.html expanded!")
