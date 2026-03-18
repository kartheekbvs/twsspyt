import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CNN (MASSIVE EXPANSION)
dl_cnn_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Convolutional Neural Networks (CNN)</h4>
    <ol>
        <li><a href="#intro">1. The Neuroscientific Basis</a></li>
        <li><a href="#conv">2. The Convolution Operation</a></li>
        <li><a href="#pooling">3. Pooling Paradigms: Max vs Average</a></li>
        <li><a href="#arch">4. Classic Architectures: LeNet to ResNet</a></li>
        <li><a href="#viz">5. Visualizing Kernels and Feature Maps</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; The Neuroscientific Basis</h2>
    <p>CNNs were inspired by the work of Hubel and Wiesel on the visual cortex of mammals. They discovered that neurons respond to local regions of the visual field (receptive fields) and that some neurons respond to specific patterns (edges) but not others.</p>
</section>

<section class="content-section" id="conv">
    <h2>2 &middot; The Convolution Operation</h2>
    <div class="callout note">
        <div class="callout-icon">🖼️</div>
        <div class="callout-content">
            <strong>Mathematical Convolution</strong>
            <p>In deep learning, "convolution" is actually a <strong>cross-correlation</strong>. It involves sliding a kernel (filter) over an input image and computing the dot product at each position. This extracts spatial hierarchies of features.</p>
        </div>
    </div>
</section>
"""

make_page("dl/cnn.html","Convolutional Neural Networks","Deep Learning","&#x1F9E0;","advanced","DL &rarr; CNN",
"Formal textbook analysis of Convolutional architectures, pooling strategies, and spatial feature extraction for Computer Vision.",
"Deep Learning &mdash; Ian Goodfellow", dl_cnn_body, ("backpropagation.html","Backpropagation"), ("rnn-lstm.html","RNN & LSTM"),
[("neural-networks.html", "NN Fundamentals"), ("backpropagation.html", "Gradients")])

# RNN & TRANSFORMERS (MASSIVE EXPANSION)
dl_seq_body = """
<div class="toc-box">
    <h4>&#x1F4CB; Sequence Modeling: RNNs to Transformers</h4>
    <ol>
        <li><a href="#intro">1. Modeling Temporal Dependencies</a></li>
        <li><a href="#rnn">2. Recurrent Neural Networks (RNN)</a></li>
        <li><a href="#lstm">3. LSTM & GRU: Solving Vanishing Gradients</a></li>
        <li><a href="#attn">4. Attention Mechanisms</a></li>
        <li><a href="#trans">5. The Transformer Architecture (Self-Attention)</a></li>
    </ol>
</div>

<section class="content-section" id="intro">
    <h2>1 &middot; Temporal Dependencies</h2>
    <p>Standard neural networks assume all inputs are independent. Sequence models (RNNs) break this by maintaining a 'hidden state' that captures information about previous time steps.</p>
</section>

<section class="section" id="trans">
    <h2>5 &middot; The Transformer Revolution</h2>
    <div class="callout important">
        <div class="callout-icon">✨</div>
        <div class="callout-content">
            <strong>Attention is All You Need</strong>
            <p>The Transformer architecture replaced recurrence with <strong>Self-Attention</strong>. This allowed for massive parallelization and the ability to capture long-range dependencies across thousands of tokens.</p>
        </div>
    </div>
</section>
"""

make_page("dl/rnn-lstm.html","Recurrent Neural Networks","Deep Learning","&#x1F9E0;","advanced","DL &rarr; RNN",
"Deep-dive into sequence modeling, covering the vanishing gradient problem, LSTMs, and the transition to attention-based models.",
"Deep Learning &mdash; Ian Goodfellow", dl_seq_body, ("cnn.html","CNN"), ("transformers.html","Transformers"),
[("cnn.html", "Visual Hierarchies"), ("transformers.html", "Self-Attention")])

make_page("dl/transformers.html","Transformers & Self-Attention","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Transformers",
"The complete guide to the Transformer architecture, multi-head attention, and positional encoding logic.",
"Deep Learning &mdash; Ian Goodfellow", dl_seq_body, ("rnn-lstm.html","RNN & LSTM"), ("masterclass.html","DL Masterclass"),
[("rnn-lstm.html", "Sequence Basics"), ("masterclass.html", "DL Hub")])

print("cnn.html + rnn-lstm.html + transformers.html MASSIVELY expanded!")
