
import sys; sys.path.insert(0, r"C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site")
from gen_template import make_page

# ===== PYTHON FUNDAMENTALS =====

make_page("python/strings.html","Strings","Python Fundamentals","&#x1F40D;","beginner","Python Fundamentals &rarr; Strings",
"Strings are immutable sequences of Unicode characters in Python. This chapter covers string creation, indexing, slicing, formatting (f-strings, .format(), %), and 40+ built-in string methods for powerful text processing.",
"Python Programming (2024), Learning Python &mdash; Mark Lutz",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Creating Strings</a></li><li><a href="#s2">Indexing &amp; Slicing</a></li><li><a href="#s3">String Formatting (f-strings)</a></li><li><a href="#s4">Common String Methods</a></li><li><a href="#s5">Escape Sequences &amp; Raw Strings</a></li><li><a href="#s6">Immutability Explained</a></li><li><a href="#s7">String Encoding (Unicode)</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Creating Strings</h2>
<p>Python strings can use single quotes, double quotes, or triple quotes for multi-line text. All produce the same <code>str</code> type.</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Different ways to create strings</span>
s1 = <span class="st">'Hello'</span>              <span class="cm"># single quotes</span>
s2 = <span class="st">"World"</span>              <span class="cm"># double quotes</span>
s3 = <span class="st">"""Multi
line string"""</span>               <span class="cm"># triple quotes preserve newlines</span>
s4 = <span class="st">r"C:\\Users\\name"</span>     <span class="cm"># raw string &mdash; backslashes literal</span>
s5 = <span class="st">b"bytes"</span>              <span class="cm"># bytes literal (not str)</span>

<span class="bi">print</span>(<span class="bi">type</span>(s1))    <span class="cm"># &lt;class 'str'&gt;</span>
<span class="bi">print</span>(<span class="bi">len</span>(s2))     <span class="cm"># 5</span>
<span class="bi">print</span>(s1 + <span class="st">" "</span> + s2)  <span class="cm"># Hello World (concatenation)</span>
<span class="bi">print</span>(s2 * <span class="nm">3</span>)     <span class="cm"># WorldWorldWorld (repetition)</span>
<span class="bi">print</span>(<span class="st">"Hello"</span> == <span class="st">'Hello'</span>)  <span class="cm"># True &mdash; same string</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>&lt;class 'str'&gt;<br>5<br>Hello World<br>WorldWorldWorld<br>True</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Indexing &amp; Slicing</h2>
<p>Strings are sequences &mdash; each character has a 0-based index (negative indexes count from end).</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">s = <span class="st">"Python"</span>
<span class="cm">#    P  y  t  h  o  n</span>
<span class="cm">#    0  1  2  3  4  5   (forward)</span>
<span class="cm">#   -6 -5 -4 -3 -2 -1   (backward)</span>

<span class="bi">print</span>(s[<span class="nm">0</span>])      <span class="cm"># P</span>
<span class="bi">print</span>(s[-<span class="nm">1</span>])     <span class="cm"># n</span>
<span class="bi">print</span>(s[<span class="nm">1</span>:<span class="nm">4</span>])    <span class="cm"># yth  (start:stop, stop exclusive)</span>
<span class="bi">print</span>(s[:<span class="nm">3</span>])     <span class="cm"># Pyt  (first 3)</span>
<span class="bi">print</span>(s[<span class="nm">3</span>:])     <span class="cm"># hon  (from index 3 onward)</span>
<span class="bi">print</span>(s[::<span class="nm">2</span>])    <span class="cm"># Pto  (every 2nd character)</span>
<span class="bi">print</span>(s[::-<span class="nm">1</span>])   <span class="cm"># nohtyP  (reverse string)</span>

<span class="cm"># Slicing never raises IndexError</span>
<span class="bi">print</span>(s[<span class="nm">100</span>:])   <span class="cm"># '' (empty string, no error)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>P &middot; n &middot; yth &middot; Pyt &middot; hon &middot; Pto &middot; nohtyP &middot; ''</div></div>
<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Textbook Insight</strong><p>"Slicing creates a <em>new</em> string object. The original is never modified because strings are immutable. The slice <code>s[i:j]</code> extracts characters from index <code>i</code> up to but not including <code>j</code>." &mdash; <em>Learning Python, Mark Lutz</em></p></div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; String Formatting</h2>
<table class="data-table"><thead><tr><th>Method</th><th>Syntax</th><th>Version</th><th>Recommended</th></tr></thead><tbody>
<tr><td>f-strings</td><td><code>f"Hello {name}"</code></td><td>3.6+</td><td><strong>Yes &#x2705;</strong></td></tr>
<tr><td>.format()</td><td><code>"Hello {}".format(name)</code></td><td>2.7+</td><td>OK</td></tr>
<tr><td>% operator</td><td><code>"Hello %s" % name</code></td><td>Legacy</td><td>Avoid</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; formatting.py</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">name, age, pi = <span class="st">"Alice"</span>, <span class="nm">30</span>, <span class="nm">3.14159</span>

<span class="cm"># f-strings (best practice)</span>
<span class="bi">print</span>(<span class="st">f"Name: {name}, Age: {age}"</span>)       <span class="cm"># Name: Alice, Age: 30</span>
<span class="bi">print</span>(<span class="st">f"Pi = {pi:.2f}"</span>)                   <span class="cm"># Pi = 3.14</span>
<span class="bi">print</span>(<span class="st">f"2^10 = {2**10}"</span>)                  <span class="cm"># 2^10 = 1024</span>
<span class="bi">print</span>(<span class="st">f"{name!r}"</span>)                        <span class="cm"># 'Alice' (repr)</span>
<span class="bi">print</span>(<span class="st">f"{age:05d}"</span>)                       <span class="cm"># 00030 (zero-padded)</span>
<span class="bi">print</span>(<span class="st">f"{1_000_000:,.0f}"</span>)               <span class="cm"># 1,000,000</span>

<span class="cm"># .format() method</span>
<span class="bi">print</span>(<span class="st">"Hello, {}! Age: {}"</span>.format(name, age))
<span class="bi">print</span>(<span class="st">"{0} + {0} = {1}"</span>.format(<span class="nm">5</span>, <span class="nm">10</span>))    <span class="cm"># 5 + 5 = 10</span>

<span class="cm"># Alignment</span>
<span class="bi">print</span>(<span class="st">f"{'left':<span><</span>20}"</span>)     <span class="cm"># left-aligned</span>
<span class="bi">print</span>(<span class="st">f"{'center':^20}"</span>)   <span class="cm"># center-aligned</span>
<span class="bi">print</span>(<span class="st">f"{'right':>20}"</span>)    <span class="cm"># right-aligned</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Name: Alice, Age: 30<br>Pi = 3.14<br>2^10 = 1024<br>'Alice'<br>00030<br>1,000,000</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Common String Methods</h2>
<table class="data-table"><thead><tr><th>Method</th><th>Description</th><th>Returns</th></tr></thead><tbody>
<tr><td><code>.upper()</code> / <code>.lower()</code></td><td>Convert case</td><td>New <code>str</code></td></tr>
<tr><td><code>.strip()</code> / <code>.lstrip()</code> / <code>.rstrip()</code></td><td>Remove whitespace</td><td>New <code>str</code></td></tr>
<tr><td><code>.split(sep)</code></td><td>Split into list</td><td><code>list[str]</code></td></tr>
<tr><td><code>.join(iterable)</code></td><td>Join strings</td><td><code>str</code></td></tr>
<tr><td><code>.replace(old, new)</code></td><td>Replace substring</td><td>New <code>str</code></td></tr>
<tr><td><code>.find(sub)</code> / <code>.index(sub)</code></td><td>Find position</td><td><code>int</code> (-1 or ValueError)</td></tr>
<tr><td><code>.startswith()</code> / <code>.endswith()</code></td><td>Check prefix/suffix</td><td><code>bool</code></td></tr>
<tr><td><code>.count(sub)</code></td><td>Count occurrences</td><td><code>int</code></td></tr>
<tr><td><code>.isdigit()</code> / <code>.isalpha()</code> / <code>.isalnum()</code></td><td>Character checks</td><td><code>bool</code></td></tr>
<tr><td><code>.title()</code> / <code>.capitalize()</code> / <code>.swapcase()</code></td><td>Case variants</td><td>New <code>str</code></td></tr>
<tr><td><code>.center(w)</code> / <code>.ljust(w)</code> / <code>.rjust(w)</code></td><td>Padding</td><td>New <code>str</code></td></tr>
<tr><td><code>.zfill(w)</code></td><td>Zero-fill</td><td>New <code>str</code></td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; methods.py</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">text = <span class="st">"  Hello, World!  "</span>
<span class="bi">print</span>(text.strip())                  <span class="cm"># "Hello, World!"</span>
<span class="bi">print</span>(text.strip().lower())          <span class="cm"># "hello, world!"</span>
<span class="bi">print</span>(<span class="st">"python,java,c++"</span>.split(<span class="st">","</span>))  <span class="cm"># ['python','java','c++']</span>
<span class="bi">print</span>(<span class="st">", "</span>.join([<span class="st">"a"</span>,<span class="st">"b"</span>,<span class="st">"c"</span>]))   <span class="cm"># a, b, c</span>
<span class="bi">print</span>(<span class="st">"banana"</span>.replace(<span class="st">"a"</span>,<span class="st">"o"</span>))   <span class="cm"># bonono</span>
<span class="bi">print</span>(<span class="st">"hello"</span>.center(<span class="nm">11</span>,<span class="st">"-"</span>))       <span class="cm"># ---hello---</span>
<span class="bi">print</span>(<span class="st">"banana"</span>.count(<span class="st">"a"</span>))          <span class="cm"># 3</span>
<span class="bi">print</span>(<span class="st">"hello world"</span>.title())        <span class="cm"># Hello World</span>
<span class="bi">print</span>(<span class="st">"42"</span>.zfill(<span class="nm">5</span>))                <span class="cm"># 00042</span>

<span class="cm"># Chaining methods (returns new string each time)</span>
result = <span class="st">"  HELLO world  "</span>.strip().lower().replace(<span class="st">"world"</span>,<span class="st">"python"</span>).title()
<span class="bi">print</span>(result)  <span class="cm"># Hello Python</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Hello, World!<br>hello, world!<br>['python','java','c++']<br>a, b, c<br>bonono<br>---hello---<br>3<br>Hello World<br>00042<br>Hello Python</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Escape Sequences &amp; Raw Strings</h2>
<table class="data-table"><thead><tr><th>Escape</th><th>Meaning</th></tr></thead><tbody>
<tr><td><code>\\n</code></td><td>Newline</td></tr>
<tr><td><code>\\t</code></td><td>Tab</td></tr>
<tr><td><code>\\\\</code></td><td>Literal backslash</td></tr>
<tr><td><code>\\'</code></td><td>Single quote</td></tr>
<tr><td><code>\\"</code></td><td>Double quote</td></tr>
<tr><td><code>\\0</code></td><td>Null character</td></tr>
<tr><td><code>\\u0041</code></td><td>Unicode character (A)</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="bi">print</span>(<span class="st">"Line1\\nLine2"</span>)         <span class="cm"># Line1 (newline) Line2</span>
<span class="bi">print</span>(<span class="st">"Col1\\tCol2"</span>)           <span class="cm"># Col1    Col2 (tab)</span>
<span class="bi">print</span>(<span class="st">"C:\\\\Users\\\\file"</span>)       <span class="cm"># C:\\Users\\file</span>

<span class="cm"># Raw strings &mdash; backslashes are literal</span>
<span class="bi">print</span>(<span class="st">r"C:\\Users\\file"</span>)       <span class="cm"># C:\\Users\\file (same!)</span>

<span class="cm"># Great for regex patterns</span>
<span class="kw">import</span> re
pattern = <span class="st">r"\\d{3}-\\d{4}"</span>    <span class="cm"># no need to double backslashes</span>
<span class="bi">print</span>(re.findall(pattern, <span class="st">"Call 555-1234"</span>))  <span class="cm"># ['555-1234']</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Line1<br>Line2<br>Col1&emsp;Col2<br>C:\\Users\\file<br>['555-1234']</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Immutability Explained</h2>
<p>Strings cannot be changed in place. Every operation returns a <em>new</em> string object. This is why <code>s[0] = "X"</code> raises <code>TypeError</code>.</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">s = <span class="st">"Hello"</span>
<span class="cm"># s[0] = "J"  # TypeError!</span>

<span class="cm"># Instead, create a new string</span>
s = <span class="st">"J"</span> + s[<span class="nm">1</span>:]
<span class="bi">print</span>(s)  <span class="cm"># Jello</span>

<span class="cm"># Performance: use list + join for building strings</span>
parts = []
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">5</span>):
    parts.append(<span class="bi">str</span>(i))
result = <span class="st">""</span>.join(parts)  <span class="cm"># "01234" &mdash; O(n) not O(n&sup2;)</span>
<span class="bi">print</span>(result)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Jello<br>01234</div></div>
<div class="callout tip"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Performance Tip</strong><p>Never build strings with <code>+=</code> in a loop &mdash; it creates a new string each iteration (O(n&sup2;)). Use <code>list.append()</code> then <code>"".join()</code> for O(n) performance.</p></div></div></section>

<section class="content-section" id="s7"><h2>7 &middot; String Encoding (Unicode)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Python 3 strings are Unicode by default</span>
<span class="bi">print</span>(<span class="st">"&#x4F60;&#x597D;"</span>)          <span class="cm"># Chinese: Hello</span>
<span class="bi">print</span>(<span class="st">"\\u03C0"</span>)          <span class="cm"># &#x3C0; (pi)</span>
<span class="bi">print</span>(<span class="bi">ord</span>(<span class="st">"A"</span>))          <span class="cm"># 65 (Unicode code point)</span>
<span class="bi">print</span>(<span class="bi">chr</span>(<span class="nm">65</span>))           <span class="cm"># A</span>

<span class="cm"># Encoding to bytes</span>
text = <span class="st">"Hello &#x1F310;"</span>
encoded = text.encode(<span class="st">"utf-8"</span>)   <span class="cm"># str &rarr; bytes</span>
<span class="bi">print</span>(encoded)                     <span class="cm"># b'Hello \\xf0\\x9f\\x8c\\x90'</span>
decoded = encoded.decode(<span class="st">"utf-8"</span>) <span class="cm"># bytes &rarr; str</span>
<span class="bi">print</span>(decoded)                     <span class="cm"># Hello &#x1F310;</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>&#x4F60;&#x597D;<br>&#x3C0;<br>65<br>A<br>b'Hello ...'<br>Hello &#x1F310;</div></div></section>''',
("functions.html","Functions"), ("lists.html","Lists"))

