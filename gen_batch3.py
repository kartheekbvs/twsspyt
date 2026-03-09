
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# OOP pages
make_page("oop/inheritance.html","Inheritance","OOP","&#x1F3D7;&#xFE0F;","intermediate","OOP &rarr; Inheritance",
"Inheritance lets a child class inherit attributes and methods from a parent class. Python supports single, multiple, and multilevel inheritance with MRO (Method Resolution Order) using C3 linearization.",
"Python Programming (2024), Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Basic Inheritance</a></li><li><a href="#s2">Method Overriding &amp; super()</a></li><li><a href="#s3">Multiple Inheritance</a></li><li><a href="#s4">MRO (Method Resolution Order)</a></li><li><a href="#s5">Abstract Base Classes</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Basic Inheritance</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Animal</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, name, species):
        self.name = name
        self.species = species

    <span class="kw">def</span> <span class="fn">speak</span>(self):
        <span class="kw">return</span> <span class="st">f"{self.name} makes a sound"</span>

<span class="kw">class</span> <span class="cl">Dog</span>(Animal):   <span class="cm"># Dog inherits from Animal</span>
    <span class="kw">def</span> <span class="fn">__init__</span>(self, name, breed):
        <span class="bi">super</span>().__init__(name, <span class="st">"Canine"</span>)  <span class="cm"># call parent __init__</span>
        self.breed = breed

    <span class="kw">def</span> <span class="fn">speak</span>(self):         <span class="cm"># override parent method</span>
        <span class="kw">return</span> <span class="st">f"{self.name} says Woof!"</span>

dog = Dog(<span class="st">"Rex"</span>, <span class="st">"Labrador"</span>)
<span class="bi">print</span>(dog.speak())          <span class="cm"># Rex says Woof!</span>
<span class="bi">print</span>(dog.species)          <span class="cm"># Canine (inherited)</span>
<span class="bi">print</span>(<span class="bi">isinstance</span>(dog, Animal))  <span class="cm"># True</span>
<span class="bi">print</span>(<span class="bi">isinstance</span>(dog, Dog))     <span class="cm"># True</span>
<span class="bi">print</span>(<span class="bi">issubclass</span>(Dog, Animal))  <span class="cm"># True</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Rex says Woof!<br>Canine<br>True<br>True<br>True</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Method Overriding &amp; super()</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Shape</span>:
    <span class="kw">def</span> <span class="fn">area</span>(self):
        <span class="kw">raise</span> <span class="cl">NotImplementedError</span>

    <span class="kw">def</span> <span class="fn">describe</span>(self):
        <span class="kw">return</span> <span class="st">f"Area = {self.area():.2f}"</span>

<span class="kw">class</span> <span class="cl">Circle</span>(Shape):
    <span class="kw">def</span> <span class="fn">__init__</span>(self, radius):
        self.radius = radius

    <span class="kw">def</span> <span class="fn">area</span>(self):   <span class="cm"># override</span>
        <span class="kw">return</span> <span class="nm">3.14159</span> * self.radius ** <span class="nm">2</span>

<span class="kw">class</span> <span class="cl">Rectangle</span>(Shape):
    <span class="kw">def</span> <span class="fn">__init__</span>(self, w, h):
        self.w, self.h = w, h

    <span class="kw">def</span> <span class="fn">area</span>(self):
        <span class="kw">return</span> self.w * self.h

c = Circle(<span class="nm">5</span>)
r = Rectangle(<span class="nm">4</span>, <span class="nm">6</span>)
<span class="bi">print</span>(c.describe())  <span class="cm"># Area = 78.54</span>
<span class="bi">print</span>(r.describe())  <span class="cm"># Area = 24.00</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Area = 78.54<br>Area = 24.00</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Multiple Inheritance</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Flyable</span>:
    <span class="kw">def</span> <span class="fn">fly</span>(self): <span class="kw">return</span> <span class="st">"Flying!"</span>

<span class="kw">class</span> <span class="cl">Swimmable</span>:
    <span class="kw">def</span> <span class="fn">swim</span>(self): <span class="kw">return</span> <span class="st">"Swimming!"</span>

<span class="kw">class</span> <span class="cl">Duck</span>(Flyable, Swimmable):  <span class="cm"># multiple inheritance</span>
    <span class="kw">pass</span>

d = Duck()
<span class="bi">print</span>(d.fly())    <span class="cm"># Flying!</span>
<span class="bi">print</span>(d.swim())   <span class="cm"># Swimming!</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Flying!<br>Swimming!</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; MRO (C3 Linearization)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Diamond problem</span>
<span class="kw">class</span> <span class="cl">A</span>:
    <span class="kw">def</span> <span class="fn">method</span>(self): <span class="kw">return</span> <span class="st">"A"</span>
<span class="kw">class</span> <span class="cl">B</span>(A):
    <span class="kw">def</span> <span class="fn">method</span>(self): <span class="kw">return</span> <span class="st">"B"</span>
<span class="kw">class</span> <span class="cl">C</span>(A):
    <span class="kw">def</span> <span class="fn">method</span>(self): <span class="kw">return</span> <span class="st">"C"</span>
<span class="kw">class</span> <span class="cl">D</span>(B, C): <span class="kw">pass</span>

<span class="bi">print</span>(D().method())   <span class="cm"># B (follows MRO)</span>
<span class="bi">print</span>(D.__mro__)      <span class="cm"># (D, B, C, A, object)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>B<br>(D, B, C, A, object)</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Abstract Base Classes</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> abc <span class="kw">import</span> ABC, abstractmethod

<span class="kw">class</span> <span class="cl">Vehicle</span>(ABC):
    @abstractmethod
    <span class="kw">def</span> <span class="fn">start</span>(self): ...

    @abstractmethod
    <span class="kw">def</span> <span class="fn">stop</span>(self): ...

<span class="kw">class</span> <span class="cl">Car</span>(Vehicle):
    <span class="kw">def</span> <span class="fn">start</span>(self): <span class="kw">return</span> <span class="st">"Engine on"</span>
    <span class="kw">def</span> <span class="fn">stop</span>(self): <span class="kw">return</span> <span class="st">"Engine off"</span>

<span class="cm"># Vehicle()  # TypeError: Can't instantiate abstract class</span>
car = Car()
<span class="bi">print</span>(car.start())  <span class="cm"># Engine on</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Engine on</div></div></section>''',
("classes-objects.html","Classes &amp; Objects"),("polymorphism.html","Polymorphism"))

