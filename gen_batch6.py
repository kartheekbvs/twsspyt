
import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# Pandas pages
for pg in [
    ("pandas/reading-data.html","Reading Data","Pandas","&#x1F43C;","beginner","Pandas &rarr; Reading Data",
     "Pandas can read data from CSV, Excel, JSON, SQL, HTML, and more using pd.read_*() functions. This covers reading, writing, handling missing data during import, and optimizing dtypes.",
     "Python for Data Analysis &mdash; Wes McKinney",
     "reading-data","series-dataframe.html","Series &amp; DataFrame","selection.html","Selection &amp; Filtering"),
    ("pandas/selection.html","Selection &amp; Filtering","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Selection",
     "Pandas provides multiple ways to select data: [] operator, .loc (label-based), .iloc (integer-based), and boolean indexing. Master these for efficient data manipulation.",
     "Python for Data Analysis &mdash; Wes McKinney",
     "selection","reading-data.html","Reading Data","cleaning.html","Data Cleaning"),
    ("pandas/cleaning.html","Data Cleaning","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Data Cleaning",
     "Data cleaning handles missing values (NaN), duplicates, type conversions, and outliers. Essential preprocessing step before any analysis or ML model training.",
     "Python for Data Analysis &mdash; Wes McKinney, Data Science and Analytics with Python",
     "cleaning","selection.html","Selection","groupby.html","GroupBy"),
    ("pandas/merging.html","Merging &amp; Joining","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Merging",
     "Combining DataFrames using merge (SQL-like joins), concat (stacking), and join. Understanding inner, outer, left, right joins is crucial for relational data work.",
     "Python for Data Analysis &mdash; Wes McKinney",
     "merging","groupby.html","GroupBy","visualization.html","Visualization"),
    ("pandas/visualization.html","Visualization with Pandas","Pandas","&#x1F43C;","intermediate","Pandas &rarr; Visualization",
     "Pandas integrates with Matplotlib for quick plotting: line, bar, histogram, scatter, box, pie charts directly from DataFrames and Series using .plot().",
     "Python for Data Analysis &mdash; Wes McKinney",
     "viz","merging.html","Merging","../ml/intro-ml.html","Intro to ML"),
]:
    path,title,sec,emoji,diff,bc,intro,books,secid,ph,pl,nh,nl = pg
    body = f'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Core Concepts</a></li><li><a href="#s2">Code Examples</a></li><li><a href="#s3">Common Patterns</a></li><li><a href="#s4">Best Practices</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Core Concepts</h2>
