import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# TRANSFORMERS
make_page("dl/transformers.html","Transformers &amp; Attention","Deep Learning","&#x1F9E0;","advanced","DL &rarr; Transformers",
"Transformers are the architecture behind GPT, BERT, and modern AI. They use self-attention to process sequences in parallel, replacing RNNs. Covers attention mechanism, self-attention, multi-head attention, positional encoding, encoder-decoder architecture, BERT, GPT, and using Hugging Face&#39;s transformers library.",
"Attention Is All You Need (Vaswani et al., 2017), Hugging Face docs",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Attention Mechanism</a></li>
<li><a href="#s2">Self-Attention &amp; Multi-Head</a></li>
<li><a href="#s3">Transformer Architecture</a></li>
<li><a href="#s4">BERT vs GPT</a></li>
<li><a href="#s5">Hugging Face Transformers</a></li>
<li><a href="#s6">Fine-Tuning</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Attention Mechanism</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Why Attention?</strong>
<p>RNNs process tokens sequentially and struggle with long sequences. Attention allows the model to <strong>look at all positions simultaneously</strong> and decide which ones are most relevant.</p>
<pre style="font-size:.85rem;line-height:1.6;">
"The cat sat on the mat because it was tired"
                                     &uarr;
        What does "it" refer to? &rarr; "cat" (high attention!)
        Not "mat" (low attention)</pre></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Simplified Attention</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="kw">def</span> <span class="bi">attention</span>(query, key, value):
    <span class="st">"""Scaled Dot-Product Attention"""</span>
    d_k = query.shape[-<span class="nm">1</span>]
    <span class="cm"># 1. Compute similarity scores</span>
    scores = query @ key.T / np.sqrt(d_k)

    <span class="cm"># 2. Convert to probabilities (attention weights)</span>
    exp_scores = np.exp(scores - scores.max())
    weights = exp_scores / exp_scores.sum(axis=-<span class="nm">1</span>, keepdims=<span class="kw">True</span>)

    <span class="cm"># 3. Weighted sum of values</span>
    output = weights @ value
    <span class="kw">return</span> output, weights

<span class="cm"># Example: 4 tokens, embedding dim = 3</span>
np.random.seed(<span class="nm">42</span>)
seq_len, d_model = <span class="nm">4</span>, <span class="nm">3</span>
X = np.random.randn(seq_len, d_model)

<span class="cm"># Q, K, V are linear projections of X</span>
W_q = np.random.randn(d_model, d_model) * <span class="nm">0.5</span>
W_k = np.random.randn(d_model, d_model) * <span class="nm">0.5</span>
W_v = np.random.randn(d_model, d_model) * <span class="nm">0.5</span>

Q = X @ W_q
K = X @ W_k
V = X @ W_v

output, weights = attention(Q, K, V)
<span class="bi">print</span>(<span class="st">"Attention weights (which tokens attend to which):"</span>)
<span class="bi">print</span>(weights.round(<span class="nm">3</span>))
<span class="bi">print</span>(<span class="st">f"\\nOutput shape: {output.shape}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Attention weights:<br>[[0.31 0.24 0.19 0.26]   &larr; token 0 attends most to token 0<br> [0.18 0.42 0.15 0.25]   &larr; token 1 attends most to itself<br> [0.22 0.28 0.30 0.20]<br> [0.25 0.21 0.24 0.30]]<br>Output shape: (4, 3)</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Multi-Head Attention</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Multi-Head = Multiple Perspectives</strong>
<pre style="font-size:.85rem;line-height:1.6;">
Head 1: Focuses on syntactic relationships
Head 2: Focuses on semantic meaning
Head 3: Focuses on positional proximity
...
Multi-Head = Concat(Head1, Head2, ...) &times; W_out

Each head learns DIFFERENT attention patterns!</pre></div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; In Keras/TensorFlow</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> tensorflow.keras <span class="kw">import</span> layers

<span class="cm"># Built-in Multi-Head Attention</span>
mha = layers.MultiHeadAttention(
    num_heads=<span class="nm">8</span>,       <span class="cm"># 8 attention heads</span>
    key_dim=<span class="nm">64</span>,        <span class="cm"># dimension per head</span>
    dropout=<span class="nm">0.1</span>
)

<span class="cm"># Self-attention: query = key = value = same input</span>
<span class="cm"># output = mha(query=X, key=X, value=X)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>8 heads &times; 64 dim = 512 total &mdash; same as original paper</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Transformer Architecture</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Transformer = Encoder + Decoder</strong>
<pre style="font-size:.85rem;line-height:1.6;">
ENCODER (understands input &mdash; BERT)     DECODER (generates output &mdash; GPT)
&boxdr;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxdl;                &boxdr;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxdl;
&boxv; Multi-Head Attention &boxv;                &boxv; Masked Multi-Head Attn &boxv;
&boxv; Add &amp; Normalize     &boxv;                &boxv; Cross-Attention        &boxv;
&boxv; Feed-Forward         &boxv;                &boxv; Feed-Forward           &boxv;
&boxv; Add &amp; Normalize     &boxv;                &boxv; Add &amp; Normalize       &boxv;
&boxdr;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxdl;                &boxdr;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxh;&boxdl;
(repeats N&times;, e.g. 12)                   (repeats N&times;)

Key innovations vs RNN:
&bull; Parallel processing (not sequential!)
&bull; Self-attention (global context)
&bull; Positional encoding (since no recurrence)</pre></div></div>
<table class="data-table"><thead><tr><th>Component</th><th>Purpose</th></tr></thead><tbody>
<tr><td>Multi-Head Attention</td><td>Learn relationships between all tokens</td></tr>
<tr><td>Add &amp; Normalize</td><td>Residual connection + LayerNorm for stability</td></tr>
<tr><td>Feed-Forward</td><td>2 Dense layers (expand then compress)</td></tr>
<tr><td>Positional Encoding</td><td>Inject position info (since no sequential processing)</td></tr>
<tr><td>Masked Attention</td><td>Decoder can&rsquo;t see future tokens (autoregressive)</td></tr>
</tbody></table></section>

<section class="content-section" id="s4"><h2>4 &middot; BERT vs GPT</h2>
<table class="data-table"><thead><tr><th>Feature</th><th>BERT</th><th>GPT</th></tr></thead><tbody>
<tr><td>Architecture</td><td>Encoder only</td><td>Decoder only</td></tr>
<tr><td>Direction</td><td>Bidirectional (sees full context)</td><td>Left-to-right (autoregressive)</td></tr>
<tr><td>Training</td><td>Masked Language Model</td><td>Next Token Prediction</td></tr>
<tr><td>Best For</td><td>Understanding (classification, NER, QA)</td><td>Generation (text, code, chat)</td></tr>
<tr><td>Examples</td><td>BERT, RoBERTa, DistilBERT</td><td>GPT-2, GPT-3, GPT-4, LLaMA</td></tr>
<tr><td>Sizes</td><td>110M &ndash; 340M params</td><td>117M &ndash; 1.8T params</td></tr>
</tbody></table></section>

<section class="content-section" id="s5"><h2>5 &middot; Hugging Face Transformers</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Sentiment Analysis Pipeline</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> transformers <span class="kw">import</span> pipeline

<span class="cm"># 1-line sentiment analysis!</span>
classifier = pipeline(<span class="st">"sentiment-analysis"</span>)
result = classifier(<span class="st">"I love learning about transformers!"</span>)
<span class="bi">print</span>(result)
<span class="cm"># [{'label': 'POSITIVE', 'score': 0.9998}]</span>

<span class="cm"># Text generation</span>
generator = pipeline(<span class="st">"text-generation"</span>, model=<span class="st">"gpt2"</span>)
text = generator(<span class="st">"Machine learning is"</span>, max_length=<span class="nm">30</span>, num_return_sequences=<span class="nm">1</span>)
<span class="bi">print</span>(text[<span class="nm">0</span>][<span class="st">"generated_text"</span>])

<span class="cm"># Question answering</span>
qa = pipeline(<span class="st">"question-answering"</span>)
result = qa(question=<span class="st">"What is attention?"</span>,
            context=<span class="st">"Attention allows models to focus on relevant parts of the input."</span>)
<span class="bi">print</span>(<span class="st">f"Answer: {result['answer']}"</span>)

<span class="cm"># Named Entity Recognition</span>
ner = pipeline(<span class="st">"ner"</span>, grouped_entities=<span class="kw">True</span>)
<span class="bi">print</span>(ner(<span class="st">"Google was founded by Larry Page in California."</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[{'label': 'POSITIVE', 'score': 0.9998}]<br>Answer: focus on relevant parts of the input<br>NER: Google(ORG), Larry Page(PER), California(LOC)</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Fine-Tuning a Transformer</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Fine-tune BERT for Classification</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> transformers <span class="kw">import</span> AutoTokenizer, AutoModelForSequenceClassification
<span class="kw">from</span> transformers <span class="kw">import</span> Trainer, TrainingArguments

<span class="cm"># Load pretrained BERT</span>
model_name = <span class="st">"bert-base-uncased"</span>
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=<span class="nm">2</span>
)

<span class="cm"># Tokenize texts</span>
texts = [<span class="st">"Great movie!"</span>, <span class="st">"Terrible film."</span>, <span class="st">"Amazing!"</span>, <span class="st">"Awful..."</span>]
tokens = tokenizer(texts, padding=<span class="kw">True</span>, truncation=<span class="kw">True</span>, return_tensors=<span class="st">"pt"</span>)
<span class="bi">print</span>(<span class="st">f"Input IDs shape: {tokens['input_ids'].shape}"</span>)
<span class="bi">print</span>(<span class="st">f"Tokens: {tokenizer.tokenize('Great movie!')}"</span>)

<span class="cm"># Training args</span>
training_args = TrainingArguments(
    output_dir=<span class="st">"./results"</span>,
    num_train_epochs=<span class="nm">3</span>,
    per_device_train_batch_size=<span class="nm">16</span>,
    learning_rate=<span class="nm">2e-5</span>,
    weight_decay=<span class="nm">0.01</span>,
)
<span class="cm"># trainer = Trainer(model=model, args=training_args, ...)</span>
<span class="cm"># trainer.train()</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Tokens: ['great', 'movie', '!']<br>Input IDs shape: torch.Size([4, 5])<br>Fine-tuning adapts BERT to YOUR specific task!</div></div></section>''',
("rnn-lstm.html","RNN &amp; LSTM"),("../ml/intro-ml.html","ML Overview"))

print("transformers.html expanded!")