make_page("oop/polymorphism.html","Polymorphism","OOP","&#x1F3D7;&#xFE0F;","intermediate","OOP &rarr; Polymorphism",
"Polymorphism means 'many forms'. In Python, it allows different classes to be used with the same interface. Python uses duck typing: 'if it quacks like a duck, it's a duck'. This covers method overriding, operator overloading, and duck typing.",
"Python Programming (2024), Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Duck Typing</a></li><li><a href="#s2">Method Overriding</a></li><li><a href="#s3">Operator Overloading</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Duck Typing</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Dog</span>:
    <span class="kw">def</span> <span class="fn">speak</span>(self): <span class="kw">return</span> <span class="st">"Woof!"</span>
<span class="kw">class</span> <span class="cl">Cat</span>:
    <span class="kw">def</span> <span class="fn">speak</span>(self): <span class="kw">return</span> <span class="st">"Meow!"</span>
<span class="kw">class</span> <span class="cl">Duck</span>:
    <span class="kw">def</span> <span class="fn">speak</span>(self): <span class="kw">return</span> <span class="st">"Quack!"</span>

<span class="cm"># Polymorphic function &mdash; works with ANY object that has .speak()</span>
<span class="kw">def</span> <span class="fn">animal_sound</span>(animal):
    <span class="bi">print</span>(animal.speak())

<span class="kw">for</span> a <span class="kw">in</span> [Dog(), Cat(), Duck()]:
    animal_sound(a)
<span class="cm"># Woof! Meow! Quack!</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Woof!<br>Meow!<br>Quack!</div></div>
<div class="callout note"><div class="callout-icon">&#x1F4A1;</div><div class="callout-content"><strong>Duck Typing</strong><p>"Don't check whether it IS-a duck: check whether it QUACKS-like-a duck." Python doesn't require inheritance for polymorphism &mdash; any object with the right methods works.</p></div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Method Overriding</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Shape</span>:
    <span class="kw">def</span> <span class="fn">area</span>(self): <span class="kw">return</span> <span class="nm">0</span>
    <span class="kw">def</span> <span class="fn">__str__</span>(self): <span class="kw">return</span> <span class="st">f"{self.__class__.__name__}: area={self.area():.2f}"</span>

<span class="kw">class</span> <span class="cl">Circle</span>(Shape):
    <span class="kw">def</span> <span class="fn">__init__</span>(self, r): self.r = r
    <span class="kw">def</span> <span class="fn">area</span>(self): <span class="kw">return</span> <span class="nm">3.14159</span> * self.r**<span class="nm">2</span>

<span class="kw">class</span> <span class="cl">Square</span>(Shape):
    <span class="kw">def</span> <span class="fn">__init__</span>(self, s): self.s = s
    <span class="kw">def</span> <span class="fn">area</span>(self): <span class="kw">return</span> self.s**<span class="nm">2</span>

shapes = [Circle(<span class="nm">5</span>), Square(<span class="nm">4</span>)]
<span class="kw">for</span> s <span class="kw">in</span> shapes:
    <span class="bi">print</span>(s)   <span class="cm"># uses overridden area() + inherited __str__</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Circle: area=78.54<br>Square: area=16.00</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Operator Overloading</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Vector</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, x, y):
        self.x, self.y = x, y
    <span class="kw">def</span> <span class="fn">__add__</span>(self, other):        <span class="cm"># + operator</span>
        <span class="kw">return</span> Vector(self.x+other.x, self.y+other.y)
    <span class="kw">def</span> <span class="fn">__mul__</span>(self, scalar):       <span class="cm"># * operator</span>
        <span class="kw">return</span> Vector(self.x*scalar, self.y*scalar)
    <span class="kw">def</span> <span class="fn">__repr__</span>(self):
        <span class="kw">return</span> <span class="st">f"Vector({self.x}, {self.y})"</span>

v1 = Vector(<span class="nm">1</span>, <span class="nm">2</span>)
v2 = Vector(<span class="nm">3</span>, <span class="nm">4</span>)
<span class="bi">print</span>(v1 + v2)    <span class="cm"># Vector(4, 6)</span>
<span class="bi">print</span>(v1 * <span class="nm">3</span>)     <span class="cm"># Vector(3, 6)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Vector(4, 6)<br>Vector(3, 6)</div></div></section>''',
("inheritance.html","Inheritance"),("encapsulation.html","Encapsulation"))