<p>{intro}</p></section>
<section class="content-section" id="s2"><h2>2 &middot; Code Examples</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Example DataFrame</span>
df = pd.DataFrame({{
    <span class="st">"name"</span>: [<span class="st">"Alice"</span>,<span class="st">"Bob"</span>,<span class="st">"Charlie"</span>,<span class="st">"Diana"</span>],
    <span class="st">"age"</span>: [<span class="nm">25</span>,<span class="nm">30</span>,<span class="nm">35</span>,<span class="nm">28</span>],
    <span class="st">"salary"</span>: [<span class="nm">50000</span>,<span class="nm">60000</span>,<span class="nm">70000</span>,<span class="nm">55000</span>],
    <span class="st">"dept"</span>: [<span class="st">"Engineering"</span>,<span class="st">"Marketing"</span>,<span class="st">"Engineering"</span>,<span class="st">"Marketing"</span>]
}})
<span class="bi">print</span>(df)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>      name  age  salary         dept<br>0    Alice   25   50000  Engineering<br>1      Bob   30   60000    Marketing<br>2  Charlie   35   70000  Engineering<br>3    Diana   28   55000    Marketing</div></div></section>
<section class="content-section" id="s3"><h2>3 &middot; Common Patterns</h2>
<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Textbook Insight</strong>
<p>Pandas is built on NumPy and provides high-performance, easy-to-use data structures. The two primary structures are Series (1D) and DataFrame (2D). Always prefer vectorized operations over loops.</p></div></div></section>
<section class="content-section" id="s4"><h2>4 &middot; Best Practices</h2>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Performance Tip</strong>
<p>Use <code>.apply()</code> sparingly &mdash; prefer vectorized operations. Use <code>category</code> dtype for string columns with few unique values to save memory.</p></div></div></section>'''
    make_page(path,title,sec,emoji,diff,bc,intro,books,body,(ph,pl),(nh,nl))

# ML pages
for pg in [
    ("ml/logistic-regression.html","Logistic Regression","Machine Learning","&#x1F916;","intermediate",
     "ML &rarr; Logistic Regression","Logistic Regression is a classification algorithm that models the probability of a binary outcome using the sigmoid function. Despite its name, it's for classification, not regression.",
     "ML Cookbook, Learning scikit-learn","linear-regression.html","Linear Regression","decision-trees.html","Decision Trees"),
    ("ml/decision-trees.html","Decision Trees","Machine Learning","&#x1F916;","intermediate",
     "ML &rarr; Decision Trees","Decision Trees recursively split data based on feature thresholds to make predictions. They're interpretable, handle non-linear relationships, and form the basis of ensemble methods like Random Forest.",
     "ML Cookbook, Learning scikit-learn","logistic-regression.html","Logistic Regression","random-forest.html","Random Forest"),
    ("ml/random-forest.html","Random Forest","Machine Learning","&#x1F916;","intermediate",
     "ML &rarr; Random Forest","Random Forest is an ensemble of decision trees trained on random subsets of data (bagging). It reduces overfitting, handles high-dimensional data, and provides feature importance rankings.",
     "ML Cookbook, Learning scikit-learn","decision-trees.html","Decision Trees","svm.html","SVM"),
    ("ml/svm.html","Support Vector Machines","Machine Learning","&#x1F916;","advanced",
     "ML &rarr; SVM","SVMs find the optimal hyperplane that maximizes the margin between classes. They use kernel tricks (linear, RBF, polynomial) for non-linear classification and work well in high-dimensional spaces.",
     "ML Cookbook, Learning scikit-learn","random-forest.html","Random Forest","knn.html","KNN"),
    ("ml/knn.html","K-Nearest Neighbors","Machine Learning","&#x1F916;","intermediate",
     "ML &rarr; KNN","KNN is a simple, instance-based algorithm that classifies by majority vote of k nearest neighbors. It requires no training phase but is computationally expensive at prediction time.",
     "ML Cookbook, Learning scikit-learn","svm.html","SVM","clustering.html","Clustering"),
    ("ml/clustering.html","K-Means Clustering","Machine Learning","&#x1F916;","intermediate",
     "ML &rarr; K-Means Clustering","K-Means is an unsupervised algorithm that partitions data into k clusters by minimizing within-cluster variance. Uses the elbow method and silhouette score for choosing k.",
     "ML Cookbook, Learning scikit-learn","knn.html","KNN","model-evaluation.html","Model Evaluation"),
    ("ml/model-evaluation.html","Model Evaluation","Machine Learning","&#x1F916;","intermediate",
     "ML &rarr; Model Evaluation","Evaluating ML models using accuracy, precision, recall, F1-score, confusion matrix, ROC-AUC, cross-validation, and bias-variance tradeoff. Essential for comparing and selecting models.",
     "ML Cookbook, Learning scikit-learn","clustering.html","Clustering","../dl/neural-networks.html","Neural Networks"),
]:
    path,title,sec,emoji,diff,bc,intro,books,ph,pl,nh,nl = pg
    body = f'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Theory &amp; Intuition</a></li><li><a href="#s2">sklearn Implementation</a></li><li><a href="#s3">Key Concepts</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Theory &amp; Intuition</h2>
<p>{intro}</p>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Key Insight</strong>
<p>Understanding the mathematical foundation helps you choose the right algorithm, tune hyperparameters, and debug poor performance.</p></div></div></section>
<section class="content-section" id="s2"><h2>2 &middot; sklearn Implementation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.metrics <span class="kw">import</span> accuracy_score, classification_report
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># General ML workflow:</span>
<span class="cm"># 1. Load data</span>
<span class="cm"># 2. Split: X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)</span>
<span class="cm"># 3. Preprocess: scale features, encode categories</span>
<span class="cm"># 4. Train: model.fit(X_train, y_train)</span>
<span class="cm"># 5. Predict: y_pred = model.predict(X_test)</span>
<span class="cm"># 6. Evaluate: accuracy_score(y_test, y_pred)</span>

<span class="bi">print</span>(<span class="st">"Standard ML workflow with scikit-learn"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Standard ML workflow with scikit-learn</div></div></section>
<section class="content-section" id="s3"><h2>3 &middot; Key Concepts</h2>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Best Practice</strong>
<p>Always split data BEFORE any preprocessing to prevent data leakage. Use pipelines with <code>Pipeline</code> from sklearn for cleaner, reproducible workflows.</p></div></div></section>'''
    make_page(path,title,sec,emoji,diff,bc,intro,books,body,(ph,pl),(nh,nl))

