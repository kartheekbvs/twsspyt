
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# sets.html
make_page("python/sets.html","Sets","Python Fundamentals","&#x1F40D;","beginner","Python Fundamentals &rarr; Sets",
"Sets are unordered, mutable collections of unique hashable elements. Optimized for O(1) membership testing, deduplication, and mathematical set operations: union, intersection, difference, symmetric difference.",
"Python Programming (2024), Learning Python &mdash; Mark Lutz",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Creating Sets</a></li><li><a href="#s2">Set Operations (Math)</a></li><li><a href="#s3">Mutating Methods</a></li><li><a href="#s4">frozenset</a></li><li><a href="#s5">Set Comprehensions</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Creating Sets</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">s1 = {<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>}
s2 = <span class="bi">set</span>([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">3</span>])    <span class="cm"># duplicates removed &rarr; {1,2,3}</span>
s3 = <span class="bi">set</span>(<span class="st">"hello"</span>)           <span class="cm"># {'h','e','l','o'}</span>
empty = <span class="bi">set</span>()               <span class="cm"># NOT {} (that creates empty dict!)</span>

<span class="bi">print</span>(s2)              <span class="cm"># {1, 2, 3}</span>
<span class="bi">print</span>(<span class="bi">len</span>(s1))         <span class="cm"># 4</span>
<span class="bi">print</span>(<span class="nm">3</span> <span class="kw">in</span> s1)         <span class="cm"># True  &mdash; O(1) lookup!</span>
<span class="bi">print</span>(<span class="bi">type</span>({}))        <span class="cm"># &lt;class 'dict'&gt; !</span>
<span class="bi">print</span>(<span class="bi">type</span>(<span class="bi">set</span>()))     <span class="cm"># &lt;class 'set'&gt;</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>{1, 2, 3} &middot; 4 &middot; True &middot; &lt;class 'dict'&gt; &middot; &lt;class 'set'&gt;</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Set Operations</h2>
<table class="data-table"><thead><tr><th>Operation</th><th>Operator</th><th>Method</th><th>Description</th></tr></thead><tbody>
<tr><td>Union</td><td><code>A | B</code></td><td><code>A.union(B)</code></td><td>All from both</td></tr>
<tr><td>Intersection</td><td><code>A &amp; B</code></td><td><code>A.intersection(B)</code></td><td>Common elements</td></tr>
<tr><td>Difference</td><td><code>A - B</code></td><td><code>A.difference(B)</code></td><td>In A not B</td></tr>
<tr><td>Symmetric Diff</td><td><code>A ^ B</code></td><td><code>A.symmetric_difference(B)</code></td><td>In one not both</td></tr>
<tr><td>Subset</td><td><code>A &lt;= B</code></td><td><code>A.issubset(B)</code></td><td>A in B?</td></tr>
<tr><td>Superset</td><td><code>A &gt;= B</code></td><td><code>A.issuperset(B)</code></td><td>B in A?</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">A = {<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>,<span class="nm">5</span>}
B = {<span class="nm">4</span>,<span class="nm">5</span>,<span class="nm">6</span>,<span class="nm">7</span>,<span class="nm">8</span>}

<span class="bi">print</span>(A | B)    <span class="cm"># {1,2,3,4,5,6,7,8}</span>
<span class="bi">print</span>(A &amp; B)    <span class="cm"># {4, 5}</span>
<span class="bi">print</span>(A - B)    <span class="cm"># {1, 2, 3}</span>
<span class="bi">print</span>(A ^ B)    <span class="cm"># {1,2,3,6,7,8}</span>
<span class="bi">print</span>({<span class="nm">1</span>,<span class="nm">2</span>} &lt;= {<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>})  <span class="cm"># True (subset)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>{1,2,3,4,5,6,7,8} &middot; {4,5} &middot; {1,2,3} &middot; {1,2,3,6,7,8} &middot; True</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Mutating Methods</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">s = {<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>}
s.add(<span class="nm">4</span>)          <span class="cm"># {1,2,3,4}</span>
s.discard(<span class="nm">10</span>)     <span class="cm"># no error if missing</span>
s.remove(<span class="nm">2</span>)       <span class="cm"># KeyError if missing</span>
s.update([<span class="nm">5</span>,<span class="nm">6</span>])   <span class="cm"># add multiple</span>
<span class="bi">print</span>(s)           <span class="cm"># {1,3,4,5,6}</span>

<span class="cm"># Deduplication (common use case)</span>
nums = [<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">3</span>,<span class="nm">3</span>,<span class="nm">4</span>]
unique = <span class="bi">sorted</span>(<span class="bi">set</span>(nums))
<span class="bi">print</span>(unique)   <span class="cm"># [1, 2, 3, 4]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>{1,3,4,5,6}<br>[1, 2, 3, 4]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; frozenset</h2>
<p><code>frozenset</code> is the <strong>immutable</strong> version of set. It is hashable &mdash; can be a dict key or member of another set.</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">fs = <span class="bi">frozenset</span>([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>])
<span class="cm"># fs.add(4)  # AttributeError!</span>

<span class="cm"># Can be dict key</span>
d = {<span class="bi">frozenset</span>([<span class="nm">1</span>,<span class="nm">2</span>]): <span class="st">"pair"</span>}
<span class="bi">print</span>(d[<span class="bi">frozenset</span>([<span class="nm">1</span>,<span class="nm">2</span>])])  <span class="cm"># pair</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>pair</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Set Comprehensions</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">squares = {x**<span class="nm">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">10</span>)}
<span class="bi">print</span>(squares)  <span class="cm"># {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}</span>

<span class="cm"># Filter unique word lengths</span>
words = [<span class="st">"hello"</span>,<span class="st">"world"</span>,<span class="st">"hi"</span>,<span class="st">"hey"</span>]
lengths = {<span class="bi">len</span>(w) <span class="kw">for</span> w <span class="kw">in</span> words}
<span class="bi">print</span>(lengths)  <span class="cm"># {2, 3, 5}</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>{0, 1, 4, 9, 16, 25, 36, 49, 64, 81}<br>{2, 3, 5}</div></div></section>''',
("dictionaries.html","Dictionaries"),("file-io.html","File I/O"))

# file-io.html
make_page("python/file-io.html","File I/O","Python Fundamentals","&#x1F40D;","beginner","Python Fundamentals &rarr; File I/O",
"File I/O in Python uses the built-in open() function with context managers (with statement) for safe file handling. This covers reading, writing, appending text and binary files, CSV files, and JSON serialization.",
"Python Programming (2024), Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Opening Files</a></li><li><a href="#s2">Reading Files</a></li><li><a href="#s3">Writing Files</a></li><li><a href="#s4">Working with CSV</a></li><li><a href="#s5">JSON Files</a></li><li><a href="#s6">The pathlib Module</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Opening Files (with Statement)</h2>
<table class="data-table"><thead><tr><th>Mode</th><th>Description</th><th>Creates?</th><th>Truncates?</th></tr></thead><tbody>
<tr><td><code>'r'</code></td><td>Read (default)</td><td>No</td><td>No</td></tr>
<tr><td><code>'w'</code></td><td>Write</td><td>Yes</td><td>Yes</td></tr>
<tr><td><code>'a'</code></td><td>Append</td><td>Yes</td><td>No</td></tr>
<tr><td><code>'x'</code></td><td>Exclusive create</td><td>Yes (error if exists)</td><td>N/A</td></tr>
<tr><td><code>'b'</code></td><td>Binary mode</td><td>-</td><td>-</td></tr>
<tr><td><code>'+'</code></td><td>Read+Write</td><td>-</td><td>-</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Always use 'with' &mdash; auto-closes file even on exceptions</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"data.txt"</span>, <span class="st">"r"</span>, encoding=<span class="st">"utf-8"</span>) <span class="kw">as</span> f:
    content = f.read()        <span class="cm"># entire file as string</span>
    <span class="bi">print</span>(content)

<span class="cm"># File is automatically closed here</span>
<span class="bi">print</span>(f.closed)  <span class="cm"># True</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>(file contents)<br>True</div></div>
<div class="callout warning"><div class="callout-icon">&#x26A0;&#xFE0F;</div><div class="callout-content"><strong>Always specify encoding</strong><p>Use <code>encoding="utf-8"</code> explicitly. The default encoding varies by OS (Windows uses cp1252), which causes cross-platform bugs.</p></div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Reading Files</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Method 1: read() &mdash; entire file</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"file.txt"</span>) <span class="kw">as</span> f:
    text = f.read()

<span class="cm"># Method 2: readline() &mdash; one line at a time</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"file.txt"</span>) <span class="kw">as</span> f:
    line = f.readline()       <span class="cm"># includes \\n</span>
    <span class="bi">print</span>(line.strip())       <span class="cm"># remove trailing newline</span>

<span class="cm"># Method 3: readlines() &mdash; list of all lines</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"file.txt"</span>) <span class="kw">as</span> f:
    lines = f.readlines()     <span class="cm"># ['line1\\n', 'line2\\n', ...]</span>

<span class="cm"># Method 4: iterate (BEST for large files &mdash; memory efficient)</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"file.txt"</span>) <span class="kw">as</span> f:
    <span class="kw">for</span> line <span class="kw">in</span> f:            <span class="cm"># lazy line-by-line</span>
        <span class="bi">print</span>(line.strip())</pre></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Writing Files</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Write (overwrites existing file)</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"output.txt"</span>, <span class="st">"w"</span>, encoding=<span class="st">"utf-8"</span>) <span class="kw">as</span> f:
    f.write(<span class="st">"Line 1\\n"</span>)       <span class="cm"># returns num chars written</span>
    f.write(<span class="st">"Line 2\\n"</span>)

<span class="cm"># Append (adds to end)</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"output.txt"</span>, <span class="st">"a"</span>) <span class="kw">as</span> f:
    f.write(<span class="st">"Line 3\\n"</span>)

<span class="cm"># Write multiple lines</span>
lines = [<span class="st">"alpha\\n"</span>, <span class="st">"beta\\n"</span>, <span class="st">"gamma\\n"</span>]
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"output.txt"</span>, <span class="st">"w"</span>) <span class="kw">as</span> f:
    f.writelines(lines)       <span class="cm"># does NOT add newlines</span></pre></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Working with CSV</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> csv

<span class="cm"># Writing CSV</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"data.csv"</span>, <span class="st">"w"</span>, newline=<span class="st">""</span>) <span class="kw">as</span> f:
    writer = csv.writer(f)
    writer.writerow([<span class="st">"Name"</span>, <span class="st">"Age"</span>, <span class="st">"City"</span>])
    writer.writerow([<span class="st">"Alice"</span>, <span class="nm">30</span>, <span class="st">"NYC"</span>])
    writer.writerow([<span class="st">"Bob"</span>, <span class="nm">25</span>, <span class="st">"LA"</span>])

<span class="cm"># Reading CSV</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"data.csv"</span>, <span class="st">"r"</span>) <span class="kw">as</span> f:
    reader = csv.DictReader(f)    <span class="cm"># each row is a dict</span>
    <span class="kw">for</span> row <span class="kw">in</span> reader:
        <span class="bi">print</span>(row[<span class="st">"Name"</span>], row[<span class="st">"Age"</span>])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Alice 30<br>Bob 25</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; JSON Files</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> json

data = {<span class="st">"name"</span>: <span class="st">"Alice"</span>, <span class="st">"age"</span>: <span class="nm">30</span>, <span class="st">"langs"</span>: [<span class="st">"Python"</span>,<span class="st">"JS"</span>]}

<span class="cm"># Write JSON</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"data.json"</span>, <span class="st">"w"</span>) <span class="kw">as</span> f:
    json.dump(data, f, indent=<span class="nm">2</span>)

<span class="cm"># Read JSON</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"data.json"</span>, <span class="st">"r"</span>) <span class="kw">as</span> f:
    loaded = json.load(f)
    <span class="bi">print</span>(loaded[<span class="st">"name"</span>])    <span class="cm"># Alice</span>

<span class="cm"># JSON &harr; string (no file)</span>
json_str = json.dumps(data)
parsed = json.loads(json_str)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Alice</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; The pathlib Module (Modern)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> pathlib <span class="kw">import</span> Path

p = Path(<span class="st">"data"</span>) / <span class="st">"output.txt"</span>   <span class="cm"># / operator for paths!</span>
p.parent.mkdir(exist_ok=<span class="kw">True</span>)

p.write_text(<span class="st">"Hello pathlib!"</span>, encoding=<span class="st">"utf-8"</span>)
content = p.read_text(encoding=<span class="st">"utf-8"</span>)
<span class="bi">print</span>(content)          <span class="cm"># Hello pathlib!</span>
<span class="bi">print</span>(p.exists())       <span class="cm"># True</span>
<span class="bi">print</span>(p.suffix)         <span class="cm"># .txt</span>
<span class="bi">print</span>(p.stem)           <span class="cm"># output</span>
<span class="bi">print</span>(<span class="bi">list</span>(Path(<span class="st">"."</span>).glob(<span class="st">"*.py"</span>)))  <span class="cm"># [PosixPath('script.py'), ...]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Hello pathlib!<br>True<br>.txt<br>output</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Prefer pathlib over os.path</strong><p><code>pathlib</code> (Python 3.4+) is more readable, object-oriented, and cross-platform than <code>os.path</code>. Use <code>Path</code> for all new code.</p></div></div></section>''',
("sets.html","Sets"),("exceptions.html","Exception Handling"))