# ===== TUPLES =====
make_page("python/tuples.html","Tuples","Python Fundamentals","&#x1F40D;","beginner","Python Fundamentals &rarr; Tuples",
"Tuples are immutable, ordered sequences. Like lists but cannot be modified after creation. They are hashable (usable as dict keys), faster to iterate, and ideal for fixed collections. Python uses them extensively for multiple return values and unpacking.",
"Python Programming (2024), Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Creating Tuples</a></li><li><a href="#s2">Accessing Elements</a></li><li><a href="#s3">Tuple Unpacking</a></li><li><a href="#s4">Methods &amp; Operations</a></li><li><a href="#s5">Named Tuples</a></li><li><a href="#s6">Tuples vs Lists</a></li></ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Creating Tuples</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">t1 = (<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>)
t2 = <span class="st">"a"</span>, <span class="st">"b"</span>, <span class="st">"c"</span>         <span class="cm"># parentheses optional</span>
t3 = (<span class="nm">42</span>,)                  <span class="cm"># single-item &mdash; COMMA required!</span>
t4 = ()                     <span class="cm"># empty tuple</span>
t5 = <span class="bi">tuple</span>([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>])        <span class="cm"># from list</span>
t6 = <span class="bi">tuple</span>(<span class="st">"hello"</span>)         <span class="cm"># ('h','e','l','l','o')</span>

<span class="bi">print</span>(<span class="bi">type</span>((<span class="nm">42</span>,)))  <span class="cm"># &lt;class 'tuple'&gt;</span>
<span class="bi">print</span>(<span class="bi">type</span>((<span class="nm">42</span>)))   <span class="cm"># &lt;class 'int'&gt; &mdash; NO comma = not tuple!</span>

<span class="cm"># Tuples can hold mixed types</span>
person = (<span class="st">"Alice"</span>, <span class="nm">30</span>, <span class="kw">True</span>, [<span class="nm">1</span>,<span class="nm">2</span>])
<span class="bi">print</span>(person[<span class="nm">0</span>])   <span class="cm"># Alice</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>&lt;class 'tuple'&gt;<br>&lt;class 'int'&gt;<br>Alice</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Accessing Elements</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">coords = (<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>)
<span class="bi">print</span>(coords[<span class="nm">0</span>])     <span class="cm"># 10</span>
<span class="bi">print</span>(coords[-<span class="nm">1</span>])    <span class="cm"># 30</span>
<span class="bi">print</span>(coords[<span class="nm">1</span>:])    <span class="cm"># (20, 30)</span>
<span class="bi">print</span>(<span class="bi">len</span>(coords))   <span class="cm"># 3</span>
<span class="bi">print</span>(<span class="nm">20</span> <span class="kw">in</span> coords)  <span class="cm"># True</span>

<span class="cm"># Immutable &mdash; cannot assign</span>
<span class="cm"># coords[0] = 99  # TypeError!</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>10 &middot; 30 &middot; (20, 30) &middot; 3 &middot; True</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Tuple Unpacking</h2>
<p>Python's most powerful tuple feature &mdash; assign multiple variables from a tuple in one line. Works with any iterable.</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; unpacking.py</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Basic unpacking</span>
x, y, z = (<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">30</span>)
<span class="bi">print</span>(x, y, z)   <span class="cm"># 10 20 30</span>

<span class="cm"># Elegant swap</span>
a, b = <span class="nm">1</span>, <span class="nm">2</span>
a, b = b, a
<span class="bi">print</span>(a, b)      <span class="cm"># 2 1</span>

<span class="cm"># Star unpacking (Python 3+)</span>
first, *rest = (<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>,<span class="nm">5</span>)
<span class="bi">print</span>(first, rest)    <span class="cm"># 1 [2,3,4,5]</span>

*init, last = (<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>,<span class="nm">4</span>,<span class="nm">5</span>)
<span class="bi">print</span>(init, last)     <span class="cm"># [1,2,3,4] 5</span>

<span class="cm"># Ignore values with _</span>
name, _, age = (<span class="st">"Alice"</span>, <span class="st">"Engineer"</span>, <span class="nm">30</span>)
<span class="bi">print</span>(name, age)      <span class="cm"># Alice 30</span>

<span class="cm"># Nested unpacking</span>
(a, b), c = (<span class="nm">1</span>, <span class="nm">2</span>), <span class="nm">3</span>
<span class="bi">print</span>(a, b, c)        <span class="cm"># 1 2 3</span>

<span class="cm"># In for loops</span>
points = [(<span class="nm">1</span>,<span class="nm">2</span>), (<span class="nm">3</span>,<span class="nm">4</span>), (<span class="nm">5</span>,<span class="nm">6</span>)]
<span class="kw">for</span> x, y <span class="kw">in</span> points:
    <span class="bi">print</span>(<span class="st">f"({x},{y})"</span>, end=<span class="st">" "</span>)
<span class="cm"># (1,2) (3,4) (5,6)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>10 20 30<br>2 1<br>1 [2,3,4,5]<br>[1,2,3,4] 5<br>Alice 30<br>1 2 3<br>(1,2) (3,4) (5,6)</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Methods &amp; Operations</h2>
<table class="data-table"><thead><tr><th>Method/Op</th><th>Description</th><th>Example</th><th>Result</th></tr></thead><tbody>
<tr><td><code>.count(x)</code></td><td>Count occurrences</td><td><code>(1,1,2).count(1)</code></td><td><code>2</code></td></tr>
<tr><td><code>.index(x)</code></td><td>First index of x</td><td><code>(1,2,3).index(2)</code></td><td><code>1</code></td></tr>
<tr><td><code>+</code></td><td>Concatenate</td><td><code>(1,2)+(3,4)</code></td><td><code>(1,2,3,4)</code></td></tr>
<tr><td><code>*</code></td><td>Repeat</td><td><code>(1,2)*3</code></td><td><code>(1,2,1,2,1,2)</code></td></tr>
<tr><td><code>sorted()</code></td><td>Returns sorted list</td><td><code>sorted((3,1,2))</code></td><td><code>[1,2,3]</code></td></tr>
</tbody></table></section>

<section class="content-section" id="s5"><h2>5 &middot; Named Tuples</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> collections <span class="kw">import</span> namedtuple

Point = namedtuple(<span class="st">"Point"</span>, [<span class="st">"x"</span>, <span class="st">"y"</span>])
p = Point(<span class="nm">3</span>, <span class="nm">4</span>)

<span class="bi">print</span>(p.x, p.y)     <span class="cm"># 3 4 (access by name)</span>
<span class="bi">print</span>(p[<span class="nm">0</span>])          <span class="cm"># 3   (still works as tuple)</span>
<span class="bi">print</span>(p)             <span class="cm"># Point(x=3, y=4)</span>
<span class="bi">print</span>(p._asdict())   <span class="cm"># {'x': 3, 'y': 4}</span>

Employee = namedtuple(<span class="st">"Employee"</span>, <span class="st">"name dept salary"</span>)
emp = Employee(<span class="st">"Alice"</span>, <span class="st">"Engineering"</span>, <span class="nm">95000</span>)
<span class="bi">print</span>(emp.name, emp.salary)  <span class="cm"># Alice 95000</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>3 4<br>3<br>Point(x=3, y=4)<br>{'x': 3, 'y': 4}<br>Alice 95000</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Tuples vs Lists</h2>
<table class="data-table"><thead><tr><th>Feature</th><th>Tuple</th><th>List</th></tr></thead><tbody>
<tr><td>Mutable</td><td>No &#x274C;</td><td>Yes &#x2705;</td></tr>
<tr><td>Hashable</td><td>Yes (dict key)</td><td>No</td></tr>
<tr><td>Speed</td><td>Faster iteration</td><td>Slightly slower</td></tr>
<tr><td>Memory</td><td>Less memory</td><td>More memory</td></tr>
<tr><td>Use case</td><td>Fixed data, records</td><td>Growing collections</td></tr>
<tr><td>Syntax</td><td><code>(1, 2, 3)</code></td><td><code>[1, 2, 3]</code></td></tr>
</tbody></table>
<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Rule of Thumb</strong><p>Use <strong>tuples</strong> for heterogeneous, fixed-size data (DB rows, coordinates, function returns). Use <strong>lists</strong> for homogeneous, variable-size collections.</p></div></div></section>''',
("lists.html","Lists"),("dictionaries.html","Dictionaries"))

print("Batch 1 done: strings.html, tuples.html")
