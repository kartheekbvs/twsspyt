import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# NEURAL NETWORKS
make_page("dl/neural-networks.html","Neural Networks Fundamentals","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Neural Networks",
"Neural networks are computing systems inspired by biological brains. This page covers formal textbook definitions and implementation details.",
"Deep Learning &mdash; Ian Goodfellow, Yoshua Bengio, Aaron Courville",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">What is a Neural Network?</a></li>
<li><a href="#s2">The Forward Pass</a></li>
<li><a href="#s3">Training &amp; History</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; What is a Neural Network?</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Deep learning is a form of machine learning that enables computers to learn from experience and understand the world in terms of a hierarchy of concepts." &mdash; <em>Ian Goodfellow, Deep Learning</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s3"><h2>2 &middot; Training &amp; History</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: .fit()</div>
    <p>In Keras, <code>model.fit()</code> returns a <strong>History object</strong>. Its <code>history</code> attribute is a dictionary recording training loss values and metrics values at successive epochs, as well as validation loss values and validation metrics values (if applicable).</p>
</div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">history = model.fit(X_train, y_train, epochs=<span class="nm">10</span>)
<span class="bi">print</span>(history.history.keys())  <span class="cm"># dict_keys(['loss', 'accuracy'])</span></pre>
</div>
</section>''',
("backpropagation.html","Backpropagation"),("cnn.html","CNN"),
[("../ml/intro-ml.html", "Intro to ML"), ("../numpy/arrays.html", "NumPy &amp; Tensors")])

# BACKPROPAGATION
make_page("dl/backpropagation.html","Backpropagation &amp; Optimizers","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Backpropagation",
"Backpropagation is how neural networks learn by computing gradients. This section covers the math and implementation.",
"Deep Learning &mdash; Ian Goodfellow",
'''<section class="content-section" id="s1"><h2>1 &middot; Chain Rule</h2>
<p>Backpropagation is essentially the chain rule of calculus applied to the network's layers.</p>
</section>''',
("neural-networks.html","Neural Networks"),("cnn.html","CNN"),
[("neural-networks.html", "NN Fundamentals"), ("../ml/model-evaluation.html", "Optimization")])

print("neural-networks.html + backpropagation.html expanded!")
