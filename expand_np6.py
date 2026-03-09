import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# ========== EXPANDED LINEAR ALGEBRA ==========
make_page("numpy/linear-algebra.html","Linear Algebra","NumPy","&#x1F522;","advanced","NumPy &rarr; Linear Algebra",
"NumPy&#39;s linalg module provides optimized linear algebra operations: dot products, matrix multiplication, determinants, inverses, eigenvalues, SVD, solving linear systems, and matrix rank. These are the mathematical foundations for machine learning and deep learning.",
"NumPy User Guide, Deep Learning &mdash; Ian Goodfellow",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Vector Operations &amp; Dot Product</a></li>
<li><a href="#s2">Matrix Multiplication</a></li>
<li><a href="#s3">Determinant, Inverse &amp; Rank</a></li>
<li><a href="#s4">Eigenvalues &amp; Eigenvectors</a></li>
<li><a href="#s5">Singular Value Decomposition (SVD)</a></li>
<li><a href="#s6">Solving Linear Systems</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Vector Operations &amp; Dot Product</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

u = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>])
v = np.array([<span class="nm">4</span>, <span class="nm">5</span>, <span class="nm">6</span>])

<span class="cm"># Dot product: sum of element-wise products</span>
<span class="bi">print</span>(np.dot(u, v))          <span class="cm"># 32 (1*4 + 2*5 + 3*6)</span>
<span class="bi">print</span>(u @ v)                 <span class="cm"># 32 (@ operator)</span>
<span class="bi">print</span>(np.inner(u, v))        <span class="cm"># 32 (same for 1D)</span>

<span class="cm"># Cross product (3D vectors only)</span>
<span class="bi">print</span>(np.cross(u, v))        <span class="cm"># [-3  6 -3]</span>

<span class="cm"># Vector norm (magnitude)</span>
<span class="bi">print</span>(np.linalg.norm(u))             <span class="cm"># 3.7417 (L2 norm)</span>
<span class="bi">print</span>(np.linalg.norm(u, ord=<span class="nm">1</span>))      <span class="cm"># 6 (L1 norm)</span>
<span class="bi">print</span>(np.linalg.norm(u, ord=np.inf)) <span class="cm"># 3 (max norm)</span>

<span class="cm"># Outer product: u &#x2297; v</span>
<span class="bi">print</span>(np.outer(u, v))
<span class="cm"># [[ 4  5  6]</span>
<span class="cm">#  [ 8 10 12]</span>
<span class="cm">#  [12 15 18]]</span>

<span class="cm"># Normalize a vector</span>
u_hat = u / np.linalg.norm(u)
<span class="bi">print</span>(<span class="st">f"Unit vector: {u_hat.round(4)}"</span>)
<span class="bi">print</span>(<span class="st">f"Magnitude:   {np.linalg.norm(u_hat):.4f}"</span>)  <span class="cm"># 1.0</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Dot: 32 &middot; Cross: [-3 6 -3] &middot; Norm: 3.7417<br>Outer: [[4 5 6] [8 10 12] [12 15 18]]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Matrix Multiplication</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">A = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]])
B = np.array([[<span class="nm">5</span>,<span class="nm">6</span>],[<span class="nm">7</span>,<span class="nm">8</span>]])

<span class="cm"># Matrix multiplication (@ operator &mdash; recommended)</span>
<span class="bi">print</span>(A @ B)
<span class="cm"># [[19 22]</span>
<span class="cm">#  [43 50]]</span>

<span class="cm"># np.matmul() &mdash; same as @</span>
<span class="bi">print</span>(np.matmul(A, B))

<span class="cm"># np.dot() &mdash; also works for matrix mul</span>
<span class="bi">print</span>(np.dot(A, B))

<span class="cm"># &#x26A0;&#xFE0F; COMMON MISTAKE: * is element-wise, NOT matrix mul!</span>
<span class="bi">print</span>(A * B)  <span class="cm"># [[5,12],[21,32]] &mdash; element-wise!</span>