# modules.html
make_page("python/modules.html","Modules &amp; Packages","Python Fundamentals","&#x1F40D;","beginner","Python Fundamentals &rarr; Modules &amp; Packages",
"Modules are Python files containing functions, classes, and variables. Packages are directories of modules. This covers import mechanics, the module search path, __init__.py, __name__ == '__main__', and popular standard library modules.",
"Python Programming (2024), Learning Python &mdash; Mark Lutz",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">What are Modules?</a></li><li><a href="#s2">Import Mechanics</a></li><li><a href="#s3">Packages</a></li><li><a href="#s4">Standard Library Highlights</a></li><li><a href="#s5">__name__ == "__main__"</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; What are Modules?</h2>
<p>Any <code>.py</code> file is a module. When you import it, Python executes the file and makes its names available.</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; mymodule.py</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># mymodule.py</span>
PI = <span class="nm">3.14159</span>

<span class="kw">def</span> <span class="fn">greet</span>(name):
    <span class="kw">return</span> <span class="st">f"Hello, {name}!"</span>

<span class="kw">class</span> <span class="cl">Calculator</span>:
    <span class="kw">def</span> <span class="fn">add</span>(self, a, b):
        <span class="kw">return</span> a + b</pre></div>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; main.py</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Different import styles</span>
<span class="kw">import</span> mymodule
<span class="bi">print</span>(mymodule.PI)                 <span class="cm"># 3.14159</span>
<span class="bi">print</span>(mymodule.greet(<span class="st">"Alice"</span>))     <span class="cm"># Hello, Alice!</span>

<span class="kw">from</span> mymodule <span class="kw">import</span> greet, PI
<span class="bi">print</span>(greet(<span class="st">"Bob"</span>))               <span class="cm"># Hello, Bob!</span>

<span class="kw">from</span> mymodule <span class="kw">import</span> Calculator <span class="kw">as</span> Calc
c = Calc()
<span class="bi">print</span>(c.add(<span class="nm">3</span>, <span class="nm">4</span>))               <span class="cm"># 7</span>

<span class="cm"># import * (avoid in production code)</span>
<span class="kw">from</span> mymodule <span class="kw">import</span> *</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>3.14159<br>Hello, Alice!<br>Hello, Bob!<br>7</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Import Mechanics</h2>
<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Module Search Path</strong><p>Python searches for modules in this order: 1) Current directory, 2) <code>PYTHONPATH</code> env var, 3) Standard library, 4) <code>site-packages</code> (pip-installed). Check with <code>sys.path</code>.</p></div></div>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> sys
<span class="bi">print</span>(sys.path)    <span class="cm"># list of directories Python searches</span>

