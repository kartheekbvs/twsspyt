import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# MATPLOTLIB (MASSIVE EXPANSION)
make_page("data/matplotlib.html","Matplotlib Visualization","Data Analysis","&#x1F4CA;","intermediate","Data &rarr; Matplotlib",
"Matplotlib is Python&#39;s foundational plotting library. This comprehensive guide covers every plot type with multiple real-world examples: line plots, scatter, bar charts, histograms, pie charts, box plots, subplots, 3D plots, customization, and saving. All with different datasets and values for easy learning.",
"Python for Data Analysis &mdash; Wes McKinney, Matplotlib Documentation",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Getting Started &amp; Basic Setup</a></li>
<li><a href="#s2">Line Plots (plt.plot)</a></li>
<li><a href="#s3">Scatter Plots (plt.scatter)</a></li>
<li><a href="#s4">Bar Charts (plt.bar)</a></li>
<li><a href="#s5">Histograms (plt.hist)</a></li>
<li><a href="#s6">Pie Charts (plt.pie)</a></li>
<li><a href="#s7">Box Plots (plt.boxplot)</a></li>
<li><a href="#s8">Subplots &amp; Multiple Plots</a></li>
<li><a href="#s9">Customization &amp; Styling</a></li>
<li><a href="#s10">Saving Plots &amp; Advanced</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Getting Started</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># The simplest plot</span>
plt.plot([<span class="nm">1</span>, <span class="nm">2</span>, <span class="nm">3</span>, <span class="nm">4</span>], [<span class="nm">10</span>, <span class="nm">20</span>, <span class="nm">25</span>, <span class="nm">30</span>])
plt.title(<span class="st">"My First Plot"</span>)
plt.xlabel(<span class="st">"X Axis"</span>)
plt.ylabel(<span class="st">"Y Axis"</span>)
plt.show()

<span class="cm"># Two ways to create plots:</span>
<span class="cm"># 1. pyplot interface (quick, simple)</span>
plt.plot(x, y)
plt.show()

<span class="cm"># 2. Object-oriented (recommended for complex plots)</span>
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(<span class="st">"Title"</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[A simple line plot from (1,10) to (4,30)]</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Line Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 1: Temperature Over a Week</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">days = [<span class="st">"Mon"</span>,<span class="st">"Tue"</span>,<span class="st">"Wed"</span>,<span class="st">"Thu"</span>,<span class="st">"Fri"</span>,<span class="st">"Sat"</span>,<span class="st">"Sun"</span>]
temp_high = [<span class="nm">28</span>, <span class="nm">30</span>, <span class="nm">32</span>, <span class="nm">29</span>, <span class="nm">27</span>, <span class="nm">31</span>, <span class="nm">33</span>]
temp_low  = [<span class="nm">18</span>, <span class="nm">20</span>, <span class="nm">22</span>, <span class="nm">19</span>, <span class="nm">17</span>, <span class="nm">21</span>, <span class="nm">23</span>]

plt.figure(figsize=(<span class="nm">10</span>, <span class="nm">5</span>))
plt.plot(days, temp_high, color=<span class="st">"red"</span>, marker=<span class="st">"o"</span>,
         linewidth=<span class="nm">2</span>, label=<span class="st">"High"</span>)
plt.plot(days, temp_low, color=<span class="st">"blue"</span>, marker=<span class="st">"s"</span>,
         linewidth=<span class="nm">2</span>, linestyle=<span class="st">"--"</span>, label=<span class="st">"Low"</span>)
plt.fill_between(days, temp_low, temp_high, alpha=<span class="nm">0.2</span>, color=<span class="st">"orange"</span>)
plt.title(<span class="st">"Weekly Temperature"</span>, fontsize=<span class="nm">16</span>, fontweight=<span class="st">"bold"</span>)
plt.xlabel(<span class="st">"Day"</span>)
plt.ylabel(<span class="st">"Temperature (&deg;C)"</span>)
plt.legend()
plt.grid(<span class="kw">True</span>, alpha=<span class="nm">0.3</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Red solid line with circles for highs, blue dashed with squares for lows, orange fill between]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 2: Stock Prices</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">42</span>)
days = np.arange(<span class="nm">1</span>, <span class="nm">31</span>)
stock_a = <span class="nm">100</span> + np.cumsum(np.random.randn(<span class="nm">30</span>) * <span class="nm">2</span>)
stock_b = <span class="nm">80</span> + np.cumsum(np.random.randn(<span class="nm">30</span>) * <span class="nm">1.5</span>)
stock_c = <span class="nm">120</span> + np.cumsum(np.random.randn(<span class="nm">30</span>) * <span class="nm">3</span>)

plt.figure(figsize=(<span class="nm">12</span>, <span class="nm">6</span>))
plt.plot(days, stock_a, <span class="st">"-o"</span>, markersize=<span class="nm">3</span>, label=<span class="st">"Tech Corp ($100)"</span>)
plt.plot(days, stock_b, <span class="st">"-s"</span>, markersize=<span class="nm">3</span>, label=<span class="st">"Health Inc ($80)"</span>)
plt.plot(days, stock_c, <span class="st">"-^"</span>, markersize=<span class="nm">3</span>, label=<span class="st">"Energy Ltd ($120)"</span>)
plt.title(<span class="st">"30-Day Stock Performance"</span>, fontsize=<span class="nm">14</span>)
plt.xlabel(<span class="st">"Day"</span>); plt.ylabel(<span class="st">"Price ($)"</span>)
plt.legend(loc=<span class="st">"upper left"</span>)
plt.grid(<span class="kw">True</span>, alpha=<span class="nm">0.3</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[3 stock price lines with different markers over 30 days]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 3: Math Functions</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">x = np.linspace(-<span class="nm">2</span>*np.pi, <span class="nm">2</span>*np.pi, <span class="nm">200</span>)

plt.figure(figsize=(<span class="nm">10</span>, <span class="nm">5</span>))
plt.plot(x, np.sin(x), label=<span class="st">"sin(x)"</span>, linewidth=<span class="nm">2</span>)
plt.plot(x, np.cos(x), label=<span class="st">"cos(x)"</span>, linewidth=<span class="nm">2</span>)
plt.plot(x, np.sin(x) + np.cos(x), <span class="st">"--"</span>, label=<span class="st">"sin+cos"</span>, linewidth=<span class="nm">1.5</span>)
plt.axhline(y=<span class="nm">0</span>, color=<span class="st">"black"</span>, linewidth=<span class="nm">0.5</span>)
plt.axvline(x=<span class="nm">0</span>, color=<span class="st">"black"</span>, linewidth=<span class="nm">0.5</span>)
plt.title(<span class="st">"Trigonometric Functions"</span>)
plt.xlabel(<span class="st">"x (radians)"</span>); plt.ylabel(<span class="st">"y"</span>)
plt.legend(); plt.grid(<span class="kw">True</span>, alpha=<span class="nm">0.3</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Smooth sine and cosine waves]</div></div>

<table class="data-table"><thead><tr><th>Marker</th><th>Meaning</th><th>Linestyle</th><th>Meaning</th></tr></thead><tbody>
<tr><td><code>"o"</code></td><td>Circle</td><td><code>"-"</code></td><td>Solid</td></tr>
<tr><td><code>"s"</code></td><td>Square</td><td><code>"--"</code></td><td>Dashed</td></tr>
<tr><td><code>"^"</code></td><td>Triangle up</td><td><code>"-."</code></td><td>Dash-dot</td></tr>
<tr><td><code>"D"</code></td><td>Diamond</td><td><code>":"</code></td><td>Dotted</td></tr>
<tr><td><code>"*"</code></td><td>Star</td><td><code>"none"</code></td><td>No line</td></tr>
</tbody></table></section>

<section class="content-section" id="s3"><h2>3 &middot; Scatter Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 1: Height vs Weight</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">42</span>)
height = np.random.normal(<span class="nm">170</span>, <span class="nm">10</span>, <span class="nm">100</span>)
weight = height * <span class="nm">0.5</span> + np.random.normal(<span class="nm">0</span>, <span class="nm">5</span>, <span class="nm">100</span>)

plt.figure(figsize=(<span class="nm">8</span>, <span class="nm">6</span>))
plt.scatter(height, weight, c=<span class="st">"steelblue"</span>, alpha=<span class="nm">0.7</span>, edgecolors=<span class="st">"white"</span>, s=<span class="nm">60</span>)
plt.title(<span class="st">"Height vs Weight"</span>, fontsize=<span class="nm">14</span>)
plt.xlabel(<span class="st">"Height (cm)"</span>); plt.ylabel(<span class="st">"Weight (kg)"</span>)
plt.grid(<span class="kw">True</span>, alpha=<span class="nm">0.3</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Scatter of 100 points showing positive height-weight correlation]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 2: Colored by Category + Size by Value</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">10</span>)
n = <span class="nm">50</span>
x = np.random.rand(n) * <span class="nm">100</span>
y = np.random.rand(n) * <span class="nm">100</span>
colors = np.random.randint(<span class="nm">0</span>, <span class="nm">4</span>, n)        <span class="cm"># 4 categories</span>
sizes = np.random.rand(n) * <span class="nm">500</span> + <span class="nm">50</span>      <span class="cm"># bubble sizes</span>

plt.figure(figsize=(<span class="nm">10</span>, <span class="nm">7</span>))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=<span class="nm">0.6</span>,
                      cmap=<span class="st">"viridis"</span>, edgecolors=<span class="st">"black"</span>)
plt.colorbar(scatter, label=<span class="st">"Category"</span>)
plt.title(<span class="st">"Bubble Chart"</span>, fontsize=<span class="nm">14</span>)
plt.xlabel(<span class="st">"Feature X"</span>); plt.ylabel(<span class="st">"Feature Y"</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Colored bubbles with size variation and colorbar]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 3: Exam Scores Correlation</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">7</span>)
math_score = np.random.randint(<span class="nm">40</span>, <span class="nm">100</span>, <span class="nm">80</span>)
science_score = math_score * <span class="nm">0.8</span> + np.random.randint(-<span class="nm">10</span>, <span class="nm">10</span>, <span class="nm">80</span>)
passed = (math_score + science_score) > <span class="nm">140</span>

plt.figure(figsize=(<span class="nm">8</span>, <span class="nm">6</span>))
plt.scatter(math_score[passed], science_score[passed],
            c=<span class="st">"green"</span>, marker=<span class="st">"o"</span>, label=<span class="st">"Passed"</span>, alpha=<span class="nm">0.7</span>)
plt.scatter(math_score[~passed], science_score[~passed],
            c=<span class="st">"red"</span>, marker=<span class="st">"x"</span>, label=<span class="st">"Failed"</span>, alpha=<span class="nm">0.7</span>)
plt.title(<span class="st">"Math vs Science Scores"</span>)
plt.xlabel(<span class="st">"Math Score"</span>); plt.ylabel(<span class="st">"Science Score"</span>)
plt.legend()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Green circles (passed) vs red X (failed) showing score clusters]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Bar Charts</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 1: Programming Language Popularity</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">languages = [<span class="st">"Python"</span>, <span class="st">"JavaScript"</span>, <span class="st">"Java"</span>, <span class="st">"C++"</span>, <span class="st">"Go"</span>, <span class="st">"Rust"</span>]
users = [<span class="nm">35</span>, <span class="nm">30</span>, <span class="nm">20</span>, <span class="nm">15</span>, <span class="nm">10</span>, <span class="nm">8</span>]
colors = [<span class="st">"#306998"</span>, <span class="st">"#F7DF1E"</span>, <span class="st">"#f89820"</span>, <span class="st">"#044F88"</span>, <span class="st">"#00ADD8"</span>, <span class="st">"#DEA584"</span>]

plt.figure(figsize=(<span class="nm">10</span>, <span class="nm">5</span>))
bars = plt.bar(languages, users, color=colors, edgecolor=<span class="st">"black"</span>, width=<span class="nm">0.6</span>)
<span class="cm"># Add value labels on bars</span>
<span class="kw">for</span> bar, val <span class="kw">in</span> <span class="bi">zip</span>(bars, users):
    plt.text(bar.get_x() + bar.get_width()/<span class="nm">2</span>, bar.get_height() + <span class="nm">0.5</span>,
             <span class="st">f"{val}%"</span>, ha=<span class="st">"center"</span>, fontweight=<span class="st">"bold"</span>)
plt.title(<span class="st">"Programming Language Popularity 2024"</span>, fontsize=<span class="nm">14</span>)
plt.ylabel(<span class="st">"Usage (%)"</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Colored bars with percentage labels on top]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 2: Grouped &amp; Stacked Bars</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">categories = [<span class="st">"Q1"</span>, <span class="st">"Q2"</span>, <span class="st">"Q3"</span>, <span class="st">"Q4"</span>]
product_a = [<span class="nm">15</span>, <span class="nm">25</span>, <span class="nm">30</span>, <span class="nm">20</span>]
product_b = [<span class="nm">20</span>, <span class="nm">15</span>, <span class="nm">25</span>, <span class="nm">35</span>]
x = np.arange(<span class="bi">len</span>(categories))
width = <span class="nm">0.35</span>

<span class="cm"># Grouped bar chart</span>
fig, (ax1, ax2) = plt.subplots(<span class="nm">1</span>, <span class="nm">2</span>, figsize=(<span class="nm">14</span>, <span class="nm">5</span>))

ax1.bar(x - width/<span class="nm">2</span>, product_a, width, label=<span class="st">"Product A"</span>, color=<span class="st">"#3498db"</span>)
ax1.bar(x + width/<span class="nm">2</span>, product_b, width, label=<span class="st">"Product B"</span>, color=<span class="st">"#e74c3c"</span>)
ax1.set_xticks(x); ax1.set_xticklabels(categories)
ax1.legend(); ax1.set_title(<span class="st">"Grouped Bar Chart"</span>)

<span class="cm"># Stacked bar chart</span>
ax2.bar(categories, product_a, label=<span class="st">"Product A"</span>, color=<span class="st">"#3498db"</span>)
ax2.bar(categories, product_b, bottom=product_a, label=<span class="st">"Product B"</span>, color=<span class="st">"#e74c3c"</span>)
ax2.legend(); ax2.set_title(<span class="st">"Stacked Bar Chart"</span>)
plt.tight_layout()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Side-by-side: grouped bars left, stacked bars right]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 3: Horizontal Bar</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">skills = [<span class="st">"Python"</span>, <span class="st">"SQL"</span>, <span class="st">"Machine Learning"</span>, <span class="st">"Data Viz"</span>, <span class="st">"Statistics"</span>]
proficiency = [<span class="nm">90</span>, <span class="nm">85</span>, <span class="nm">75</span>, <span class="nm">80</span>, <span class="nm">70</span>]

