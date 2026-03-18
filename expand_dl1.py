import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# NEURAL NETWORKS (MASSIVE EXPANSION)
dl_nn_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Neural Networks: The Theoretical Framework</h4>
    <ol>
        <li><a href="#intro">1. The Biological Inspiration</a></li>
        <li><a href="#perceptron">2. The Perceptron vs Sigmoid Neuron</a></li>
        <li><a href="#architecture">3. Multilayer Perceptrons (MLP)</a></li>
        <li><a href="#activation">4. Activation Functions: ReLU, Sigmoid, Tanh</a></li>
        <li><a href="#loss">5. Loss Functions: MSE vs Cross-Entropy</a></li>
        <li><a href="#forward">6. The Forward Pass Algorithm</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Biological Inspiration</h2>
    <p>Neural networks are computing systems vaguely inspired by the biological neural networks that constitute animal brains. The 'neurons' in our networks are mathematical functions that receive inputs, weight them, and pass them through an activation function.</p>
</section>

<section class="content-section" id="activation">
    <h2>4 &middot; Activation Functions</h2>
    <div class="callout note">
        <div class="callout-icon">🧠</div>
        <div class="callout-content">
            <strong>The ReLU Revolution</strong>
            <p>The Rectified Linear Unit (ReLU) is defined as \( f(x) = \max(0, x) \). It solved the <strong>Vanishing Gradient Problem</strong> that plagued Sigmoid and Tanh functions, allowing for the training of much deeper networks.</p>
        </div>
    </div>
</section>

<section class="content-section" id="forward">
    <h2>6 &middot; The Forward Pass</h2>
    <p>The forward pass is the process of mapping an input vector to an output prediction through successive linear transformations and non-linear activations.</p>
    <div class="return-value-box">
        <div class="rv-label">🔁 Return Value: .predict()</div>
        <p>In Keras/TensorFlow, <code>model.predict()</code> returns a <strong>NumPy ndarray</strong> of probabilities (for classification) or continuous values (for regression). For a single input, it returns a 2D array of shape <code>(1, num_classes)</code>.</p>
    </div>
</section>
"""

make_page("dl/neural-networks.html","Neural Networks Fundamentals","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Neural Networks",
"Formal textbook analysis of neural network architectures, activation functions, and the mathematics of the forward pass.",
"Deep Learning &mdash; Ian Goodfellow", dl_nn_body, ("../ml/intro-ml.html","Intro to ML"), ("backpropagation.html","Backpropagation"),
[("../ml/intro-ml.html", "Intro to ML"), ("../numpy/arrays.html", "NumPy & Tensors"), ("backpropagation.html", "Calculus")])

# BACKPROPAGATION (MASSIVE EXPANSION)
dl_bp_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Backpropagation: Calculus of Learning</h4>
    <ol>
        <li><a href="#intro">1. The Chain Rule of Calculus</a></li>
        <li><a href="#gradient">2. Gradient Descent & Step Size</a></li>
        <li><a href="#vanish">3. The Vanishing Gradient Problem</a></li>
        <li><a href="#optimizers">4. Optimizers: SGD, Adam, RMSProp</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Chain Rule</h2>
    <p>Backpropagation is the application of the chain rule to the network's computational graph. It calculates the partial derivative of the cost function with respect to every weight in the system, moving backward from the output layer to the input.</p>
</section>

<section class="content-section" id="optimizers">
    <h2>4 &middot; Modern Optimizers</h2>
    <div class="callout important">
        <div class="callout-icon">⚙️</div>
        <div class="callout-content">
            <strong>Adam: Adaptive Moment Estimation</strong>
            <p>Adam is currently the industry-standard optimizer. It combines the advantages of AdaGrad (which handles sparse gradients) and RMSProp (which handles non-stationary objectives).</p>
        </div>
    </div>
</section>
"""

make_page("dl/backpropagation.html","Backpropagation & Optimizers","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Backpropagation",
"Deep-dive into the mathematics of backpropagation, the chain rule, and modern optimization algorithms like Adam and SGD.",
"Deep Learning &mdash; Ian Goodfellow", dl_bp_body, ("neural-networks.html","Neural Networks"), ("cnn.html","CNN"),
[("neural-networks.html", "NN Fundamentals"), ("../ml/model-evaluation.html", "Optimization"), ("cnn.html", "Computer Vision")])

print("neural-networks.html + backpropagation.html MASSIVELY expanded!")
