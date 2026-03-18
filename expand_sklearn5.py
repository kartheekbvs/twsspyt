import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# DIMENSIONALITY REDUCTION
make_page("ml/dimensionality-reduction.html","Dimensionality Reduction (PCA)","Machine Learning","&#x1F916;","intermediate","ML &rarr; PCA",
"Dimensionality reduction simplifies data while retaining essential variance. This section provides textbook precision on PCA and explained variance.",
"Hands-On Machine Learning &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">PCA and Singular Values</a></li>
<li><a href="#s2">Return Value: explained_variance_</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; PCA and Singular Values</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"Principal Component Analysis (PCA) identifies the hyperplane that lies closest to the data, and then it projects the data onto it. This preserves the maximum amount of variance." &mdash; <em>Aur&eacute;lien G&eacute;ron</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: explained_variance_</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>The <code>.explained_variance_ratio_</code> attribute returns a <strong>1D NumPy Array</strong> where each element is the proportion of the dataset's variance that lies along each principal component.</p>
</div>
</section>''',
("clustering.html","Clustering"),("model-evaluation.html","Model Evaluation"),
[("clustering.html", "Visualizing Clusters"), ("model-evaluation.html", "Performance Impact")])

print("dimensionality-reduction.html expanded!")