plt.figure(figsize=(<span class="nm">8</span>, <span class="nm">4</span>))
plt.barh(skills, proficiency, color=<span class="st">"#2ecc71"</span>, edgecolor=<span class="st">"#27ae60"</span>, height=<span class="nm">0.6</span>)
plt.xlabel(<span class="st">"Proficiency %"</span>)
plt.title(<span class="st">"Skill Proficiency"</span>)
plt.xlim(<span class="nm">0</span>, <span class="nm">100</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Horizontal green bars for skill levels]</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Histograms</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 1: Student Grades Distribution</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">42</span>)
grades = np.random.normal(<span class="nm">72</span>, <span class="nm">12</span>, <span class="nm">200</span>)   <span class="cm"># mean=72, std=12</span>

plt.figure(figsize=(<span class="nm">10</span>, <span class="nm">5</span>))
plt.hist(grades, bins=<span class="nm">20</span>, color=<span class="st">"#3498db"</span>, edgecolor=<span class="st">"black"</span>,
         alpha=<span class="nm">0.8</span>, label=<span class="st">"Grades"</span>)
plt.axvline(grades.mean(), color=<span class="st">"red"</span>, linewidth=<span class="nm">2</span>,
            linestyle=<span class="st">"--"</span>, label=<span class="st">f"Mean: {grades.mean():.1f}"</span>)
