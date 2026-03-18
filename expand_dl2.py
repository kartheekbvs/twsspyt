import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CNN
make_page("dl/cnn.html","Convolutional Neural Networks","Deep Learning","&#x1F9E0;","advanced","DL &rarr; CNN",
"CNNs are the gold standard for image recognition. This section covers convolution operations and architecture with textbook definitions.",
"Deep Learning with Python &mdash; Fran&ccedil;ois Chollet",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Convolutional Layers</a></li>
<li><a href="#s2">Return Value: Keras Layers</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Convolutional Layers</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"The fundamental difference between a densely connected layer and a convolutional layer is this: <code>Dense</code> layers learn global patterns, while <code>convolution</code> layers learn local patterns." &mdash; <em>Fran&ccedil;ois Chollet</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: Keras Layers</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>In Keras, a layer call (e.g., <code>layers.Conv2D(...)(input)</code>) returns a <strong>Keras Tensor</strong> or <strong>Symbolic Tensor</strong>. In an Eager execution environment, it may return an <strong>EagerTensor</strong> containing the actual data.</p>
</div>
</section>''',
("backpropagation.html","Backpropagation"),("rnn-lstm.html","RNN &amp; LSTM"),
[("backpropagation.html", "Training"), ("../numpy/operations.html", "Vectorization")])

# RNN-LSTM
make_page("dl/rnn-lstm.html","RNN, LSTM &amp; GRU","Deep Learning","&#x1F9E0;","advanced","DL &rarr; RNN &amp; LSTM",
"Processing sequential data requires memory. This section explores RNNs and LSTMs with textbook insights into sequence processing.",
"Deep Learning with Python &mdash; Fran&ccedil;ois Chollet",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Recurrent Neural Networks</a></li>
<li><a href="#s2">LSTM &amp; Memory</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Recurrent Neural Networks (RNN)</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"A recurrent neural network (RNN) processes sequences by iterating through the sequence elements and maintaining a <em>state</em> containing information relative to what it has seen so far." &mdash; <em>Fran&ccedil;ois Chollet</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: RNN Layers</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>By default, Keras RNN layers (LSTM/GRU) return only the <strong>last output</strong> in the sequence. If <code>return_sequences=True</code> is set, they return the <strong>entire sequence</strong> of outputs.</p>
</div>
</section>''',
("backpropagation.html","Backpropagation"),("transformers.html","Transformers"),
[("cnn.html", "Spatial patterns"), ("../python/generators.html", "Iterators")])

print("cnn.html + rnn-lstm.html expanded!")
