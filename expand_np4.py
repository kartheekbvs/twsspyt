import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# ========== EXPANDED RESHAPING ==========
make_page("numpy/reshaping.html","Reshaping &amp; Stacking","NumPy","&#x1F522;","intermediate","NumPy &rarr; Reshaping &amp; Stacking",
"Reshaping changes array dimensions without copying data. NumPy provides reshape, flatten, ravel, resize, transpose, swapaxes, expand_dims, squeeze for shape manipulation, plus stack, concatenate, vstack, hstack, split, array_split for combining and splitting arrays.",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">reshape() &amp; resize()</a></li>
<li><a href="#s2">flatten() &amp; ravel()</a></li>
<li><a href="#s3">transpose() &amp; swapaxes()</a></li>
<li><a href="#s4">expand_dims() &amp; squeeze()</a></li>
<li><a href="#s5">Stacking: vstack, hstack, stack, concatenate</a></li>
<li><a href="#s6">Splitting: split, array_split, hsplit, vsplit</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; reshape() &amp; resize()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

a = np.arange(<span class="nm">12</span>)  <span class="cm"># [0,1,2,...,11]</span>

<span class="cm"># reshape(new_shape) &mdash; returns VIEW (no copy)</span>
<span class="bi">print</span>(a.reshape(<span class="nm">3</span>, <span class="nm">4</span>))
<span class="cm"># [[ 0  1  2  3]</span>
<span class="cm">#  [ 4  5  6  7]</span>
<span class="cm">#  [ 8  9 10 11]]</span>

<span class="bi">print</span>(a.reshape(<span class="nm">4</span>, <span class="nm">3</span>))  <span class="cm"># 4 rows, 3 cols</span>
<span class="bi">print</span>(a.reshape(<span class="nm">2</span>, <span class="nm">2</span>, <span class="nm">3</span>))  <span class="cm"># 3D: 2 layers x 2 rows x 3 cols</span>

<span class="cm"># Use -1 to auto-infer one dimension</span>
<span class="bi">print</span>(a.reshape(<span class="nm">2</span>, -<span class="nm">1</span>))   <span class="cm"># (2, 6) &mdash; inferred 6</span>
<span class="bi">print</span>(a.reshape(-<span class="nm">1</span>, <span class="nm">1</span>))   <span class="cm"># (12, 1) &mdash; column vector</span>
<span class="bi">print</span>(a.reshape(<span class="nm">1</span>, -<span class="nm">1</span>))   <span class="cm"># (1, 12) &mdash; row vector</span>

<span class="cm"># resize() &mdash; modifies IN-PLACE (no return!)</span>
b = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>])
b.resize(<span class="nm">2</span>, <span class="nm">3</span>)
<span class="bi">print</span>(b)  <span class="cm"># [[1 2 3] [4 5 6]]</span>

<span class="cm"># np.resize() &mdash; repeats if new size &gt; old</span>
<span class="bi">print</span>(np.resize([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], (<span class="nm">2</span>,<span class="nm">4</span>)))  <span class="cm"># [[1,2,3,1],[2,3,1,2]]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[ 0 1 2 3]<br> [ 4 5 6 7]<br> [ 8 9 10 11]]<br>Shapes: (2,6) (12,1) (1,12)<br>[[1 2 3] [4 5 6]]</div></div>
<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>reshape() vs resize()</strong><p><code>reshape()</code> returns a view (shared memory) and requires compatible sizes. <code>resize()</code> modifies in-place and can change total size by repeating or truncating.</p></div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; flatten() &amp; ravel()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]])

<span class="cm"># flatten() &mdash; always returns a COPY</span>
flat = M.flatten()
<span class="bi">print</span>(flat)         <span class="cm"># [1 2 3 4 5 6]</span>
flat[<span class="nm">0</span>] = <span class="nm">999</span>
<span class="bi">print</span>(M[<span class="nm">0</span>,<span class="nm">0</span>])      <span class="cm"># 1 &mdash; original unchanged!</span>

<span class="cm"># ravel() &mdash; returns VIEW if possible (faster)</span>
rav = M.ravel()
<span class="bi">print</span>(rav)          <span class="cm"># [1 2 3 4 5 6]</span>
rav[<span class="nm">0</span>] = <span class="nm">999</span>
<span class="bi">print</span>(M[<span class="nm">0</span>,<span class="nm">0</span>])      <span class="cm"># 999 &mdash; original changed!</span>