plt.axvline(np.median(grades), color=<span class="st">"green"</span>, linewidth=<span class="nm">2</span>,
            linestyle=<span class="st">":"</span>, label=<span class="st">f"Median: {np.median(grades):.1f}"</span>)
plt.title(<span class="st">"Grade Distribution (200 Students)"</span>, fontsize=<span class="nm">14</span>)
plt.xlabel(<span class="st">"Grade"</span>); plt.ylabel(<span class="st">"Frequency"</span>)
plt.legend()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Bell curve with red dashed mean and green dotted median lines]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 2: Comparing Distributions</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">5</span>)
class_a = np.random.normal(<span class="nm">70</span>, <span class="nm">10</span>, <span class="nm">150</span>)
class_b = np.random.normal(<span class="nm">80</span>, <span class="nm">8</span>, <span class="nm">150</span>)

plt.figure(figsize=(<span class="nm">10</span>, <span class="nm">5</span>))
plt.hist(class_a, bins=<span class="nm">15</span>, alpha=<span class="nm">0.6</span>, color=<span class="st">"blue"</span>, label=<span class="st">"Class A (avg=70)"</span>)
plt.hist(class_b, bins=<span class="nm">15</span>, alpha=<span class="nm">0.6</span>, color=<span class="st">"orange"</span>, label=<span class="st">"Class B (avg=80)"</span>)
plt.title(<span class="st">"Grade Comparison: Two Classes"</span>)
plt.xlabel(<span class="st">"Score"</span>); plt.ylabel(<span class="st">"Count"</span>)
plt.legend()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Two overlapping translucent histograms, blue and orange]</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Pie Charts</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 1: Market Share</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">companies = [<span class="st">"Apple"</span>, <span class="st">"Samsung"</span>, <span class="st">"Xiaomi"</span>, <span class="st">"Others"</span>]
shares = [<span class="nm">27</span>, <span class="nm">20</span>, <span class="nm">13</span>, <span class="nm">40</span>]
explode = (<span class="nm">0.05</span>, <span class="nm">0</span>, <span class="nm">0</span>, <span class="nm">0</span>)   <span class="cm"># explode Apple slice</span>
colors = [<span class="st">"#A2AAAD"</span>, <span class="st">"#1428A0"</span>, <span class="st">"#FF6900"</span>, <span class="st">"#95a5a6"</span>]

