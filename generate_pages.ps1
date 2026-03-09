
$base = "C:\Users\DELL\.gemini\antigravity\scratch\python-textbook-site\pages"

# Full nav for pages that are 1 level deep (pages/section/file.html)
$fullNav = @'
        <div class="nav-items" id="navItems">
            <div class="nav-section">
                <div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F40D; Python Fundamentals</span><span class="chevron">&#x25BC;</span></div>
                <div class="nav-section-items">
                    <a href="{P}python/introduction.html" class="nav-item">Introduction</a>
                    <a href="{P}python/variables-datatypes.html" class="nav-item">Variables &amp; Data Types</a>
                    <a href="{P}python/operators.html" class="nav-item">Operators</a>
                    <a href="{P}python/control-flow.html" class="nav-item">Control Flow</a>
                    <a href="{P}python/loops.html" class="nav-item">Loops</a>
                    <a href="{P}python/functions.html" class="nav-item">Functions</a>
                    <a href="{P}python/strings.html" class="nav-item">Strings</a>
                    <a href="{P}python/lists.html" class="nav-item">Lists</a>
                    <a href="{P}python/tuples.html" class="nav-item">Tuples</a>
                    <a href="{P}python/dictionaries.html" class="nav-item">Dictionaries</a>
                    <a href="{P}python/sets.html" class="nav-item">Sets</a>
                    <a href="{P}python/file-io.html" class="nav-item">File I/O</a>
                    <a href="{P}python/exceptions.html" class="nav-item">Exception Handling</a>
                    <a href="{P}python/modules.html" class="nav-item">Modules &amp; Packages</a>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F3D7;&#xFE0F; OOP</span><span class="chevron">&#x25BC;</span></div>
                <div class="nav-section-items">
                    <a href="{P}oop/classes-objects.html" class="nav-item">Classes &amp; Objects</a>
                    <a href="{P}oop/inheritance.html" class="nav-item">Inheritance</a>
                    <a href="{P}oop/polymorphism.html" class="nav-item">Polymorphism</a>
                    <a href="{P}oop/encapsulation.html" class="nav-item">Encapsulation</a>
                    <a href="{P}oop/magic-methods.html" class="nav-item">Magic Methods</a>
                    <a href="{P}oop/decorators.html" class="nav-item">Decorators</a>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-section-header" onclick="toggleSection(this)"><span>&#x26A1; Advanced Python</span><span class="chevron">&#x25BC;</span></div>
                <div class="nav-section-items">
                    <a href="{P}advanced/generators.html" class="nav-item">Generators &amp; Iterators</a>
                    <a href="{P}advanced/comprehensions.html" class="nav-item">Comprehensions</a>
                    <a href="{P}advanced/lambda.html" class="nav-item">Lambda &amp; Functional</a>
                    <a href="{P}advanced/context-managers.html" class="nav-item">Context Managers</a>
                    <a href="{P}advanced/async.html" class="nav-item">Async &amp; Await</a>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F522; NumPy</span><span class="chevron">&#x25BC;</span></div>
                <div class="nav-section-items">
                    <a href="{P}numpy/arrays.html" class="nav-item">Arrays &amp; ndarray</a>
                    <a href="{P}numpy/operations.html" class="nav-item">Array Operations</a>
                    <a href="{P}numpy/indexing.html" class="nav-item">Indexing &amp; Slicing</a>
                    <a href="{P}numpy/reshaping.html" class="nav-item">Reshaping &amp; Stacking</a>
                    <a href="{P}numpy/math-functions.html" class="nav-item">Math Functions</a>
                    <a href="{P}numpy/linear-algebra.html" class="nav-item">Linear Algebra</a>
                    <a href="{P}numpy/random.html" class="nav-item">Random Module</a>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F43C; Pandas</span><span class="chevron">&#x25BC;</span></div>
                <div class="nav-section-items">
                    <a href="{P}pandas/series-dataframe.html" class="nav-item">Series &amp; DataFrame</a>
                    <a href="{P}pandas/reading-data.html" class="nav-item">Reading Data</a>
                    <a href="{P}pandas/selection.html" class="nav-item">Selection &amp; Filtering</a>
                    <a href="{P}pandas/cleaning.html" class="nav-item">Data Cleaning</a>
                    <a href="{P}pandas/groupby.html" class="nav-item">GroupBy &amp; Aggregation</a>
                    <a href="{P}pandas/merging.html" class="nav-item">Merging &amp; Joining</a>
                    <a href="{P}pandas/visualization.html" class="nav-item">Visualization</a>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F916; Machine Learning</span><span class="chevron">&#x25BC;</span></div>
                <div class="nav-section-items">
                    <a href="{P}ml/intro-ml.html" class="nav-item">Introduction to ML</a>
                    <a href="{P}ml/linear-regression.html" class="nav-item">Linear Regression</a>
                    <a href="{P}ml/logistic-regression.html" class="nav-item">Logistic Regression</a>
                    <a href="{P}ml/decision-trees.html" class="nav-item">Decision Trees</a>
                    <a href="{P}ml/random-forest.html" class="nav-item">Random Forest</a>
                    <a href="{P}ml/svm.html" class="nav-item">Support Vector Machine</a>
                    <a href="{P}ml/knn.html" class="nav-item">K-Nearest Neighbors</a>
                    <a href="{P}ml/clustering.html" class="nav-item">K-Means Clustering</a>
                    <a href="{P}ml/model-evaluation.html" class="nav-item">Model Evaluation</a>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F9E0; Deep Learning</span><span class="chevron">&#x25BC;</span></div>
                <div class="nav-section-items">
                    <a href="{P}dl/neural-networks.html" class="nav-item">Neural Networks</a>
                    <a href="{P}dl/backpropagation.html" class="nav-item">Backpropagation</a>
                    <a href="{P}dl/cnn.html" class="nav-item">CNN</a>
                    <a href="{P}dl/rnn-lstm.html" class="nav-item">RNN &amp; LSTM</a>
                    <a href="{P}dl/transformers.html" class="nav-item">Transformers</a>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-section-header" onclick="toggleSection(this)"><span>&#x1F4CA; Data Analysis</span><span class="chevron">&#x25BC;</span></div>
                <div class="nav-section-items">
                    <a href="{P}data/exploratory.html" class="nav-item">Exploratory Data Analysis</a>
                    <a href="{P}data/preprocessing.html" class="nav-item">Data Preprocessing</a>
                    <a href="{P}data/feature-engineering.html" class="nav-item">Feature Engineering</a>
                    <a href="{P}data/matplotlib.html" class="nav-item">Matplotlib</a>
                    <a href="{P}data/seaborn.html" class="nav-item">Seaborn</a>
                </div>
            </div>
        </div>
