import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# LAMBDA, MAP, FILTER
make_page("advanced/lambda.html","Lambda, Map, Filter &amp; Reduce","Advanced Python","&#x2699;&#xFE0F;","intermediate","Advanced &rarr; Lambda",
"Lambda functions are anonymous one-liner functions. Combined with map(), filter(), and reduce(), they enable powerful functional programming patterns in Python. This section explores their formal definitions, behavior, and return values.",
"Python Docs, Fluent Python &mdash; Luciano Ramalho, Learning Python &mdash; Mark Lutz",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Lambda Functions (Anonymous Functions)</a></li>
<li><a href="#s2">map(): Transformation</a></li>
<li><a href="#s3">filter(): Selection</a></li>
<li><a href="#s4">reduce(): Aggregation</a></li>
<li><a href="#s5">Custom Sorting with Lambda</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Lambda Functions</h2>
<p>In computer science, a <strong>lambda abstraction</strong> is the definition of an anonymous function. In Python, the <code>lambda</code> keyword creates a function object that can be used anywhere a function is expected, but without a formal name (unless assigned to a variable).</p>

<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"A lambda is an expression that creates a function object, but it is limited to a single expression. It is often called an 'anonymous function' because it doesn't require a <code>def</code> statement or a name." &mdash; <em>Learning Python, Mark Lutz</em></p>
    </div>
</div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Anonymous function to square a number</span>
square = <span class="kw">lambda</span> x: x ** <span class="nm">2</span>
<span class="bi">print</span>(square(<span class="nm">5</span>))  <span class="cm"># Output: 25</span>

<span class="cm"># Immediately Invoked Function Expression (IIFE)</span>
<span class="bi">print</span>((<span class="kw">lambda</span> x, y: x + y)(<span class="nm">10</span>, <span class="nm">20</span>))  <span class="cm"># Output: 30</span></pre>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>A <code>lambda</code> expression returns a <strong>function object</strong> at runtime. This object behaves exactly like a function defined with <code>def</code>, but it is restricted to a single expression whose result is the function's return value.</p>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; map(): Functional Transformation</h2>
<p>The <code>map(function, iterable)</code> function applies a given function to every item of an iterable (list, tuple, etc.) and returns a map object.</p>

<div class="callout tip">
    <div class="callout-icon">💡</div>
    <div class="callout-content">
        <strong>FastAPI Style Tip</strong>
        <p>In modern Python, list comprehensions are often preferred over <code>map()</code> for readability, but <code>map()</code> is highly efficient when using built-in functions.</p>
    </div>
</div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">names = [<span class="st">"alice"</span>, <span class="st">"bob"</span>, <span class="st">"charlie"</span>]
upper_names = <span class="bi">map</span>(<span class="bi">str</span>.upper, names)
<span class="bi">print</span>(<span class="bi">list</span>(upper_names))  <span class="cm"># ['ALICE', 'BOB', 'CHARLIE']</span></pre>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>In Python 3.x, <code>map()</code> returns an <strong>iterator</strong> (specifically a <code>map object</code>). It is <em>lazy</em>, meaning it doesn't compute the values until you iterate over it (e.g., using <code>list()</code> or a <code>for</code> loop).</p>
</div>
</section>

<section class="content-section" id="s3"><h2>3 &middot; filter(): Boolean Selection</h2>
<p><code>filter(function, iterable)</code> constructs an iterator from those elements of an iterable for which the function returns true.</p>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">numbers = [<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>, <span class="nm">6</span>]
evens = <span class="bi">filter</span>(<span class="kw">lambda</span> x: x % <span class="nm">2</span> == <span class="nm">0</span>, numbers)
<span class="bi">print</span>(<span class="bi">list</span>(evens))  <span class="cm"># [2, 4, 6]</span></pre>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Similar to <code>map()</code>, <code>filter()</code> returns a <strong>filter object</strong> (an iterator). Elements are processed only when requested, saving memory for large datasets.</p>
</div>
</section>''',
("../python/functions.html","Functions"), ("../advanced/comprehensions.html","Comprehensions"),
[("../python/functions.html", "Standard Functions"), ("../advanced/generators.html", "Generators"), ("../advanced/comprehensions.html", "List Comprehensions")])

# COMPREHENSIONS
make_page("advanced/comprehensions.html","List, Dict &amp; Set Comprehensions","Advanced Python","&#x2699;&#xFE0F;","intermediate","Advanced &rarr; Comprehensions",
"Comprehensions provide a concise way to create lists, dictionaries, and sets. They are often more efficient and readable than traditional loops.",
"Fluent Python &mdash; Luciano Ramalho, Python Cookbook",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">List Comprehensions</a></li>
<li><a href="#s2">Dict &amp; Set Comprehensions</a></li>
<li><a href="#s3">Conditional Comprehensions</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; List Comprehensions</h2>
<p>A list comprehension consists of brackets containing an expression followed by a <code>for</code> clause, then zero or more <code>for</code> or <code>if</code> clauses.</p>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">squares = [x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">5</span>)]
<span class="bi">print</span>(squares)  <span class="cm"># [0, 1, 4, 9, 16]</span></pre>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>A list comprehension returns a <strong>new List object</strong> containing the results of the expression for each item.</p>
</div>
</section>''',
("lambda.html","Lambda"),("generators.html","Generators"),
[("lambda.html", "Lambda Functions"), ("generators.html", "Generators")])

# GENERATORS
make_page("advanced/generators.html","Generators &amp; Iterators","Advanced Python","&#x2699;&#xFE0F;","advanced","Advanced &rarr; Generators",
"Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data.",
"Python Docs, Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Generator Functions (yield)</a></li>
<li><a href="#s2">Generator Expressions</a></li>
<li><a href="#s3">Memory Efficiency</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Generator Functions</h2>
<p>When a generator function is called, it returns a generator object without even beginning execution of the function. When <code>next()</code> is called, the function resumes execution until a <code>yield</code> is reached.</p>

<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"A generator is a function that remembers its state between calls. Unlike regular functions that start from the top every time, generators 'resume' where they left off." &mdash; <em>Fluent Python</em></p>
    </div>
</div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">def</span> <span class="bi">countdown</span>(n):
    <span class="kw">while</span> n > <span class="nm">0</span>:
        <span class="kw">yield</span> n
        n -= <span class="nm">1</span>

counter = countdown(<span class="nm">3</span>)
<span class="bi">print</span>(<span class="bi">next</span>(counter))  <span class="cm"># 3</span>
<span class="bi">print</span>(<span class="bi">next</span>(counter))  <span class="cm"># 2</span></pre>
</div>

<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Calling a generator function returns a <strong>generator iterator object</strong>. It does <em>not</em> return the value yielded; you must iterate over the generator object to retrieve values.</p>
</div>
</section>''',
("comprehensions.html","Comprehensions"),("context-managers.html","Context Managers"),
[("comprehensions.html", "List Comprehensions"), ("lambda.html", "Lambda and Map")])

print("lambda.html + comprehensions.html + generators.html expanded with enriched content!")