plt.figure(figsize=(<span class="nm">8</span>, <span class="nm">8</span>))
plt.pie(shares, labels=companies, autopct=<span class="st">"%.1f%%"</span>, explode=explode,
        colors=colors, shadow=<span class="kw">True</span>, startangle=<span class="nm">90</span>,
        textprops={<span class="st">"fontsize"</span>: <span class="nm">12</span>})
plt.title(<span class="st">"Smartphone Market Share 2024"</span>, fontsize=<span class="nm">14</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Pie chart with Apple slice slightly pulled out, percentages shown]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 2: Donut Chart</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">expenses = [<span class="nm">35</span>, <span class="nm">25</span>, <span class="nm">15</span>, <span class="nm">10</span>, <span class="nm">15</span>]
labels = [<span class="st">"Rent"</span>, <span class="st">"Food"</span>, <span class="st">"Transport"</span>, <span class="st">"Entertainment"</span>, <span class="st">"Savings"</span>]

plt.figure(figsize=(<span class="nm">8</span>, <span class="nm">8</span>))
wedges, texts, autotexts = plt.pie(expenses, labels=labels, autopct=<span class="st">"%.0f%%"</span>,
    pctdistance=<span class="nm">0.85</span>, colors=plt.cm.Set3.colors[:<span class="nm">5</span>])