'@

function Build-Page {
    param(
        [string]$FilePath,
        [string]$Title,
        [string]$Section,
        [string]$Emoji,
        [string]$Difficulty,   # beginner | intermediate | advanced | expert
        [string]$Breadcrumb,
        [string]$Intro,
        [string]$Books,
        [string]$BodyHtml,
        [string]$PrevHref,
        [string]$PrevLabel,
        [string]$NextHref,
        [string]$NextLabel,
        [string]$NavPrefix     # ../ for 1-deep, ../../ for deeper
    )

    $nav = $fullNav -replace '\{P\}', $NavPrefix
    $cssPath = "${NavPrefix}../css/style.css"
    $jsPath  = "${NavPrefix}../js/main.js"
    # breadcrumb home link
    $homeHref = "${NavPrefix}../index.html"

    $diffBadge = $Difficulty

    $html = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$Title - Python Learning Hub</title>
    <meta name="description" content="$Title — comprehensive textbook-level reference with code examples and explanations.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="$cssPath">
</head>
<body>
    <nav class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <a href="$homeHref" class="logo">
                <div class="logo-icon">🐍</div>
                <div class="logo-text"><span class="logo-title">PyTextbook</span><span class="logo-sub">Complete Reference</span></div>
            </a>
            <button class="sidebar-toggle" id="sidebarToggle">&#x2630;</button>
        </div>
        <div class="search-box"><input type="text" id="searchInput" placeholder="&#x1F50D; Search topics..." class="search-input"></div>
        $nav
    </nav>
    <main class="main-content" id="mainContent">
        <header class="topbar">
            <button class="mobile-toggle" id="mobileToggle">&#x2630;</button>
            <div class="topbar-breadcrumb"><a href="$homeHref" style="color:var(--accent);text-decoration:none;">Home</a> $Breadcrumb</div>
            <div class="topbar-progress">
                <span class="progress-text">Reading</span>
                <div class="progress-bar-wrap"><div class="progress-bar-fill" id="progressFill"></div></div>
                <span id="progressPercent">0%</span>
            </div>
        </header>
        <div class="page-content">
            <div class="page-header">
                <span class="topic-badge">$Emoji $Section</span>
                <h1>$Title</h1>
                <p class="page-intro">$Intro</p>
                <div style="display:flex;gap:0.75rem;margin-top:1rem;flex-wrap:wrap;">
                    <span class="difficulty-badge $Difficulty">&#x25CF; $diffBadge</span>
                    <span style="font-size:0.8rem;color:var(--text-muted);align-self:center;">&#x1F4D6; Based on: <em>$Books</em></span>
                </div>
            </div>
            $BodyHtml
        </div>
        <div class="page-nav">
            <a href="$PrevHref"><span class="nav-direction">&#8592; Previous</span><span class="nav-topic">$PrevLabel</span></a>
            <a href="$NextHref" class="next"><span class="nav-direction">Next &#8594;</span><span class="nav-topic">$NextLabel</span></a>
        </div>
        <footer class="footer"><p>&#x1F40D; Python Learning Hub &mdash; Built from leading textbooks for deep understanding</p></footer>
    </main>
    <script src="$jsPath"></script>
</body>
</html>
"@
    $dir = Split-Path $FilePath -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    Set-Content -Path $FilePath -Value $html -Encoding UTF8
    Write-Host "Created: $FilePath"
}