<span class="cm"># Matrix-vector multiplication</span>
v = np.array([<span class="nm">1</span>, <span class="nm">2</span>])
<span class="bi">print</span>(A @ v)     <span class="cm"># [5, 11]</span>

<span class="cm"># Matrix power</span>
<span class="bi">print</span>(np.linalg.matrix_power(A, <span class="nm">2</span>))  <span class="cm"># A @ A</span>
<span class="bi">print</span>(np.linalg.matrix_power(A, <span class="nm">3</span>))  <span class="cm"># A @ A @ A</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[19 22]<br> [43 50]]<br>A @ v: [5 11]</div></div>
<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>Critical Distinction</strong><p><code>A * B</code> = element-wise product (Hadamard). <code>A @ B</code> = matrix multiplication. This is the #1 source of linear algebra bugs in NumPy.</p></div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Determinant, Inverse &amp; Rank</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">A = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>]])

<span class="cm"># Determinant</span>
det = np.linalg.det(A)
<span class="bi">print</span>(<span class="st">f"det(A) = {det:.1f}"</span>)  <span class="cm"># -2.0</span>

<span class="cm"># Inverse (only if det &ne; 0)</span>
A_inv = np.linalg.inv(A)
<span class="bi">print</span>(<span class="st">f"A&sup;-&sup1; =\\n{A_inv}"</span>)
<span class="cm"># [[-2.   1. ]</span>
<span class="cm">#  [ 1.5 -0.5]]</span>

<span class="cm"># Verify: A @ A&sup;-&sup1; should be identity</span>
<span class="bi">print</span>(np.allclose(A @ A_inv, np.eye(<span class="nm">2</span>)))  <span class="cm"># True</span>

<span class="cm"># Matrix rank</span>
<span class="bi">print</span>(<span class="st">f"rank(A) = {np.linalg.matrix_rank(A)}"</span>)  <span class="cm"># 2</span>

<span class="cm"># Rank-deficient matrix</span>
B = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">2</span>,<span class="nm">4</span>]])  <span class="cm"># row 2 = 2 * row 1</span>
<span class="bi">print</span>(<span class="st">f"rank(B) = {np.linalg.matrix_rank(B)}"</span>)  <span class="cm"># 1</span>
<span class="bi">print</span>(<span class="st">f"det(B) = {np.linalg.det(B):.1f}"</span>)       <span class="cm"># 0.0 (singular!)</span>

<span class="cm"># Trace (sum of diagonal)</span>
<span class="bi">print</span>(<span class="st">f"trace(A) = {np.trace(A)}"</span>)  <span class="cm"># 5 (1 + 4)</span>

<span class="cm"># Condition number (sensitivity to perturbation)</span>
<span class="bi">print</span>(<span class="st">f"cond(A) = {np.linalg.cond(A):.2f}"</span>)  <span class="cm"># 14.93</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>det(A) = -2.0<br>A&sup;-&sup1; = [[-2. 1.] [1.5 -0.5]]<br>rank(A) = 2 &middot; rank(B) = 1<br>trace(A) = 5 &middot; cond(A) = 14.93</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Eigenvalues &amp; Eigenvectors</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Eigendecomposition: Av = &lambda;v</span>
A = np.array([[<span class="nm">4</span>, <span class="nm">2</span>], [<span class="nm">1</span>, <span class="nm">3</span>]])

eigenvalues, eigenvectors = np.linalg.eig(A)
<span class="bi">print</span>(<span class="st">f"Eigenvalues:  {eigenvalues}"</span>)    <span class="cm"># [5. 2.]</span>
<span class="bi">print</span>(<span class="st">f"Eigenvectors:\\n{eigenvectors}"</span>)

