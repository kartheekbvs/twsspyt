import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# LAMBDA
make_page("advanced/lambda.html","Lambda, Map, Filter &amp; Reduce","Advanced Python","&#x2699;&#xFE0F;","intermediate","Advanced &rarr; Lambda",
"Lambda functions are anonymous one-liner functions. Combined with map(), filter(), and reduce(), they enable powerful functional programming patterns in Python. Covers lambda syntax, map, filter, reduce, functools, sorted with key, and practical examples.",
"Python Docs, Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Lambda Functions</a></li>
<li><a href="#s2">map()</a></li>
<li><a href="#s3">filter()</a></li>
<li><a href="#s4">reduce()</a></li>
<li><a href="#s5">sorted() with key</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Lambda Functions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Regular function vs lambda</span>
<span class="kw">def</span> <span class="bi">square</span>(x):
    <span class="kw">return</span> x ** <span class="nm">2</span>

square_lambda = <span class="kw">lambda</span> x: x ** <span class="nm">2</span>

<span class="bi">print</span>(square(<span class="nm">5</span>))          <span class="cm"># 25</span>
<span class="bi">print</span>(square_lambda(<span class="nm">5</span>))   <span class="cm"># 25</span>

<span class="cm"># Multiple arguments</span>
add = <span class="kw">lambda</span> a, b: a + b
<span class="bi">print</span>(add(<span class="nm">3</span>, <span class="nm">7</span>))  <span class="cm"># 10</span>

<span class="cm"># With default arguments</span>
power = <span class="kw">lambda</span> x, n=<span class="nm">2</span>: x ** n
<span class="bi">print</span>(power(<span class="nm">3</span>))     <span class="cm"># 9 (default n=2)</span>
<span class="bi">print</span>(power(<span class="nm">3</span>, <span class="nm">3</span>))  <span class="cm"># 27</span>

<span class="cm"># Conditional expression</span>
classify = <span class="kw">lambda</span> x: <span class="st">"positive"</span> <span class="kw">if</span> x > <span class="nm">0</span> <span class="kw">else</span> (<span class="st">"zero"</span> <span class="kw">if</span> x == <span class="nm">0</span> <span class="kw">else</span> <span class="st">"negative"</span>)
<span class="bi">print</span>(classify(-<span class="nm">5</span>))  <span class="cm"># negative</span>
<span class="bi">print</span>(classify(<span class="nm">0</span>))   <span class="cm"># zero</span>

<span class="cm"># Immediately invoked (IIFE)</span>
result = (<span class="kw">lambda</span> x, y: x * y)(<span class="nm">4</span>, <span class="nm">5</span>)
<span class="bi">print</span>(result)  <span class="cm"># 20</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>25 &middot; 10 &middot; 9 &middot; 27 &middot; negative &middot; zero &middot; 20</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; map()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Apply function to every element</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">nums = [<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>]

<span class="cm"># Square each number</span>
squared = <span class="bi">list</span>(<span class="bi">map</span>(<span class="kw">lambda</span> x: x**<span class="nm">2</span>, nums))
<span class="bi">print</span>(squared)  <span class="cm"># [1, 4, 9, 16, 25]</span>

<span class="cm"># Convert temperatures</span>
celsius = [<span class="nm">0</span>, <span class="nm">20</span>, <span class="nm">37</span>, <span class="nm">100</span>]
fahrenheit = <span class="bi">list</span>(<span class="bi">map</span>(<span class="kw">lambda</span> c: c * <span class="nm">9</span>/<span class="nm">5</span> + <span class="nm">32</span>, celsius))
<span class="bi">print</span>(fahrenheit)  <span class="cm"># [32.0, 68.0, 98.6, 212.0]</span>

<span class="cm"># Multiple iterables</span>
a = [<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>]
b = [<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>]
sums = <span class="bi">list</span>(<span class="bi">map</span>(<span class="kw">lambda</span> x, y: x + y, a, b))
<span class="bi">print</span>(sums)  <span class="cm"># [11, 22, 33]</span>

<span class="cm"># String operations</span>
names = [<span class="st">"alice"</span>, <span class="st">"BOB"</span>, <span class="st">"Charlie"</span>]
title_names = <span class="bi">list</span>(<span class="bi">map</span>(<span class="bi">str</span>.title, names))
<span class="bi">print</span>(title_names)  <span class="cm"># ['Alice', 'Bob', 'Charlie']</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1, 4, 9, 16, 25]<br>[32.0, 68.0, 98.6, 212.0]<br>[11, 22, 33]<br>['Alice', 'Bob', 'Charlie']</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; filter()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Keep elements that pass a test</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">nums = [<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>, <span class="nm">6</span>, <span class="nm">7</span>, <span class="nm">8</span>, <span class="nm">9</span>, <span class="nm">10</span>]

<span class="cm"># Even numbers only</span>
evens = <span class="bi">list</span>(<span class="bi">filter</span>(<span class="kw">lambda</span> x: x % <span class="nm">2</span> == <span class="nm">0</span>, nums))
<span class="bi">print</span>(evens)  <span class="cm"># [2, 4, 6, 8, 10]</span>

<span class="cm"># Filter strings by length</span>
words = [<span class="st">"hi"</span>, <span class="st">"hello"</span>, <span class="st">"hey"</span>, <span class="st">"greetings"</span>, <span class="st">"yo"</span>]
long_words = <span class="bi">list</span>(<span class="bi">filter</span>(<span class="kw">lambda</span> w: <span class="bi">len</span>(w) > <span class="nm">3</span>, words))
<span class="bi">print</span>(long_words)  <span class="cm"># ['hello', 'greetings']</span>

<span class="cm"># Remove None/empty values</span>
data = [<span class="nm">0</span>, <span class="st">""</span>, <span class="kw">None</span>, <span class="nm">42</span>, <span class="st">"hello"</span>, [], <span class="kw">False</span>]
truthy = <span class="bi">list</span>(<span class="bi">filter</span>(<span class="kw">None</span>, data))
<span class="bi">print</span>(truthy)  <span class="cm"># [42, 'hello']</span>

<span class="cm"># Chain map + filter</span>
result = <span class="bi">list</span>(<span class="bi">map</span>(<span class="kw">lambda</span> x: x**<span class="nm">2</span>,
              <span class="bi">filter</span>(<span class="kw">lambda</span> x: x % <span class="nm">2</span> == <span class="nm">0</span>, nums)))
<span class="bi">print</span>(result)  <span class="cm"># [4, 16, 36, 64, 100]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[2, 4, 6, 8, 10]<br>['hello', 'greetings']<br>[42, 'hello']<br>[4, 16, 36, 64, 100]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; reduce()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Accumulate into single value</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> functools <span class="kw">import</span> reduce

nums = [<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>, <span class="nm">5</span>]

<span class="cm"># Sum (1+2+3+4+5 = 15)</span>
total = reduce(<span class="kw">lambda</span> a, b: a + b, nums)
<span class="bi">print</span>(total)  <span class="cm"># 15</span>

<span class="cm"># Product (1*2*3*4*5 = 120)</span>
product = reduce(<span class="kw">lambda</span> a, b: a * b, nums)
<span class="bi">print</span>(product)  <span class="cm"># 120</span>

<span class="cm"># Max</span>
maximum = reduce(<span class="kw">lambda</span> a, b: a <span class="kw">if</span> a > b <span class="kw">else</span> b, nums)
<span class="bi">print</span>(maximum)  <span class="cm"># 5</span>

<span class="cm"># With initial value</span>
total_with_init = reduce(<span class="kw">lambda</span> a, b: a + b, nums, <span class="nm">100</span>)
<span class="bi">print</span>(total_with_init)  <span class="cm"># 115 (100 + 15)</span>

<span class="cm"># Flatten nested list</span>
nested = [[<span class="nm">1</span>,<span class="nm">2</span>], [<span class="nm">3</span>,<span class="nm">4</span>], [<span class="nm">5</span>,<span class="nm">6</span>]]
flat = reduce(<span class="kw">lambda</span> a, b: a + b, nested)
<span class="bi">print</span>(flat)  <span class="cm"># [1, 2, 3, 4, 5, 6]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>15 &middot; 120 &middot; 5 &middot; 115 &middot; [1, 2, 3, 4, 5, 6]</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; sorted() with key</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Sort by custom key using lambda</span>
students = [(<span class="st">"Alice"</span>, <span class="nm">85</span>), (<span class="st">"Bob"</span>, <span class="nm">92</span>), (<span class="st">"Charlie"</span>, <span class="nm">78</span>)]

<span class="cm"># By score</span>
by_score = <span class="bi">sorted</span>(students, key=<span class="kw">lambda</span> s: s[<span class="nm">1</span>], reverse=<span class="kw">True</span>)
<span class="bi">print</span>(by_score)  <span class="cm"># [('Bob', 92), ('Alice', 85), ('Charlie', 78)]</span>

<span class="cm"># Sort strings by length</span>
words = [<span class="st">"python"</span>, <span class="st">"is"</span>, <span class="st">"awesome"</span>, <span class="st">"and"</span>, <span class="st">"fun"</span>]
<span class="bi">print</span>(<span class="bi">sorted</span>(words, key=<span class="bi">len</span>))
<span class="cm"># ['is', 'and', 'fun', 'python', 'awesome']</span>

<span class="cm"># Sort dicts</span>
people = [{<span class="st">"name"</span>:<span class="st">"Alice"</span>,<span class="st">"age"</span>:<span class="nm">30</span>}, {<span class="st">"name"</span>:<span class="st">"Bob"</span>,<span class="st">"age"</span>:<span class="nm">25</span>}]
<span class="bi">print</span>(<span class="bi">sorted</span>(people, key=<span class="kw">lambda</span> p: p[<span class="st">"age"</span>]))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[('Bob', 92), ('Alice', 85), ('Charlie', 78)]<br>['is', 'and', 'fun', 'python', 'awesome']</div></div></section>''',
("../oop/decorators.html","Decorators"),("comprehensions.html","Comprehensions"))

# COMPREHENSIONS
make_page("advanced/comprehensions.html","List, Dict &amp; Set Comprehensions","Advanced Python","&#x2699;&#xFE0F;","intermediate","Advanced &rarr; Comprehensions",
"Comprehensions are concise one-liner ways to create lists, dicts, and sets. They replace verbose loops with elegant, readable expressions. Covers list comprehensions, dict comprehensions, set comprehensions, nested comprehensions, conditional expressions, and walrus operator.",
"Python Docs, Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">List Comprehensions</a></li>
<li><a href="#s2">Conditionals in Comprehensions</a></li>
<li><a href="#s3">Nested Comprehensions</a></li>
<li><a href="#s4">Dict &amp; Set Comprehensions</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; List Comprehensions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Syntax: [expression for item in iterable]</span>

<span class="cm"># Squares</span>
squares = [x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>)]
<span class="bi">print</span>(squares)  <span class="cm"># [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]</span>

<span class="cm"># String operations</span>
words = [<span class="st">"hello"</span>, <span class="st">"world"</span>, <span class="st">"python"</span>]
upper = [w.upper() <span class="kw">for</span> w <span class="kw">in</span> words]
<span class="bi">print</span>(upper)  <span class="cm"># ['HELLO', 'WORLD', 'PYTHON']</span>

<span class="cm"># Vs traditional loop (same result)</span>
result = []
<span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>):
    result.append(x**<span class="nm">2</span>)
<span class="cm"># Comprehension is ~30% faster!</span>

<span class="cm"># With function calls</span>
lengths = [<span class="bi">len</span>(w) <span class="kw">for</span> w <span class="kw">in</span> words]
<span class="bi">print</span>(lengths)  <span class="cm"># [5, 5, 6]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]<br>['HELLO', 'WORLD', 'PYTHON']<br>[5, 5, 6]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Conditionals</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Filter (if at the END)</span>
evens = [x <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">20</span>) <span class="kw">if</span> x % <span class="nm">2</span> == <span class="nm">0</span>]
<span class="bi">print</span>(evens)  <span class="cm"># [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]</span>

<span class="cm"># Transform (if/else BEFORE for)</span>
parity = [<span class="st">"even"</span> <span class="kw">if</span> x % <span class="nm">2</span> == <span class="nm">0</span> <span class="kw">else</span> <span class="st">"odd"</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">5</span>)]
<span class="bi">print</span>(parity)  <span class="cm"># ['even', 'odd', 'even', 'odd', 'even']</span>

<span class="cm"># Multiple conditions</span>
fizzbuzz = [
    <span class="st">"FizzBuzz"</span> <span class="kw">if</span> x%<span class="nm">15</span>==<span class="nm">0</span>
    <span class="kw">else</span> <span class="st">"Fizz"</span> <span class="kw">if</span> x%<span class="nm">3</span>==<span class="nm">0</span>
    <span class="kw">else</span> <span class="st">"Buzz"</span> <span class="kw">if</span> x%<span class="nm">5</span>==<span class="nm">0</span>
    <span class="kw">else</span> x
    <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">1</span>, <span class="nm">16</span>)
]
<span class="bi">print</span>(fizzbuzz)

<span class="cm"># Filter AND transform</span>
squared_evens = [x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>) <span class="kw">if</span> x % <span class="nm">2</span> == <span class="nm">0</span>]
<span class="bi">print</span>(squared_evens)  <span class="cm"># [0, 4, 16, 36, 64]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Nested Comprehensions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Flatten a 2D list</span>
matrix = [[<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], [<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>], [<span class="nm">7</span>,<span class="nm">8</span>,<span class="nm">9</span>]]
flat = [x <span class="kw">for</span> row <span class="kw">in</span> matrix <span class="kw">for</span> x <span class="kw">in</span> row]
<span class="bi">print</span>(flat)  <span class="cm"># [1, 2, 3, 4, 5, 6, 7, 8, 9]</span>

<span class="cm"># Create 2D list (matrix)</span>
grid = [[i*<span class="nm">3</span>+j <span class="kw">for</span> j <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">3</span>)] <span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">3</span>)]
<span class="bi">print</span>(grid)  <span class="cm"># [[0,1,2], [3,4,5], [6,7,8]]</span>

<span class="cm"># Transpose a matrix</span>
transposed = [[row[i] <span class="kw">for</span> row <span class="kw">in</span> matrix] <span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">3</span>)]
<span class="bi">print</span>(transposed)  <span class="cm"># [[1,4,7], [2,5,8], [3,6,9]]</span>

<span class="cm"># Cartesian product</span>
colors = [<span class="st">"red"</span>, <span class="st">"blue"</span>]
sizes = [<span class="st">"S"</span>, <span class="st">"M"</span>, <span class="st">"L"</span>]
combos = [(c, s) <span class="kw">for</span> c <span class="kw">in</span> colors <span class="kw">for</span> s <span class="kw">in</span> sizes]
<span class="bi">print</span>(combos)
<span class="cm"># [('red','S'), ('red','M'), ('red','L'), ('blue','S'), ...]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[1, 2, 3, 4, 5, 6, 7, 8, 9]<br>[[1,4,7], [2,5,8], [3,6,9]]<br>[('red','S'), ('red','M'), ('red','L'), ('blue','S'), ('blue','M'), ('blue','L')]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Dict &amp; Set Comprehensions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Dict comprehension</span>
squares_dict = {x: x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">6</span>)}
<span class="bi">print</span>(squares_dict)  <span class="cm"># {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}</span>

<span class="cm"># Swap keys and values</span>
original = {<span class="st">"a"</span>: <span class="nm">1</span>, <span class="st">"b"</span>: <span class="nm">2</span>, <span class="st">"c"</span>: <span class="nm">3</span>}
swapped = {v: k <span class="kw">for</span> k, v <span class="kw">in</span> original.items()}
<span class="bi">print</span>(swapped)  <span class="cm"># {1: 'a', 2: 'b', 3: 'c'}</span>

<span class="cm"># Filter a dict</span>
scores = {<span class="st">"Alice"</span>: <span class="nm">85</span>, <span class="st">"Bob"</span>: <span class="nm">42</span>, <span class="st">"Charlie"</span>: <span class="nm">91</span>, <span class="st">"Diana"</span>: <span class="nm">67</span>}
passed = {k: v <span class="kw">for</span> k, v <span class="kw">in</span> scores.items() <span class="kw">if</span> v >= <span class="nm">60</span>}
<span class="bi">print</span>(passed)  <span class="cm"># {'Alice': 85, 'Charlie': 91, 'Diana': 67}</span>

<span class="cm"># Set comprehension (unique values)</span>
text = <span class="st">"hello world"</span>
vowels = {c <span class="kw">for</span> c <span class="kw">in</span> text <span class="kw">if</span> c <span class="kw">in</span> <span class="st">"aeiou"</span>}
<span class="bi">print</span>(vowels)  <span class="cm"># {'e', 'o'}</span>

<span class="cm"># Word frequency</span>
words = <span class="st">"the cat sat on the mat"</span>.split()
freq = {w: words.count(w) <span class="kw">for</span> w <span class="kw">in</span> <span class="bi">set</span>(words)}
<span class="bi">print</span>(freq)  <span class="cm"># {'the': 2, 'cat': 1, 'sat': 1, ...}</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>{0:0, 1:1, 2:4, 3:9, 4:16, 5:25}<br>{1: 'a', 2: 'b', 3: 'c'}<br>{'Alice': 85, 'Charlie': 91, 'Diana': 67}<br>{'e', 'o'}</div></div></section>''',
("lambda.html","Lambda"),("generators.html","Generators"))

