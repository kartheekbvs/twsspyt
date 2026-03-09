
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# Advanced Python
make_page("advanced/generators.html","Generators &amp; Iterators","Advanced Python","&#x26A1;","intermediate","Advanced Python &rarr; Generators",
"Generators are functions that yield values lazily using the yield keyword. They produce values one at a time, saving memory. Combined with iterators and the iterator protocol (__iter__/__next__), they enable elegant, memory-efficient data processing pipelines.",
"Fluent Python &mdash; Luciano Ramalho, Python Programming (2024)",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Iterators Protocol</a></li><li><a href="#s2">Generator Functions (yield)</a></li><li><a href="#s3">Generator Expressions</a></li><li><a href="#s4">Chaining &amp; Pipelines</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; The Iterator Protocol</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Any object with __iter__() and __next__() is an iterator</span>
<span class="kw">class</span> <span class="cl">CountDown</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, start):
        self.current = start
    <span class="kw">def</span> <span class="fn">__iter__</span>(self): <span class="kw">return</span> self
    <span class="kw">def</span> <span class="fn">__next__</span>(self):
        <span class="kw">if</span> self.current &lt;= <span class="nm">0</span>: <span class="kw">raise</span> <span class="cl">StopIteration</span>
        self.current -= <span class="nm">1</span>
        <span class="kw">return</span> self.current + <span class="nm">1</span>

<span class="kw">for</span> n <span class="kw">in</span> CountDown(<span class="nm">3</span>):
    <span class="bi">print</span>(n, end=<span class="st">" "</span>)  <span class="cm"># 3 2 1</span>

<span class="cm"># Built-in iter() / next()</span>
it = <span class="bi">iter</span>([<span class="nm">10</span>,<span class="nm">20</span>,<span class="nm">30</span>])
<span class="bi">print</span>(<span class="bi">next</span>(it))  <span class="cm"># 10</span>
<span class="bi">print</span>(<span class="bi">next</span>(it))  <span class="cm"># 20</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>3 2 1<br>10<br>20</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Generator Functions (yield)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">def</span> <span class="fn">fibonacci</span>(n):
    <span class="st">"""Yield first n Fibonacci numbers lazily."""</span>
    a, b = <span class="nm">0</span>, <span class="nm">1</span>
    <span class="kw">for</span> _ <span class="kw">in</span> <span class="bi">range</span>(n):
        <span class="kw">yield</span> a         <span class="cm"># pauses here, returns value</span>
        a, b = b, a + b  <span class="cm"># resumes on next()</span>

<span class="cm"># Lazy &mdash; values computed on demand</span>
gen = fibonacci(<span class="nm">10</span>)
<span class="bi">print</span>(<span class="bi">type</span>(gen))         <span class="cm"># &lt;class 'generator'&gt;</span>
<span class="bi">print</span>(<span class="bi">list</span>(gen))          <span class="cm"># [0,1,1,2,3,5,8,13,21,34]</span>

