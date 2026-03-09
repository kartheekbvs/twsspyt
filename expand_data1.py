import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_template import make_page

# EDA
make_page("data/exploratory.html","Exploratory Data Analysis","Data Analysis","&#x1F4CA;","intermediate","Data &rarr; EDA",
"EDA is the first step in any data science project. Explore, understand, and visualize your data before modeling. Covers df.info(), describe(), value_counts(), groupby(), correlation matrices, distribution plots, missing values analysis, and outlier detection.",
"Python for Data Analysis &mdash; Wes McKinney",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Dataset Overview</a></li>
<li><a href="#s2">Statistical Summary</a></li>
<li><a href="#s3">Missing Values Analysis</a></li>
<li><a href="#s4">Distribution Analysis</a></li>
<li><a href="#s5">Correlation Analysis</a></li>
<li><a href="#s6">Outlier Detection</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Dataset Overview</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; First Look at Data</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="cm"># Load a dataset</span>
df = pd.read_csv(<span class="st">"data.csv"</span>)

<span class="cm"># First look</span>
<span class="bi">print</span>(df.shape)              <span class="cm"># (rows, columns)</span>
<span class="bi">print</span>(df.head())              <span class="cm"># first 5 rows</span>
<span class="bi">print</span>(df.tail(<span class="nm">3</span>))             <span class="cm"># last 3 rows</span>
<span class="bi">print</span>(df.sample(<span class="nm">5</span>))           <span class="cm"># 5 random rows</span>

<span class="cm"># Data types and memory</span>
<span class="bi">print</span>(df.info())              <span class="cm"># columns, types, non-null counts</span>
<span class="bi">print</span>(df.dtypes)              <span class="cm"># just data types</span>
<span class="bi">print</span>(df.memory_usage(deep=<span class="kw">True</span>).sum() / <span class="nm">1024</span>**<span class="nm">2</span>, <span class="st">"MB"</span>)

<span class="cm"># Column names</span>
<span class="bi">print</span>(df.columns.tolist())

<span class="cm"># Unique values</span>
<span class="kw">for</span> col <span class="kw">in</span> df.select_dtypes(include=<span class="st">"object"</span>).columns:
    <span class="bi">print</span>(<span class="st">f"{col}: {df[col].nunique()} unique &rarr; {df[col].unique()[:5]}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Shape: (891, 12)<br>info(): 5 numeric, 5 object, 2 boolean columns<br>Memory: 0.34 MB</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Statistical Summary</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Numeric statistics</span>
<span class="bi">print</span>(df.describe())
<span class="cm">#        count   mean     std     min    25%    50%    75%    max</span>
<span class="cm"># age    714.0  29.70   14.53   0.42  20.12  28.00  38.00  80.00</span>
<span class="cm"># fare   891.0  32.20   49.69   0.00   7.91  14.45  31.00 512.33</span>

<span class="cm"># Categorical statistics</span>
<span class="bi">print</span>(df.describe(include=<span class="st">"object"</span>))
<span class="cm">#        count  unique   top    freq</span>
<span class="cm"># sex     891     2    male    577</span>

<span class="cm"># Value counts for each column</span>
<span class="bi">print</span>(df[<span class="st">"class"</span>].value_counts())
<span class="bi">print</span>(df[<span class="st">"class"</span>].value_counts(normalize=<span class="kw">True</span>))  <span class="cm"># percentages</span>

<span class="cm"># GroupBy analysis</span>
<span class="bi">print</span>(df.groupby(<span class="st">"class"</span>)[<span class="st">"age"</span>].agg([<span class="st">"mean"</span>, <span class="st">"median"</span>, <span class="st">"std"</span>]))</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Third    491 (55.1%)<br>First    216 (24.2%)<br>Second   184 (20.7%)</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Missing Values Analysis</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Missing values count and percentage</span>
missing = df.isnull().sum()
missing_pct = (missing / <span class="bi">len</span>(df) * <span class="nm">100</span>).round(<span class="nm">2</span>)
missing_df = pd.DataFrame({
    <span class="st">"Missing"</span>: missing,
    <span class="st">"Percentage"</span>: missing_pct
}).sort_values(<span class="st">"Missing"</span>, ascending=<span class="kw">False</span>)
<span class="bi">print</span>(missing_df[missing_df[<span class="st">"Missing"</span>] > <span class="nm">0</span>])

<span class="cm"># Visualize missing values</span>
<span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt
plt.figure(figsize=(<span class="nm">10</span>, <span class="nm">4</span>))
plt.bar(missing_df.index, missing_df[<span class="st">"Percentage"</span>], color=<span class="st">"#e74c3c"</span>)
plt.title(<span class="st">"Missing Values by Column"</span>)
plt.xticks(rotation=<span class="nm">45</span>)
plt.ylabel(<span class="st">"% Missing"</span>)
plt.show()

<span class="cm"># Handle missing values</span>
df[<span class="st">"age"</span>].fillna(df[<span class="st">"age"</span>].median(), inplace=<span class="kw">True</span>)
df[<span class="st">"city"</span>].fillna(<span class="st">"Unknown"</span>, inplace=<span class="kw">True</span>)
df.dropna(subset=[<span class="st">"target"</span>], inplace=<span class="kw">True</span>)  <span class="cm"># drop rows missing target</span></pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>cabin     687  77.10%<br>age       177  19.87%<br>embarked    2   0.22%</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Distribution Analysis</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt

<span class="cm"># Histogram for each numeric column</span>
df.select_dtypes(include=np.number).hist(bins=<span class="nm">20</span>, figsize=(<span class="nm">12</span>, <span class="nm">8</span>),
                                          edgecolor=<span class="st">"black"</span>)
plt.suptitle(<span class="st">"Feature Distributions"</span>, fontsize=<span class="nm">16</span>)
plt.tight_layout()
plt.show()

<span class="cm"># Skewness check</span>
<span class="kw">for</span> col <span class="kw">in</span> df.select_dtypes(include=np.number).columns:
    skew = df[col].skew()
    <span class="bi">print</span>(<span class="st">f"{col:>15}: skew = {skew:+.3f}"</span>,
          <span class="st">"&larr; highly skewed"</span> <span class="kw">if</span> <span class="bi">abs</span>(skew) > <span class="nm">1</span> <span class="kw">else</span> <span class="st">""</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>            age: skew = +0.389<br>           fare: skew = +4.787 &larr; highly skewed<br>     siblings: skew = +3.695 &larr; highly skewed</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Correlation Analysis</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Correlation matrix</span>
corr = df.select_dtypes(include=np.number).corr()
<span class="bi">print</span>(corr.round(<span class="nm">3</span>))

<span class="cm"># Heatmap</span>
fig, ax = plt.subplots(figsize=(<span class="nm">10</span>, <span class="nm">8</span>))
im = ax.imshow(corr, cmap=<span class="st">"RdBu_r"</span>, vmin=-<span class="nm">1</span>, vmax=<span class="nm">1</span>)
ax.set_xticks(<span class="bi">range</span>(<span class="bi">len</span>(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=<span class="nm">45</span>, ha=<span class="st">"right"</span>)
ax.set_yticks(<span class="bi">range</span>(<span class="bi">len</span>(corr.columns)))
ax.set_yticklabels(corr.columns)
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="bi">len</span>(corr)):
    <span class="kw">for</span> j <span class="kw">in</span> <span class="bi">range</span>(<span class="bi">len</span>(corr)):
        ax.text(j, i, <span class="st">f"{corr.iloc[i,j]:.2f}"</span>, ha=<span class="st">"center"</span>, va=<span class="st">"center"</span>)
plt.colorbar(im)
plt.title(<span class="st">"Correlation Heatmap"</span>)
plt.tight_layout()
plt.show()

<span class="cm"># Strong correlations</span>
<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="bi">len</span>(corr)):
    <span class="kw">for</span> j <span class="kw">in</span> <span class="bi">range</span>(i+<span class="nm">1</span>, <span class="bi">len</span>(corr)):
        <span class="kw">if</span> <span class="bi">abs</span>(corr.iloc[i,j]) > <span class="nm">0.5</span>:
            <span class="bi">print</span>(<span class="st">f"  {corr.columns[i]} &harr; {corr.columns[j]}: {corr.iloc[i,j]:.3f}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Strong correlations:<br>  fare &harr; class: -0.549<br>  age &harr; fare: 0.096 (weak)</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Outlier Detection</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># IQR method for outlier detection</span>
<span class="kw">def</span> <span class="bi">find_outliers_iqr</span>(series):
    Q1 = series.quantile(<span class="nm">0.25</span>)
    Q3 = series.quantile(<span class="nm">0.75</span>)
    IQR = Q3 - Q1
    lower = Q1 - <span class="nm">1.5</span> * IQR
    upper = Q3 + <span class="nm">1.5</span> * IQR
    outliers = series[(series < lower) | (series > upper)]
    <span class="kw">return</span> outliers, lower, upper

<span class="kw">for</span> col <span class="kw">in</span> [<span class="st">"age"</span>, <span class="st">"fare"</span>]:
    outliers, lo, hi = find_outliers_iqr(df[col])
    <span class="bi">print</span>(<span class="st">f"{col}: {len(outliers)} outliers ({lo:.1f} &ndash; {hi:.1f})"</span>)

<span class="cm"># Z-score method</span>
<span class="kw">from</span> scipy <span class="kw">import</span> stats
z_scores = np.abs(stats.zscore(df.select_dtypes(include=np.number).dropna()))
outliers_z = (z_scores > <span class="nm">3</span>).sum(axis=<span class="nm">0</span>)
<span class="bi">print</span>(<span class="st">f"Z-score outliers (|z|>3): {outliers_z}"</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>age: 1 outlier (bound: -6.7 to 64.8)<br>fare: 116 outliers (bound: -26.7 to 65.6)</div></div></section>''',
("matplotlib.html","Matplotlib"),("feature-engineering.html","Feature Engineering"))

# FEATURE ENGINEERING
make_page("data/feature-engineering.html","Feature Engineering","Data Analysis","&#x1F4CA;","advanced","Data &rarr; Feature Engineering",
"Feature engineering is the art of creating new features from existing data to improve model performance. Covers feature creation, binning, log transforms, interaction features, text feature extraction, date features, target encoding, and feature importance.",
"Hands-On ML &mdash; Aur&eacute;lien G&eacute;ron",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Numerical Transformations</a></li>
<li><a href="#s2">Binning &amp; Discretization</a></li>
<li><a href="#s3">Interaction Features</a></li>
<li><a href="#s4">Date/Time Features</a></li>
<li><a href="#s5">Text Feature Extraction</a></li>
<li><a href="#s6">Feature Importance</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Numerical Transformations</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> numpy <span class="kw">as</span> np

df = pd.DataFrame({
    <span class="st">"price"</span>: [<span class="nm">500</span>, <span class="nm">15000</span>, <span class="nm">200</span>, <span class="nm">80000</span>, <span class="nm">3000</span>],
    <span class="st">"rooms"</span>: [<span class="nm">2</span>, <span class="nm">4</span>, <span class="nm">1</span>, <span class="nm">6</span>, <span class="nm">3</span>],
    <span class="st">"area"</span>:  [<span class="nm">50</span>, <span class="nm">120</span>, <span class="nm">30</span>, <span class="nm">200</span>, <span class="nm">80</span>]
})

<span class="cm"># Log transform &mdash; reduces skewness</span>
df[<span class="st">"log_price"</span>] = np.log1p(df[<span class="st">"price"</span>])

<span class="cm"># Square root transform</span>
df[<span class="st">"sqrt_price"</span>] = np.sqrt(df[<span class="st">"price"</span>])

<span class="cm"># Polynomial features</span>
df[<span class="st">"area_squared"</span>] = df[<span class="st">"area"</span>] ** <span class="nm">2</span>

<span class="cm"># Ratios</span>
df[<span class="st">"price_per_room"</span>] = df[<span class="st">"price"</span>] / df[<span class="st">"rooms"</span>]
df[<span class="st">"price_per_sqm"</span>] = df[<span class="st">"price"</span>] / df[<span class="st">"area"</span>]

<span class="bi">print</span>(df[[<span class="st">"price"</span>, <span class="st">"log_price"</span>, <span class="st">"price_per_room"</span>, <span class="st">"price_per_sqm"</span>]])</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>  price  log_price  price_per_room  price_per_sqm<br>    500      6.22          250.0          10.0<br>  15000      9.62         3750.0         125.0<br>    200      5.30          200.0           6.7<br>  80000     11.29        13333.3         400.0<br>   3000      8.01         1000.0          37.5</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Binning &amp; Discretization</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Equal-width bins</span>
df[<span class="st">"age_bin"</span>] = pd.cut(df[<span class="st">"age"</span>], bins=<span class="nm">5</span>, labels=[<span class="st">"very young"</span>,<span class="st">"young"</span>,<span class="st">"mid"</span>,<span class="st">"senior"</span>,<span class="st">"old"</span>])

<span class="cm"># Custom bins</span>
df[<span class="st">"age_group"</span>] = pd.cut(df[<span class="st">"age"</span>], bins=[<span class="nm">0</span>,<span class="nm">18</span>,<span class="nm">35</span>,<span class="nm">50</span>,<span class="nm">100</span>],
                          labels=[<span class="st">"child"</span>,<span class="st">"young"</span>,<span class="st">"middle"</span>,<span class="st">"senior"</span>])

<span class="cm"># Quantile-based bins (equal count in each bin)</span>
df[<span class="st">"income_quartile"</span>] = pd.qcut(df[<span class="st">"income"</span>], q=<span class="nm">4</span>,
                                 labels=[<span class="st">"low"</span>,<span class="st">"mid-low"</span>,<span class="st">"mid-high"</span>,<span class="st">"high"</span>])

<span class="bi">print</span>(df[<span class="st">"age_group"</span>].value_counts())</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>young     345<br>middle    234<br>senior    189<br>child     123</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Interaction Features</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.preprocessing <span class="kw">import</span> PolynomialFeatures

<span class="cm"># Create interaction features automatically</span>
X = df[[<span class="st">"rooms"</span>, <span class="st">"area"</span>]].values
poly = PolynomialFeatures(degree=<span class="nm">2</span>, include_bias=<span class="kw">False</span>, interaction_only=<span class="kw">False</span>)
X_poly = poly.fit_transform(X)
<span class="bi">print</span>(<span class="st">f"Features: {poly.get_feature_names_out()}"</span>)
<span class="cm"># ['rooms', 'area', 'rooms^2', 'rooms area', 'area^2']</span>

<span class="cm"># Manual interaction</span>
df[<span class="st">"rooms_x_area"</span>] = df[<span class="st">"rooms"</span>] * df[<span class="st">"area"</span>]
df[<span class="st">"total_baths_per_room"</span>] = df[<span class="st">"bathrooms"</span>] / df[<span class="st">"rooms"</span>]</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Features: ['rooms', 'area', 'rooms^2', 'rooms area', 'area^2']</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Date/Time Features</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">df[<span class="st">"date"</span>] = pd.to_datetime(df[<span class="st">"date_string"</span>])

<span class="cm"># Extract components</span>
df[<span class="st">"year"</span>]     = df[<span class="st">"date"</span>].dt.year
df[<span class="st">"month"</span>]    = df[<span class="st">"date"</span>].dt.month
df[<span class="st">"day"</span>]      = df[<span class="st">"date"</span>].dt.day
df[<span class="st">"weekday"</span>]  = df[<span class="st">"date"</span>].dt.dayofweek  <span class="cm"># 0=Mon, 6=Sun</span>
df[<span class="st">"is_weekend"</span>] = df[<span class="st">"weekday"</span>].isin([<span class="nm">5</span>,<span class="nm">6</span>]).astype(<span class="bi">int</span>)
df[<span class="st">"quarter"</span>]  = df[<span class="st">"date"</span>].dt.quarter
df[<span class="st">"hour"</span>]     = df[<span class="st">"date"</span>].dt.hour
df[<span class="st">"day_of_year"</span>] = df[<span class="st">"date"</span>].dt.dayofyear

<span class="cm"># Days since an event</span>
df[<span class="st">"days_since_start"</span>] = (df[<span class="st">"date"</span>] - df[<span class="st">"date"</span>].min()).dt.days</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Extracted: year, month, day, weekday, is_weekend, quarter, hour</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Text Feature Extraction</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.feature_extraction.text <span class="kw">import</span> CountVectorizer, TfidfVectorizer

texts = [<span class="st">"python is great"</span>, <span class="st">"machine learning with python"</span>,
         <span class="st">"deep learning is amazing"</span>]

<span class="cm"># Bag of Words (word counts)</span>
cv = CountVectorizer()
bow = cv.fit_transform(texts)
<span class="bi">print</span>(<span class="st">f"Vocabulary: {cv.get_feature_names_out()}"</span>)
<span class="bi">print</span>(bow.toarray())

<span class="cm"># TF-IDF (weighted word importance)</span>
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(texts)
<span class="bi">print</span>(<span class="st">f"TF-IDF shape: {tfidf_matrix.shape}"</span>)

<span class="cm"># Simple text features</span>
df[<span class="st">"text_len"</span>] = df[<span class="st">"text"</span>].str.len()
df[<span class="st">"word_count"</span>] = df[<span class="st">"text"</span>].str.split().str.len()
df[<span class="st">"has_number"</span>] = df[<span class="st">"text"</span>].str.contains(r<span class="st">"\\d"</span>).astype(<span class="bi">int</span>)</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>Vocabulary: ['amazing', 'deep', 'great', 'is', 'learning', 'machine', 'python', 'with']</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Feature Importance</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">from</span> sklearn.ensemble <span class="kw">import</span> RandomForestClassifier
<span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt

<span class="cm"># Train model and extract importances</span>
rf = RandomForestClassifier(n_estimators=<span class="nm">100</span>, random_state=<span class="nm">42</span>)
rf.fit(X_train, y_train)

importances = rf.feature_importances_
feature_names = X_train.columns

<span class="cm"># Plot top features</span>
top_n = <span class="nm">10</span>
idx = np.argsort(importances)[-top_n:]
plt.figure(figsize=(<span class="nm">8</span>, <span class="nm">5</span>))
plt.barh(feature_names[idx], importances[idx], color=<span class="st">"#3498db"</span>)
plt.xlabel(<span class="st">"Importance"</span>)
plt.title(<span class="st">"Top 10 Feature Importances"</span>)
plt.tight_layout()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Horizontal bar chart: top features ranked by Random Forest importance]</div></div></section>''',
("exploratory.html","EDA"),("../ml/preprocessing.html","Preprocessing"))

# SEABORN
make_page("data/seaborn.html","Seaborn Visualization","Data Analysis","&#x1F4CA;","intermediate","Data &rarr; Seaborn",
"Seaborn is a statistical visualization library built on Matplotlib. It provides beautiful, informative plots with minimal code. Covers relational, categorical, distribution, matrix, and regression plots with multiple real-world examples.",
"Python Data Science Handbook &mdash; Jake VanderPlas",
'''<div class="toc-box"><h4>&#x1F4CB; Table of Contents</h4><ol>
<li><a href="#s1">Setup &amp; Themes</a></li>
<li><a href="#s2">Distribution Plots</a></li>
<li><a href="#s3">Categorical Plots</a></li>
<li><a href="#s4">Relational Plots</a></li>
<li><a href="#s5">Matrix Plots (Heatmap)</a></li>
<li><a href="#s6">Pair Plots &amp; Joint Plots</a></li>
</ol></div>

<section class="content-section" id="s1"><h2>1 &middot; Setup &amp; Themes</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="kw">import</span> seaborn <span class="kw">as</span> sns
<span class="kw">import</span> matplotlib.pyplot <span class="kw">as</span> plt
<span class="kw">import</span> pandas <span class="kw">as</span> pd

<span class="cm"># Set theme</span>
sns.set_theme(style=<span class="st">"whitegrid"</span>)  <span class="cm"># darkgrid, white, dark, ticks</span>
sns.set_palette(<span class="st">"husl"</span>)            <span class="cm"># deep, muted, bright, pastel, husl</span>
sns.set_context(<span class="st">"notebook"</span>)        <span class="cm"># paper, talk, poster</span>

<span class="cm"># Built-in datasets</span>
tips = sns.load_dataset(<span class="st">"tips"</span>)
iris = sns.load_dataset(<span class="st">"iris"</span>)
penguins = sns.load_dataset(<span class="st">"penguins"</span>)
<span class="bi">print</span>(tips.head())</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>   total_bill   tip   sex smoker  day   time  size<br>0       16.99  1.01  Female  No  Sun  Dinner   2<br>1       10.34  1.66    Male  No  Sun  Dinner   3</div></div></section>

<section class="content-section" id="s2"><h2>2 &middot; Distribution Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; histplot, kdeplot, rugplot</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">fig, axes = plt.subplots(<span class="nm">2</span>, <span class="nm">2</span>, figsize=(<span class="nm">12</span>, <span class="nm">10</span>))

<span class="cm"># Histogram with KDE</span>
sns.histplot(tips[<span class="st">"total_bill"</span>], kde=<span class="kw">True</span>, bins=<span class="nm">20</span>, ax=axes[<span class="nm">0</span>,<span class="nm">0</span>], color=<span class="st">"steelblue"</span>)
axes[<span class="nm">0</span>,<span class="nm">0</span>].set_title(<span class="st">"Histogram + KDE"</span>)

<span class="cm"># KDE plot by group</span>
sns.kdeplot(data=tips, x=<span class="st">"total_bill"</span>, hue=<span class="st">"time"</span>, ax=axes[<span class="nm">0</span>,<span class="nm">1</span>], fill=<span class="kw">True</span>)
axes[<span class="nm">0</span>,<span class="nm">1</span>].set_title(<span class="st">"KDE by Meal Time"</span>)

<span class="cm"># ECDF (Empirical Cumulative Distribution)</span>
sns.ecdfplot(data=tips, x=<span class="st">"total_bill"</span>, hue=<span class="st">"sex"</span>, ax=axes[<span class="nm">1</span>,<span class="nm">0</span>])
axes[<span class="nm">1</span>,<span class="nm">0</span>].set_title(<span class="st">"ECDF"</span>)

<span class="cm"># Rug plot (1D scatter)</span>
sns.histplot(tips[<span class="st">"tip"</span>], kde=<span class="kw">True</span>, ax=axes[<span class="nm">1</span>,<span class="nm">1</span>])
sns.rugplot(tips[<span class="st">"tip"</span>], ax=axes[<span class="nm">1</span>,<span class="nm">1</span>], color=<span class="st">"red"</span>)
axes[<span class="nm">1</span>,<span class="nm">1</span>].set_title(<span class="st">"Histogram + Rug"</span>)

plt.suptitle(<span class="st">"Distribution Plots"</span>, fontsize=<span class="nm">16</span>)
plt.tight_layout()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[2&times;2 grid: histogram+KDE, grouped KDE, ECDF, rugplot]</div></div></section>

<section class="content-section" id="s3"><h2>3 &middot; Categorical Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; box, violin, swarm, bar, count</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">fig, axes = plt.subplots(<span class="nm">2</span>, <span class="nm">3</span>, figsize=(<span class="nm">18</span>, <span class="nm">10</span>))

<span class="cm"># Box plot</span>
sns.boxplot(data=tips, x=<span class="st">"day"</span>, y=<span class="st">"total_bill"</span>, hue=<span class="st">"sex"</span>, ax=axes[<span class="nm">0</span>,<span class="nm">0</span>])
axes[<span class="nm">0</span>,<span class="nm">0</span>].set_title(<span class="st">"Box Plot"</span>)

<span class="cm"># Violin plot (box + kernel density)</span>
sns.violinplot(data=tips, x=<span class="st">"day"</span>, y=<span class="st">"total_bill"</span>, hue=<span class="st">"sex"</span>,
               split=<span class="kw">True</span>, ax=axes[<span class="nm">0</span>,<span class="nm">1</span>])
axes[<span class="nm">0</span>,<span class="nm">1</span>].set_title(<span class="st">"Violin Plot"</span>)

<span class="cm"># Swarm plot (actual data points)</span>
sns.swarmplot(data=tips, x=<span class="st">"day"</span>, y=<span class="st">"total_bill"</span>, hue=<span class="st">"sex"</span>,
              ax=axes[<span class="nm">0</span>,<span class="nm">2</span>], size=<span class="nm">3</span>)
axes[<span class="nm">0</span>,<span class="nm">2</span>].set_title(<span class="st">"Swarm Plot"</span>)

<span class="cm"># Bar plot (with confidence interval)</span>
sns.barplot(data=tips, x=<span class="st">"day"</span>, y=<span class="st">"total_bill"</span>, hue=<span class="st">"sex"</span>,
            ax=axes[<span class="nm">1</span>,<span class="nm">0</span>], ci=<span class="nm">95</span>)
axes[<span class="nm">1</span>,<span class="nm">0</span>].set_title(<span class="st">"Bar Plot (mean + CI)"</span>)

<span class="cm"># Count plot</span>
sns.countplot(data=tips, x=<span class="st">"day"</span>, hue=<span class="st">"time"</span>, ax=axes[<span class="nm">1</span>,<span class="nm">1</span>])
axes[<span class="nm">1</span>,<span class="nm">1</span>].set_title(<span class="st">"Count Plot"</span>)

<span class="cm"># Strip plot (jittered scatter)</span>
sns.stripplot(data=tips, x=<span class="st">"day"</span>, y=<span class="st">"tip"</span>, hue=<span class="st">"sex"</span>,
              ax=axes[<span class="nm">1</span>,<span class="nm">2</span>], jitter=<span class="kw">True</span>, alpha=<span class="nm">0.6</span>)
axes[<span class="nm">1</span>,<span class="nm">2</span>].set_title(<span class="st">"Strip Plot"</span>)

plt.suptitle(<span class="st">"Categorical Plots"</span>, fontsize=<span class="nm">16</span>)
plt.tight_layout()
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[2&times;3 grid: box, violin, swarm, bar, count, strip plots]</div></div></section>

<section class="content-section" id="s4"><h2>4 &middot; Relational Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python &middot; scatterplot, lineplot, relplot</span><button class="copy-btn">Copy</button></div>
<pre class="code-block">fig, axes = plt.subplots(<span class="nm">1</span>, <span class="nm">3</span>, figsize=(<span class="nm">18</span>, <span class="nm">5</span>))

<span class="cm"># Scatter with regression line</span>
sns.regplot(data=tips, x=<span class="st">"total_bill"</span>, y=<span class="st">"tip"</span>, ax=axes[<span class="nm">0</span>],
            scatter_kws={<span class="st">"alpha"</span>:<span class="nm">0.5</span>})
axes[<span class="nm">0</span>].set_title(<span class="st">"Scatter + Regression"</span>)

<span class="cm"># Scatter colored by category</span>
sns.scatterplot(data=tips, x=<span class="st">"total_bill"</span>, y=<span class="st">"tip"</span>,
                hue=<span class="st">"time"</span>, size=<span class="st">"size"</span>, ax=axes[<span class="nm">1</span>])
axes[<span class="nm">1</span>].set_title(<span class="st">"Multi-dim Scatter"</span>)

<span class="cm"># Line plot (with CI)</span>
fmri = sns.load_dataset(<span class="st">"fmri"</span>)
sns.lineplot(data=fmri, x=<span class="st">"timepoint"</span>, y=<span class="st">"signal"</span>,
             hue=<span class="st">"event"</span>, style=<span class="st">"region"</span>, ax=axes[<span class="nm">2</span>])
axes[<span class="nm">2</span>].set_title(<span class="st">"Line Plot (mean + CI)"</span>)

plt.tight_layout()
plt.show()

<span class="cm"># FacetGrid with relplot</span>
g = sns.relplot(data=tips, x=<span class="st">"total_bill"</span>, y=<span class="st">"tip"</span>,
                col=<span class="st">"time"</span>, hue=<span class="st">"smoker"</span>, style=<span class="st">"smoker"</span>,
                kind=<span class="st">"scatter"</span>, height=<span class="nm">4</span>)
g.fig.suptitle(<span class="st">"Faceted Scatter"</span>, y=<span class="nm">1.02</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[3 panels: regression scatter, multi-dim scatter, line plot with CI]</div></div></section>

<section class="content-section" id="s5"><h2>5 &middot; Matrix Plots (Heatmap)</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Correlation heatmap</span>
corr = tips.select_dtypes(include=<span class="st">"number"</span>).corr()

plt.figure(figsize=(<span class="nm">8</span>, <span class="nm">6</span>))
sns.heatmap(corr, annot=<span class="kw">True</span>, cmap=<span class="st">"coolwarm"</span>, center=<span class="nm">0</span>,
            fmt=<span class="st">".2f"</span>, square=<span class="kw">True</span>, linewidths=<span class="nm">0.5</span>,
            vmin=-<span class="nm">1</span>, vmax=<span class="nm">1</span>)
plt.title(<span class="st">"Correlation Heatmap"</span>)
plt.show()

<span class="cm"># Cluster map (hierarchical clustering + heatmap)</span>
sns.clustermap(corr, annot=<span class="kw">True</span>, cmap=<span class="st">"viridis"</span>, figsize=(<span class="nm">6</span>,<span class="nm">6</span>))
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Annotated heatmap with warm/cool colors for positive/negative correlations]</div></div></section>

<section class="content-section" id="s6"><h2>6 &middot; Pair Plots &amp; Joint Plots</h2>
<div class="code-block-wrapper"><div class="code-block-header"><div class="code-dots"><span></span><span></span><span></span></div><span class="code-lang-badge">Python</span><button class="copy-btn">Copy</button></div>
<pre class="code-block"><span class="cm"># Pair plot: all pairwise relationships</span>
sns.pairplot(iris, hue=<span class="st">"species"</span>, diag_kind=<span class="st">"kde"</span>,
             plot_kws={<span class="st">"alpha"</span>: <span class="nm">0.6</span>})
plt.suptitle(<span class="st">"Iris Pair Plot"</span>, y=<span class="nm">1.02</span>)
plt.show()

<span class="cm"># Joint plot: 2 variables with marginal distributions</span>
g = sns.jointplot(data=tips, x=<span class="st">"total_bill"</span>, y=<span class="st">"tip"</span>,
                  kind=<span class="st">"hex"</span>, color=<span class="st">"#4ECDC4"</span>)
<span class="cm"># kind options: "scatter", "kde", "hist", "hex", "reg", "resid"</span>
plt.show()

<span class="cm"># Joint plot with KDE</span>
g = sns.jointplot(data=tips, x=<span class="st">"total_bill"</span>, y=<span class="st">"tip"</span>,
                  kind=<span class="st">"kde"</span>, fill=<span class="kw">True</span>, cmap=<span class="st">"Blues"</span>)
plt.show()</pre>
<div class="output-block"><div class="output-label">&#x25B6; Output</div>[Pair plot: 4&times;4 grid of Iris species colored in 3 colors]<br>[Joint plot: scatter + marginal histograms]</div></div></section>''',
("matplotlib.html","Matplotlib"),("feature-engineering.html","Feature Engineering"))

print("exploratory.html + feature-engineering.html + seaborn.html expanded!")