<span class="cm"># Verify: Av = &lambda;v for each eigenvalue</span>
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="bi">len</span>(eigenvalues)):
    v = eigenvectors[:, i]
    lam = eigenvalues[i]
    <span class="bi">print</span>(<span class="st">f"A @ v{i} = {(A @ v).round(4)}"</span>)
    <span class="bi">print</span>(<span class="st">f"&lambda;{i} * v{i} = {(lam * v).round(4)}"</span>)
    <span class="bi">print</span>(<span class="st">f"Match: {np.allclose(A @ v, lam * v)}"</span>)

<span class="cm"># For symmetric matrices (real eigenvalues)</span>
S = np.array([[<span class="nm">2</span>,<span class="nm">1</span>],[<span class="nm">1</span>,<span class="nm">3</span>]])
vals, vecs = np.linalg.eigh(S)  <span class="cm"># eigh = symmetric</span>
<span class="bi">print</span>(<span class="st">f"Symmetric eigenvalues: {vals}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Eigenvalues: [5. 2.]<br>Match: True (for both)</div></div>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>ML Application</strong><p>Eigendecomposition is the mathematical foundation of <strong>PCA</strong> (Principal Component Analysis). The eigenvectors of the covariance matrix define the principal components, and eigenvalues indicate the variance explained.</p></div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Singular Value Decomposition (SVD)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># SVD: M = U &middot; &Sigma; &middot; V&sup;T</span>
M = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>],[<span class="nm">5</span>,<span class="nm">6</span>]])  <span class="cm"># 3x2 matrix</span>

U, S, Vt = np.linalg.svd(M, full_matrices=<span class="kw">False</span>)
<span class="bi">print</span>(<span class="st">f"U  shape: {U.shape}"</span>)   <span class="cm"># (3, 2)</span>
<span class="bi">print</span>(<span class="st">f"S  (singular values): {S.round(4)}"</span>)  <span class="cm"># [9.5255, 0.5143]</span>
<span class="bi">print</span>(<span class="st">f"Vt shape: {Vt.shape}"</span>)  <span class="cm"># (2, 2)</span>

<span class="cm"># Reconstruct original matrix</span>
M_reconstructed = U @ np.diag(S) @ Vt
<span class="bi">print</span>(np.allclose(M, M_reconstructed))  <span class="cm"># True</span>