# =================== PYTHON FUNDAMENTALS ===================

# strings.html
Build-Page `
  -FilePath "$base\python\strings.html" `
  -Title "Strings" `
  -Section "Python Fundamentals" `
  -Emoji "&#x1F40D;" `
  -Difficulty "beginner" `
  -Breadcrumb " &rarr; Python Fundamentals &rarr; Strings" `
  -Intro "Strings are immutable sequences of Unicode characters. Python provides a rich set of string methods, formatting options (f-strings, format(), %), and slicing operations for powerful text processing." `
  -Books "Python Programming (2024), Learning Python — Mark Lutz" `
  -PrevHref "functions.html" -PrevLabel "Functions" `
  -NextHref "lists.html" -NextLabel "Lists" `
  -NavPrefix "../" `
  -BodyHtml @'
            <div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
                <li><a href="#creation">Creating Strings</a></li>
                <li><a href="#indexing">Indexing &amp; Slicing</a></li>
                <li><a href="#formatting">String Formatting</a></li>
                <li><a href="#methods">Common String Methods</a></li>
                <li><a href="#immutability">Immutability</a></li>
            </ol></div>

            <section class="content-section" id="creation">
                <h2>1 &middot; Creating Strings</h2>
                <p>Python strings can use single quotes, double quotes, or triple quotes for multi-line text.</p>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; strings_basic.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">s1 = 'Hello'
s2 = "World"
s3 = """Multi
line string"""
s4 = r"C:\Users\name"   # raw string — backslash not escaped
s5 = b"bytes"           # bytes literal

print(type(s1))         # &lt;class 'str'&gt;
print(len(s2))          # 5
print(s1 + " " + s2)   # Hello World  (concatenation)
print(s2 * 3)           # WorldWorldWorld  (repetition)</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>&lt;class 'str'&gt;<br>5<br>Hello World<br>WorldWorldWorld</div>
                </div>
            </section>

            <section class="content-section" id="indexing">
                <h2>2 &middot; Indexing &amp; Slicing</h2>
                <p>Strings are sequences — each character has an index (0-based from left, -1-based from right).</p>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; slice.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5
#   -6 -5 -4 -3 -2 -1