<span class="cm"># Create donut by adding white circle in center</span>
centre_circle = plt.Circle((<span class="nm">0</span>,<span class="nm">0</span>), <span class="nm">0.60</span>, fc=<span class="st">"white"</span>)
plt.gca().add_artist(centre_circle)
plt.title(<span class="st">"Monthly Budget Breakdown"</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Donut chart with white center and percentages on ring]</div></div></section>

<section class="content-section" id="s7"><h2>7 &middot; Box Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 1: Salary by Department</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">42</span>)
engineering = np.random.normal(<span class="nm">90000</span>, <span class="nm">15000</span>, <span class="nm">50</span>)
marketing   = np.random.normal(<span class="nm">70000</span>, <span class="nm">12000</span>, <span class="nm">50</span>)
sales       = np.random.normal(<span class="nm">60000</span>, <span class="nm">20000</span>, <span class="nm">50</span>)
hr          = np.random.normal(<span class="nm">65000</span>, <span class="nm">10000</span>, <span class="nm">50</span>)

plt.figure(figsize=(<span class="nm">10</span>, <span class="nm">6</span>))
bp = plt.boxplot([engineering, marketing, sales, hr],
    labels=[<span class="st">"Engineering"</span>, <span class="st">"Marketing"</span>, <span class="st">"Sales"</span>, <span class="st">"HR"</span>],
    patch_artist=<span class="kw">True</span>,    <span class="cm"># filled boxes</span>
    notch=<span class="kw">True</span>,            <span class="cm"># confidence interval</span>
    showmeans=<span class="kw">True</span>,        <span class="cm"># show mean marker</span>
    meanprops={<span class="st">"marker"</span>:<span class="st">"D"</span>, <span class="st">"markerfacecolor"</span>:<span class="st">"red"</span>}
)
colors = [<span class="st">"#3498db"</span>, <span class="st">"#e74c3c"</span>, <span class="st">"#2ecc71"</span>, <span class="st">"#f39c12"</span>]
<span class="kw">for</span> patch, color <span class="kw">in</span> <span class="bi">zip</span>(bp[<span class="st">"boxes"</span>], colors):
    patch.set_facecolor(color)
    patch.set_alpha(<span class="nm">0.7</span>)