# GENERATORS
make_page("advanced/generators.html","Generators &amp; Iterators","Advanced Python","&#x2699;&#xFE0F;","advanced","Advanced &rarr; Generators",
"Generators produce values lazily using yield, consuming memory for one item at a time. Essential for processing large datasets. Covers yield, generator expressions, itertools, custom iterators, send/throw, and practical applications.",
"Python Docs, Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Generator Functions (yield)</a></li>
<li><a href="#s2">Generator Expressions</a></li>
<li><a href="#s3">itertools Module</a></li>
<li><a href="#s4">Custom Iterators</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Generator Functions (yield)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Regular function returns ALL at once (uses memory!)</span>
<span class="kw">def</span> <span class="bi">get_squares_list</span>(n):
    <span class="kw">return</span> [x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(n)]

<span class="cm"># Generator yields ONE AT A TIME (lazy!)</span>
<span class="kw">def</span> <span class="bi">get_squares_gen</span>(n):
    <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(n):
        <span class="kw">yield</span> x ** <span class="nm">2</span>

<span class="cm"># Use the generator</span>
gen = get_squares_gen(<span class="nm">5</span>)
<span class="bi">print</span>(<span class="bi">type</span>(gen))        <span class="cm"># &lt;class 'generator'&gt;</span>
<span class="bi">print</span>(<span class="bi">next</span>(gen))        <span class="cm"># 0</span>
<span class="bi">print</span>(<span class="bi">next</span>(gen))        <span class="cm"># 1</span>
<span class="bi">print</span>(<span class="bi">next</span>(gen))        <span class="cm"># 4</span>
<span class="bi">print</span>(<span class="bi">list</span>(gen))        <span class="cm"># [9, 16] (remaining)</span>

<span class="cm"># Fibonacci generator</span>
<span class="kw">def</span> <span class="bi">fibonacci</span>():
    a, b = <span class="nm">0</span>, <span class="nm">1</span>
    <span class="kw">while</span> <span class="kw">True</span>:
        <span class="kw">yield</span> a
        a, b = b, a + b

fib = fibonacci()
first_10 = [<span class="bi">next</span>(fib) <span class="kw">for</span> _ <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>)]
<span class="bi">print</span>(first_10)  <span class="cm"># [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]</span>

