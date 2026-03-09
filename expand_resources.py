import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# PYTHON PROGRAMS (from Drive PDF)
programs_body = '''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Basic Programs (IO, Math)</a></li>
<li><a href="#s2">Control Flow Programs</a></li>
<li><a href="#s3">Mathematical & Armstrong Numbers</a></li>
<li><a href="#s4">List & Array Programs</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Basic Programs</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Addition</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">num1 = <span class="bi">float</span>(<span class="bi">input</span>(<span class="st">"Enter first number: "</span>))
num2 = <span class="bi">float</span>(<span class="bi">input</span>(<span class="st">"Enter second number: "</span>))
sum = num1 + num2
<span class="bi">print</span>(<span class="st">f"The sum is {sum}"</span>)</pre></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Quadratic Equation</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> cmath
a, b, c = <span class="nm">1</span>, <span class="nm">5</span>, <span class="nm">6</span>
d = (b**<span class="nm">2</span>) - (<span class="nm">4</span>*a*c)
sol1 = (-b-cmath.sqrt(d))/(<span class="nm">2</span>*a)
sol2 = (-b+cmath.sqrt(d))/(<span class="nm">2</span>*a)
<span class="bi">print</span>(<span class="st">f"The solutions are {sol1} and {sol2}"</span>)</pre></div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Control Flow</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Leap Year</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">year = <span class="nm">2024</span>
<span class="kw">if</span> (year % <span class="nm">400</span> == <span class="nm">0</span>) <span class="kw">and</span> (year % <span class="nm">100</span> == <span class="nm">0</span>):
    <span class="bi">print</span>(<span class="st">"Leap Year"</span>)
<span class="kw">elif</span> (year % <span class="nm">4</span> == <span class="nm">0</span>) <span class="kw">and</span> (year % <span class="nm">100</span> != <span class="nm">0</span>):
    <span class="bi">print</span>(<span class="st">"Leap Year"</span>)
<span class="kw">else</span>:
    <span class="bi">print</span>(<span class="st">"Not a Leap Year"</span>)</pre></div>
</section>

<section class="content-section" id="s3"><h2>3 &middot; Armstrong Numbers</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Check Armstrong</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">num = <span class="nm">153</span>
sum = <span class="nm">0</span>
temp = num
<span class="kw">while</span> temp > <span class="nm">0</span>:
   digit = temp % <span class="nm">10</span>
   sum += digit ** <span class="nm">3</span>
   temp //= <span class="nm">10</span>
<span class="kw">if</span> num == sum:
   <span class="bi">print</span>(num, <span class="st">"is an Armstrong number"</span>)
<span class="kw">else</span>:
   <span class="bi">print</span>(num, <span class="st">"is not an Armstrong number"</span>)</pre></div>
</section>'''

make_page("resources/python-programs.html", "140+ Basic Python Programs", "Practical Guide", "&#x1F4D6;", "beginner", "Resources &rarr; Programs",
"A collection of 140+ practical Python programs ranging from simple math to complex algorithms, compiled for interview preparation and fundamental practice.",
"Basic Python Programs (Drive Resource)", programs_body, ("../index.html", "Home"), ("../index.html", "Home"))

# UPDATING Gen Template to include Resources in NAV
with open(r".\gen_template.py", "r", encoding="utf-8") as f:
    content = f.read()

resource_nav = '''<div class="nav-section"><div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F4DA; Resources</span><span class="chevron">&#x25BC;</span></div>
<div class="nav-section-items">
<a href="{P}resources/python-programs.html" class="nav-item">140+ Python Programs</a>
</div></div>'''

if 'Resources' not in content:
    content = content.replace('</div></div></div>', resource_nav + '</div></div></div>')
    with open(r".\gen_template.py", "w", encoding="utf-8") as f:
        f.write(content)

print("Resources page created and template updated!")