print(s[0])      # P
print(s[-1])     # n
print(s[1:4])    # yth
print(s[:3])     # Pyt
print(s[3:])     # hon
print(s[::2])    # Pto  (every 2nd char)
print(s[::-1])   # nohtyP  (reverse)</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>P · n · yth · Pyt · hon · Pto · nohtyP</div>
                </div>
            </section>

            <section class="content-section" id="formatting">
                <h2>3 &middot; String Formatting</h2>
                <table class="data-table">
                    <thead><tr><th>Method</th><th>Syntax</th><th>Python Version</th></tr></thead>
                    <tbody>
                        <tr><td>f-strings (recommended)</td><td><code>f"Hello {name}"</code></td><td>3.6+</td></tr>
                        <tr><td>.format()</td><td><code>"Hello {}".format(name)</code></td><td>2.7+</td></tr>
                        <tr><td>% formatting (old)</td><td><code>"Hello %s" % name</code></td><td>2.x</td></tr>
                    </tbody>
                </table>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; formatting.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">name, age, pi = "Alice", 30, 3.14159

# f-strings (best Python 3 option)
print(f"Name: {name}, Age: {age}")         # Name: Alice, Age: 30
print(f"Pi = {pi:.2f}")                    # Pi = 3.14
print(f"Expr: {2 ** 10}")                  # Expr: 1024
print(f"{name!r}")                          # 'Alice' (repr)
print(f"{age:05d}")                         # 00030 (zero-padded)

# .format()
print("Hello, {}! You are {} years old.".format(name, age))
print("{0} + {0} = {1}".format(5, 10))    # 5 + 5 = 10</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>Name: Alice, Age: 30<br>Pi = 3.14<br>Expr: 1024<br>'Alice'<br>00030<br>Hello, Alice! You are 30 years old.<br>5 + 5 = 10</div>
                </div>
            </section>

            <section class="content-section" id="methods">
                <h2>4 &middot; Common String Methods</h2>
                <table class="data-table">
                    <thead><tr><th>Method</th><th>Description</th><th>Example</th><th>Result</th></tr></thead>
                    <tbody>
                        <tr><td><code>.upper()</code></td><td>Uppercase</td><td><code>"hello".upper()</code></td><td><code>"HELLO"</code></td></tr>
                        <tr><td><code>.lower()</code></td><td>Lowercase</td><td><code>"HELLO".lower()</code></td><td><code>"hello"</code></td></tr>
                        <tr><td><code>.strip()</code></td><td>Remove whitespace</td><td><code>"  hi  ".strip()</code></td><td><code>"hi"</code></td></tr>
                        <tr><td><code>.split()</code></td><td>Split to list</td><td><code>"a,b,c".split(",")</code></td><td><code>["a","b","c"]</code></td></tr>
                        <tr><td><code>.join()</code></td><td>Join iterable</td><td><code>"-".join(["a","b"])</code></td><td><code>"a-b"</code></td></tr>
                        <tr><td><code>.replace()</code></td><td>Replace substring</td><td><code>"cat".replace("c","b")</code></td><td><code>"bat"</code></td></tr>
                        <tr><td><code>.find()</code></td><td>Find index (-1 if not found)</td><td><code>"hello".find("l")</code></td><td><code>2</code></td></tr>
                        <tr><td><code>.startswith()</code></td><td>Starts with prefix</td><td><code>"Python".startswith("Py")</code></td><td><code>True</code></td></tr>
                        <tr><td><code>.count()</code></td><td>Count occurrences</td><td><code>"banana".count("a")</code></td><td><code>3</code></td></tr>
                        <tr><td><code>.isdigit()</code></td><td>All characters digits</td><td><code>"123".isdigit()</code></td><td><code>True</code></td></tr>
                    </tbody>
                </table>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; methods.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">text = "  Hello, World!  "
print(text.strip())                  # "Hello, World!"
print(text.strip().lower())          # "hello, world!"
print("python,java,c++".split(","))  # ['python', 'java', 'c++']
print(", ".join(["a", "b", "c"]))   # a, b, c
print("banana".replace("a", "o"))   # bonono
print("hello".center(11, "-"))       # ---hello---</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>Hello, World!<br>hello, world!<br>['python', 'java', 'c++']<br>a, b, c<br>bonono<br>---hello---</div>
                </div>
            </section>

            <section class="content-section" id="immutability">
                <h2>5 &middot; Immutability</h2>
                <p>Strings in Python are <strong>immutable</strong> — you cannot change individual characters. Every string operation returns a new string.</p>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; immutable.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">s = "Hello"