<span class="cm"># Memory comparison</span>
<span class="kw">import</span> sys
list_size = sys.getsizeof([i <span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">1000000</span>)])
gen_size  = sys.getsizeof(i <span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">1000000</span>))
<span class="bi">print</span>(<span class="st">f"List: {list_size:,} bytes"</span>)  <span class="cm"># ~8 MB</span>
<span class="bi">print</span>(<span class="st">f"Gen:  {gen_size} bytes"</span>)     <span class="cm"># ~200 bytes!</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>&lt;class 'generator'&gt;<br>[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]<br>List: 8,448,728 bytes<br>Gen: 200 bytes</div></div>
<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Key Insight</strong><p>Generators use <strong>constant memory</strong> regardless of data size. A list of 1M items uses ~8MB, but a generator uses only 200 bytes because it computes values on-the-fly.</p></div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Generator Expressions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Like list comprehension but with () instead of []</span>
squares = (x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>))  <span class="cm"># generator</span>
<span class="bi">print</span>(<span class="bi">sum</span>(squares))  <span class="cm"># 285</span>

<span class="cm"># Can be passed directly to functions</span>
<span class="bi">print</span>(<span class="bi">max</span>(x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>)))  <span class="cm"># 81</span>
<span class="bi">print</span>(<span class="st">","</span>.join(<span class="bi">str</span>(i) <span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">5</span>)))  <span class="cm"># 0,1,2,3,4</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>285<br>81<br>0,1,2,3,4</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Generator Pipelines</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">def</span> <span class="fn">read_lines</span>(filename):
    <span class="kw">with</span> <span class="bi">open</span>(filename) <span class="kw">as</span> f:
        <span class="kw">for</span> line <span class="kw">in</span> f: <span class="kw">yield</span> line.strip()

<span class="kw">def</span> <span class="fn">filter_comments</span>(lines):
    <span class="kw">for</span> line <span class="kw">in</span> lines:
        <span class="kw">if</span> <span class="kw">not</span> line.startswith(<span class="st">"#"</span>): <span class="kw">yield</span> line

<span class="kw">def</span> <span class="fn">to_upper</span>(lines):
    <span class="kw">for</span> line <span class="kw">in</span> lines: <span class="kw">yield</span> line.upper()

<span class="cm"># Pipeline: read &rarr; filter &rarr; transform (all lazy!)</span>
<span class="cm"># pipeline = to_upper(filter_comments(read_lines("data.txt")))</span>
<span class="cm"># for line in pipeline: print(line)</span>

<span class="cm"># yield from (delegate to sub-generator)</span>
<span class="kw">def</span> <span class="fn">chain</span>(*iterables):
    <span class="kw">for</span> it <span class="kw">in</span> iterables:
        <span class="kw">yield from</span> it  <span class="cm"># equivalent to: for x in it: yield x</span>

<span class="bi">print</span>(<span class="bi">list</span>(chain([<span class="nm">1</span>,<span class="nm">2</span>], [<span class="nm">3</span>,<span class="nm">4</span>], [<span class="nm">5</span>])))  <span class="cm"># [1,2,3,4,5]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1, 2, 3, 4, 5]</div></div></section>''',
("../oop/decorators.html","Decorators"),("comprehensions.html","Comprehensions"))

make_page("advanced/lambda.html","Lambda &amp; Functional Programming","Advanced Python","&#x26A1;","intermediate","Advanced Python &rarr; Lambda &amp; Functional",
"Lambda functions are anonymous, one-expression functions. Combined with map(), filter(), reduce(), and functools, they enable a functional programming style in Python. This covers closures, higher-order functions, and partial application.",
"Python Programming (2024), Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Lambda Functions</a></li><li><a href="#s2">map, filter, reduce</a></li><li><a href="#s3">Closures</a></li><li><a href="#s4">functools Utilities</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Lambda Functions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># lambda args: expression</span>
square = <span class="kw">lambda</span> x: x ** <span class="nm">2</span>
<span class="bi">print</span>(square(<span class="nm">5</span>))  <span class="cm"># 25</span>

add = <span class="kw">lambda</span> a, b: a + b
<span class="bi">print</span>(add(<span class="nm">3</span>, <span class="nm">4</span>))  <span class="cm"># 7</span>

<span class="cm"># Common use: sorting key</span>
pairs = [(<span class="st">"b"</span>,<span class="nm">2</span>), (<span class="st">"a"</span>,<span class="nm">1</span>), (<span class="st">"c"</span>,<span class="nm">3</span>)]
<span class="bi">print</span>(<span class="bi">sorted</span>(pairs, key=<span class="kw">lambda</span> x: x[<span class="nm">1</span>]))
<span class="cm"># [('a',1), ('b',2), ('c',3)]</span>

<span class="cm"># Conditional expression in lambda</span>
classify = <span class="kw">lambda</span> x: <span class="st">"even"</span> <span class="kw">if</span> x%<span class="nm">2</span>==<span class="nm">0</span> <span class="kw">else</span> <span class="st">"odd"</span>
<span class="bi">print</span>(classify(<span class="nm">7</span>))  <span class="cm"># odd</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>25<br>7<br>[('a',1), ('b',2), ('c',3)]<br>odd</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; map, filter, reduce</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># map(func, iterable) &mdash; apply func to each element</span>
nums = [<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>,<span class="nm">5</span>]
squared = <span class="bi">list</span>(<span class="bi">map</span>(<span class="kw">lambda</span> x: x**<span class="nm">2</span>, nums))
<span class="bi">print</span>(squared)  <span class="cm"># [1,4,9,16,25]</span>

<span class="cm"># filter(func, iterable) &mdash; keep elements where func returns True</span>
evens = <span class="bi">list</span>(<span class="bi">filter</span>(<span class="kw">lambda</span> x: x%<span class="nm">2</span>==<span class="nm">0</span>, nums))
<span class="bi">print</span>(evens)    <span class="cm"># [2, 4]</span>

<span class="cm"># reduce(func, iterable) &mdash; accumulate</span>
<span class="kw">from</span> functools <span class="kw">import</span> reduce
total = reduce(<span class="kw">lambda</span> a, b: a + b, nums)
<span class="bi">print</span>(total)    <span class="cm"># 15</span>

product = reduce(<span class="kw">lambda</span> a, b: a * b, nums)
<span class="bi">print</span>(product)  <span class="cm"># 120 (5!)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1, 4, 9, 16, 25]<br>[2, 4]<br>15<br>120</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Prefer Comprehensions</strong><p>In modern Python, list/generator comprehensions are preferred over <code>map()</code>/<code>filter()</code> for readability: <code>[x**2 for x in nums]</code> beats <code>list(map(lambda x: x**2, nums))</code>.</p></div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Closures</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">def</span> <span class="fn">multiplier</span>(factor):
    <span class="kw">def</span> <span class="fn">inner</span>(x):
        <span class="kw">return</span> x * factor  <span class="cm"># captures 'factor' from enclosing scope</span>
    <span class="kw">return</span> inner

double = multiplier(<span class="nm">2</span>)
triple = multiplier(<span class="nm">3</span>)
<span class="bi">print</span>(double(<span class="nm">5</span>))   <span class="cm"># 10</span>
<span class="bi">print</span>(triple(<span class="nm">5</span>))   <span class="cm"># 15</span>
<span class="bi">print</span>(double.__closure__[<span class="nm">0</span>].cell_contents)  <span class="cm"># 2</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>10<br>15<br>2</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; functools Utilities</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> functools <span class="kw">import</span> partial, lru_cache

<span class="cm"># partial &mdash; freeze some arguments</span>
<span class="kw">def</span> <span class="fn">power</span>(base, exp):
    <span class="kw">return</span> base ** exp

square = partial(power, exp=<span class="nm">2</span>)
cube   = partial(power, exp=<span class="nm">3</span>)
<span class="bi">print</span>(square(<span class="nm">5</span>))  <span class="cm"># 25</span>
<span class="bi">print</span>(cube(<span class="nm">5</span>))    <span class="cm"># 125</span>

<span class="cm"># lru_cache &mdash; memoization</span>
@lru_cache(maxsize=<span class="nm">128</span>)
<span class="kw">def</span> <span class="fn">fib</span>(n):
    <span class="kw">if</span> n &lt; <span class="nm">2</span>: <span class="kw">return</span> n
    <span class="kw">return</span> fib(n-<span class="nm">1</span>) + fib(n-<span class="nm">2</span>)

<span class="bi">print</span>(fib(<span class="nm">50</span>))  <span class="cm"># 12586269025 (instant with cache!)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>25<br>125<br>12586269025</div></div></section>''',
("comprehensions.html","Comprehensions"),("context-managers.html","Context Managers"))

make_page("advanced/context-managers.html","Context Managers","Advanced Python","&#x26A1;","intermediate","Advanced Python &rarr; Context Managers",
"Context managers handle resource setup and cleanup automatically using the with statement. They implement __enter__/__exit__ or use @contextmanager. Essential for file handling, database connections, locks, and transactions.",
"Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">The with Statement</a></li><li><a href="#s2">Custom Context Managers</a></li><li><a href="#s3">@contextmanager Decorator</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; The with Statement</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># with ensures cleanup even if exceptions occur</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"file.txt"</span>, <span class="st">"w"</span>) <span class="kw">as</span> f:
    f.write(<span class="st">"hello"</span>)
<span class="cm"># f is guaranteed closed here</span>

<span class="cm"># Equivalent without 'with':</span>
f = <span class="bi">open</span>(<span class="st">"file.txt"</span>, <span class="st">"w"</span>)
<span class="kw">try</span>:
    f.write(<span class="st">"hello"</span>)
<span class="kw">finally</span>:
    f.close()  <span class="cm"># must remember to close!</span></pre></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Custom Context Manager (Class)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> time

<span class="kw">class</span> <span class="cl">Timer</span>:
    <span class="kw">def</span> <span class="fn">__enter__</span>(self):
        self.start = time.time()
        <span class="kw">return</span> self

    <span class="kw">def</span> <span class="fn">__exit__</span>(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        <span class="bi">print</span>(<span class="st">f"Elapsed: {self.elapsed:.4f}s"</span>)
        <span class="kw">return</span> <span class="kw">False</span>  <span class="cm"># don't suppress exceptions</span>

<span class="kw">with</span> Timer() <span class="kw">as</span> t:
    <span class="bi">sum</span>(i**<span class="nm">2</span> <span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">1000000</span>))
<span class="cm"># Elapsed: 0.0832s</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Elapsed: 0.0832s</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; @contextmanager Decorator</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> contextlib <span class="kw">import</span> contextmanager

@contextmanager
<span class="kw">def</span> <span class="fn">managed_resource</span>(name):
    <span class="bi">print</span>(<span class="st">f"Acquiring {name}"</span>)   <span class="cm"># __enter__</span>
    <span class="kw">try</span>:
        <span class="kw">yield</span> name                  <span class="cm"># value for 'as'</span>
    <span class="kw">finally</span>:
        <span class="bi">print</span>(<span class="st">f"Releasing {name}"</span>)  <span class="cm"># __exit__</span>

<span class="kw">with</span> managed_resource(<span class="st">"DB Connection"</span>) <span class="kw">as</span> r:
    <span class="bi">print</span>(<span class="st">f"Using {r}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Acquiring DB Connection<br>Using DB Connection<br>Releasing DB Connection</div></div></section>''',
("lambda.html","Lambda &amp; Functional"),("async.html","Async &amp; Await"))

make_page("advanced/async.html","Async &amp; Await","Advanced Python","&#x26A1;","advanced","Advanced Python &rarr; Async &amp; Await",
"Python's asyncio module enables concurrent programming with async/await syntax. It uses an event loop to manage coroutines, allowing thousands of I/O operations concurrently without threads. Essential for web servers, API clients, and data pipelines.",
"Python Programming (2024)",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Coroutines &amp; async def</a></li><li><a href="#s2">asyncio.gather</a></li><li><a href="#s3">Async Context Managers</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Coroutines &amp; async def</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> asyncio

<span class="kw">async def</span> <span class="fn">fetch_data</span>(name, delay):
    <span class="bi">print</span>(<span class="st">f"Fetching {name}..."</span>)
    <span class="kw">await</span> asyncio.sleep(delay)     <span class="cm"># non-blocking sleep</span>
    <span class="bi">print</span>(<span class="st">f"{name} done!"</span>)
    <span class="kw">return</span> <span class="st">f"{name}_data"</span>

<span class="kw">async def</span> <span class="fn">main</span>():
    result = <span class="kw">await</span> fetch_data(<span class="st">"API"</span>, <span class="nm">1</span>)
    <span class="bi">print</span>(result)

asyncio.run(main())   <span class="cm"># entry point</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Fetching API...<br>API done!<br>API_data</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Concurrent Tasks with gather</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">async def</span> <span class="fn">main</span>():
    <span class="cm"># Run 3 tasks concurrently (total ~2s, not 6s)</span>
    results = <span class="kw">await</span> asyncio.gather(
        fetch_data(<span class="st">"API_1"</span>, <span class="nm">2</span>),
        fetch_data(<span class="st">"API_2"</span>, <span class="nm">1</span>),
        fetch_data(<span class="st">"API_3"</span>, <span class="nm">1.5</span>),
    )
    <span class="bi">print</span>(results)

asyncio.run(main())
<span class="cm"># All 3 run concurrently &mdash; total time ~2 seconds!</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Fetching API_1...<br>Fetching API_2...<br>Fetching API_3...<br>API_2 done!<br>API_3 done!<br>API_1 done!<br>['API_1_data', 'API_2_data', 'API_3_data']</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Async Context Managers</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">AsyncDB</span>:
    <span class="kw">async def</span> <span class="fn">__aenter__</span>(self):
        <span class="bi">print</span>(<span class="st">"Connecting..."</span>)
        <span class="kw">await</span> asyncio.sleep(<span class="nm">0.1</span>)
        <span class="kw">return</span> self

    <span class="kw">async def</span> <span class="fn">__aexit__</span>(self, *args):
        <span class="bi">print</span>(<span class="st">"Disconnecting..."</span>)
        <span class="kw">await</span> asyncio.sleep(<span class="nm">0.1</span>)

    <span class="kw">async def</span> <span class="fn">query</span>(self, sql):
        <span class="kw">await</span> asyncio.sleep(<span class="nm">0.1</span>)
        <span class="kw">return</span> [<span class="st">"row1"</span>, <span class="st">"row2"</span>]

<span class="kw">async def</span> <span class="fn">main</span>():
    <span class="kw">async with</span> AsyncDB() <span class="kw">as</span> db:
        rows = <span class="kw">await</span> db.query(<span class="st">"SELECT *"</span>)
        <span class="bi">print</span>(rows)

asyncio.run(main())</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Connecting...<br>['row1', 'row2']<br>Disconnecting...</div></div></section>''',
("context-managers.html","Context Managers"),("../numpy/arrays.html","NumPy Arrays"))

print("Batch 4: Advanced Python pages done (generators, lambda, context-managers, async).")