<span class="cm"># Low-rank approximation (keep top-k singular values)</span>
k = <span class="nm">1</span>
M_approx = U[:,:k] @ np.diag(S[:k]) @ Vt[:k,:]
<span class="bi">print</span>(<span class="st">f"Rank-1 approx:\\n{M_approx.round(2)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>S: [9.5255 0.5143]<br>Reconstruction matches: True</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Solving Linear Systems</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Solve Ax = b</span>
<span class="cm"># 2x + y = 11</span>
<span class="cm"># 5x + 7y = 13</span>
A = np.array([[<span class="nm">2</span>, <span class="nm">1</span>], [<span class="nm">5</span>, <span class="nm">7</span>]])
b = np.array([<span class="nm">11</span>, <span class="nm">13</span>])

x = np.linalg.solve(A, b)
<span class="bi">print</span>(<span class="st">f"Solution: x={x[0]:.3f}, y={x[1]:.3f}"</span>)

<span class="cm"># Verify</span>
<span class="bi">print</span>(<span class="st">f"Check: {np.allclose(A @ x, b)}"</span>)  <span class="cm"># True</span>

<span class="cm"># Least squares (overdetermined systems)</span>
<span class="cm"># More equations than unknowns</span>
A = np.array([[<span class="nm">1</span>,<span class="nm">1</span>],[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">1</span>,<span class="nm">3</span>]])
b = np.array([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">2</span>])
x, residuals, rank, sv = np.linalg.lstsq(A, b, rcond=<span class="kw">None</span>)
<span class="bi">print</span>(<span class="st">f"Least squares solution: {x.round(4)}"</span>)
<span class="bi">print</span>(<span class="st">f"Residuals: {residuals.round(4)}"</span>)

<span class="cm"># Cholesky decomposition (for positive definite matrices)</span>
P = np.array([[<span class="nm">4</span>,<span class="nm">2</span>],[<span class="nm">2</span>,<span class="nm">3</span>]])
L = np.linalg.cholesky(P)
<span class="bi">print</span>(<span class="st">f"Cholesky L:\\n{L.round(4)}"</span>)
<span class="bi">print</span>(np.allclose(L @ L.T, P))  <span class="cm"># True</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Solution: x=7.111, y=-3.222<br>Check: True<br>Least squares: [0.6667 0.5]</div></div></section>''',
("math-functions.html","Math Functions"),("random.html","Random Module"))

# ========== EXPANDED RANDOM MODULE ==========
make_page("numpy/random.html","Random Module","NumPy","&#x1F522;","intermediate","NumPy &rarr; Random Module",
"NumPy&#39;s random module generates arrays of random numbers from various distributions. Essential for simulations, data augmentation, train/test splits, initializing neural network weights, and Monte Carlo methods. Covers legacy API, new Generator API, distributions, seeding, shuffling, and sampling.",
"NumPy User Guide, Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">New Generator API vs Legacy</a></li>
<li><a href="#s2">Uniform &amp; Integer Generation</a></li>
<li><a href="#s3">Distributions</a></li>
<li><a href="#s4">Seeds &amp; Reproducibility</a></li>
<li><a href="#s5">Shuffling &amp; Sampling</a></li>
<li><a href="#s6">Permutations</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; New Generator API vs Legacy</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># NEW API (recommended &mdash; NumPy 1.17+)</span>
rng = np.random.default_rng(seed=<span class="nm">42</span>)
<span class="bi">print</span>(rng.random(<span class="nm">5</span>))              <span class="cm"># 5 uniform [0,1)</span>
<span class="bi">print</span>(rng.integers(<span class="nm">0</span>, <span class="nm">100</span>, <span class="nm">5</span>))   <span class="cm"># 5 random ints [0,100)</span>
<span class="bi">print</span>(rng.standard_normal(<span class="nm">5</span>))     <span class="cm"># 5 standard normal</span>

<span class="cm"># LEGACY API (still widely used in tutorials)</span>
np.random.seed(<span class="nm">42</span>)
<span class="bi">print</span>(np.random.rand(<span class="nm">5</span>))          <span class="cm"># 5 uniform [0,1)</span>
<span class="bi">print</span>(np.random.randn(<span class="nm">5</span>))         <span class="cm"># 5 standard normal</span>
<span class="bi">print</span>(np.random.randint(<span class="nm">0</span>,<span class="nm">100</span>,<span class="nm">5</span>)) <span class="cm"># 5 random ints [0,100)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0.773 0.438 0.859 0.697 0.094]<br>[72 10 35 81 24]</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Best Practice</strong><p>Use the new <code>default_rng()</code> API. It has better statistical properties, is thread-safe, and supports modern seeding. The legacy API is maintained for backward compatibility.</p></div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Uniform &amp; Integer Generation</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">rng = np.random.default_rng(<span class="nm">42</span>)

<span class="cm"># Uniform [0, 1)</span>
<span class="bi">print</span>(rng.random((<span class="nm">2</span>,<span class="nm">3</span>)))  <span class="cm"># 2x3 matrix</span>

<span class="cm"># Uniform [low, high)</span>
<span class="bi">print</span>(rng.uniform(<span class="nm">5</span>, <span class="nm">10</span>, <span class="nm">4</span>))    <span class="cm"># 4 floats in [5,10)</span>

<span class="cm"># Integers [low, high)</span>
<span class="bi">print</span>(rng.integers(<span class="nm">1</span>, <span class="nm">7</span>, <span class="nm">10</span>))   <span class="cm"># 10 dice rolls</span>
<span class="bi">print</span>(rng.integers(<span class="nm">0</span>, <span class="nm">2</span>, (<span class="nm">3</span>,<span class="nm">3</span>)))  <span class="cm"># 3x3 binary matrix</span>

<span class="cm"># Legacy equivalents</span>
np.random.seed(<span class="nm">42</span>)
<span class="bi">print</span>(np.random.rand(<span class="nm">3</span>,<span class="nm">2</span>))      <span class="cm"># 3x2 uniform</span>
<span class="bi">print</span>(np.random.randint(<span class="nm">1</span>,<span class="nm">7</span>,<span class="nm">10</span>)) <span class="cm"># 10 dice rolls</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[0.77 0.44 0.86] [0.70 0.09 0.98]]<br>[7.3 5.9 8.1 6.4]<br>[2 5 1 3 6 4 1 2 5 3]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Distributions</h2>
<table class="data-table"><thead><tr><th>Distribution</th><th>New API</th><th>Legacy API</th><th>Use Case</th></tr></thead><tbody>
<tr><td>Normal</td><td><code>rng.normal(mu, sigma, size)</code></td><td><code>np.random.normal()</code></td><td>Data simulation</td></tr>
<tr><td>Uniform</td><td><code>rng.uniform(lo, hi, size)</code></td><td><code>np.random.uniform()</code></td><td>Random init</td></tr>
<tr><td>Binomial</td><td><code>rng.binomial(n, p, size)</code></td><td><code>np.random.binomial()</code></td><td>Coin flips</td></tr>
<tr><td>Poisson</td><td><code>rng.poisson(lam, size)</code></td><td><code>np.random.poisson()</code></td><td>Event count</td></tr>
<tr><td>Exponential</td><td><code>rng.exponential(scale, size)</code></td><td><code>np.random.exponential()</code></td><td>Wait times</td></tr>
<tr><td>Multinomial</td><td><code>rng.multinomial(n, pvals)</code></td><td><code>np.random.multinomial()</code></td><td>Multi-class</td></tr>
<tr><td>Beta</td><td><code>rng.beta(a, b, size)</code></td><td><code>np.random.beta()</code></td><td>Probabilities</td></tr>
<tr><td>Gamma</td><td><code>rng.gamma(shape, scale, size)</code></td><td><code>np.random.gamma()</code></td><td>Right-skewed data</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">rng = np.random.default_rng(<span class="nm">42</span>)

<span class="cm"># Normal distribution</span>
samples = rng.normal(loc=<span class="nm">0</span>, scale=<span class="nm">1</span>, size=<span class="nm">10000</span>)
<span class="bi">print</span>(<span class="st">f"Normal: mean={samples.mean():.3f}, std={samples.std():.3f}"</span>)

<span class="cm"># Binomial (10 coin flips, fair coin, 5 experiments)</span>
flips = rng.binomial(n=<span class="nm">10</span>, p=<span class="nm">0.5</span>, size=<span class="nm">5</span>)
<span class="bi">print</span>(<span class="st">f"Coin flip heads: {flips}"</span>)  <span class="cm"># e.g., [4 6 5 3 7]</span>

<span class="cm"># Poisson (events per interval)</span>
events = rng.poisson(lam=<span class="nm">5</span>, size=<span class="nm">10</span>)
<span class="bi">print</span>(<span class="st">f"Poisson events: {events}"</span>)

<span class="cm"># Exponential (wait between events)</span>
waits = rng.exponential(scale=<span class="nm">2.0</span>, size=<span class="nm">5</span>)
<span class="bi">print</span>(<span class="st">f"Wait times: {waits.round(2)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Normal: mean=-0.003, std=0.998<br>Coin flip heads: [4 6 5 3 7]<br>Poisson: [6 4 3 7 5 4 8 2 6 5]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Seeds &amp; Reproducibility</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Same seed = same sequence EVERY TIME</span>
rng1 = np.random.default_rng(seed=<span class="nm">42</span>)
rng2 = np.random.default_rng(seed=<span class="nm">42</span>)
<span class="bi">print</span>(rng1.random(<span class="nm">3</span>))  <span class="cm"># [0.773 0.438 0.859]</span>
<span class="bi">print</span>(rng2.random(<span class="nm">3</span>))  <span class="cm"># [0.773 0.438 0.859] SAME!</span>

<span class="cm"># Legacy seeding</span>
np.random.seed(<span class="nm">42</span>)
<span class="bi">print</span>(np.random.rand(<span class="nm">3</span>))  <span class="cm"># reproducible</span>
np.random.seed(<span class="nm">42</span>)
<span class="bi">print</span>(np.random.rand(<span class="nm">3</span>))  <span class="cm"># same output</span>

<span class="cm"># SeedSequence for advanced spawning</span>
<span class="kw">from</span> numpy.random <span class="kw">import</span> SeedSequence
ss = SeedSequence(<span class="nm">12345</span>)
child_seeds = ss.spawn(<span class="nm">4</span>)  <span class="cm"># for parallel workers</span>
rngs = [np.random.default_rng(s) <span class="kw">for</span> s <span class="kw">in</span> child_seeds]</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0.773 0.438 0.859]<br>[0.773 0.438 0.859] &mdash; Same!</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Shuffling &amp; Sampling</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">rng = np.random.default_rng(<span class="nm">42</span>)

<span class="cm"># shuffle() &mdash; modifies IN-PLACE</span>
arr = np.arange(<span class="nm">10</span>)
rng.shuffle(arr)
<span class="bi">print</span>(<span class="st">f"Shuffled: {arr}"</span>)

<span class="cm"># choice() &mdash; random sampling</span>
<span class="bi">print</span>(rng.choice([<span class="st">"a"</span>,<span class="st">"b"</span>,<span class="st">"c"</span>,<span class="st">"d"</span>], size=<span class="nm">5</span>, replace=<span class="kw">True</span>))
<span class="bi">print</span>(rng.choice(<span class="nm">100</span>, size=<span class="nm">5</span>, replace=<span class="kw">False</span>))  <span class="cm"># no repeats</span>

<span class="cm"># Weighted sampling</span>
items = [<span class="st">"common"</span>, <span class="st">"uncommon"</span>, <span class="st">"rare"</span>]
weights = [<span class="nm">0.7</span>, <span class="nm">0.25</span>, <span class="nm">0.05</span>]
<span class="bi">print</span>(rng.choice(items, size=<span class="nm">10</span>, p=weights))

<span class="cm"># Legacy shuffle</span>
np.random.seed(<span class="nm">42</span>)
a = np.arange(<span class="nm">10</span>)
np.random.shuffle(a)  <span class="cm"># in-place</span>
<span class="bi">print</span>(a)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Shuffled: [8 1 5 0 7 2 9 4 3 6]<br>['b' 'a' 'c' 'a' 'd']</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Permutations</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">rng = np.random.default_rng(<span class="nm">42</span>)

<span class="cm"># permutation() &mdash; returns NEW shuffled array (original unchanged)</span>
a = np.arange(<span class="nm">10</span>)
perm = rng.permutation(a)
<span class="bi">print</span>(<span class="st">f"Original:    {a}"</span>)     <span class="cm"># unchanged</span>
<span class="bi">print</span>(<span class="st">f"Permutation: {perm}"</span>)

<span class="cm"># permutation with integer &mdash; permute range(n)</span>
<span class="bi">print</span>(rng.permutation(<span class="nm">5</span>))   <span class="cm"># e.g., [3 0 4 1 2]</span>

<span class="cm"># Common ML pattern: shuffle rows of dataset</span>
X = np.array([[<span class="nm">1</span>,<span class="nm">2</span>],[<span class="nm">3</span>,<span class="nm">4</span>],[<span class="nm">5</span>,<span class="nm">6</span>],[<span class="nm">7</span>,<span class="nm">8</span>],[<span class="nm">9</span>,<span class="nm">10</span>]])
y = np.array([<span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">0</span>, <span class="nm">1</span>, <span class="nm">0</span>])

idx = rng.permutation(<span class="bi">len</span>(X))
X_shuffled = X[idx]
y_shuffled = y[idx]
<span class="bi">print</span>(<span class="st">f"Shuffled X:\\n{X_shuffled}"</span>)
<span class="bi">print</span>(<span class="st">f"Shuffled y: {y_shuffled}"</span>)

<span class="cm"># Legacy</span>
np.random.seed(<span class="nm">0</span>)
<span class="bi">print</span>(np.random.permutation(<span class="nm">10</span>))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Original: [0 1 2 3 4 5 6 7 8 9]<br>Permutation: [8 1 5 0 7 2 9 4 3 6]</div></div></section>''',
("linear-algebra.html","Linear Algebra"),("../pandas/series-dataframe.html","Pandas Series"))

# ========== NEW: FILE HANDLING PAGE ==========
make_page("numpy/file-handling.html","File Handling","NumPy","&#x1F522;","intermediate","NumPy &rarr; File Handling",
"NumPy provides functions to save and load arrays from disk: np.save/load for binary .npy files, np.savez for compressed archives, np.savetxt/loadtxt for text CSV files, and np.genfromtxt for handling messy data with missing values.",
"NumPy User Guide",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Binary Files: save &amp; load</a></li>
<li><a href="#s2">Compressed Archives: savez</a></li>
<li><a href="#s3">Text Files: savetxt &amp; loadtxt</a></li>
<li><a href="#s4">genfromtxt (Missing Data)</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Binary Files: np.save() &amp; np.load()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> numpy <span class="kw">as</span> np

arr = np.array([[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>],[<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>]])

<span class="cm"># np.save() &mdash; save single array as .npy (binary)</span>
np.save(<span class="st">"my_array.npy"</span>, arr)

<span class="cm"># np.load() &mdash; load .npy file</span>
loaded = np.load(<span class="st">"my_array.npy"</span>)
<span class="bi">print</span>(loaded)
<span class="bi">print</span>(np.array_equal(arr, loaded))  <span class="cm"># True</span>

<span class="cm"># .npy format preserves dtype, shape, and order exactly</span>
<span class="bi">print</span>(<span class="st">f"dtype: {loaded.dtype}, shape: {loaded.shape}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[1 2 3] [4 5 6]]<br>True<br>dtype: int64, shape: (2, 3)</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Compressed Archives: np.savez()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Save multiple arrays in one .npz file</span>
a = np.array([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>])
b = np.array([[<span class="nm">4</span>,<span class="nm">5</span>],[<span class="nm">6</span>,<span class="nm">7</span>]])

np.savez(<span class="st">"arrays.npz"</span>, x=a, y=b)

<span class="cm"># Load .npz file</span>
data = np.load(<span class="st">"arrays.npz"</span>)
<span class="bi">print</span>(data.files)     <span class="cm"># ['x', 'y']</span>
<span class="bi">print</span>(data[<span class="st">'x'</span>])      <span class="cm"># [1 2 3]</span>
<span class="bi">print</span>(data[<span class="st">'y'</span>])      <span class="cm"># [[4 5] [6 7]]</span>

<span class="cm"># Compressed version (smaller file size)</span>
np.savez_compressed(<span class="st">"compressed.npz"</span>, x=a, y=b)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>files: ['x', 'y']<br>x: [1 2 3]<br>y: [[4 5] [6 7]]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Text Files: savetxt &amp; loadtxt</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">data = np.array([[<span class="nm">1.5</span>, <span class="nm">2.3</span>, <span class="nm">3.7</span>],
                 [<span class="nm">4.1</span>, <span class="nm">5.9</span>, <span class="nm">6.2</span>]])

<span class="cm"># np.savetxt() &mdash; save as human-readable text</span>
np.savetxt(<span class="st">"data.csv"</span>, data, delimiter=<span class="st">","</span>,
           header=<span class="st">"col1,col2,col3"</span>, fmt=<span class="st">"%.2f"</span>,
           comments=<span class="st">""</span>)

<span class="cm"># np.loadtxt() &mdash; load text file</span>
loaded = np.loadtxt(<span class="st">"data.csv"</span>, delimiter=<span class="st">","</span>, skiprows=<span class="nm">1</span>)
<span class="bi">print</span>(loaded)

<span class="cm"># Options for loadtxt</span>
<span class="cm"># skiprows=N    &mdash; skip N header rows</span>
<span class="cm"># usecols=(0,2) &mdash; load only columns 0 and 2</span>
<span class="cm"># dtype=float   &mdash; specify output dtype</span>
<span class="cm"># unpack=True   &mdash; transpose (cols become separate vars)</span>
col1, col2, col3 = np.loadtxt(<span class="st">"data.csv"</span>, delimiter=<span class="st">","</span>,
                               skiprows=<span class="nm">1</span>, unpack=<span class="kw">True</span>)
<span class="bi">print</span>(<span class="st">f"Column 1: {col1}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[1.5 2.3 3.7]<br> [4.1 5.9 6.2]]<br>Column 1: [1.5 4.1]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; genfromtxt (Missing Data Handling)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># np.genfromtxt() &mdash; handles missing values gracefully</span>
<span class="cm"># Suppose data.csv has missing entries:</span>
<span class="cm"># 1.0,2.0,3.0</span>
<span class="cm"># 4.0,,6.0</span>
<span class="cm"># 7.0,8.0,</span>

<span class="kw">from</span> io <span class="kw">import</span> StringIO
csv_data = <span class="st">"""1.0,2.0,3.0
4.0,,6.0
7.0,8.0,"""</span>

data = np.genfromtxt(StringIO(csv_data), delimiter=<span class="st">","</span>,
                     filling_values=<span class="nm">0</span>)
<span class="bi">print</span>(data)
<span class="cm"># [[1. 2. 3.]</span>
<span class="cm">#  [4. 0. 6.]   &mdash; missing filled with 0</span>
<span class="cm">#  [7. 8. 0.]]</span>

<span class="cm"># With NaN for missing (default)</span>
data_nan = np.genfromtxt(StringIO(csv_data), delimiter=<span class="st">","</span>)
<span class="bi">print</span>(data_nan)
<span class="cm"># [[1. 2. 3.]</span>
<span class="cm">#  [4. nan 6.]</span>
<span class="cm">#  [7. 8. nan]]</span>

<span class="cm"># Key parameters:</span>
<span class="cm"># missing_values=''   &mdash; what counts as missing</span>
<span class="cm"># filling_values=0    &mdash; what to substitute</span>
<span class="cm"># dtype=None          &mdash; auto-detect types</span>
<span class="cm"># names=True          &mdash; use first row as column names</span>
<span class="cm"># skip_header=1       &mdash; skip header rows</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[[1. 2. 3.]<br> [4. 0. 6.]<br> [7. 8. 0.]]</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>When to use which?</strong>
<ul><li><code>np.save/load</code>: Fastest. Use for NumPy-only workflows.</li>
<li><code>np.savez</code>: Multiple arrays in one file.</li>
<li><code>np.savetxt/loadtxt</code>: Human-readable CSV. Clean data only.</li>
<li><code>np.genfromtxt</code>: Messy data with missing values.</li>
<li><code>pd.read_csv</code>: Use Pandas for anything more complex.</li></ul></div></div></section>''',
("random.html","Random Module"),("../pandas/series-dataframe.html","Pandas"))

print("linear-algebra.html + random.html + file-handling.html expanded!")