# s[0] = "J"  # TypeError: 'str' object does not support item assignment

# To "change" a string, create a new one
s = "J" + s[1:]   # "Jello"
print(s)           # Jello

# Efficient string building: use list + join
parts = []
for i in range(5):
    parts.append(str(i))
result = "".join(parts)   # "01234" — faster than += in loop
print(result)</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>Jello<br>01234</div>
                </div>
                <div class="callout tip">
                    <div class="callout-icon">&#x1F4A1;</div>
                    <div class="callout-content">
                        <strong>Performance Tip</strong>
                        <p>Avoid building strings with <code>+=</code> in a loop — it creates a new string each iteration. Use <code>list.append()</code> then <code>"".join(list)</code> for O(n) performance instead of O(n²).</p>
                    </div>
                </div>
            </section>
'@

# tuples.html
Build-Page `
  -FilePath "$base\python\tuples.html" `
  -Title "Tuples" `
  -Section "Python Fundamentals" `
  -Emoji "&#x1F40D;" `
  -Difficulty "beginner" `
  -Breadcrumb " &rarr; Python Fundamentals &rarr; Tuples" `
  -Intro "Tuples are immutable, ordered sequences — like lists but cannot be modified after creation. They are hashable (can be dict keys), faster to iterate, and ideal for fixed collections of heterogeneous data." `
  -Books "Python Programming (2024), Fluent Python — Luciano Ramalho" `
  -PrevHref "lists.html" -PrevLabel "Lists" `
  -NextHref "dictionaries.html" -NextLabel "Dictionaries" `
  -NavPrefix "../" `
  -BodyHtml @'
            <div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
                <li><a href="#create">Creating Tuples</a></li>
                <li><a href="#access">Accessing Elements</a></li>
                <li><a href="#unpacking">Tuple Unpacking</a></li>
                <li><a href="#methods">Methods &amp; Operations</a></li>
                <li><a href="#named">Named Tuples</a></li>
            </ol></div>

            <section class="content-section" id="create">
                <h2>1 &middot; Creating Tuples</h2>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; tuples_create.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">t1 = (1, 2, 3)
t2 = "a", "b", "c"         # parens optional
t3 = (42,)                  # single-item tuple — comma required!
t4 = ()                     # empty tuple
t5 = tuple([1, 2, 3])       # from list

print(type(t3))   # &lt;class 'tuple'&gt;
print(type((42))) # &lt;class 'int'&gt; — no comma = not a tuple!

# Tuples are heterogeneous
person = ("Alice", 30, True, [1, 2])
print(person[0])   # Alice</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>&lt;class 'tuple'&gt;<br>&lt;class 'int'&gt;<br>Alice</div>
                </div>
            </section>

            <section class="content-section" id="access">
                <h2>2 &middot; Accessing Elements</h2>
                <p>Tuples support all read-only sequence operations: indexing, slicing, iteration, membership testing.</p>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; tuple_access.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">coords = (10, 20, 30)
print(coords[0])     # 10
print(coords[-1])    # 30
print(coords[1:])    # (20, 30)
print(len(coords))   # 3
print(20 in coords)  # True

for val in coords:
    print(val, end=" ")   # 10 20 30

# Immutability check
# coords[0] = 99   # TypeError: tuple object does not support item assignment</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>10 · 30 · (20, 30) · 3 · True · 10 20 30</div>
                </div>
            </section>

            <section class="content-section" id="unpacking">
                <h2>3 &middot; Tuple Unpacking</h2>
                <p>Python's most powerful tuple feature — assign multiple variables at once from a tuple. Works with any iterable.</p>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; unpacking.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">x, y, z = (10, 20, 30)
print(x, y, z)    # 10 20 30

# Swap values elegantly
a, b = 1, 2
a, b = b, a
print(a, b)       # 2 1

# Star unpacking (Python 3)
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

*init, last = (1, 2, 3, 4, 5)
print(last)    # 5
print(init)    # [1, 2, 3, 4]