<span class="cm"># Modules are cached after first import</span>
<span class="cm"># Re-import does nothing unless you use:</span>
<span class="kw">from</span> importlib <span class="kw">import</span> reload
reload(mymodule)   <span class="cm"># forces re-execution</span>

<span class="cm"># Check module location</span>
<span class="bi">print</span>(mymodule.__file__)   <span class="cm"># /path/to/mymodule.py</span></pre></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Packages</h2>
<p>A package is a directory with an <code>__init__.py</code> file (can be empty). It groups related modules.</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Project Structure</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">mypackage/
    __init__.py       # makes it a package
    utils.py
    models/
        __init__.py
        linear.py
        tree.py</pre></div>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> mypackage.utils <span class="kw">import</span> helper_fn
<span class="kw">from</span> mypackage.models.linear <span class="kw">import</span> LinearModel

<span class="cm"># Relative imports (inside package)</span>
<span class="kw">from</span> . <span class="kw">import</span> utils             <span class="cm"># current package</span>
<span class="kw">from</span> ..models <span class="kw">import</span> linear     <span class="cm"># parent package</span></pre></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Standard Library Highlights</h2>
<table class="data-table"><thead><tr><th>Module</th><th>Purpose</th><th>Key Functions</th></tr></thead><tbody>
<tr><td><code>os</code></td><td>OS interface</td><td><code>os.getcwd()</code>, <code>os.listdir()</code></td></tr>
<tr><td><code>sys</code></td><td>System config</td><td><code>sys.argv</code>, <code>sys.path</code></td></tr>
<tr><td><code>math</code></td><td>Math functions</td><td><code>sqrt()</code>, <code>pi</code>, <code>ceil()</code></td></tr>
<tr><td><code>datetime</code></td><td>Date/time</td><td><code>datetime.now()</code>, <code>timedelta</code></td></tr>
<tr><td><code>json</code></td><td>JSON encoding</td><td><code>dumps()</code>, <code>loads()</code></td></tr>
<tr><td><code>re</code></td><td>Regular expressions</td><td><code>findall()</code>, <code>sub()</code></td></tr>
<tr><td><code>collections</code></td><td>Data structures</td><td><code>Counter</code>, <code>defaultdict</code>, <code>deque</code></td></tr>
<tr><td><code>itertools</code></td><td>Iterator tools</td><td><code>chain()</code>, <code>combinations()</code></td></tr>
<tr><td><code>functools</code></td><td>Higher-order functions</td><td><code>reduce()</code>, <code>lru_cache</code></td></tr>
<tr><td><code>pathlib</code></td><td>Path handling</td><td><code>Path()</code>, <code>glob()</code></td></tr>
</tbody></table></section>

<section class="content-section" id="s5"><h2>5 &middot; __name__ == "__main__"</h2>
<p>This guards code that should only run when the file is executed directly (not imported).</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; script.py</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">def</span> <span class="fn">main</span>():
    <span class="bi">print</span>(<span class="st">"Running as main script"</span>)

<span class="kw">if</span> __name__ == <span class="st">"__main__"</span>:
    main()
<span class="cm"># When imported: __name__ == "script" (module name)</span>
<span class="cm"># When run directly: __name__ == "__main__"</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Running as main script</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Best Practice</strong><p>Always wrap executable code in <code>if __name__ == "__main__":</code> so your module can be both imported and run as a script without side effects.</p></div></div></section>''',
("exceptions.html","Exception Handling"),("../oop/classes-objects.html","Classes &amp; Objects"))

print("Batch 2: sets, file-io, modules done.")
