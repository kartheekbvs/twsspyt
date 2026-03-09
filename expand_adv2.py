import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CONTEXT MANAGERS
make_page("advanced/context-managers.html","Context Managers &amp; with Statement","Advanced Python","&#x2699;&#xFE0F;","intermediate","Advanced &rarr; Context Managers",
"Context managers use the with statement to automatically handle setup and cleanup. Essential for file handling, database connections, locks, and resource management. Covers with statement, __enter__/__exit__, contextlib.contextmanager, and practical patterns.",
"Python Docs, Fluent Python &mdash; Luciano Ramalho",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">The with Statement</a></li>
<li><a href="#s2">Custom Context Manager (Class)</a></li>
<li><a href="#s3">contextlib.contextmanager</a></li>
<li><a href="#s4">Practical Patterns</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; The with Statement</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Without with (manual cleanup &mdash; error prone!)</span>
f = <span class="bi">open</span>(<span class="st">"data.txt"</span>, <span class="st">"r"</span>)
<span class="kw">try</span>:
    content = f.read()
<span class="kw">finally</span>:
    f.close()  <span class="cm"># must always close!</span>

<span class="cm"># With with (automatic cleanup &mdash; guaranteed!)</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"data.txt"</span>, <span class="st">"r"</span>) <span class="kw">as</span> f:
    content = f.read()
<span class="cm"># f.close() called automatically, even if exception!</span>

<span class="cm"># Multiple context managers</span>
<span class="kw">with</span> <span class="bi">open</span>(<span class="st">"input.txt"</span>) <span class="kw">as</span> fin, <span class="bi">open</span>(<span class="st">"output.txt"</span>, <span class="st">"w"</span>) <span class="kw">as</span> fout:
    fout.write(fin.read().upper())

<span class="cm"># Common examples</span>
<span class="kw">import</span> threading
lock = threading.Lock()
<span class="kw">with</span> lock:
    <span class="cm"># thread-safe code</span>
    <span class="kw">pass</span>

<span class="kw">import</span> sqlite3
<span class="kw">with</span> sqlite3.connect(<span class="st">"db.sqlite"</span>) <span class="kw">as</span> conn:
    conn.execute(<span class="st">"CREATE TABLE IF NOT EXISTS users (name TEXT)"</span>)
    <span class="cm"># auto-commit or rollback</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>with ensures cleanup happens even if an exception occurs!</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Custom Context Manager (Class)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> time

<span class="kw">class</span> <span class="bi">Timer</span>:
    <span class="st">"""Context manager that times code execution."""</span>

    <span class="kw">def</span> <span class="bi">__enter__</span>(self):
        self.start = time.perf_counter()
        <span class="kw">return</span> self  <span class="cm"># returned as 'as' variable</span>

    <span class="kw">def</span> <span class="bi">__exit__</span>(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        <span class="bi">print</span>(<span class="st">f"Elapsed: {self.elapsed:.4f}s"</span>)
        <span class="kw">return</span> <span class="kw">False</span>  <span class="cm"># don't suppress exceptions</span>

<span class="cm"># Usage</span>
<span class="kw">with</span> Timer() <span class="kw">as</span> t:
    total = <span class="bi">sum</span>(i**<span class="nm">2</span> <span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="nm">1000000</span>))
<span class="bi">print</span>(<span class="st">f"Time stored: {t.elapsed:.4f}s"</span>)

<span class="cm"># Error handling context manager</span>
<span class="kw">class</span> <span class="bi">SuppressErrors</span>:
    <span class="kw">def</span> <span class="bi">__enter__</span>(self):
        <span class="kw">return</span> self
    <span class="kw">def</span> <span class="bi">__exit__</span>(self, exc_type, exc_val, exc_tb):
        <span class="kw">if</span> exc_type <span class="kw">is not None</span>:
            <span class="bi">print</span>(<span class="st">f"Suppressed: {exc_type.__name__}: {exc_val}"</span>)
            <span class="kw">return</span> <span class="kw">True</span>  <span class="cm"># suppress the exception!</span>

<span class="kw">with</span> SuppressErrors():
    x = <span class="nm">1</span> / <span class="nm">0</span>  <span class="cm"># ZeroDivisionError</span>
<span class="bi">print</span>(<span class="st">"Code continues!"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Elapsed: 0.1234s<br>Suppressed: ZeroDivisionError: division by zero<br>Code continues!</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; contextlib.contextmanager</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Generator-based (simpler!)</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> contextlib <span class="kw">import</span> contextmanager

@contextmanager
<span class="kw">def</span> <span class="bi">timer</span>(label):
    start = time.perf_counter()
    <span class="kw">try</span>:
        <span class="kw">yield</span>   <span class="cm"># code in 'with' block runs here</span>
    <span class="kw">finally</span>:
        elapsed = time.perf_counter() - start
        <span class="bi">print</span>(<span class="st">f"[{label}] {elapsed:.4f}s"</span>)

<span class="kw">with</span> timer(<span class="st">"sorting"</span>):
    <span class="bi">sorted</span>(<span class="bi">range</span>(<span class="nm">100000</span>), reverse=<span class="kw">True</span>)

<span class="cm"># Temporary directory change</span>
<span class="kw">import</span> os

@contextmanager
<span class="kw">def</span> <span class="bi">working_directory</span>(path):
    old = os.getcwd()
    os.chdir(path)
    <span class="kw">try</span>:
        <span class="kw">yield</span>
    <span class="kw">finally</span>:
        os.chdir(old)

<span class="kw">with</span> working_directory(<span class="st">"/tmp"</span>):
    <span class="bi">print</span>(os.getcwd())  <span class="cm"># /tmp</span>
<span class="bi">print</span>(os.getcwd())      <span class="cm"># back to original</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[sorting] 0.0123s<br>/tmp &rarr; back to original directory</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Practical Patterns</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> contextlib <span class="kw">import</span> suppress, redirect_stdout
<span class="kw">import</span> io

<span class="cm"># suppress: ignore specific exceptions</span>
<span class="kw">with</span> suppress(FileNotFoundError):
    os.remove(<span class="st">"nonexistent.txt"</span>)  <span class="cm"># no error!</span>

<span class="cm"># redirect_stdout: capture print output</span>
f = io.StringIO()
<span class="kw">with</span> redirect_stdout(f):
    <span class="bi">print</span>(<span class="st">"captured!"</span>)
output = f.getvalue()
<span class="bi">print</span>(<span class="st">f"Got: {output.strip()}"</span>)  <span class="cm"># "Got: captured!"</span>

<span class="cm"># Database transaction pattern</span>
@contextmanager
<span class="kw">def</span> <span class="bi">transaction</span>(conn):
    <span class="kw">try</span>:
        <span class="kw">yield</span> conn
        conn.commit()
    <span class="kw">except</span> <span class="bi">Exception</span>:
        conn.rollback()
        <span class="kw">raise</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>suppress, redirect_stdout, and transaction are built-in contextlib tools</div></div></section>''',
("generators.html","Generators"),("async.html","Async"))

# ASYNC
make_page("advanced/async.html","Async/Await &amp; Concurrency","Advanced Python","&#x2699;&#xFE0F;","advanced","Advanced &rarr; Async",
"Python&#39;s asyncio enables non-blocking concurrent code. Essential for I/O-bound tasks like web requests, file I/O, and database queries. Covers async/await, asyncio, event loop, aiohttp, tasks, gather, semaphores, and comparison with threading/multiprocessing.",
"Python Docs, asyncio Documentation",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Sync vs Async</a></li>
<li><a href="#s2">async/await Basics</a></li>
<li><a href="#s3">asyncio.gather &amp; Tasks</a></li>
<li><a href="#s4">Async HTTP with aiohttp</a></li>
<li><a href="#s5">Threading vs Multiprocessing vs Async</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Sync vs Async</h2>
<div class="callout note"><div class="callout-icon">&#x1F4D0;</div><div class="callout-content"><strong>Why Async?</strong>
<pre style="font-size:.85rem;line-height:1.6;">
Synchronous (blocking):
  fetch_url_1()  &mdash; waits 2 sec
  fetch_url_2()  &mdash; waits 2 sec
  fetch_url_3()  &mdash; waits 2 sec
  Total: 6 seconds &#x1F422;

Asynchronous (non-blocking):
  fetch_url_1()  &brvbar;
  fetch_url_2()  &brvbar; all run concurrently
  fetch_url_3()  &brvbar;
  Total: ~2 seconds &#x26A1;</pre></div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; async/await Basics</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> asyncio

<span class="cm"># async function (coroutine)</span>
<span class="kw">async def</span> <span class="bi">greet</span>(name, delay):
    <span class="bi">print</span>(<span class="st">f"Hello, {name}!"</span>)
    <span class="kw">await</span> asyncio.sleep(delay)  <span class="cm"># non-blocking sleep</span>
    <span class="bi">print</span>(<span class="st">f"Goodbye, {name}! (after {delay}s)"</span>)
    <span class="kw">return</span> <span class="st">f"{name} done"</span>

<span class="cm"># Run a single coroutine</span>
<span class="kw">async def</span> <span class="bi">main</span>():
    result = <span class="kw">await</span> greet(<span class="st">"Alice"</span>, <span class="nm">1</span>)
    <span class="bi">print</span>(result)

asyncio.run(main())

<span class="cm"># Run multiple concurrently</span>
<span class="kw">async def</span> <span class="bi">main_concurrent</span>():
    <span class="cm"># These run at the SAME TIME!</span>
    results = <span class="kw">await</span> asyncio.gather(
        greet(<span class="st">"Alice"</span>, <span class="nm">2</span>),
        greet(<span class="st">"Bob"</span>, <span class="nm">1</span>),
        greet(<span class="st">"Charlie"</span>, <span class="nm">3</span>)
    )
    <span class="bi">print</span>(results)  <span class="cm"># all 3 results</span>

asyncio.run(main_concurrent())
<span class="cm"># Total time: ~3 seconds (not 6!)</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Hello, Alice! Hello, Bob! Hello, Charlie!<br>Goodbye, Bob! (1s) &rarr; Goodbye, Alice! (2s) &rarr; Goodbye, Charlie! (3s)<br>Total: ~3 seconds instead of 6!</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; asyncio.gather &amp; Tasks</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> asyncio, time

<span class="kw">async def</span> <span class="bi">download_file</span>(name, size):
    <span class="bi">print</span>(<span class="st">f"Downloading {name} ({size}MB)..."</span>)
    <span class="kw">await</span> asyncio.sleep(size / <span class="nm">10</span>)  <span class="cm"># simulate download time</span>
    <span class="bi">print</span>(<span class="st">f"  &check; {name} complete!"</span>)
    <span class="kw">return</span> {<span class="st">"file"</span>: name, <span class="st">"size"</span>: size}

<span class="kw">async def</span> <span class="bi">main</span>():
    start = time.time()

    <span class="cm"># Method 1: gather (wait for all)</span>
    results = <span class="kw">await</span> asyncio.gather(
        download_file(<span class="st">"video.mp4"</span>, <span class="nm">50</span>),
        download_file(<span class="st">"image.png"</span>, <span class="nm">5</span>),
        download_file(<span class="st">"data.csv"</span>, <span class="nm">20</span>)
    )
    <span class="bi">print</span>(<span class="st">f"All done in {time.time()-start:.1f}s"</span>)
    <span class="bi">print</span>(results)

    <span class="cm"># Method 2: create_task (fire and forget)</span>
    task1 = asyncio.create_task(download_file(<span class="st">"report.pdf"</span>, <span class="nm">10</span>))
    task2 = asyncio.create_task(download_file(<span class="st">"log.txt"</span>, <span class="nm">2</span>))
    <span class="kw">await</span> task1
    <span class="kw">await</span> task2

asyncio.run(main())</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Downloading video.mp4 (50MB)...<br>Downloading image.png (5MB)...<br>Downloading data.csv (20MB)...<br>  &check; image.png complete! (0.5s)<br>  &check; data.csv complete! (2.0s)<br>  &check; video.mp4 complete! (5.0s)<br>All done in 5.0s (not 7.5s!)</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Async HTTP with aiohttp</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> aiohttp
<span class="kw">import</span> asyncio

<span class="kw">async def</span> <span class="bi">fetch_url</span>(session, url):
    <span class="kw">async with</span> session.get(url) <span class="kw">as</span> response:
        data = <span class="kw">await</span> response.text()
        <span class="kw">return</span> {<span class="st">"url"</span>: url, <span class="st">"status"</span>: response.status, <span class="st">"length"</span>: <span class="bi">len</span>(data)}

<span class="kw">async def</span> <span class="bi">main</span>():
    urls = [
        <span class="st">"https://httpbin.org/get"</span>,
        <span class="st">"https://httpbin.org/ip"</span>,
        <span class="st">"https://httpbin.org/user-agent"</span>,
    ]

    <span class="kw">async with</span> aiohttp.ClientSession() <span class="kw">as</span> session:
        tasks = [fetch_url(session, url) <span class="kw">for</span> url <span class="kw">in</span> urls]
        results = <span class="kw">await</span> asyncio.gather(*tasks)

    <span class="kw">for</span> r <span class="kw">in</span> results:
        <span class="bi">print</span>(<span class="st">f"  {r['url']}: status={r['status']}, len={r['length']}"</span>)

asyncio.run(main())

<span class="cm"># With semaphore (limit concurrent requests)</span>
sem = asyncio.Semaphore(<span class="nm">5</span>)  <span class="cm"># max 5 concurrent</span>

<span class="kw">async def</span> <span class="bi">limited_fetch</span>(session, url):
    <span class="kw">async with</span> sem:
        <span class="kw">return</span> <span class="kw">await</span> fetch_url(session, url)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>All 3 URLs fetched concurrently!<br>httpbin.org/get: status=200, len=345<br>httpbin.org/ip: status=200, len=32</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Threading vs Multiprocessing vs Async</h2>
<table class="data-table"><thead><tr><th>Feature</th><th>threading</th><th>multiprocessing</th><th>asyncio</th></tr></thead><tbody>
<tr><td>Concurrency Type</td><td>Threads (GIL limited)</td><td>Separate processes</td><td>Coroutines (single thread)</td></tr>
<tr><td>Best For</td><td>I/O-bound (simple)</td><td>CPU-bound (parallel)</td><td>I/O-bound (scalable)</td></tr>
<tr><td>Overhead</td><td>Medium (OS threads)</td><td>High (process creation)</td><td>Low (lightweight)</td></tr>
<tr><td>GIL</td><td>Shared (limited parallelism)</td><td>No GIL per process</td><td>Single thread (no issue)</td></tr>
<tr><td>Data Sharing</td><td>Shared memory (need locks)</td><td>IPC (pipes, queues)</td><td>Shared memory (single thread)</td></tr>
<tr><td>Use Case</td><td>File I/O, simple HTTP</td><td>Data processing, ML training</td><td>Web servers, many connections</td></tr>
</tbody></table>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; Quick Threading Example</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> concurrent.futures <span class="kw">import</span> ThreadPoolExecutor, ProcessPoolExecutor
<span class="kw">import</span> time

<span class="kw">def</span> <span class="bi">heavy_task</span>(n):
    time.sleep(<span class="nm">1</span>)
    <span class="kw">return</span> n ** <span class="nm">2</span>

<span class="cm"># ThreadPoolExecutor (I/O-bound)</span>
<span class="kw">with</span> ThreadPoolExecutor(max_workers=<span class="nm">4</span>) <span class="kw">as</span> executor:
    results = <span class="bi">list</span>(executor.map(heavy_task, <span class="bi">range</span>(<span class="nm">4</span>)))
<span class="bi">print</span>(results)  <span class="cm"># [0, 1, 4, 9] in ~1s (not 4s)</span>

<span class="cm"># ProcessPoolExecutor (CPU-bound)</span>
<span class="kw">with</span> ProcessPoolExecutor(max_workers=<span class="nm">4</span>) <span class="kw">as</span> executor:
    results = <span class="bi">list</span>(executor.map(heavy_task, <span class="bi">range</span>(<span class="nm">4</span>)))
<span class="bi">print</span>(results)  <span class="cm"># [0, 1, 4, 9] truly parallel</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[0, 1, 4, 9] in ~1 second (4x speedup)</div></div></section>''',
("context-managers.html","Context Managers"),("../oop/decorators.html","Decorators"))

print("context-managers.html + async.html expanded!")