# Ignore values with _
name, _, age = ("Alice", "Engineer", 30)
print(name, age)   # Alice 30

# Nested unpacking
(a, b), c = (1, 2), 3
print(a, b, c)     # 1 2 3</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>10 20 30 · 2 1 · 1 · [2,3,4,5] · 5 · [1,2,3,4] · Alice 30 · 1 2 3</div>
                </div>
            </section>

            <section class="content-section" id="methods">
                <h2>4 &middot; Methods &amp; Operations</h2>
                <p>Tuples only have two methods (since they're immutable):</p>
                <table class="data-table">
                    <thead><tr><th>Method/Operation</th><th>Description</th><th>Example</th><th>Result</th></tr></thead>
                    <tbody>
                        <tr><td><code>.count(x)</code></td><td>Count occurrences of x</td><td><code>(1,1,2).count(1)</code></td><td><code>2</code></td></tr>
                        <tr><td><code>.index(x)</code></td><td>First index of x</td><td><code>(1,2,3).index(2)</code></td><td><code>1</code></td></tr>
                        <tr><td><code>+</code></td><td>Concatenate</td><td><code>(1,2) + (3,4)</code></td><td><code>(1,2,3,4)</code></td></tr>
                        <tr><td><code>*</code></td><td>Repeat</td><td><code>(1,2) * 3</code></td><td><code>(1,2,1,2,1,2)</code></td></tr>
                        <tr><td><code>sorted()</code></td><td>Returns sorted list</td><td><code>sorted((3,1,2))</code></td><td><code>[1,2,3]</code></td></tr>
                    </tbody>
                </table>
                <div class="callout note">
                    <div class="callout-icon">&#x1F4A1;</div>
                    <div class="callout-content"><strong>Tuple vs List</strong>
                    <p>Use tuples for <strong>heterogeneous, fixed-size</strong> data (e.g., database rows, coordinates, function returns). Use lists for <strong>homogeneous, variable-size</strong> collections. Tuples are also hashable so can be used as dict keys.</p></div>
                </div>
            </section>

            <section class="content-section" id="named">
                <h2>5 &middot; Named Tuples</h2>
                <p><code>collections.namedtuple</code> creates tuple subclasses with named fields — like lightweight classes.</p>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; named_tuple.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

print(p.x, p.y)     # 3 4  (access by name)
print(p[0], p[1])   # 3 4  (still works as tuple)
print(p)            # Point(x=3, y=4)

# Unpack just like regular tuple
x, y = p
print(x, y)         # 3 4

# New in Python 3.7+: dataclasses are often preferred
# but namedtuple is lighter (immutable, hashable)
Employee = namedtuple("Employee", "name dept salary")
emp = Employee("Alice", "Engineering", 95000)
print(emp.name, emp.salary)   # Alice 95000</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>3 4 · 3 4 · Point(x=3, y=4) · 3 4 · Alice 95000</div>
                </div>
            </section>
'@

# sets.html
Build-Page `
  -FilePath "$base\python\sets.html" `
  -Title "Sets" `
  -Section "Python Fundamentals" `
  -Emoji "&#x1F40D;" `
  -Difficulty "beginner" `
  -Breadcrumb " &rarr; Python Fundamentals &rarr; Sets" `
  -Intro "Sets are unordered, mutable collections of unique, hashable elements. They are optimised for membership testing (O(1) average), deduplication, and set-theoretic operations: union, intersection, difference, symmetric difference." `
  -Books "Python Programming (2024), Learning Python — Mark Lutz" `
  -PrevHref "dictionaries.html" -PrevLabel "Dictionaries" `
  -NextHref "file-io.html" -NextLabel "File I/O" `
  -NavPrefix "../" `
  -BodyHtml @'
            <div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
                <li><a href="#create">Creating Sets</a></li>
                <li><a href="#ops">Set Operations</a></li>
                <li><a href="#methods">Set Methods</a></li>
                <li><a href="#frozenset">frozenset</a></li>
            </ol></div>

            <section class="content-section" id="create">
                <h2>1 &middot; Creating Sets</h2>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; sets_create.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">s1 = {1, 2, 3, 4}
s2 = set([1, 2, 2, 3, 3])    # duplicates removed
s3 = set("hello")             # {'h','e','l','o'}
empty = set()                  # NOT {} (that's a dict!)

print(s1)                  # {1, 2, 3, 4}
print(s2)                  # {1, 2, 3}  — unordered, unique
print(len(s1))             # 4
print(3 in s1)             # True  — O(1) lookup!
print(type(empty))         # &lt;class 'set'&gt;</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>{1, 2, 3, 4} · {1, 2, 3} · 4 · True · &lt;class 'set'&gt;</div>
                </div>
            </section>

            <section class="content-section" id="ops">
                <h2>2 &middot; Set Operations (Mathematical)</h2>
                <table class="data-table">
                    <thead><tr><th>Operation</th><th>Operator</th><th>Method</th><th>Description</th></tr></thead>
                    <tbody>
                        <tr><td>Union</td><td><code>A | B</code></td><td><code>A.union(B)</code></td><td>All elements from both</td></tr>
                        <tr><td>Intersection</td><td><code>A &amp; B</code></td><td><code>A.intersection(B)</code></td><td>Elements in both</td></tr>
                        <tr><td>Difference</td><td><code>A - B</code></td><td><code>A.difference(B)</code></td><td>In A but not B</td></tr>
                        <tr><td>Symmetric Diff</td><td><code>A ^ B</code></td><td><code>A.symmetric_difference(B)</code></td><td>In one but not both</td></tr>
                        <tr><td>Subset</td><td><code>A &lt;= B</code></td><td><code>A.issubset(B)</code></td><td>A is contained in B</td></tr>
                        <tr><td>Superset</td><td><code>A &gt;= B</code></td><td><code>A.issuperset(B)</code></td><td>A contains B</td></tr>
                        <tr><td>Disjoint</td><td>—</td><td><code>A.isdisjoint(B)</code></td><td>No common elements</td></tr>
                    </tbody>
                </table>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; set_ops.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)    # {1,2,3,4,5,6,7,8}  union