<span class="cm"># Memory comparison</span>
<span class="kw">import</span> sys
list_size = sys.getsizeof(get_squares_list(<span class="nm">1000000</span>))
gen_size = sys.getsizeof(get_squares_gen(<span class="nm">1000000</span>))
<span class="bi">print</span>(<span class="st">f"List: {list_size:,} bytes"</span>)   <span class="cm"># ~8,000,000</span>
<span class="bi">print</span>(<span class="st">f"Gen:  {gen_size:,} bytes"</span>)    <span class="cm"># ~200</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>&lt;class 'generator'&gt;<br>0 &rarr; 1 &rarr; 4 &rarr; [9, 16]<br>Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]<br>List: 8,000,056 bytes vs Gen: 200 bytes &#x1F4A5;</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Generator Expressions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Like list comprehension but with () instead of []</span>
gen = (x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>))  <span class="cm"># generator</span>
lst = [x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>)]  <span class="cm"># list</span>

<span class="cm"># Use with sum, min, max, any, all</span>
total = <span class="bi">sum</span>(x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">100</span>))
<span class="bi">print</span>(total)  <span class="cm"># 328350</span>

<span class="cm"># Check if any number is even</span>
nums = [<span class="nm">1</span>, <span class="nm">3</span>, <span class="nm">5</span>, <span class="nm">8</span>, <span class="nm">9</span>]
<span class="bi">print</span>(<span class="bi">any</span>(x % <span class="nm">2</span> == <span class="nm">0</span> <span class="kw">for</span> x <span class="kw">in</span> nums))  <span class="cm"># True</span>
<span class="bi">print</span>(<span class="bi">all</span>(x > <span class="nm">0</span> <span class="kw">for</span> x <span class="kw">in</span> nums))        <span class="cm"># True</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>328350 &middot; True &middot; True</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; itertools Module</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> itertools

<span class="cm"># count: infinite counter</span>
counter = itertools.count(start=<span class="nm">10</span>, step=<span class="nm">5</span>)
<span class="bi">print</span>([<span class="bi">next</span>(counter) <span class="kw">for</span> _ <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">5</span>)])  <span class="cm"># [10, 15, 20, 25, 30]</span>

<span class="cm"># cycle: repeat infinitely</span>
colors = itertools.cycle([<span class="st">"red"</span>, <span class="st">"green"</span>, <span class="st">"blue"</span>])
<span class="bi">print</span>([<span class="bi">next</span>(colors) <span class="kw">for</span> _ <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">6</span>)])

<span class="cm"># chain: concatenate iterables</span>
<span class="bi">print</span>(<span class="bi">list</span>(itertools.chain([<span class="nm">1</span>,<span class="nm">2</span>], [<span class="nm">3</span>,<span class="nm">4</span>], [<span class="nm">5</span>])))  <span class="cm"># [1,2,3,4,5]</span>

<span class="cm"># product: cartesian product</span>
<span class="bi">print</span>(<span class="bi">list</span>(itertools.product(<span class="st">"AB"</span>, <span class="st">"12"</span>)))
<span class="cm"># [('A','1'), ('A','2'), ('B','1'), ('B','2')]</span>

<span class="cm"># combinations &amp; permutations</span>
<span class="bi">print</span>(<span class="bi">list</span>(itertools.combinations(<span class="st">"ABC"</span>, <span class="nm">2</span>)))  <span class="cm"># AB AC BC</span>
<span class="bi">print</span>(<span class="bi">list</span>(itertools.permutations(<span class="st">"AB"</span>, <span class="nm">2</span>)))   <span class="cm"># AB BA</span>

<span class="cm"># islice: slice a generator</span>
fib = fibonacci()
first_5 = <span class="bi">list</span>(itertools.islice(fib, <span class="nm">5</span>))
<span class="bi">print</span>(first_5)  <span class="cm"># [0, 1, 1, 2, 3]</span>

<span class="cm"># groupby: group consecutive elements</span>
data = [(<span class="st">"A"</span>,<span class="nm">1</span>),(<span class="st">"A"</span>,<span class="nm">2</span>),(<span class="st">"B"</span>,<span class="nm">3</span>),(<span class="st">"B"</span>,<span class="nm">4</span>)]
<span class="kw">for</span> key, group <span class="kw">in</span> itertools.groupby(data, key=<span class="kw">lambda</span> x: x[<span class="nm">0</span>]):
    <span class="bi">print</span>(<span class="st">f"{key}: {list(group)}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[10, 15, 20, 25, 30]<br>['red','green','blue','red','green','blue']<br>[('A','1'),('A','2'),('B','1'),('B','2')]<br>A: [('A',1),('A',2)] &middot; B: [('B',3),('B',4)]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Custom Iterator Class</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="bi">Countdown</span>:
    <span class="kw">def</span> <span class="bi">__init__</span>(self, start):
        self.current = start

    <span class="kw">def</span> <span class="bi">__iter__</span>(self):
        <span class="kw">return</span> self

    <span class="kw">def</span> <span class="bi">__next__</span>(self):
        <span class="kw">if</span> self.current <= <span class="nm">0</span>:
            <span class="kw">raise</span> <span class="bi">StopIteration</span>
        val = self.current
        self.current -= <span class="nm">1</span>
        <span class="kw">return</span> val

<span class="kw">for</span> num <span class="kw">in</span> Countdown(<span class="nm">5</span>):
    <span class="bi">print</span>(num, end=<span class="st">" "</span>)
<span class="cm"># 5 4 3 2 1</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>5 4 3 2 1</div></div></section>''',
("comprehensions.html","Comprehensions"),("context-managers.html","Context Managers"))

print("lambda.html + comprehensions.html + generators.html expanded!")