plt.title(<span class="st">"Salary Distribution by Department"</span>, fontsize=<span class="nm">14</span>)
plt.ylabel(<span class="st">"Annual Salary ($)"</span>)
plt.grid(<span class="kw">True</span>, alpha=<span class="nm">0.3</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[4 notched boxplots: Eng highest, Sales widest spread, outliers visible]</div></div>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Box Plot Anatomy</strong>
<ul><li><strong>Box</strong>: Q1 to Q3 (interquartile range)</li>
<li><strong>Line inside</strong>: Median (Q2)</li>
<li><strong>Diamond</strong>: Mean (when showmeans=True)</li>
<li><strong>Whiskers</strong>: 1.5 × IQR beyond Q1/Q3</li>
<li><strong>Dots beyond</strong>: Outliers</li></ul></div></div></section>

<section class="content-section" id="s8"><h2>8 &middot; Subplots &amp; Multiple Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 1: plt.subplot()</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">x = np.linspace(<span class="nm">0</span>, <span class="nm">10</span>, <span class="nm">100</span>)

plt.figure(figsize=(<span class="nm">12</span>, <span class="nm">4</span>))

plt.subplot(<span class="nm">1</span>, <span class="nm">3</span>, <span class="nm">1</span>)  <span class="cm"># 1 row, 3 cols, position 1</span>
plt.plot(x, np.sin(x), <span class="st">"r-"</span>)
plt.title(<span class="st">"Sine"</span>)

plt.subplot(<span class="nm">1</span>, <span class="nm">3</span>, <span class="nm">2</span>)
plt.plot(x, np.cos(x), <span class="st">"b-"</span>)
plt.title(<span class="st">"Cosine"</span>)

plt.subplot(<span class="nm">1</span>, <span class="nm">3</span>, <span class="nm">3</span>)
plt.plot(x, np.tan(x), <span class="st">"g-"</span>)
plt.ylim(-<span class="nm">5</span>, <span class="nm">5</span>)
plt.title(<span class="st">"Tangent"</span>)

plt.tight_layout()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[3 plots side by side: sine, cosine, tangent]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Example 2: plt.subplots() (recommended)</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">42</span>)
data = np.random.randn(<span class="nm">100</span>)

fig, axes = plt.subplots(<span class="nm">2</span>, <span class="nm">2</span>, figsize=(<span class="nm">12</span>, <span class="nm">10</span>))

<span class="cm"># Top-left: Line</span>
axes[<span class="nm">0</span>,<span class="nm">0</span>].plot(np.cumsum(data), <span class="st">"b-"</span>, linewidth=<span class="nm">2</span>)
axes[<span class="nm">0</span>,<span class="nm">0</span>].set_title(<span class="st">"Cumulative Sum"</span>)
axes[<span class="nm">0</span>,<span class="nm">0</span>].grid(<span class="kw">True</span>, alpha=<span class="nm">0.3</span>)

<span class="cm"># Top-right: Histogram</span>
axes[<span class="nm">0</span>,<span class="nm">1</span>].hist(data, bins=<span class="nm">20</span>, color=<span class="st">"#e74c3c"</span>, edgecolor=<span class="st">"black"</span>)
axes[<span class="nm">0</span>,<span class="nm">1</span>].set_title(<span class="st">"Distribution"</span>)

<span class="cm"># Bottom-left: Scatter</span>
x2, y2 = np.random.rand(<span class="nm">50</span>), np.random.rand(<span class="nm">50</span>)
axes[<span class="nm">1</span>,<span class="nm">0</span>].scatter(x2, y2, c=<span class="st">"#2ecc71"</span>, s=<span class="nm">50</span>)
axes[<span class="nm">1</span>,<span class="nm">0</span>].set_title(<span class="st">"Random Scatter"</span>)

<span class="cm"># Bottom-right: Box</span>
axes[<span class="nm">1</span>,<span class="nm">1</span>].boxplot([data, data*<span class="nm">1.5</span>], labels=[<span class="st">"Set A"</span>, <span class="st">"Set B"</span>])
axes[<span class="nm">1</span>,<span class="nm">1</span>].set_title(<span class="st">"Box Plot"</span>)

fig.suptitle(<span class="st">"Dashboard: 4 Different Plot Types"</span>, fontsize=<span class="nm">16</span>, fontweight=<span class="st">"bold"</span>)
plt.tight_layout()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[2x2 grid: cumulative line, histogram, scatter, boxplot]</div></div></section>

<section class="content-section" id="s9"><h2>9 &middot; Customization &amp; Styling</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; All Customization Options</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Title, labels, legend, grid</span>
plt.title(<span class="st">"Title"</span>, fontsize=<span class="nm">16</span>, fontweight=<span class="st">"bold"</span>, color=<span class="st">"#2c3e50"</span>)
plt.xlabel(<span class="st">"X Label"</span>, fontsize=<span class="nm">12</span>)
plt.ylabel(<span class="st">"Y Label"</span>, fontsize=<span class="nm">12</span>)
plt.legend(loc=<span class="st">"best"</span>, frameon=<span class="kw">True</span>, fontsize=<span class="nm">10</span>)
plt.grid(<span class="kw">True</span>, alpha=<span class="nm">0.3</span>, linestyle=<span class="st">"--"</span>)

<span class="cm"># Axis limits and ticks</span>
plt.xlim(<span class="nm">0</span>, <span class="nm">100</span>)
plt.ylim(-<span class="nm">10</span>, <span class="nm">50</span>)
plt.xticks([<span class="nm">0</span>, <span class="nm">25</span>, <span class="nm">50</span>, <span class="nm">75</span>, <span class="nm">100</span>])
plt.yticks(rotation=<span class="nm">45</span>)

<span class="cm"># Figure size</span>
plt.figure(figsize=(<span class="nm">width</span>, <span class="nm">height</span>))

<span class="cm"># Annotations</span>
plt.annotate(<span class="st">"Peak"</span>, xy=(<span class="nm">5</span>, <span class="nm">30</span>), xytext=(<span class="nm">7</span>, <span class="nm">35</span>),
             arrowprops=<span class="bi">dict</span>(arrowstyle=<span class="st">"->"</span>, color=<span class="st">"red"</span>),
             fontsize=<span class="nm">12</span>)

<span class="cm"># Horizontal/Vertical lines</span>
plt.axhline(y=<span class="nm">0</span>, color=<span class="st">"gray"</span>, linewidth=<span class="nm">0.5</span>)
plt.axvline(x=<span class="nm">50</span>, color=<span class="st">"gray"</span>, linestyle=<span class="st">"--"</span>)

<span class="cm"># Style sheets</span>
<span class="bi">print</span>(plt.style.available)  <span class="cm"># list all styles</span>
plt.style.use(<span class="st">"ggplot"</span>)      <span class="cm"># set a style</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Available styles: ['Solarize_Light2', 'bmh', 'dark_background', 'ggplot', ...]</div></div>

<table class="data-table"><thead><tr><th>Style</th><th>Look</th><th>Best For</th></tr></thead><tbody>
<tr><td><code>"ggplot"</code></td><td>Clean, R-style with grid</td><td>Academic papers</td></tr>
<tr><td><code>"seaborn-v0_8"</code></td><td>Statistical, muted colors</td><td>Data analysis</td></tr>
<tr><td><code>"dark_background"</code></td><td>Dark theme</td><td>Presentations</td></tr>
<tr><td><code>"bmh"</code></td><td>Bayesian methods style</td><td>Reports</td></tr>
<tr><td><code>"fivethirtyeight"</code></td><td>News-style, bold</td><td>Dashboards</td></tr>
</tbody></table></section>

<section class="content-section" id="s10"><h2>10 &middot; Saving &amp; Advanced Features</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Saving Plots</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Save to file</span>
fig, ax = plt.subplots(figsize=(<span class="nm">8</span>, <span class="nm">5</span>))
ax.plot([<span class="nm">1</span>,<span class="nm">2</span>,<span class="nm">3</span>], [<span class="nm">1</span>,<span class="nm">4</span>,<span class="nm">9</span>])

<span class="cm"># Different formats</span>
fig.savefig(<span class="st">"plot.png"</span>, dpi=<span class="nm">300</span>, bbox_inches=<span class="st">"tight"</span>)
fig.savefig(<span class="st">"plot.pdf"</span>, bbox_inches=<span class="st">"tight"</span>)
fig.savefig(<span class="st">"plot.svg"</span>, bbox_inches=<span class="st">"tight"</span>)

<span class="cm"># With transparent background</span>
fig.savefig(<span class="st">"plot_transparent.png"</span>, transparent=<span class="kw">True</span>, dpi=<span class="nm">300</span>)

<span class="cm"># Key parameters:</span>
<span class="cm"># dpi=300           high resolution</span>
<span class="cm"># bbox_inches="tight"  remove whitespace</span>
<span class="cm"># facecolor="white" white background</span>
<span class="cm"># transparent=True  transparent background</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Files saved: plot.png, plot.pdf, plot.svg]</div></div>

<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Heatmap</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">np.random.seed(<span class="nm">42</span>)
data = np.random.rand(<span class="nm">5</span>, <span class="nm">5</span>)
labels = [<span class="st">"A"</span>,<span class="st">"B"</span>,<span class="st">"C"</span>,<span class="st">"D"</span>,<span class="st">"E"</span>]

fig, ax = plt.subplots(figsize=(<span class="nm">8</span>, <span class="nm">6</span>))
im = ax.imshow(data, cmap=<span class="st">"YlOrRd"</span>)
ax.set_xticks(np.arange(<span class="nm">5</span>)); ax.set_xticklabels(labels)
ax.set_yticks(np.arange(<span class="nm">5</span>)); ax.set_yticklabels(labels)
<span class="cm"># Add text annotations</span>
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">5</span>):
    <span class="kw">for</span> j <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">5</span>):
        ax.text(j, i, <span class="st">f"{data[i,j]:.2f}"</span>, ha=<span class="st">"center"</span>, va=<span class="st">"center"</span>)
plt.colorbar(im)
plt.title(<span class="st">"Correlation Heatmap"</span>)
plt.tight_layout()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[5x5 heatmap with values displayed in each cell]</div></div></section>''',
("preprocessing.html","Preprocessing"),("seaborn.html","Seaborn"))

print("matplotlib.html expanded with 10+ examples!")
