import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# RANDOM & SIMULATIONS
make_page("numpy/random.html","Random Sampling &amp; Simulations","NumPy","&#x1F522;","intermediate","NumPy &rarr; Random",
"Randomness is key to simulations and ML. This section covers textbook definitions for distributions and PRNG state management.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">PRNG State</a></li>
<li><a href="#s2">Return Value: np.random.seed()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; PRNG State</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"NumPy's random number generation functions are not truly random; they are <em>pseudo-random</em>. They use algorithms to generate sequences of numbers that follow a specific distribution." &mdash; <em>Wes McKinney</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: np.random.seed()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Calling <code>np.random.seed()</code> returns <strong>None</strong>. It is a side-effect function that modifies the global internal state of the random number generator to ensure reproducibility.</p>
</div>
</section>''',
("operations.html","Operations"),("linalg.html","Linear Algebra"),
[("operations.html", "Mathematical Functions"), ("linalg.html", "Vector Operations")])

print("random.html expanded!")
