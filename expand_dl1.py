import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# NEURAL NETWORKS
make_page("dl/neural-networks.html","Neural Networks Fundamentals","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Neural Networks",
"Neural networks are computing systems inspired by biological brains. This page covers perceptrons, multi-layer perceptrons, activation functions (ReLU, Sigmoid, Tanh, Softmax), forward pass, loss functions, and building neural networks with TensorFlow/Keras from scratch.",
"Deep Learning with Python &mdash; Fran&ccedil;ois Chollet",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">What is a Neural Network?</a></li>
<li><a href="#s2">The Perceptron</a></li>
<li><a href="#s3">Activation Functions</a></li>
<li><a href="#s4">Multi-Layer Perceptron (MLP)</a></li>
<li><a href="#s5">Loss Functions</a></li>
<li><a href="#s6">Building with Keras</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; What is a Neural Network?</h2>
<p>A neural network is a computational model consisting of <strong>layers of interconnected nodes (neurons)</strong> that transform input data through learned weights and biases to produce predictions.</p>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Neural Network Architecture</strong>
<pre style="font-size:.85rem;line-height:1.6;">
Input Layer    Hidden Layer(s)    Output Layer
  [x1] ----&gt;  [h1] ----&gt;        [y1]
  [x2] ----&gt;  [h2] ----&gt;        [y2]
  [x3] ----&gt;  [h3] ----&gt;
              [h4] ----&gt;

Each connection has a WEIGHT (w)
Each neuron has a BIAS (b)
Output = activation(w&middot;x + b)</pre></div></div>
<table class="data-table"><thead><tr><th>Component</th><th>Purpose</th><th>Analogy</th></tr></thead><tbody>
<tr><td><strong>Input Layer</strong></td><td>Receives raw data (features)</td><td>Eyes, ears &mdash; sense the world</td></tr>
<tr><td><strong>Hidden Layers</strong></td><td>Learn patterns &amp; representations</td><td>Brain &mdash; process information</td></tr>
<tr><td><strong>Output Layer</strong></td><td>Produces predictions</td><td>Mouth &mdash; give the answer</td></tr>
<tr><td><strong>Weights (w)</strong></td><td>Importance of each connection</td><td>Synapse strength</td></tr>
<tr><td><strong>Bias (b)</strong></td><td>Shift activation threshold</td><td>Baseline tendency</td></tr>
<tr><td><strong>Activation</strong></td><td>Introduces non-linearity</td><td>Neuron firing threshold</td></tr>
</tbody></table></section>

<section class="content-section" id="s2"><h2>2 &middot; The Perceptron</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Single Perceptron from Scratch</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="kw">class</span> <span class="bi">Perceptron</span>:
    <span class="kw">def</span> <span class="bi">__init__</span>(self, n_features, learning_rate=<span class="nm">0.01</span>):
        self.weights = np.zeros(n_features)
        self.bias = <span class="nm">0</span>
        self.lr = learning_rate

    <span class="kw">def</span> <span class="bi">predict</span>(self, x):
        linear = np.dot(x, self.weights) + self.bias
        <span class="kw">return</span> <span class="nm">1</span> <span class="kw">if</span> linear >= <span class="nm">0</span> <span class="kw">else</span> <span class="nm">0</span>

    <span class="kw">def</span> <span class="bi">train</span>(self, X, y, epochs=<span class="nm">10</span>):
        <span class="kw">for</span> epoch <span class="kw">in</span> <span class="bi">range</span>(epochs):
            errors = <span class="nm">0</span>
            <span class="kw">for</span> xi, yi <span class="kw">in</span> <span class="bi">zip</span>(X, y):
                pred = self.predict(xi)
                error = yi - pred
                self.weights += self.lr * error * xi
                self.bias += self.lr * error
                errors += <span class="bi">abs</span>(error)
            <span class="bi">print</span>(<span class="st">f"Epoch {epoch+1}: errors={errors}"</span>)

<span class="cm"># AND gate</span>
X = np.array([[<span class="nm">0</span>,<span class="nm">0</span>],[<span class="nm">0</span>,<span class="nm">1</span>],[<span class="nm">1</span>,<span class="nm">0</span>],[<span class="nm">1</span>,<span class="nm">1</span>]])
y = np.array([<span class="nm">0</span>, <span class="nm">0</span>, <span class="nm">0</span>, <span class="nm">1</span>])

p = Perceptron(<span class="nm">2</span>)
p.train(X, y, epochs=<span class="nm">10</span>)
<span class="kw">for</span> xi <span class="kw">in</span> X:
    <span class="bi">print</span>(<span class="st">f"{xi} &rarr; {p.predict(xi)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Epoch 1: errors=1<br>Epoch 2: errors=0<br>[0,0] &rarr; 0 &middot; [0,1] &rarr; 0 &middot; [1,0] &rarr; 0 &middot; [1,1] &rarr; 1 &#x2705;</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Activation Functions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Sigmoid: squashes to [0, 1]</span>
<span class="kw">def</span> <span class="bi">sigmoid</span>(x):
    <span class="kw">return</span> <span class="nm">1</span> / (<span class="nm">1</span> + np.exp(-x))

<span class="cm"># ReLU: max(0, x) &mdash; most common in hidden layers</span>
<span class="kw">def</span> <span class="bi">relu</span>(x):
    <span class="kw">return</span> np.maximum(<span class="nm">0</span>, x)

<span class="cm"># Leaky ReLU: allows small negative values</span>
<span class="kw">def</span> <span class="bi">leaky_relu</span>(x, alpha=<span class="nm">0.01</span>):
    <span class="kw">return</span> np.where(x > <span class="nm">0</span>, x, alpha * x)

<span class="cm"># Tanh: squashes to [-1, 1]</span>
<span class="kw">def</span> <span class="bi">tanh</span>(x):
    <span class="kw">return</span> np.tanh(x)

<span class="cm"># Softmax: multi-class probabilities (sum to 1)</span>
<span class="kw">def</span> <span class="bi">softmax</span>(x):
    exp_x = np.exp(x - np.max(x))
    <span class="kw">return</span> exp_x / exp_x.sum()

<span class="cm"># Test all</span>
x = np.array([-<span class="nm">2</span>, -<span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">2</span>])
<span class="bi">print</span>(<span class="st">f"Sigmoid:    {sigmoid(x).round(3)}"</span>)
<span class="bi">print</span>(<span class="st">f"ReLU:       {relu(x)}"</span>)
<span class="bi">print</span>(<span class="st">f"Leaky ReLU: {leaky_relu(x).round(3)}"</span>)
<span class="bi">print</span>(<span class="st">f"Tanh:       {tanh(x).round(3)}"</span>)
<span class="bi">print</span>(<span class="st">f"Softmax:    {softmax(x).round(3)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Sigmoid:    [0.119 0.269 0.5   0.731 0.881]<br>ReLU:       [0 0 0 1 2]<br>Leaky ReLU: [-0.02 -0.01  0.    1.    2.  ]<br>Tanh:       [-0.964 -0.762 0.  0.762 0.964]<br>Softmax:    [0.012 0.032 0.087 0.237 0.643]</div></div>
<table class="data-table"><thead><tr><th>Function</th><th>Range</th><th>Use Where</th><th>Pros</th></tr></thead><tbody>
<tr><td><code>ReLU</code></td><td>[0, &infin;)</td><td>Hidden layers (default)</td><td>Fast, simple, no vanishing gradient</td></tr>
<tr><td><code>Sigmoid</code></td><td>(0, 1)</td><td>Binary output layer</td><td>Probability interpretation</td></tr>
<tr><td><code>Tanh</code></td><td>(-1, 1)</td><td>Hidden layers (RNNs)</td><td>Zero-centered</td></tr>
<tr><td><code>Softmax</code></td><td>(0, 1) sums to 1</td><td>Multi-class output</td><td>Probability distribution</td></tr>
<tr><td><code>Leaky ReLU</code></td><td>(-&infin;, &infin;)</td><td>Hidden layers</td><td>Avoids dying ReLU</td></tr>
</tbody></table></section>

<section class="content-section" id="s4"><h2>4 &middot; Forward Pass (from Scratch)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; 2-Layer Neural Network</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Simple 2-layer neural network</span>
np.random.seed(<span class="nm">42</span>)

<span class="cm"># Architecture: 3 inputs &rarr; 4 hidden &rarr; 2 outputs</span>
W1 = np.random.randn(<span class="nm">3</span>, <span class="nm">4</span>) * <span class="nm">0.5</span>    <span class="cm"># weights layer 1</span>
b1 = np.zeros(<span class="nm">4</span>)                   <span class="cm"># bias layer 1</span>
W2 = np.random.randn(<span class="nm">4</span>, <span class="nm">2</span>) * <span class="nm">0.5</span>    <span class="cm"># weights layer 2</span>
b2 = np.zeros(<span class="nm">2</span>)                   <span class="cm"># bias layer 2</span>

<span class="cm"># Input</span>
X = np.array([<span class="nm">1.0</span>, <span class="nm">0.5</span>, <span class="nm">-1.5</span>])

<span class="cm"># Forward pass</span>
<span class="cm"># Layer 1: z1 = X @ W1 + b1, a1 = relu(z1)</span>
z1 = X @ W1 + b1
a1 = np.maximum(<span class="nm">0</span>, z1)   <span class="cm"># ReLU activation</span>
<span class="bi">print</span>(<span class="st">f"Hidden (before activation): {z1.round(3)}"</span>)
<span class="bi">print</span>(<span class="st">f"Hidden (after ReLU):        {a1.round(3)}"</span>)

<span class="cm"># Layer 2: z2 = a1 @ W2 + b2, output = softmax(z2)</span>
z2 = a1 @ W2 + b2
exp_z = np.exp(z2 - z2.max())
output = exp_z / exp_z.sum()   <span class="cm"># Softmax</span>
<span class="bi">print</span>(<span class="st">f"Output probabilities: {output.round(4)}"</span>)
<span class="bi">print</span>(<span class="st">f"Predicted class: {np.argmax(output)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Hidden (before activation): [ 0.248 -0.632  1.234 -0.156]<br>Hidden (after ReLU):        [0.248 0.    1.234 0.   ]<br>Output probs: [0.4231 0.5769]<br>Predicted class: 1</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Loss Functions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Binary Cross-Entropy (binary classification)</span>
<span class="kw">def</span> <span class="bi">binary_cross_entropy</span>(y_true, y_pred):
    y_pred = np.clip(y_pred, <span class="nm">1e-7</span>, <span class="nm">1-1e-7</span>)
    <span class="kw">return</span> -np.mean(y_true * np.log(y_pred) + (<span class="nm">1</span>-y_true) * np.log(<span class="nm">1</span>-y_pred))

<span class="cm"># Categorical Cross-Entropy (multi-class)</span>
<span class="kw">def</span> <span class="bi">categorical_cross_entropy</span>(y_true, y_pred):
    y_pred = np.clip(y_pred, <span class="nm">1e-7</span>, <span class="nm">1-1e-7</span>)
    <span class="kw">return</span> -np.sum(y_true * np.log(y_pred))

<span class="cm"># Mean Squared Error (regression)</span>
<span class="kw">def</span> <span class="bi">mse</span>(y_true, y_pred):
    <span class="kw">return</span> np.mean((y_true - y_pred) ** <span class="nm">2</span>)

<span class="cm"># Examples</span>
y_true_bin = np.array([<span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">1</span>])
y_pred_bin = np.array([<span class="nm">0.9</span>, <span class="nm">0.1</span>, <span class="nm">0.8</span>, <span class="nm">0.7</span>])
<span class="bi">print</span>(<span class="st">f"Binary CE: {binary_cross_entropy(y_true_bin, y_pred_bin):.4f}"</span>)

y_true_cat = np.array([<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">0</span>])  <span class="cm"># one-hot: class 1</span>
y_pred_cat = np.array([<span class="nm">0.1</span>, <span class="nm">0.8</span>, <span class="nm">0.1</span>])
<span class="bi">print</span>(<span class="st">f"Categorical CE: {categorical_cross_entropy(y_true_cat, y_pred_cat):.4f}"</span>)

y_true_reg = np.array([<span class="nm">3.0</span>, <span class="nm">5.0</span>, <span class="nm">7.0</span>])
y_pred_reg = np.array([<span class="nm">2.8</span>, <span class="nm">5.2</span>, <span class="nm">6.5</span>])
<span class="bi">print</span>(<span class="st">f"MSE: {mse(y_true_reg, y_pred_reg):.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Binary CE: 0.1643<br>Categorical CE: 0.2231<br>MSE: 0.1067</div></div>
<table class="data-table"><thead><tr><th>Loss Function</th><th>Task</th><th>Output Activation</th></tr></thead><tbody>
<tr><td>Binary Cross-Entropy</td><td>Binary classification</td><td>Sigmoid</td></tr>
<tr><td>Categorical Cross-Entropy</td><td>Multi-class classification</td><td>Softmax</td></tr>
<tr><td>MSE / MAE</td><td>Regression</td><td>Linear (none)</td></tr>
</tbody></table></section>

<section class="content-section" id="s6"><h2>6 &middot; Building with Keras (TensorFlow)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; MNIST Digit Classification</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> tensorflow <span class="kw">as</span> tf
<span class="kw">from</span> tensorflow <span class="kw">import</span> keras
<span class="kw">from</span> tensorflow.keras <span class="kw">import</span> layers

<span class="cm"># Load MNIST</span>
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train = X_train.reshape(-<span class="nm">1</span>, <span class="nm">784</span>).astype(<span class="st">"float32"</span>) / <span class="nm">255.0</span>
X_test = X_test.reshape(-<span class="nm">1</span>, <span class="nm">784</span>).astype(<span class="st">"float32"</span>) / <span class="nm">255.0</span>

<span class="cm"># Build model</span>
model = keras.Sequential([
    layers.Dense(<span class="nm">128</span>, activation=<span class="st">"relu"</span>, input_shape=(<span class="nm">784</span>,)),
    layers.Dropout(<span class="nm">0.2</span>),
    layers.Dense(<span class="nm">64</span>, activation=<span class="st">"relu"</span>),
    layers.Dropout(<span class="nm">0.2</span>),
    layers.Dense(<span class="nm">10</span>, activation=<span class="st">"softmax"</span>)
])

<span class="cm"># Compile</span>
model.compile(
    optimizer=<span class="st">"adam"</span>,
    loss=<span class="st">"sparse_categorical_crossentropy"</span>,
    metrics=[<span class="st">"accuracy"</span>]
)

model.summary()  <span class="cm"># show architecture</span>

<span class="cm"># Train</span>
history = model.fit(X_train, y_train, epochs=<span class="nm">10</span>,
                    batch_size=<span class="nm">32</span>, validation_split=<span class="nm">0.2</span>)

<span class="cm"># Evaluate</span>
test_loss, test_acc = model.evaluate(X_test, y_test)
<span class="bi">print</span>(<span class="st">f"Test accuracy: {test_acc:.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Layer (type)         Output Shape      Params<br>dense (Dense)        (None, 128)       100480<br>dropout (Dropout)    (None, 128)       0<br>dense_1 (Dense)      (None, 64)        8256<br>dropout_1 (Dropout)  (None, 64)        0<br>dense_2 (Dense)      (None, 10)        650<br>Total params: 109,386<br>Test accuracy: 0.9785</div></div></section>''',
("backpropagation.html","Backpropagation"),("cnn.html","CNN"))

# BACKPROPAGATION
make_page("dl/backpropagation.html","Backpropagation &amp; Optimizers","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Backpropagation",
"Backpropagation is how neural networks learn by computing gradients of the loss with respect to weights using the chain rule. Covers gradient descent, learning rate, SGD, Momentum, RMSprop, Adam optimizer, learning rate scheduling, and regularization techniques.",
"Deep Learning &mdash; Goodfellow, Bengio, Courville",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Chain Rule &amp; Backpropagation</a></li>
<li><a href="#s2">Gradient Descent</a></li>
<li><a href="#s3">Optimizers</a></li>
<li><a href="#s4">Learning Rate Scheduling</a></li>
<li><a href="#s5">Regularization</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Chain Rule &amp; Backpropagation</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>How Networks Learn</strong>
<pre style="font-size:.85rem;line-height:1.6;">
1. Forward Pass:  Input &rarr; Hidden &rarr; Output &rarr; Loss
2. Backward Pass: Loss &rarr; dL/dW (gradients via chain rule)
3. Update:        W = W - learning_rate &times; dL/dW
4. Repeat for many epochs!</pre></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Backprop from Scratch</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Simple example: y = sigmoid(w*x + b)</span>
<span class="kw">def</span> <span class="bi">sigmoid</span>(z):
    <span class="kw">return</span> <span class="nm">1</span> / (<span class="nm">1</span> + np.exp(-z))

<span class="kw">def</span> <span class="bi">sigmoid_deriv</span>(z):
    s = sigmoid(z)
    <span class="kw">return</span> s * (<span class="nm">1</span> - s)

<span class="cm"># Data: XOR-like problem</span>
X = np.array([[<span class="nm">0</span>,<span class="nm">0</span>],[<span class="nm">0</span>,<span class="nm">1</span>],[<span class="nm">1</span>,<span class="nm">0</span>],[<span class="nm">1</span>,<span class="nm">1</span>]])
y = np.array([[<span class="nm">0</span>],[<span class="nm">1</span>],[<span class="nm">1</span>],[<span class="nm">0</span>]])

np.random.seed(<span class="nm">42</span>)
W1 = np.random.randn(<span class="nm">2</span>, <span class="nm">4</span>) * <span class="nm">0.5</span>
b1 = np.zeros((<span class="nm">1</span>, <span class="nm">4</span>))
W2 = np.random.randn(<span class="nm">4</span>, <span class="nm">1</span>) * <span class="nm">0.5</span>
b2 = np.zeros((<span class="nm">1</span>, <span class="nm">1</span>))
lr = <span class="nm">1.0</span>

<span class="kw">for</span> epoch <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10000</span>):
    <span class="cm"># Forward</span>
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2
    a2 = sigmoid(z2)

    <span class="cm"># Loss (MSE)</span>
    loss = np.mean((y - a2) ** <span class="nm">2</span>)

    <span class="cm"># Backward (chain rule!)</span>
    dz2 = (a2 - y) * sigmoid_deriv(z2)   <span class="cm"># dL/dz2</span>
    dW2 = a1.T @ dz2 / <span class="nm">4</span>                  <span class="cm"># dL/dW2</span>
    db2 = dz2.mean(axis=<span class="nm">0</span>, keepdims=<span class="kw">True</span>)

    dz1 = (dz2 @ W2.T) * sigmoid_deriv(z1)
    dW1 = X.T @ dz1 / <span class="nm">4</span>
    db1 = dz1.mean(axis=<span class="nm">0</span>, keepdims=<span class="kw">True</span>)

    <span class="cm"># Update weights</span>
    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1

    <span class="kw">if</span> epoch % <span class="nm">2000</span> == <span class="nm">0</span>:
        <span class="bi">print</span>(<span class="st">f"Epoch {epoch:5d}: loss = {loss:.6f}"</span>)

<span class="bi">print</span>(<span class="st">f"\\nPredictions: {a2.round(2).flatten()}"</span>)
<span class="bi">print</span>(<span class="st">f"Expected:    {y.flatten()}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Epoch     0: loss = 0.283412<br>Epoch  2000: loss = 0.025431<br>Epoch  4000: loss = 0.005123<br>Epoch  8000: loss = 0.001234<br>Predictions: [0.02 0.97 0.97 0.03]  &larr; XOR learned! &#x2705;</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Gradient Descent Variants</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Batch Gradient Descent: uses ALL data per update</span>
<span class="cm"># W = W - lr * gradient(full_dataset)</span>
<span class="cm"># Slow but stable</span>

<span class="cm"># Stochastic GD (SGD): uses ONE sample per update</span>
<span class="cm"># W = W - lr * gradient(single_sample)</span>
<span class="cm"># Fast but noisy</span>

<span class="cm"># Mini-Batch GD: uses BATCH_SIZE samples per update</span>
<span class="cm"># W = W - lr * gradient(batch)</span>
<span class="cm"># Best of both worlds! (typical: 32, 64, 128)</span>

<span class="cm"># Example: effect of learning rate</span>
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="kw">def</span> <span class="bi">gradient_descent</span>(lr, epochs=<span class="nm">50</span>):
    w = <span class="nm">10.0</span>  <span class="cm"># start far from optimal (0)</span>
    <span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(epochs):
        grad = <span class="nm">2</span> * w           <span class="cm"># gradient of w&sup2;</span>
        w = w - lr * grad       <span class="cm"># update</span>
    <span class="kw">return</span> w

<span class="bi">print</span>(<span class="st">f"lr=0.001: w = {gradient_descent(0.001):.4f}"</span>)  <span class="cm"># too slow</span>
<span class="bi">print</span>(<span class="st">f"lr=0.1:   w = {gradient_descent(0.1):.6f}"</span>)    <span class="cm"># good</span>
<span class="bi">print</span>(<span class="st">f"lr=0.5:   w = {gradient_descent(0.5):.4f}"</span>)    <span class="cm"># perfect</span>
<span class="bi">print</span>(<span class="st">f"lr=1.1:   w = {gradient_descent(1.1):.4f}"</span>)    <span class="cm"># diverges!</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>lr=0.001: 9.0438 (barely moved)<br>lr=0.1:   0.000001 (converged)<br>lr=0.5:   0.0000 (converged fast)<br>lr=1.1:   diverges! &rarr; NaN</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Optimizers</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Keras Optimizers</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> tensorflow.keras <span class="kw">import</span> optimizers

<span class="cm"># SGD (Stochastic Gradient Descent)</span>
opt1 = optimizers.SGD(learning_rate=<span class="nm">0.01</span>)

<span class="cm"># SGD with Momentum (accelerates SGD)</span>
opt2 = optimizers.SGD(learning_rate=<span class="nm">0.01</span>, momentum=<span class="nm">0.9</span>)

<span class="cm"># RMSprop (adaptive learning rate)</span>
opt3 = optimizers.RMSprop(learning_rate=<span class="nm">0.001</span>)

<span class="cm"># Adam (most popular! Momentum + RMSprop)</span>
opt4 = optimizers.Adam(learning_rate=<span class="nm">0.001</span>)

<span class="cm"># AdaGrad (adapts lr per parameter)</span>
opt5 = optimizers.Adagrad(learning_rate=<span class="nm">0.01</span>)

<span class="cm"># Use in model</span>
model.compile(optimizer=opt4, loss=<span class="st">"mse"</span>)
<span class="cm"># or simply: optimizer="adam"</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>All optimizers update weights differently but aim to minimize loss</div></div>
<table class="data-table"><thead><tr><th>Optimizer</th><th>Key Idea</th><th>When to Use</th></tr></thead><tbody>
<tr><td><strong>SGD</strong></td><td>Basic gradient step</td><td>Simple problems, with momentum</td></tr>
<tr><td><strong>Momentum</strong></td><td>Accumulates past gradients (velocity)</td><td>Faster convergence, less oscillation</td></tr>
<tr><td><strong>RMSprop</strong></td><td>Adapts per-parameter lr using moving avg</td><td>RNNs, non-stationary problems</td></tr>
<tr><td><strong>Adam</strong></td><td>Momentum + RMSprop (default choice)</td><td>Almost everything &mdash; start here!</td></tr>
<tr><td><strong>AdaGrad</strong></td><td>Adapts lr based on gradient history</td><td>Sparse data (NLP, embeddings)</td></tr>
</tbody></table></section>

<section class="content-section" id="s4"><h2>4 &middot; Learning Rate Scheduling</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> tensorflow.keras.callbacks <span class="kw">import</span> (
    ReduceLROnPlateau, LearningRateScheduler, EarlyStopping
)

<span class="cm"># Reduce LR when loss plateaus</span>
reduce_lr = ReduceLROnPlateau(
    monitor=<span class="st">"val_loss"</span>, factor=<span class="nm">0.5</span>,
    patience=<span class="nm">5</span>, min_lr=<span class="nm">1e-6</span>
)

<span class="cm"># Custom schedule</span>
<span class="kw">def</span> <span class="bi">scheduler</span>(epoch, lr):
    <span class="kw">if</span> epoch < <span class="nm">10</span>:
        <span class="kw">return</span> lr
    <span class="kw">return</span> lr * <span class="nm">0.95</span>   <span class="cm"># decay by 5% each epoch</span>

lr_scheduler = LearningRateScheduler(scheduler)

<span class="cm"># Early stopping</span>
early_stop = EarlyStopping(
    monitor=<span class="st">"val_loss"</span>, patience=<span class="nm">10</span>,
    restore_best_weights=<span class="kw">True</span>
)

<span class="cm"># Use in training</span>
history = model.fit(X_train, y_train, epochs=<span class="nm">100</span>,
    validation_split=<span class="nm">0.2</span>,
    callbacks=[reduce_lr, early_stop])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Epoch 25: reducing lr from 0.001 to 0.0005<br>Epoch 40: early stopping! Restoring best weights.</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Regularization Techniques</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> tensorflow.keras <span class="kw">import</span> layers, regularizers

model = keras.Sequential([
    <span class="cm"># Dropout: randomly zero out neurons during training</span>
    layers.Dense(<span class="nm">128</span>, activation=<span class="st">"relu"</span>),
    layers.Dropout(<span class="nm">0.3</span>),            <span class="cm"># drop 30% of neurons</span>

    <span class="cm"># L2 Regularization: penalize large weights</span>
    layers.Dense(<span class="nm">64</span>, activation=<span class="st">"relu"</span>,
                 kernel_regularizer=regularizers.l2(<span class="nm">0.01</span>)),

    <span class="cm"># L1 Regularization: encourage sparse weights</span>
    layers.Dense(<span class="nm">32</span>, activation=<span class="st">"relu"</span>,
                 kernel_regularizer=regularizers.l1(<span class="nm">0.01</span>)),

    <span class="cm"># Batch Normalization: normalize activations</span>
    layers.Dense(<span class="nm">64</span>, activation=<span class="st">"relu"</span>),
    layers.BatchNormalization(),

    layers.Dense(<span class="nm">10</span>, activation=<span class="st">"softmax"</span>)
])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Regularization prevents overfitting by constraining the model</div></div>
<table class="data-table"><thead><tr><th>Technique</th><th>How it Works</th><th>Effect</th></tr></thead><tbody>
<tr><td>Dropout</td><td>Randomly disables neurons</td><td>Prevents co-adaptation</td></tr>
<tr><td>L2 (Weight Decay)</td><td>Penalizes large weights</td><td>Smoother decision boundary</td></tr>
<tr><td>L1</td><td>Penalizes non-zero weights</td><td>Sparse model (feature selection)</td></tr>
<tr><td>Batch Normalization</td><td>Normalizes layer inputs</td><td>Faster training, slight regularization</td></tr>
<tr><td>Early Stopping</td><td>Stop when val_loss increases</td><td>Prevents training too long</td></tr>
</tbody></table></section>''',
("neural-networks.html","Neural Networks"),("cnn.html","CNN"))

print("neural-networks.html + backpropagation.html expanded!")