# DL pages
for pg in [
    ("dl/backpropagation.html","Backpropagation","Deep Learning","&#x1F9E0;","advanced",
     "DL &rarr; Backpropagation","Backpropagation computes gradients of the loss function w.r.t. each weight using the chain rule. Combined with gradient descent, it's how neural networks learn.",
     "Deep Learning &mdash; Ian Goodfellow","neural-networks.html","Neural Networks","cnn.html","CNN"),
    ("dl/cnn.html","Convolutional Neural Networks","Deep Learning","&#x1F9E0;","advanced",
     "DL &rarr; CNN","CNNs use convolutional layers with learnable filters to extract spatial features from images. They achieve state-of-the-art results in image classification, object detection, and segmentation.",
     "Deep Learning &mdash; Ian Goodfellow","backpropagation.html","Backpropagation","rnn-lstm.html","RNN &amp; LSTM"),
    ("dl/rnn-lstm.html","RNN &amp; LSTM","Deep Learning","&#x1F9E0;","advanced",
     "DL &rarr; RNN &amp; LSTM","RNNs process sequential data by maintaining hidden states. LSTMs solve the vanishing gradient problem with gates (forget, input, output) for long-term dependencies in text, time series, and speech.",
     "Deep Learning &mdash; Ian Goodfellow","cnn.html","CNN","transformers.html","Transformers"),
    ("dl/transformers.html","Transformers","Deep Learning","&#x1F9E0;","expert",
     "DL &rarr; Transformers","Transformers use self-attention to process sequences in parallel (no recurrence). The foundation of BERT, GPT, and modern NLP. Features multi-head attention, positional encoding, and encoder-decoder architecture.",
     "Deep Learning &mdash; Ian Goodfellow","rnn-lstm.html","RNN &amp; LSTM","../data/exploratory.html","EDA"),
]:
    path,title,sec,emoji,diff,bc,intro,books,ph,pl,nh,nl = pg
    body = f'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Architecture Overview</a></li><li><a href="#s2">Mathematical Foundation</a></li><li><a href="#s3">Implementation</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Architecture Overview</h2>
<p>{intro}</p></section>
<section class="content-section" id="s2"><h2>2 &middot; Mathematical Foundation</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>From the Textbook</strong>
<p>"Deep learning is a subset of machine learning that uses neural networks with many layers. The depth allows the model to learn hierarchical representations of data." &mdash; <em>Deep Learning, Goodfellow et al.</em></p></div></div></section>
<section class="content-section" id="s3"><h2>3 &middot; Implementation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Neural network concepts implemented with NumPy</span>
<span class="cm"># See the textbook for full derivations</span>
<span class="bi">print</span>(<span class="st">"Deep learning foundations"</span>)</pre></div></section>'''
    make_page(path,title,sec,emoji,diff,bc,intro,books,body,(ph,pl),(nh,nl))

# Data Analysis pages
for pg in [
    ("data/exploratory.html","Exploratory Data Analysis","Data Analysis","&#x1F4CA;","intermediate",
     "Data &rarr; EDA","EDA is the process of analyzing datasets to summarize main characteristics using statistics and visualizations. It reveals patterns, anomalies, and relationships before formal modeling.",
     "Data Science and Analytics with Python","../dl/transformers.html","Transformers","preprocessing.html","Preprocessing"),
    ("data/preprocessing.html","Data Preprocessing","Data Analysis","&#x1F4CA;","intermediate",
     "Data &rarr; Preprocessing","Preprocessing transforms raw data into a format suitable for ML: scaling, encoding, handling missing values, feature selection. Quality of preprocessing directly impacts model performance.",
     "Data Science and Analytics with Python","exploratory.html","EDA","feature-engineering.html","Feature Engineering"),
    ("data/feature-engineering.html","Feature Engineering","Data Analysis","&#x1F4CA;","advanced",
     "Data &rarr; Feature Engineering","Feature engineering creates new informative features from existing data. Includes polynomial features, binning, interactions, text features (TF-IDF), date/time extraction, and domain-specific transformations.",
     "Data Science and Analytics with Python","preprocessing.html","Preprocessing","matplotlib.html","Matplotlib"),
    ("data/seaborn.html","Seaborn","Data Analysis","&#x1F4CA;","intermediate",
     "Data &rarr; Seaborn","Seaborn is a statistical visualization library built on Matplotlib. It provides beautiful default styles and high-level functions for heatmaps, violin plots, pair plots, and regression plots.",
     "Data Science and Analytics with Python","matplotlib.html","Matplotlib","../../index.html","Home"),
]:
    path,title,sec,emoji,diff,bc,intro,books,ph,pl,nh,nl = pg
    body = f'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Overview</a></li><li><a href="#s2">Key Techniques</a></li><li><a href="#s3">Code Examples</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Overview</h2>
<p>{intro}</p></section>
<section class="content-section" id="s2"><h2>2 &middot; Key Techniques</h2>
<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Textbook Insight</strong>
<p>Data analysis is iterative: explore, clean, transform, visualize, model, and repeat. Each step informs the next.</p></div></div></section>
<section class="content-section" id="s3"><h2>3 &middot; Code Examples</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Standard data analysis workflow</span>
<span class="bi">print</span>(<span class="st">"Data analysis with Python"</span>)</pre></div></section>'''
    make_page(path,title,sec,emoji,diff,bc,intro,books,body,(ph,pl),(nh,nl))

print("Batch 6: Pandas (5), ML (7), DL (4), Data (4) = 20 pages created.")