make_page("oop/encapsulation.html","Encapsulation","OOP","&#x1F3D7;&#xFE0F;","intermediate","OOP &rarr; Encapsulation",
"Encapsulation bundles data and methods that operate on that data within a class, and restricts direct access. Python uses naming conventions: _protected, __private (name mangling), and @property decorators for controlled access.",
"Python Programming (2024), Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Access Levels</a></li><li><a href="#s2">@property Decorator</a></li><li><a href="#s3">Name Mangling</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Access Levels</h2>
<table class="data-table"><thead><tr><th>Convention</th><th>Meaning</th><th>Accessible?</th></tr></thead><tbody>
<tr><td><code>name</code></td><td>Public</td><td>Everywhere</td></tr>
<tr><td><code>_name</code></td><td>Protected (by convention)</td><td>Yes, but "don't touch"</td></tr>
<tr><td><code>__name</code></td><td>Private (name mangling)</td><td>Only via <code>_Class__name</code></td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">BankAccount</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, owner, balance):
        self.owner = owner        <span class="cm"># public</span>
        self._bank = <span class="st">"MyBank"</span>     <span class="cm"># protected</span>
        self.__balance = balance   <span class="cm"># private</span>

    <span class="kw">def</span> <span class="fn">get_balance</span>(self):
        <span class="kw">return</span> self.__balance

acc = BankAccount(<span class="st">"Alice"</span>, <span class="nm">1000</span>)
<span class="bi">print</span>(acc.owner)          <span class="cm"># Alice</span>
<span class="bi">print</span>(acc._bank)          <span class="cm"># MyBank (works, but discouraged)</span>
<span class="cm"># print(acc.__balance)    # AttributeError!</span>
<span class="bi">print</span>(acc.get_balance())  <span class="cm"># 1000</span>
<span class="bi">print</span>(acc._BankAccount__balance)  <span class="cm"># 1000 (name mangling)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Alice<br>MyBank<br>1000<br>1000</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; @property Decorator</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Temperature</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, celsius):
        self._celsius = celsius

    @property
    <span class="kw">def</span> <span class="fn">celsius</span>(self):        <span class="cm"># getter</span>
        <span class="kw">return</span> self._celsius

    @celsius.setter
    <span class="kw">def</span> <span class="fn">celsius</span>(self, value):  <span class="cm"># setter with validation</span>
        <span class="kw">if</span> value &lt; -<span class="nm">273.15</span>:
            <span class="kw">raise</span> <span class="cl">ValueError</span>(<span class="st">"Below absolute zero!"</span>)
        self._celsius = value

    @property
    <span class="kw">def</span> <span class="fn">fahrenheit</span>(self):     <span class="cm"># computed property</span>
        <span class="kw">return</span> self._celsius * <span class="nm">9</span>/<span class="nm">5</span> + <span class="nm">32</span>

t = Temperature(<span class="nm">100</span>)
<span class="bi">print</span>(t.celsius)      <span class="cm"># 100 (calls getter)</span>
<span class="bi">print</span>(t.fahrenheit)   <span class="cm"># 212.0</span>
t.celsius = <span class="nm">0</span>         <span class="cm"># calls setter</span>
<span class="bi">print</span>(t.fahrenheit)   <span class="cm"># 32.0</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>100<br>212.0<br>32.0</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Name Mangling (__dunder)</h2>
<p>Python transforms <code>__attr</code> to <code>_ClassName__attr</code> to prevent accidental override in subclasses. This is <em>not</em> true security &mdash; just a safety mechanism.</p>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Parent</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self):
        self.__secret = <span class="st">"parent_secret"</span>

