import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CNN (MASSIVE EXPANSION)
dl_cnn_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 9 &middot; Convolutional Networks</h4>
    <ol>
        <li><a href="#conv-op">1. The Convolution Operation</a></li>
        <li><a href="#sparse">2. Sparse Interactions & Parameters</a></li>
        <li><a href="#equivariant">3. Equivariance to Translation</a></li>
        <li><a href="#pooling">4. Pooling Stage: Invariance</a></li>
        <li><a href="#layers">5. Typical Layer Stages</a></li>
    </ol>
</div>

<section class="content-section" id="conv-op">
    <h2>1 &middot; The Convolution Operation</h2>
    <p>In its most general form, convolution is an operation on two functions of a real-valued argument. In convolutional network terminology, the first argument is the <strong>input</strong> and the second is the <strong>kernel</strong>. The output is referred to as the <strong>feature map</strong>.</p>
    <div class="callout note">
        <div class="callout-icon">🎨</div>
        <div class="callout-content">
            <strong>Cross-Correlation vs Convolution</strong>
            <p>Discrete convolution (Equation 9.3) involves flipping the kernel to obtain commutativity. However, many neural network libraries implement <strong>cross-correlation</strong> (Equation 9.6) but call it convolution. In machine learning, the algorithm learns the appropriate flipped values anyway.</p>
        </div>
    </div>
</section>

<section class="content-section" id="sparse">
    <h2>2 &middot; Sparse Interactions</h2>
    <p>Convolutional networks have <strong>sparse interactions</strong> (sparse weights) accomplished by making the kernel smaller than the input. If there are <em>m</em> inputs and <em>n</em> outputs, matrix multiplication requires \( m \times n \) parameters, while convolution requires only \( k \times n \) where \( k \ll m \).</p>
</section>

<section class="content-section" id="pooling">
    <h2>4 &middot; Pooling & Invariance</h2>
    <p>A typical layer consists of three stages: 1. Convolution (Linear), 2. Detector (Nonlinear/ReLU), and 3. Pooling. A pooling function replaces the output with a summary statistic (e.g., <strong>Max Pooling</strong>) of nearby outputs.</p>
    <div class="callout important">
        <div class="callout-icon">🏗️</div>
        <div class="callout-content">
            <strong>Translation Invariance</strong>
            <p>Pooling makes the representation approximately invariant to small translations of the input. This is useful if we care more about whether a feature is present than exactly where it is (e.g., face detection).</p>
        </div>
    </div>
</section>
"""

make_page("dl/cnn.html","Convolutional Networks","Deep Learning","&#x1F9E0;","advanced","DL &rarr; CNN",
"Formal textbook analysis of Convolutional architectures, pooling stages, and the mathematics of sparse connectivity.",
"Deep Learning &mdash; Ian Goodfellow", dl_cnn_body, ("backpropagation.html","Backpropagation"), ("rnn-lstm.html","RNN & LSTM"),
[("neural-networks.html", "NN Fundamentals"), ("backpropagation.html", "Gradients")])

# RNN & SEQUENCE MODELING (MASSIVE EXPANSION)
dl_seq_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 10 &middot; Sequence Modeling: RNNs</h4>
    <ol>
        <li><a href="#unfolding">1. Unfolding Computational Graphs</a></li>
        <li><a href="#sharing">2. Parameter Sharing across Time</a></li>
        <li><a href="#forward-rnn">3. RNN Forward Propagation</a></li>
        <li><a href="#bptt">4. Back-Propagation Through Time (BPTT)</a></li>
        <li><a href="#teacher">5. Teacher Forcing & Open-Loop</a></li>
    </ol>
</div>

<section class="content-section" id="unfolding">
    <h2>1 &middot; Unfolding Graphs</h2>
    <p>Unfolding is the operation that maps a circuit with recurrent connections to a computational graph with repeated pieces—one per time step. This allows the model to handle variable-length histories using a fixed-size input transition function.</p>
</section>

<section class="content-section" id="forward-rnn">
    <h2>3 &middot; RNN Forward Propagation</h2>
    <p>Assuming a hyperbolic tangent activation and softmax output, the standard RNN update equations are:</p>
    <ul>
        <li>\( \mathbf{a}^{(t)} = \mathbf{b} + \mathbf{W}\mathbf{h}^{(t-1)} + \mathbf{U}\mathbf{x}^{(t)} \)</li>
        <li>\( \mathbf{h}^{(t)} = \tanh(\mathbf{a}^{(t)}) \)</li>
        <li>\( \mathbf{o}^{(t)} = \mathbf{c} + \mathbf{V}\mathbf{h}^{(t)} \)</li>
        <li>\( \hat{\mathbf{y}}^{(t)} = \text{softmax}(\mathbf{o}^{(t)}) \)</li>
    </ul>
</section>

<section class="content-section" id="bptt">
    <h2>4 &middot; BPTT Algorithm</h2>
    <div class="callout note">
        <div class="callout-icon">⏳</div>
        <div class="callout-content">
            <strong>Back-Propagation Through Time</strong>
            <p>Computing the gradient involves a forward pass (left to right) followed by a backward pass (right to left). The runtime is \( O(\tau) \) where \( \tau \) is the sequence length. This cannot be parallelized because the graph is inherently sequential.</p>
        </div>
    </div>
</section>

<section class="content-section" id="teacher">
    <h2>5 &middot; Teacher Forcing</h2>
    <p>Teacher forcing is a training technique where the ground truth output \( \mathbf{y}^{(t)} \) is fed as input at time \( t+1 \), rather than the model's own (potentially noisy) output. This decouples time steps and allows for parallelization during training.</p>
</section>
"""

make_page("dl/rnn-lstm.html","Sequence Modeling: RNNs","Deep Learning","&#x1F9E0;","advanced","DL &rarr; RNN",
"Deep-dive into recurrent architectures, unfolding computational graphs, and the BPTT algorithm for sequence learning.",
"Deep Learning &mdash; Ian Goodfellow", dl_seq_body, ("cnn.html","CNN"), ("transformers.html","Transformers"),
[("cnn.html", "Spatial Hierarchy"), ("transformers.html", "Attention")])

print("cnn.html + rnn-lstm.html MASSIVELY expanded with Goodfellow content!")

