import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# CLUSTERING
make_page("ml/clustering.html","Clustering (K-Means &amp; DBSCAN)","Machine Learning","&#x1F916;","intermediate","ML &rarr; Clustering",
"Clustering is the primary unsupervised learning task. This section provides textbook precision on inertia, centroids, and density-based clustering.",
"Hands-On Machine Learning &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">K-Means Logic</a></li>
<li><a href="#s2">Return Value: .labels_</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; K-Means Logic</h2>
<div class="callout note">
    <div class="callout-icon">📖</div>
    <div class="callout-content">
        <strong>Textbook Definition</strong>
        <p>"K-Means is a simple algorithm capable of clustering this kind of dataset very quickly and efficiently, often in just a few iterations. It searches for a fixed number of clusters by minimizing <em>inertia</em> (within-cluster sum-of-squares)." &mdash; <em>Aur&eacute;lien G&eacute;ron</em></p>
    </div>
</div>
</section>

<section class="content-section" id="s2"><h2>2 &middot; Return Value: .labels_</h2>
<div class="return-value-box">
    <div class="rv-label">🔁 Return Value</div>
    <p>After calling <code>.fit()</code>, the <code>.labels_</code> attribute contains a <strong>1D NumPy Array</strong> of integers. Each integer represents the cluster index (0 to K-1) assigned to the corresponding sample in the input data.</p>
</div>
</section>''',
("logistic-regression.html","Logistic Regression"),("dimensionality-reduction.html","Dimensionality Reduction"),
[("logistic-regression.html", "Classification vs Clustering"), ("dimensionality-reduction.html", "Pre-processing for Clustering")])

print("clustering.html expanded!")