print(A &amp; B)    # {4, 5}              intersection
print(A - B)    # {1, 2, 3}          difference
print(A ^ B)    # {1,2,3,6,7,8}      symmetric difference

print({1,2} &lt;= {1,2,3})    # True  (subset)
print({1,2,3} &gt;= {1,2})    # True  (superset)
print({1,2}.isdisjoint({3,4}))  # True (no overlap)</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>{1,2,3,4,5,6,7,8} · {4,5} · {1,2,3} · {1,2,3,6,7,8} · True · True · True</div>
                </div>
            </section>

            <section class="content-section" id="methods">
                <h2>3 &middot; Mutating Set Methods</h2>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; set_methods.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">s = {1, 2, 3}
s.add(4)          # {1,2,3,4}
s.discard(10)     # no error if not found
s.remove(2)       # KeyError if not found
print(s)          # {1,3,4}

popped = s.pop()  # removes and returns arbitrary element
print(popped)

# Update (in-place union)
s.update([5, 6, 7])
print(s)

# Common use case: deduplication
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(sorted(unique))   # [1, 2, 3, 4]</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>{1, 3, 4} · (some element) · (updated set) · [1, 2, 3, 4]</div>
                </div>
            </section>

            <section class="content-section" id="frozenset">
                <h2>4 &middot; frozenset — Immutable Sets</h2>
                <p><code>frozenset</code> is the immutable version of <code>set</code>. It is hashable and can be used as a dictionary key or stored inside another set.</p>
                <div class="code-block-wrapper">
                    <div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; frozenset.py</span><button class="copy-btn">Copy</button></div>
                    <pre class="code-block">fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError — immutable!

# Can be used as dict key
d = {frozenset([1, 2]): "pair", frozenset([1, 2, 3]): "triple"}
print(d[frozenset([1, 2])])    # pair

# Can be element of a set
s = {frozenset([1]), frozenset([2, 3])}
print(s)</pre>
                    <div class="output-block"><div class="output-label">&#x25B6; Output</div>pair · {frozenset({1}), frozenset({2, 3})}</div>
                </div>
            </section>
'@

Write-Host "Python fundamentals (strings, tuples, sets) created."