<span class="kw">class</span> <span class="cl">Child</span>(Parent):
    <span class="kw">def</span> <span class="fn">__init__</span>(self):
        <span class="bi">super</span>().__init__()
        self.__secret = <span class="st">"child_secret"</span>  <span class="cm"># different attribute!</span>

c = Child()
<span class="bi">print</span>(c._Parent__secret)  <span class="cm"># parent_secret</span>
<span class="bi">print</span>(c._Child__secret)   <span class="cm"># child_secret</span>
<span class="cm"># Both coexist! Name mangling prevents collision.</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>parent_secret<br>child_secret</div></div></section>''',
("polymorphism.html","Polymorphism"),("magic-methods.html","Magic Methods"))

make_page("oop/magic-methods.html","Magic Methods","OOP","&#x1F3D7;&#xFE0F;","intermediate","OOP &rarr; Magic Methods",
"Magic (dunder) methods let you define how objects behave with built-in Python operations: printing, comparison, arithmetic, iteration, context management, and more. They make your classes feel 'Pythonic'.",
"Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Overview Table</a></li><li><a href="#s2">String Representation</a></li><li><a href="#s3">Comparison &amp; Arithmetic</a></li><li><a href="#s4">Container Protocol</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Overview of Common Magic Methods</h2>
<table class="data-table"><thead><tr><th>Method</th><th>Triggered By</th><th>Example</th></tr></thead><tbody>
<tr><td><code>__init__</code></td><td>Constructor</td><td><code>obj = MyClass()</code></td></tr>
<tr><td><code>__str__</code></td><td><code>str(obj)</code>, <code>print(obj)</code></td><td>Human-readable</td></tr>
<tr><td><code>__repr__</code></td><td><code>repr(obj)</code>, REPL</td><td>Developer repr</td></tr>
<tr><td><code>__len__</code></td><td><code>len(obj)</code></td><td>Length</td></tr>
<tr><td><code>__getitem__</code></td><td><code>obj[key]</code></td><td>Indexing</td></tr>
<tr><td><code>__setitem__</code></td><td><code>obj[key] = val</code></td><td>Assignment</td></tr>
<tr><td><code>__contains__</code></td><td><code>x in obj</code></td><td>Membership</td></tr>
<tr><td><code>__iter__</code></td><td><code>for x in obj</code></td><td>Iteration</td></tr>
<tr><td><code>__eq__</code></td><td><code>obj == other</code></td><td>Equality</td></tr>
<tr><td><code>__lt__</code></td><td><code>obj &lt; other</code></td><td>Less than</td></tr>
<tr><td><code>__add__</code></td><td><code>obj + other</code></td><td>Addition</td></tr>
<tr><td><code>__enter__/__exit__</code></td><td><code>with obj:</code></td><td>Context manager</td></tr>
<tr><td><code>__call__</code></td><td><code>obj()</code></td><td>Callable</td></tr>
<tr><td><code>__hash__</code></td><td><code>hash(obj)</code></td><td>Dict key</td></tr>
</tbody></table></section>

<section class="content-section" id="s2"><h2>2 &middot; __str__ vs __repr__</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Point</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, x, y):
        self.x, self.y = x, y
    <span class="kw">def</span> <span class="fn">__repr__</span>(self):   <span class="cm"># for developers</span>
        <span class="kw">return</span> <span class="st">f"Point({self.x}, {self.y})"</span>
    <span class="kw">def</span> <span class="fn">__str__</span>(self):    <span class="cm"># for users</span>
        <span class="kw">return</span> <span class="st">f"({self.x}, {self.y})"</span>

