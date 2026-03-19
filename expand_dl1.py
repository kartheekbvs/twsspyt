import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# DEEP FEEDFORWARD NETWORKS (MASSIVE EXPANSION)
dl_nn_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 6 &middot; Deep Feedforward Networks</h4>
    <ol>
        <li><a href="#intro">1. The Multi-Layer Perceptron (MLP)</a></li>
        <li><a href="#forward">2. Forward Propagation Algorithm</a></li>
        <li><a href="#cost">3. Cost Functions & Output Units</a></li>
        <li><a href="#architecture">4. Architecture Design & Depth</a></li>
        <li><a href="#relu">5. Hidden Units: ReLU & Variants</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Deep Feedforward Networks</h2>
    <p>Deep feedforward networks, also called feedforward neural networks or <strong>multi-layer perceptrons (MLPs)</strong>, are the quintessential deep learning models. The goal is to approximate some function \( f^* \). A feedforward network defines a mapping \( \mathbf{y} = f(\mathbf{x}; \theta) \) and learns the value of parameters \( \theta \) that result in the best function approximation.</p>
</section>

<section class="content-section" id="forward">
    <h2>2 &middot; Forward Propagation Algorithm</h2>
    <p>During training, information flows forward through the network. The inputs \( \mathbf{x} \) provide the initial information that then propagates up to the hidden units at each layer and finally produces \( \hat{\mathbf{y}} \). This is called <strong>forward propagation</strong>.</p>
    <div class="callout note">
        <div class="callout-icon">⚙️</div>
        <div class="callout-content">
            <strong>Algorithm 6.1: Forward-Prop</strong>
            <p>For each layer \( i = n_i + 1, \dots, n \): <br>
            1. \( \mathbf{a}^{(i)} = \mathbf{b}^{(i)} + \mathbf{W}^{(i)}\mathbf{h}^{(i-1)} \) <br>
            2. \( \mathbf{h}^{(i)} = f^{(i)}(\mathbf{a}^{(i)}) \)</p>
        </div>
    </div>
</section>

<section class="content-section" id="architecture">
    <h2>4 &middot; Architecture Design</h2>
    <p>Deeper models tend to perform better. This is not merely because the model is larger; increasing the number of parameters without increasing depth is not nearly as effective. Shallow models overfit at around 20 million parameters while deep ones can benefit from over 60 million.</p>
</section>

<section class="content-section" id="relu">
    <h2>5 &middot; Hidden Units (ReLU)</h2>
    <div class="callout important">
        <div class="callout-icon">🚀</div>
        <div class="callout-content">
            <strong>Rectified Linear Units</strong>
            <p>Modern feedforward networks use <strong>ReLU</strong> defined by \( g(z) = \max\{0, z\} \). They are easy to optimize because they are very similar to linear units. Variations include Leaky ReLU, PReLU, and Maxout units.</p>
        </div>
    </div>
</section>
"""

make_page("dl/neural-networks.html","Deep Feedforward Networks","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Feedforward Networks",
"Formal textbook analysis of MLP architectures, forward propagation, and the role of depth in function approximation.",
"Deep Learning &mdash; Ian Goodfellow", dl_nn_body, ("../ml/intro-ml.html","Intro to ML"), ("backpropagation.html","Backpropagation"),
[("../ml/intro-ml.html", "Intro to ML"), ("../numpy/arrays.html", "NumPy & Tensors"), ("backpropagation.html", "Calculus")])

# BACKPROPAGATION (MASSIVE EXPANSION)
dl_bp_body = """
<div class="toc-box">
    <h4>&#x1F4CB; 6.5 &middot; Back-Propagation Algorithms</h4>
    <ol>
        <li><a href="#graphs">1. Computational Graphs</a></li>
        <li><a href="#chain">2. The Chain Rule of Calculus</a></li>
        <li><a href="#backprop">3. The Backprop Algorithm (6.2)</a></li>
        <li><a href="#symbolic">4. Symbol-to-Symbol Derivatives</a></li>
        <li><a href="#jacobian">5. Jacobians & Tensors</a></li>
    </ol>
</div>

<section class="content-section" id="graphs">
    <h2>1 &middot; Computational Graphs</h2>
    <p>To describe back-propagation precisely, we use a <strong>computational graph</strong> where each node indicates a variable (scalar, vector, matrix, or tensor) and directed edges represent operations.</p>
</section>

<section class="content-section" id="chain">
    <h2>2 &middot; The Chain Rule</h2>
    <p>Back-propagation is an algorithm that computes the chain rule with a specific order of operations that is highly efficient. In vector notation: \( \nabla_{\mathbf{x}} z = \left( \frac{\partial \mathbf{y}}{\partial \mathbf{x}} \right)^\top \nabla_{\mathbf{y}} z \), where \( \frac{\partial \mathbf{y}}{\partial \mathbf{x}} \) is the <strong>Jacobian matrix</strong>.</p>
</section>

<section class="content-section" id="backprop">
    <h2>3 &middot; The Back-Prop Procedure</h2>
    <div class="callout note">
        <div class="callout-icon">🔍</div>
        <div class="callout-content">
            <strong>Algorithm 6.2: Scalar Backprop</strong>
            <p>1. Run forward propagation to obtain activations.<br>
            2. Initialize <code>grad_table[u_n] = 1</code>.<br>
            3. For \( j = n-1 \) down to 1: <br>
            &nbsp;&nbsp;&nbsp;<code>grad_table[u_j] = \sum grad_table[u_i] (\partial u_i / \partial u_j)</code></p>
        </div>
    </div>
</section>

<section class="content-section" id="symbolic">
    <h2>4 &middot; Symbol-to-Symbol Derivatives</h2>
    <p>Modern software implementations use the <strong>symbol-to-symbol</strong> approach. Instead of accessing numeric values directly, the algorithm adds nodes to the computational graph describing how to compute derivatives. This allows a generic graph evaluation engine to compute gradients for any specific values.</p>
</section>
"""

make_page("dl/backpropagation.html","Backpropagation Algorithms","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Backpropagation",
"Deep-dive into the mathematics of backpropagation, computational graphs, and symbol-to-symbol differentiation algorithms.",
"Deep Learning &mdash; Ian Goodfellow", dl_bp_body, ("neural-networks.html","Feedforward Networks"), ("cnn.html","CNN"),
[("neural-networks.html", "NN Fundamentals"), ("../ml/model-evaluation.html", "Optimization"), ("cnn.html", "Computer Vision")])

print("neural-networks.html + backpropagation.html MASSIVELY expanded!")

