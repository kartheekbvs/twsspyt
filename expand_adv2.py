import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CONTEXT MANAGERS
make_page("advanced/context-managers.html","Context Managers &amp; with Statement","Advanced Python","&#x2699;&#xFE0F;","intermediate","Advanced &rarr; Context Managers",
"Context managers automate resource management using the with statement. This section provides textbook precision on the protocol and return value behavior.",
"Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">The Protocol</a></li>
<li><a href="#s2">Return Value Analysis</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; The Protocol</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Context manager objects exist to control a <code>with</code> statement, just as iterators exist to control a <code>for</code> statement. The protocol consists of <code>__enter__</code> and <code>__exit__</code> methods." &mdash; <em>Luciano Ramalho</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value Analysis</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value: __enter__</div>
    <p>The value returned by <code>__enter__</code> is what is bound to the target variable in the <code>as</code> clause. It is frequently <code>self</code>, but it can be any object (or <code>None</code>). Note that the context manager <em>object</em> and the <em>return value</em> of <code>__enter__</code> are not necessarily the same.</p>
</div>
</section>''',
("generators.html","Generators"),("async.html","Async"),
[("generators.html", "Iteration Protocol"), ("async.html", "Concurrent Contexts")])

# ASYNC
make_page("advanced/async.html","Async/Await &amp; Concurrency","Advanced Python","&#x2699;&#xFE0F;","advanced","Advanced &rarr; Async",
"Asyncio enables non-blocking I/O in a single thread. This section provides a textbook deep dive into coroutines and event loops.",
"Python Documentation &mdash; asyncio",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Coroutines</a></li>
<li><a href="#s2">Return Value: async def</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Coroutines</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points." &mdash; <em>Python Docs</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: async def</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Calling an <code>async def</code> function <strong>does not execute it</strong>. It returns a <strong>coroutine object</strong>. To actually run the code, the coroutine must be scheduled on an event loop (e.g., via <code>await</code> or <code>asyncio.run()</code>).</p>
</div>
</section>''',
("context-managers.html","Context Managers"),("../oop/decorators.html","Decorators"),
[("context-managers.html", "Resource Safety"), ("generators.html", "Yield vs Await")])

print("context-managers.html + async.html expanded!")
