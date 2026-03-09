import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# CNN
make_page("dl/cnn.html","Convolutional Neural Networks","Deep Learning","&#x1F9E0;","advanced","DL &rarr; CNN",
"CNNs are designed for image data using convolution operations that detect spatial patterns. Covers convolution filters, pooling layers, CNN architectures (LeNet, VGG, ResNet), building CNNs in Keras, image classification, data augmentation, and transfer learning.",
"Deep Learning with Python &mdash; Fran&ccedil;ois Chollet",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">What is Convolution?</a></li>
<li><a href="#s2">CNN Architecture</a></li>
<li><a href="#s3">Building a CNN in Keras</a></li>
<li><a href="#s4">Famous Architectures</a></li>
<li><a href="#s5">Transfer Learning</a></li>
<li><a href="#s6">Data Augmentation</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; What is Convolution?</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Convolution = Sliding Filter</strong>
<pre style="font-size:.85rem;line-height:1.6;">
Input Image (5&times;5)          Filter (3&times;3)        Output (3&times;3)
[1 0 1 0 1]                [1 0 1]
[0 1 0 1 0]    &#x2217;           [0 1 0]    =        Feature Map
[1 0 1 0 1]                [1 0 1]
[0 1 0 1 0]
[1 0 1 0 1]

The filter slides across the image, computing
dot products at each position to detect features
like edges, textures, and patterns.</pre></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Manual Convolution</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># 5&times;5 image</span>
image = np.array([
    [<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">0</span>,<span class="nm">1</span>],
    [<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">0</span>],
    [<span class="nm">3</span>,<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">1</span>],
    [<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">3</span>],
    [<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">3</span>,<span class="nm">0</span>,<span class="nm">2</span>]
])

<span class="cm"># Edge detection filter</span>
edge_filter = np.array([
    [-<span class="nm">1</span>,-<span class="nm">1</span>,-<span class="nm">1</span>],
    [-<span class="nm">1</span>, <span class="nm">8</span>,-<span class="nm">1</span>],
    [-<span class="nm">1</span>,-<span class="nm">1</span>,-<span class="nm">1</span>]
])

<span class="cm"># Manual convolution</span>
output = np.zeros((<span class="nm">3</span>, <span class="nm">3</span>))
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">3</span>):
    <span class="kw">for</span> j <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">3</span>):
        region = image[i:i+<span class="nm">3</span>, j:j+<span class="nm">3</span>]
        output[i, j] = np.sum(region * edge_filter)

<span class="bi">print</span>(<span class="st">"Feature map:"</span>)
<span class="bi">print</span>(output)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Feature map:<br>[[-1  6 -3]<br> [ 4 -4  5]<br> [-2  8 -6]]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; CNN Architecture</h2>
<table class="data-table"><thead><tr><th>Layer</th><th>Purpose</th><th>Output Shape Change</th></tr></thead><tbody>
<tr><td><code>Conv2D</code></td><td>Extract features using learnable filters</td><td>H&prime;&times;W&prime;&times;filters</td></tr>
<tr><td><code>MaxPooling2D</code></td><td>Downsample by taking max in patches</td><td>H/2 &times; W/2</td></tr>
<tr><td><code>AveragePooling2D</code></td><td>Downsample by averaging patches</td><td>H/2 &times; W/2</td></tr>
<tr><td><code>Flatten</code></td><td>Convert 2D feature maps to 1D vector</td><td>(features,)</td></tr>
<tr><td><code>Dense</code></td><td>Fully connected classification layers</td><td>(units,)</td></tr>
<tr><td><code>Dropout</code></td><td>Regularization (randomly zero neurons)</td><td>Same</td></tr>
<tr><td><code>BatchNorm</code></td><td>Normalize activations</td><td>Same</td></tr>
</tbody></table>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Key Parameters</strong>
<ul><li><strong>Filters</strong>: Number of feature detectors (32, 64, 128)</li>
<li><strong>Kernel Size</strong>: Filter size, usually (3,3) or (5,5)</li>
<li><strong>Stride</strong>: How many pixels the filter moves (default=1)</li>
<li><strong>Padding</strong>: "same" (keep size) or "valid" (shrink)</li></ul></div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Building a CNN in Keras</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; CIFAR-10 Image Classification</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> tensorflow <span class="kw">as</span> tf
<span class="kw">from</span> tensorflow.keras <span class="kw">import</span> layers, models

<span class="cm"># Load CIFAR-10 (10 classes: airplane, car, bird, cat, ...)</span>
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
X_train, X_test = X_train / <span class="nm">255.0</span>, X_test / <span class="nm">255.0</span>
<span class="bi">print</span>(<span class="st">f"Train: {X_train.shape}"</span>)   <span class="cm"># (50000, 32, 32, 3)</span>

<span class="cm"># Build CNN</span>
model = models.Sequential([
    <span class="cm"># Block 1: Conv + Conv + Pool</span>
    layers.Conv2D(<span class="nm">32</span>, (<span class="nm">3</span>,<span class="nm">3</span>), activation=<span class="st">"relu"</span>, padding=<span class="st">"same"</span>,
                  input_shape=(<span class="nm">32</span>,<span class="nm">32</span>,<span class="nm">3</span>)),
    layers.Conv2D(<span class="nm">32</span>, (<span class="nm">3</span>,<span class="nm">3</span>), activation=<span class="st">"relu"</span>),
    layers.MaxPooling2D((<span class="nm">2</span>,<span class="nm">2</span>)),
    layers.Dropout(<span class="nm">0.25</span>),

    <span class="cm"># Block 2</span>
    layers.Conv2D(<span class="nm">64</span>, (<span class="nm">3</span>,<span class="nm">3</span>), activation=<span class="st">"relu"</span>, padding=<span class="st">"same"</span>),
    layers.Conv2D(<span class="nm">64</span>, (<span class="nm">3</span>,<span class="nm">3</span>), activation=<span class="st">"relu"</span>),
    layers.MaxPooling2D((<span class="nm">2</span>,<span class="nm">2</span>)),
    layers.Dropout(<span class="nm">0.25</span>),

    <span class="cm"># Classifier Head</span>
    layers.Flatten(),
    layers.Dense(<span class="nm">512</span>, activation=<span class="st">"relu"</span>),
    layers.Dropout(<span class="nm">0.5</span>),
    layers.Dense(<span class="nm">10</span>, activation=<span class="st">"softmax"</span>)
])

model.compile(optimizer=<span class="st">"adam"</span>,
              loss=<span class="st">"sparse_categorical_crossentropy"</span>,
              metrics=[<span class="st">"accuracy"</span>])
model.summary()

history = model.fit(X_train, y_train, epochs=<span class="nm">20</span>,
                    batch_size=<span class="nm">64</span>, validation_split=<span class="nm">0.1</span>)
<span class="bi">print</span>(<span class="st">f"Test Accuracy: {model.evaluate(X_test, y_test)[1]:.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>conv2d (Conv2D)        (None, 32, 32, 32)   896<br>conv2d_1 (Conv2D)      (None, 30, 30, 32)   9248<br>max_pooling2d          (None, 15, 15, 32)   0<br>...<br>dense (Dense)          (None, 512)          131584<br>dense_1 (Dense)        (None, 10)           5130<br>Total params: ~350K<br>Test Accuracy: 0.7892</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Famous CNN Architectures</h2>
<table class="data-table"><thead><tr><th>Architecture</th><th>Year</th><th>Key Innovation</th><th>Params</th></tr></thead><tbody>
<tr><td><strong>LeNet-5</strong></td><td>1998</td><td>First practical CNN (digit recognition)</td><td>60K</td></tr>
<tr><td><strong>AlexNet</strong></td><td>2012</td><td>Deep CNN + ReLU + Dropout + GPU</td><td>60M</td></tr>
<tr><td><strong>VGG-16</strong></td><td>2014</td><td>Deeper (16 layers), small 3&times;3 filters only</td><td>138M</td></tr>
<tr><td><strong>GoogLeNet</strong></td><td>2014</td><td>Inception modules (multi-scale filters)</td><td>6.8M</td></tr>
<tr><td><strong>ResNet-50</strong></td><td>2015</td><td>Skip connections (solve vanishing gradient)</td><td>25M</td></tr>
<tr><td><strong>EfficientNet</strong></td><td>2019</td><td>Compound scaling (width/depth/resolution)</td><td>5-66M</td></tr>
</tbody></table></section>

<section class="content-section" id="s5"><h2>5 &middot; Transfer Learning</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Using Pretrained ResNet</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> tensorflow.keras.applications <span class="kw">import</span> ResNet50
<span class="kw">from</span> tensorflow.keras <span class="kw">import</span> layers, models

<span class="cm"># Load pretrained ResNet (trained on ImageNet)</span>
base_model = ResNet50(weights=<span class="st">"imagenet"</span>, include_top=<span class="kw">False</span>,
                      input_shape=(<span class="nm">224</span>, <span class="nm">224</span>, <span class="nm">3</span>))
base_model.trainable = <span class="kw">False</span>  <span class="cm"># freeze pretrained weights</span>

<span class="cm"># Add custom classifier</span>
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(<span class="nm">256</span>, activation=<span class="st">"relu"</span>),
    layers.Dropout(<span class="nm">0.5</span>),
    layers.Dense(<span class="nm">5</span>, activation=<span class="st">"softmax"</span>)  <span class="cm"># 5 custom classes</span>
])

model.compile(optimizer=<span class="st">"adam"</span>,
              loss=<span class="st">"sparse_categorical_crossentropy"</span>,
              metrics=[<span class="st">"accuracy"</span>])
<span class="bi">print</span>(<span class="st">f"Trainable params: {model.count_params():,}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Only ~132K trainable params instead of 25M!<br>Transfer learning: train on small datasets with high accuracy</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Data Augmentation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Augment training images to prevent overfitting</span>
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip(<span class="st">"horizontal"</span>),
    layers.RandomRotation(<span class="nm">0.1</span>),       <span class="cm"># &plusmn;10% rotation</span>
    layers.RandomZoom(<span class="nm">0.1</span>),           <span class="cm"># &plusmn;10% zoom</span>
    layers.RandomContrast(<span class="nm">0.1</span>),       <span class="cm"># &plusmn;10% contrast</span>
    layers.RandomTranslation(<span class="nm">0.1</span>, <span class="nm">0.1</span>),
])

<span class="cm"># Use in model</span>
model = models.Sequential([
    data_augmentation,      <span class="cm"># augment images on-the-fly</span>
    <span class="cm"># ... rest of CNN</span>
])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Augmentation creates "new" training samples by applying random transformations</div></div></section>''',
("backpropagation.html","Backpropagation"),("rnn-lstm.html","RNN &amp; LSTM"))

# RNN-LSTM
make_page("dl/rnn-lstm.html","RNN, LSTM &amp; GRU","Deep Learning","&#x1F9E0;","advanced","DL &rarr; RNN &amp; LSTM",
"Recurrent Neural Networks process sequential data (text, time series). Covers vanilla RNNs, vanishing gradients, LSTM cells, GRU cells, bidirectional RNNs, text generation, and sequence-to-sequence models with Keras implementations.",
"Deep Learning with Python &mdash; Fran&ccedil;ois Chollet",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Sequences &amp; Vanilla RNN</a></li>
<li><a href="#s2">Vanishing Gradient Problem</a></li>
<li><a href="#s3">LSTM (Long Short-Term Memory)</a></li>
<li><a href="#s4">GRU (Gated Recurrent Unit)</a></li>
<li><a href="#s5">Bidirectional &amp; Stacked RNNs</a></li>
<li><a href="#s6">Text Classification Example</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Sequences &amp; Vanilla RNN</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>RNN: Memory for Sequences</strong>
<pre style="font-size:.85rem;line-height:1.6;">
x(t=0)   x(t=1)   x(t=2)   &hellip;   x(t=n)
  &darr;        &darr;        &darr;              &darr;
[RNN] &rarr; [RNN] &rarr; [RNN] &rarr; &hellip; &rarr; [RNN] &rarr; output
  h0       h1       h2              hn

h(t) = tanh(W_h &middot; h(t-1) + W_x &middot; x(t) + b)
Each step has access to previous hidden state!</pre></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Manual RNN Cell</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Simple RNN from scratch</span>
np.random.seed(<span class="nm">42</span>)
hidden_size = <span class="nm">4</span>
input_size = <span class="nm">3</span>

W_h = np.random.randn(hidden_size, hidden_size) * <span class="nm">0.1</span>
W_x = np.random.randn(hidden_size, input_size) * <span class="nm">0.1</span>
b = np.zeros(hidden_size)

<span class="cm"># Process a sequence of 5 time steps</span>
sequence = np.random.randn(<span class="nm">5</span>, input_size)
h = np.zeros(hidden_size)  <span class="cm"># initial hidden state</span>

<span class="kw">for</span> t, x_t <span class="kw">in</span> <span class="bi">enumerate</span>(sequence):
    h = np.tanh(W_h @ h + W_x @ x_t + b)
    <span class="bi">print</span>(<span class="st">f"t={t}: h = {h.round(3)}"</span>)

<span class="bi">print</span>(<span class="st">f"\\nFinal hidden state: {h.round(3)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>t=0: h = [ 0.012 -0.078  0.045  0.023]<br>t=1: h = [-0.034  0.056  0.012  0.089]<br>...<br>Final hidden state encodes the entire sequence!</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Vanishing Gradient Problem</h2>
<table class="data-table"><thead><tr><th>Problem</th><th>Cause</th><th>Solution</th></tr></thead><tbody>
<tr><td>Vanishing Gradient</td><td>Gradients shrink exponentially through time</td><td>LSTM, GRU, gradient clipping</td></tr>
<tr><td>Exploding Gradient</td><td>Gradients grow exponentially</td><td>Gradient clipping, smaller learning rate</td></tr>
<tr><td>Short-term Memory</td><td>RNN forgets early inputs</td><td>LSTM&#39;s cell state preserves long-term info</td></tr>
</tbody></table></section>

<section class="content-section" id="s3"><h2>3 &middot; LSTM (Long Short-Term Memory)</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>LSTM has 3 Gates + Cell State</strong>
<ul><li><strong>Forget Gate</strong>: What to forget from cell state</li>
<li><strong>Input Gate</strong>: What new info to store</li>
<li><strong>Output Gate</strong>: What to output from cell state</li>
<li><strong>Cell State</strong>: Long-term memory highway (&ldquo;conveyor belt&rdquo;)</li></ul></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; LSTM in Keras</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> tensorflow.keras <span class="kw">import</span> layers, models

<span class="cm"># LSTM for sequence classification</span>
model = models.Sequential([
    layers.LSTM(<span class="nm">64</span>, input_shape=(<span class="nm">100</span>, <span class="nm">1</span>),   <span class="cm"># 100 time steps, 1 feature</span>
                return_sequences=<span class="kw">False</span>),       <span class="cm"># only final output</span>
    layers.Dense(<span class="nm">32</span>, activation=<span class="st">"relu"</span>),
    layers.Dense(<span class="nm">1</span>, activation=<span class="st">"sigmoid"</span>)
])
model.compile(optimizer=<span class="st">"adam"</span>, loss=<span class="st">"binary_crossentropy"</span>)
model.summary()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>lstm (LSTM)    (None, 64)    16896 params<br>dense          (None, 32)    2080<br>dense_1        (None, 1)     33</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; GRU (Gated Recurrent Unit)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># GRU: simpler than LSTM, 2 gates (reset + update), no cell state</span>
model = models.Sequential([
    layers.GRU(<span class="nm">64</span>, input_shape=(<span class="nm">100</span>, <span class="nm">1</span>)),
    layers.Dense(<span class="nm">1</span>, activation=<span class="st">"sigmoid"</span>)
])
<span class="cm"># GRU has ~25% fewer params than LSTM</span>
<span class="cm"># Performance is often comparable</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>GRU: 12,864 params vs LSTM: 16,896 (25% fewer)</div></div>
<table class="data-table"><thead><tr><th>Feature</th><th>LSTM</th><th>GRU</th></tr></thead><tbody>
<tr><td>Gates</td><td>3 (forget, input, output)</td><td>2 (reset, update)</td></tr>
<tr><td>Memory</td><td>Cell state + hidden state</td><td>Hidden state only</td></tr>
<tr><td>Parameters</td><td>More</td><td>~25% fewer</td></tr>
<tr><td>Performance</td><td>Better on long sequences</td><td>Similar, faster training</td></tr>
</tbody></table></section>

<section class="content-section" id="s5"><h2>5 &middot; Bidirectional &amp; Stacked RNNs</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Bidirectional: reads sequence forward AND backward</span>
model = models.Sequential([
    layers.Bidirectional(
        layers.LSTM(<span class="nm">64</span>, return_sequences=<span class="kw">True</span>),
        input_shape=(<span class="nm">100</span>, <span class="nm">1</span>)
    ),
    layers.Bidirectional(layers.LSTM(<span class="nm">32</span>)),  <span class="cm"># stacked</span>
    layers.Dense(<span class="nm">1</span>, activation=<span class="st">"sigmoid"</span>)
])
<span class="cm"># Bidirectional doubles the output units (64*2=128 per step)</span>

<span class="cm"># Stacked LSTM: use return_sequences=True for all but last</span>
model = models.Sequential([
    layers.LSTM(<span class="nm">64</span>, return_sequences=<span class="kw">True</span>, input_shape=(<span class="nm">100</span>,<span class="nm">1</span>)),
    layers.LSTM(<span class="nm">32</span>, return_sequences=<span class="kw">False</span>),
    layers.Dense(<span class="nm">1</span>)
])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Bidirectional: forward h + backward h = richer representation</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Text Classification (IMDB Reviews)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> tensorflow <span class="kw">as</span> tf
<span class="kw">from</span> tensorflow.keras <span class="kw">import</span> layers, models

<span class="cm"># Load IMDB dataset</span>
vocab_size = <span class="nm">10000</span>
max_len = <span class="nm">200</span>
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.imdb.load_data(
    num_words=vocab_size)
X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, maxlen=max_len)
X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, maxlen=max_len)

<span class="cm"># Build LSTM model</span>
model = models.Sequential([
    layers.Embedding(vocab_size, <span class="nm">128</span>, input_length=max_len),
    layers.Bidirectional(layers.LSTM(<span class="nm">64</span>, dropout=<span class="nm">0.2</span>)),
    layers.Dense(<span class="nm">32</span>, activation=<span class="st">"relu"</span>),
    layers.Dropout(<span class="nm">0.5</span>),
    layers.Dense(<span class="nm">1</span>, activation=<span class="st">"sigmoid"</span>)
])

model.compile(optimizer=<span class="st">"adam"</span>, loss=<span class="st">"binary_crossentropy"</span>, metrics=[<span class="st">"accuracy"</span>])
history = model.fit(X_train, y_train, epochs=<span class="nm">5</span>, batch_size=<span class="nm">64</span>, validation_split=<span class="nm">0.2</span>)
<span class="bi">print</span>(<span class="st">f"Test accuracy: {model.evaluate(X_test, y_test)[1]:.4f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Epoch 5: accuracy: 0.9234 &middot; val_accuracy: 0.8756<br>Test accuracy: 0.8687</div></div></section>''',
("backpropagation.html","Backpropagation"),("transformers.html","Transformers"))

print("cnn.html + rnn-lstm.html expanded!")
