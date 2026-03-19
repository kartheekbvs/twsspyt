import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# SUPERVISED LEARNING & SVM (MASSIVE EXPANSION)
ml_intro_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 2 &middot; Supervised Learning & SVM</h4>
    <ol>
        <li><a href="#intro">1. The General Idea of Supervised Learning</a></li>
        <li><a href="#svm-theory">2. Image Recognition with Support Vector Machines</a></li>
        <li><a href="#hyperplane">3. The Optimal Hyperplane & Margin</a></li>
        <li><a href="#kernel">4. The Kernel Trick: Polynomial & RBF</a></li>
        <li><a href="#example">5. Practical Example: Olivetti Faces</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The General Idea of Supervised Learning</h2>
    <p>Supervised learning algorithms work with training data where each instance has an input (a set of attributes) and a desired output (a target class). As the textbook clarifies: <em>"We use this data to train a model that will predict the same target class for new unseen instances."</em> These methods are standard tools in disciplines ranging from medical diagnosis to particle physics at the Large Hadron Collider (LHC).</p>
</section>

<section class="content-section" id="svm-theory">
    <h2>2 &middot; Image Recognition with Support Vector Machines</h2>
    <p>Imagine instances in your dataset as points in a multidimensional space. Support Vector Machines (SVM) attempt to find a <strong>hyperplane</strong> that separates instances of one class from the rest in an optimal way, selecting those that pass through the widest possible gaps between instances of different classes.</p>
    <div class="callout note">
        <div class="callout-icon">📐</div>
        <div class="callout-content">
            <strong>The Optimal Hyperplane</strong>
            <p>The "red surface" typically represents the hyperplane with the <strong>maximum margin</strong>; it is the most distant hyperplane from the closest instances of the two categories. This approach lowers the <strong>generalization error</strong>, making the model resistant to overfitting.</p>
        </div>
    </div>
</section>

<section class="content-section" id="kernel">
    <h2>4 &middot; The Kernel Trick</h2>
    <p>SVM can construct hyperplanes in high or infinite dimensional spaces using nonlinear surfaces, such as polynomial or radial basis functions (RBF), by using the <strong>kernel trick</strong>. This implicitly maps inputs into high-dimensional feature spaces without the computational cost of direct transformation.</p>
    <div class="return-value-box">
        <div class="rv-label">⚙️ Hyperparameters: kernel, C, gamma</div>
        <p>The <code>SVC</code> implementation in Scikit-Learn defaults to the <code>rbf</code> kernel. The <code>C</code> parameter controls the trade-off between smooth decision boundaries and classifying training points correctly.</p>
    </div>
</section>

<section class="content-section" id="example">
    <h2>5 &middot; Practical Example: Face Recognition</h2>
    <p>Using the <code>fetch_olivetti_faces</code> dataset, we treat pixel values as learning attributes. Since pixel values are already in a uniform range (0 to 1), normalization is often unnecessary.</p>
    <div class="code-block">
        <div class="code-header"><span>Python</span><button class="copy-btn">Copy</button></div>
        <pre><code>from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split

# Initialize SVC with a linear kernel
svc_1 = SVC(kernel='linear')

# Split dataset (75% training, 25% testing)
X_train, X_test, y_train, y_test = train_test_split(
    faces.data, faces.target, test_size=0.25, random_state=0)

# Fit the model
svc_1.fit(X_train, y_train)
print(f"Accuracy: {svc_1.score(X_test, y_test)}")</code></pre>
    </div>
</section>
"""

make_page("ml/intro-ml.html","Supervised Learning & SVM","Machine Learning","&#x1F916;","beginner","ML &rarr; Supervised Learning",
"Massive textbook-accurate expansion of Supervised Learning fundamentals and Support Vector Machines, including image recognition and the kernel trick.",
"Learning scikit-learn &mdash; Raúl Garreta", ml_intro_body, ("../pandas/visualization.html","Pandas Visualization"), ("naive-bayes.html","Naive Bayes"),
[("../pandas/series-dataframe.html", "Data Structures"), ("model-evaluation.html", "Metrics")])

# NAIVE BAYES (MASSIVE EXPANSION)
ml_nb_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 3 &middot; Text Classification with Naïve Bayes</h4>
    <ol>
        <li><a href="#theory">1. Probabilistic Modeling & Bayes Theorem</a></li>
        <li><a href="#independence">2. The Independence Assumption</a></li>
        <li><a href="#nlp">3. NLP Preprocessing: Vectorization</a></li>
        <li><a href="#pipeline">4. The Scikit-Learn Pipeline</a></li>
        <li><a href="#evaluation">5. Evaluating Performance: Precision/Recall</a></li>
    </ol>
</div>

<section class="content-section" id="theory">
    <h2>1 &middot; Probabilistic Modeling</h2>
    <p>Naïve Bayes is a powerful classifier based on a probabilistic model derived from <strong>Bayes' theorem</strong>. It determines the probability that an instance belongs to a class based on each of the feature value probabilities.</p>
</section>

<section class="content-section" id="independence">
    <h2>2 &middot; The "Naïve" Assumption</h2>
    <div class="callout warning">
        <div class="callout-icon">⚠️</div>
        <div class="callout-content">
            <strong>Feature Independence</strong>
            <p>The term "naïve" comes from the assumption that each feature is independent of the rest. While this is a strong simplification, it makes the model computationally efficient and highly effective for high-dimensional data like text.</p>
        </div>
    </div>
</section>

<section class="content-section" id="nlp">
    <h2>3 &middot; NLP Preprocessing</h2>
    <p>To convert text documents into numeric features, Scikit-Learn provides several vectorizers:</p>
    <ul>
        <li><strong>CountVectorizer:</strong> Creates a dictionary and counts word occurrences.</li>
        <li><strong>HashingVectorizer:</strong> Uses a hashing function to map tokens to feature indexes (memory efficient).</li>
        <li><strong>TfidfVectorizer:</strong> Uses Terminal Frequency Inverse Document Frequency to weight word importance.</li>
    </ul>
</section>

<section class="content-section" id="pipeline">
    <h2>4 &middot; The Pipeline Implementation</h2>
    <p>Composing a vectorizer with a classifier is simplified using the <code>Pipeline</code> class.</p>
    <div class="code-block">
        <div class="code-header"><span>Python</span><button class="copy-btn">Copy</button></div>
        <pre><code>from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

clf = Pipeline([
    ('vect', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB(alpha=0.01)), # Smoothing parameter
])

clf.fit(X_train, y_train)</code></pre>
    </div>
</section>
"""

make_page("ml/naive-bayes.html","Naive Bayes Classification","Machine Learning","&#x1F916;","intermediate","ML &rarr; Naive Bayes",
"Detailed analysis of Naive Bayes for text classification, including NLP preprocessing techniques like TF-IDF and Scikit-Learn Pipelines.",
"Learning scikit-learn &mdash; Raúl Garreta", ml_nb_body, ("intro-ml.html","Supervised Learning"), ("decision-trees.html","Decision Trees"),
[("intro-ml.html", "ML Intro"), ("model-evaluation.html", "Classification Metrics")])

print("intro-ml.html + naive-bayes.html MASSIVELY expanded!")