p = Point(<span class="nm">3</span>, <span class="nm">4</span>)
<span class="bi">print</span>(p)         <span class="cm"># (3, 4)  calls __str__</span>
<span class="bi">print</span>(<span class="bi">repr</span>(p))   <span class="cm"># Point(3, 4)  calls __repr__</span>
<span class="bi">print</span>([p])       <span class="cm"># [Point(3, 4)]  containers use __repr__</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>(3, 4)<br>Point(3, 4)<br>[Point(3, 4)]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Comparison &amp; Arithmetic</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> functools <span class="kw">import</span> total_ordering

@total_ordering  <span class="cm"># auto-generates &lt;=, &gt;, &gt;= from __eq__ + __lt__</span>
<span class="kw">class</span> <span class="cl">Money</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, amount):
        self.amount = amount
    <span class="kw">def</span> <span class="fn">__eq__</span>(self, other): <span class="kw">return</span> self.amount == other.amount
    <span class="kw">def</span> <span class="fn">__lt__</span>(self, other): <span class="kw">return</span> self.amount &lt; other.amount
    <span class="kw">def</span> <span class="fn">__add__</span>(self, other): <span class="kw">return</span> Money(self.amount + other.amount)
    <span class="kw">def</span> <span class="fn">__repr__</span>(self): <span class="kw">return</span> <span class="st">f"${self.amount}"</span>

a, b = Money(<span class="nm">10</span>), Money(<span class="nm">20</span>)
<span class="bi">print</span>(a &lt; b)     <span class="cm"># True</span>
<span class="bi">print</span>(a + b)     <span class="cm"># $30</span>
<span class="bi">print</span>(<span class="bi">sorted</span>([Money(<span class="nm">30</span>), Money(<span class="nm">10</span>), Money(<span class="nm">20</span>)]))  <span class="cm"># [$10, $20, $30]</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>True<br>$30<br>[$10, $20, $30]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Container Protocol (__getitem__, __len__)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Playlist</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, songs):
        self._songs = <span class="bi">list</span>(songs)
    <span class="kw">def</span> <span class="fn">__len__</span>(self): <span class="kw">return</span> <span class="bi">len</span>(self._songs)
    <span class="kw">def</span> <span class="fn">__getitem__</span>(self, idx): <span class="kw">return</span> self._songs[idx]
    <span class="kw">def</span> <span class="fn">__contains__</span>(self, song): <span class="kw">return</span> song <span class="kw">in</span> self._songs

pl = Playlist([<span class="st">"Song A"</span>, <span class="st">"Song B"</span>, <span class="st">"Song C"</span>])
<span class="bi">print</span>(<span class="bi">len</span>(pl))          <span class="cm"># 3</span>
<span class="bi">print</span>(pl[<span class="nm">0</span>])            <span class="cm"># Song A</span>
<span class="bi">print</span>(pl[-<span class="nm">1</span>])           <span class="cm"># Song C</span>
<span class="bi">print</span>(<span class="st">"Song B"</span> <span class="kw">in</span> pl)  <span class="cm"># True</span>
<span class="kw">for</span> s <span class="kw">in</span> pl: <span class="bi">print</span>(s, end=<span class="st">" | "</span>)
<span class="cm"># Song A | Song B | Song C |</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>3<br>Song A<br>Song C<br>True<br>Song A | Song B | Song C |</div></div></section>''',
("encapsulation.html","Encapsulation"),("decorators.html","Decorators"))

