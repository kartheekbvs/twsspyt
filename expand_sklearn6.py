import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# PIPELINES
make_page("ml/pipelines.html","Machine Learning Pipelines","Machine Learning","&#x1F916;","advanced","ML &rarr; Pipelines",
"Pipelines automate the workflow from preprocessing to prediction. This section provides textbook precision on preventing data leakage.",
"Scikit-Learn Documentation &mdash; Pipeline API",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Encapsulated Workflow</a></li>
<li><a href="#s2">Return Value: fit_transform()</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Encapsulated Workflow</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"The purpose of the pipeline is to assemble several steps that can be cross-validated together while setting different parameters. It ensures that transformer fitting happens only on training data." &mdash; <em>Sklearn Docs</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: fit_transform()</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>Calling <code>.fit_transform()</code> on a Pipeline returns a <strong>NumPy Array</strong> (or sparse matrix) that has been processed by every transformer in the chain. The last estimator in the pipeline must be a transformer for this to work.</p>
</div>
</section>''',
("dimensionality-reduction.html","PCA"),("model-evaluation.html","Evaluation"),
[("preprocessing.html", "Preprocessing Steps"), ("model-evaluation.html", "Cross-Validation")])

print("pipelines.html expanded!")