<span class="cm"># Order parameter: 'C' (row-major) or 'F' (column-major)</span>
M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]])
<span class="bi">print</span>(M.flatten(order=<span class="st">'C'</span>))  <span class="cm"># [1 2 3 4] (row by row)</span>
<span class="bi">print</span>(M.flatten(order=<span class="st">'F'</span>))  <span class="cm"># [1 3 2 4] (column by column)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1 2 3 4 5 6]<br>1 (unchanged)<br>999 (changed via ravel!)<br>C: [1 2 3 4] &middot; F: [1 3 2 4]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; transpose() &amp; swapaxes()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]])  <span class="cm"># (2, 3)</span>

<span class="cm"># .T property (shorthand)</span>
<span class="bi">print</span>(M.T)   <span class="cm"># [[1,4],[2,5],[3,6]] &mdash; (3, 2)</span>
<span class="bi">print</span>(M.T.shape)  <span class="cm"># (3, 2)</span>

<span class="cm"># transpose() method &mdash; can specify axis order</span>
<span class="bi">print</span>(M.transpose())       <span class="cm"># same as .T</span>
<span class="bi">print</span>(np.transpose(M))     <span class="cm"># same</span>

<span class="cm"># swapaxes() &mdash; swap two specific axes</span>
cube = np.arange(<span class="nm">24</span>).reshape(<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>)
<span class="bi">print</span>(<span class="st">f"Original: {cube.shape}"</span>)          <span class="cm"># (2,3,4)</span>
<span class="bi">print</span>(<span class="st">f"Swapped:  {cube.swapaxes(0,2).shape}"</span>)  <span class="cm"># (4,3,2)</span>
<span class="bi">print</span>(<span class="st">f"Transposed:{cube.transpose(2,0,1).shape}"</span>) <span class="cm"># (4,2,3)</span>

<span class="cm"># 1D transpose does nothing</span>
v = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>])
<span class="bi">print</span>(v.T.shape)  <span class="cm"># (3,) &mdash; still 1D!</span>
<span class="cm"># For column vector: use reshape or newaxis</span>
<span class="bi">print</span>(v.reshape(-<span class="nm">1</span>,<span class="nm">1</span>).shape)  <span class="cm"># (3,1)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[1 4] [2 5] [3 6]]<br>(3, 2)<br>Original: (2,3,4) | Swapped: (4,3,2)</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; expand_dims() &amp; squeeze()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>])  <span class="cm"># shape (3,)</span>

<span class="cm"># expand_dims &mdash; add a new axis</span>
<span class="bi">print</span>(np.expand_dims(a, axis=<span class="nm">0</span>).shape)  <span class="cm"># (1, 3) &mdash; row vector</span>
<span class="bi">print</span>(np.expand_dims(a, axis=<span class="nm">1</span>).shape)  <span class="cm"># (3, 1) &mdash; column vector</span>

<span class="cm"># Equivalent using np.newaxis</span>
<span class="bi">print</span>(a[np.newaxis, :].shape)  <span class="cm"># (1, 3)</span>
<span class="bi">print</span>(a[:, np.newaxis].shape)  <span class="cm"># (3, 1)</span>

<span class="cm"># squeeze() &mdash; remove axes of length 1</span>
b = np.array([[[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>]]])  <span class="cm"># shape (1, 1, 3)</span>
<span class="bi">print</span>(b.squeeze().shape)     <span class="cm"># (3,)</span>
<span class="bi">print</span>(np.squeeze(b, axis=<span class="nm">0</span>).shape)  <span class="cm"># (1, 3) &mdash; remove only axis 0</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>(1, 3) &middot; (3, 1)<br>(3,) &middot; (1, 3)</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Stacking &amp; Concatenation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>])
b = np.array([<span class="nm">4</span>, <span class="nm">5</span>, <span class="nm">6</span>])

<span class="cm"># vstack &mdash; vertical (row-wise)</span>
<span class="bi">print</span>(np.vstack([a, b]))     <span class="cm"># [[1,2,3],[4,5,6]]</span>

<span class="cm"># hstack &mdash; horizontal (column-wise)</span>
<span class="bi">print</span>(np.hstack([a, b]))     <span class="cm"># [1 2 3 4 5 6]</span>

<span class="cm"># stack &mdash; join along NEW axis</span>
<span class="bi">print</span>(np.stack([a, b], axis=<span class="nm">0</span>))  <span class="cm"># [[1,2,3],[4,5,6]] shape (2,3)</span>
<span class="bi">print</span>(np.stack([a, b], axis=<span class="nm">1</span>))  <span class="cm"># [[1,4],[2,5],[3,6]] shape (3,2)</span>