make_page("oop/decorators.html","Decorators","OOP","&#x1F3D7;&#xFE0F;","intermediate","OOP &rarr; Decorators",
"Decorators are functions that modify the behavior of other functions or classes. They use the @decorator syntax and are built on closures. Common uses: logging, timing, access control, caching, and class method types (@staticmethod, @classmethod).",
"Python Programming (2024), Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol><li><a href="#s1">Basic Decorators</a></li><li><a href="#s2">Decorators with Arguments</a></li><li><a href="#s3">@classmethod &amp; @staticmethod</a></li><li><a href="#s4">Built-in Decorators</a></li></ol></div>
<section class="content-section" id="s1"><h2>1 &middot; Basic Decorators</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> time
<span class="kw">from</span> functools <span class="kw">import</span> wraps

<span class="kw">def</span> <span class="fn">timer</span>(func):
    @wraps(func)  <span class="cm"># preserves func name/docstring</span>
    <span class="kw">def</span> <span class="fn">wrapper</span>(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        <span class="bi">print</span>(<span class="st">f"{func.__name__} took {elapsed:.4f}s"</span>)
        <span class="kw">return</span> result
    <span class="kw">return</span> wrapper

@timer
<span class="kw">def</span> <span class="fn">slow_function</span>():
    time.sleep(<span class="nm">0.5</span>)
    <span class="kw">return</span> <span class="st">"Done"</span>

result = slow_function()
<span class="cm"># slow_function took 0.5001s</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>slow_function took 0.5001s</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Decorators with Arguments</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">def</span> <span class="fn">repeat</span>(n):
    <span class="kw">def</span> <span class="fn">decorator</span>(func):
        @wraps(func)
        <span class="kw">def</span> <span class="fn">wrapper</span>(*args, **kwargs):
            <span class="kw">for</span> _ <span class="kw">in</span> <span class="bi">range</span>(n):
                result = func(*args, **kwargs)
            <span class="kw">return</span> result
        <span class="kw">return</span> wrapper
    <span class="kw">return</span> decorator

@repeat(<span class="nm">3</span>)
<span class="kw">def</span> <span class="fn">greet</span>(name):
    <span class="bi">print</span>(<span class="st">f"Hello {name}!"</span>)

greet(<span class="st">"Alice"</span>)
<span class="cm"># Hello Alice! (printed 3 times)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Hello Alice!<br>Hello Alice!<br>Hello Alice!</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; @classmethod &amp; @staticmethod</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">class</span> <span class="cl">Date</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod   <span class="cm"># receives class, not instance</span>
    <span class="kw">def</span> <span class="fn">from_string</span>(cls, date_str):
        y, m, d = date_str.split(<span class="st">"-"</span>)
        <span class="kw">return</span> cls(<span class="bi">int</span>(y), <span class="bi">int</span>(m), <span class="bi">int</span>(d))

    @staticmethod  <span class="cm"># no self or cls</span>
    <span class="kw">def</span> <span class="fn">is_valid</span>(date_str):
        parts = date_str.split(<span class="st">"-"</span>)
        <span class="kw">return</span> <span class="bi">len</span>(parts) == <span class="nm">3</span>

    <span class="kw">def</span> <span class="fn">__repr__</span>(self):
        <span class="kw">return</span> <span class="st">f"{self.year}-{self.month:02d}-{self.day:02d}"</span>

d = Date.from_string(<span class="st">"2024-06-15"</span>)
<span class="bi">print</span>(d)                           <span class="cm"># 2024-06-15</span>
<span class="bi">print</span>(Date.is_valid(<span class="st">"2024-06-15"</span>)) <span class="cm"># True</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>2024-06-15<br>True</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Built-in Decorators</h2>
<table class="data-table"><thead><tr><th>Decorator</th><th>Purpose</th></tr></thead><tbody>
<tr><td><code>@property</code></td><td>Getter method as attribute</td></tr>
<tr><td><code>@staticmethod</code></td><td>No self/cls parameter</td></tr>
<tr><td><code>@classmethod</code></td><td>Class method (cls param)</td></tr>
<tr><td><code>@functools.wraps</code></td><td>Preserve decorated function metadata</td></tr>
<tr><td><code>@functools.lru_cache</code></td><td>Memoization cache</td></tr>
<tr><td><code>@functools.total_ordering</code></td><td>Auto-generate comparison methods</td></tr>
<tr><td><code>@dataclasses.dataclass</code></td><td>Auto-generate __init__, __repr__, etc.</td></tr>
<tr><td><code>@abc.abstractmethod</code></td><td>Enforce method implementation</td></tr>
</tbody></table></section>''',
("magic-methods.html","Magic Methods"),("../advanced/generators.html","Generators"))

print("Batch 3: OOP pages done (inheritance, polymorphism, encapsulation, magic-methods, decorators).")
