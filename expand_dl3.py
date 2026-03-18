import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# TRANSFORMERS
make_page("dl/transformers.html","Transformers &amp; Attention","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Transformers",
"Transformers revolutionized NLP with the self-attention mechanism. This section provides textbook precision on the architecture that powers GPT and BERT.",
"Attention Is All You Need &mdash; Vaswani et al.",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Self-Attention</a></li>
<li><a href="#s2">Return Value: Attention Map</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Self-Attention</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"An attention function can be described as mapping a query and a set of key-value pairs to an output. The output is computed as a weighted sum of the values." &mdash; <em>Vaswani et al.</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: Attention Map</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The self-attention calculation returns an <strong>Attention Map</strong> (a square matrix). Each entry <code>A[i, j]</code> represents how much the token at position <code>i</code> should "attend" to the token at position <code>j</code>.</p>
</div>
</section>''',
("rnn-lstm.html","RNN &amp; LSTM"),("../ml/intro-ml.html","ML Overview"),
[("rnn-lstm.html", "Sequence Models"), ("../ml/intro-ml.html", "Architecture Comparison")])

print("transformers.html expanded!")