<span class="cm"># column_stack &mdash; stack 1D as columns</span>
<span class="bi">print</span>(np.column_stack([a, b]))  <span class="cm"># [[1,4],[2,5],[3,6]]</span>

<span class="cm"># row_stack &mdash; same as vstack</span>
<span class="bi">print</span>(np.row_stack([a, b]))    <span class="cm"># [[1,2,3],[4,5,6]]</span>

<span class="cm"># concatenate &mdash; most general</span>
A = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]])
B = np.array([[<span class="nm">5</span>,<span class="nm">6</span>],[<span class="nm">7</span>,<span class="nm">8</span>]])
<span class="bi">print</span>(np.concatenate([A, B], axis=<span class="nm">0</span>))  <span class="cm"># [[1,2],[3,4],[5,6],[7,8]]</span>
<span class="bi">print</span>(np.concatenate([A, B], axis=<span class="nm">1</span>))  <span class="cm"># [[1,2,5,6],[3,4,7,8]]</span>

<span class="cm"># dstack &mdash; depth-wise (along 3rd axis)</span>
<span class="bi">print</span>(np.dstack([A, B]).shape)  <span class="cm"># (2, 2, 2)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>vstack: [[1 2 3] [4 5 6]]<br>hstack: [1 2 3 4 5 6]<br>stack axis=1: [[1 4] [2 5] [3 6]]<br>concat axis=0: [[1 2] [3 4] [5 6] [7 8]]</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Splitting</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">a = np.arange(<span class="nm">12</span>)

<span class="cm"># split &mdash; equal parts (error if not divisible)</span>
parts = np.split(a, <span class="nm">3</span>)
<span class="bi">print</span>(parts)  <span class="cm"># [array([0,1,2,3]), array([4,5,6,7]), array([8,9,10,11])]</span>

<span class="cm"># split at specific indices</span>
parts = np.split(a, [<span class="nm">3</span>, <span class="nm">7</span>])  <span class="cm"># split at index 3 and 7</span>
<span class="bi">print</span>(parts)  <span class="cm"># [array([0,1,2]), array([3,4,5,6]), array([7,8,9,10,11])]</span>

<span class="cm"># array_split &mdash; uneven splits OK</span>
parts = np.array_split(a, <span class="nm">5</span>)
<span class="bi">print</span>([p.shape <span class="kw">for</span> p <span class="kw">in</span> parts])  <span class="cm"># [(3,),(3,),(2,),(2,),(2,)]</span>

<span class="cm"># hsplit, vsplit for 2D</span>
M = np.arange(<span class="nm">12</span>).reshape(<span class="nm">3</span>, <span class="nm">4</span>)
left, right = np.hsplit(M, <span class="nm">2</span>)   <span class="cm"># split columns in half</span>
<span class="bi">print</span>(left)   <span class="cm"># [[0,1],[4,5],[8,9]]</span>
<span class="bi">print</span>(right)  <span class="cm"># [[2,3],[6,7],[10,11]]</span>

top, bottom = np.vsplit(M[[<span class="nm">0</span>,<span class="nm">1</span>,<span class="nm">2</span>]], [<span class="nm">2</span>])
<span class="bi">print</span>(top.shape, bottom.shape)  <span class="cm"># (2,4) (1,4)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[array([0,1,2,3]), array([4,5,6,7]), array([8,9,10,11])]<br>hsplit: [[0 1] [4 5] [8 9]] | [[2 3] [6 7] [10 11]]</div></div>

<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Quick Reference</strong>
<table style="width:100%;font-size:.85rem">
<tr><td><code>vstack / vsplit</code></td><td>Stack/split vertically (along rows, axis=0)</td></tr>
<tr><td><code>hstack / hsplit</code></td><td>Stack/split horizontally (along columns, axis=1)</td></tr>
<tr><td><code>dstack / dsplit</code></td><td>Stack/split depth-wise (along axis=2)</td></tr>
<tr><td><code>concatenate</code></td><td>Most general &mdash; specify any axis</td></tr>
<tr><td><code>stack</code></td><td>Join along a NEW axis</td></tr>
</table></div></div></section>''',
("indexing.html","Indexing &amp; Slicing"),("math-functions.html","Math Functions"))

print("reshaping.html expanded!")
