# 🐍 PYTHON CODES — COMPLETE EXAM CHEAT SHEET

*(Intro Data Analysis • Probability • Sampling • Inference)*

---

## 1️⃣ Imports (ALWAYS FIRST)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from scipy.stats import norm

import statsmodels.api as sm
from statsmodels.stats.weightstats import DescrStatsW
from statsmodels.stats.weightstats import zconfint_mean
```

---

## 2️⃣ Load Dataset

```python
df = pd.read_csv("file.csv")
```

OR (example dataset)

```python
df = sm.datasets.randhie.load_pandas().data.copy()
```

---

## 3️⃣ Inspect Data

```python
df.head()
df.info()
df.describe()
```

---

## 4️⃣ Select & Filter Data

```python
df["col"]
df[["col1", "col2"]]

df[df["age"] < 16]
df[df["Label"] == "BENIGN"]
```

---

## 5️⃣ Convert & Clean Numeric Data

```python
x = pd.to_numeric(df["col"], errors="coerce")
x = x[np.isfinite(x)]
x = x.to_numpy()
```

❗ Use `df["col"]` → 1D
❌ Avoid `df[["col"]]` → 2D

---

## 6️⃣ Basic Statistics

```python
df[col].mean()
df[col].median()
df[col].mode()
df[col].std()
df[col].var()
df[col].min()
df[col].max()
```

---

## 7️⃣ Quartiles & IQR (Outliers)

```python
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

---

## 8️⃣ Missing Values

```python
df.isna().sum()
df[col].fillna(df[col].median(), inplace=True)
```

---

## 9️⃣ Value Counts & Mode

```python
df[col].value_counts()
df[col].value_counts().idxmax()
```

---

## 1️⃣0️⃣ GroupBy & Aggregation

```python
df.groupby("category")[col].mean()
df.groupby("Label").agg({"col": "mean"})
```

---

## 1️⃣1️⃣ Create New Columns

```python
df["new_col"] = df["col"].apply(lambda x: 1 if x > 0 else 0)
```

---

## 1️⃣2️⃣ Plots (CORE)

### Histogram

```python
df[col].hist(bins=30)
```

### Box Plot

```python
sns.boxplot(x="Label", y=col, data=df)
```

### Count / Bar Plot

```python
sns.countplot(x="mode", data=df)
```

### Scatter Plot

```python
sns.scatterplot(x=a, y=b, hue="Label", data=df)
```

### Correlation Heatmap

```python
sns.heatmap(df[[a,b,c]].corr(), annot=True)
```

---

## 1️⃣3️⃣ Correlation

```python
df[[a,b,c]].corr()
```

---

## 1️⃣4️⃣ Conditional Probability

```python
P_A_given_B = len(df[A & B]) / len(df[B])
```

Shortcut for proportions:

```python
(df["Label"] != "BENIGN").mean()
```

---

## 1️⃣5️⃣ Bayes Components

```python
p_attack = (df["Label"] != "BENIGN").mean()
p_port80_given_attack = (
    (df["Label"] != "BENIGN") & (df["Port"] == 80)
).mean()
```

---

## 1️⃣6️⃣ Binomial Distribution

```python
stats.binom.pmf(k, n, p)
```

---

## 1️⃣7️⃣ Sampling (Random Samples)

```python
rng = np.random.default_rng(42)
x_sample = rng.choice(x, size=100, replace=False)
```

---

## 1️⃣8️⃣ Sampling Distribution (CLT)

```python
sample_means = np.random.choice(
    x, size=(1000, n), replace=True
).mean(axis=1)
```

---

## 1️⃣9️⃣ Sample Proportions

```python
y = (df[col] > threshold).astype(int)
phat = np.random.choice(
    y, size=(1000, n), replace=True
).mean(axis=1)
```

---

## 2️⃣0️⃣ Normal Fit (MLE)

```python
mu, std = stats.norm.fit(x)
xs = np.linspace(min(x), max(x), 100)
plt.plot(xs, stats.norm.pdf(xs, mu, std))
```

---

## 2️⃣1️⃣ Standard Error

```python
SE_mean = sigma / np.sqrt(n)
SE_prop = np.sqrt(p * (1 - p) / n)
```

---

## 2️⃣2️⃣ DescrStatsW (Mean & SE)

```python
ds = DescrStatsW(x)
mean = ds.mean
se = ds.std_mean
```

---

## 2️⃣3️⃣ Confidence Interval (Mean, Z)

```python
ci_low, ci_high = zconfint_mean(x, alpha=0.05)
```

---

## 2️⃣4️⃣ Margin of Error (MOE)

```python
moe = (ci_high - ci_low) / 2
```

OR

```python
moe = 1.96 * se
```

---

## 2️⃣5️⃣ CI vs Sample Size (Loop)

```python
rows = []
for n in [25, 50, 100, 250, 500]:
    xs = rng.choice(x, size=n, replace=False)
    ds = DescrStatsW(xs)
    ci_l, ci_h = zconfint_mean(xs)
    rows.append({
        "n": n,
        "mean": ds.mean,
        "moe": (ci_h - ci_l) / 2
    })
res = pd.DataFrame(rows)
```

---

## 2️⃣6️⃣ Plot Mean with CI

```python
plt.errorbar(
    x=res["n"],
    y=res["mean"],
    yerr=res["moe"],
    fmt="o"
)
plt.xscale("log")
plt.show()
```

---

## 2️⃣7️⃣ Plot MOE vs Sample Size

```python
plt.plot(res["n"], res["moe"], marker="o")
plt.xscale("log")
plt.show()
```

---

## 2️⃣8️⃣ Repeated Sampling (CI Coverage)

```python
cis = []
for i in range(40):
    xs = rng.choice(x, size=100, replace=False)
    ds = DescrStatsW(xs)
    ci_l, ci_h = zconfint_mean(xs)
    cis.append({
        "rep": i,
        "mean": ds.mean,
        "ci_low": ci_l,
        "ci_high": ci_h
    })
res3 = pd.DataFrame(cis)
```

---

## 2️⃣9️⃣ Plot Repeated CIs

```python
for _, r in res3.iterrows():
    plt.plot([r["ci_low"], r["ci_high"]], [r["rep"], r["rep"]])
    plt.plot(r["mean"], r["rep"], "o")
plt.show()
```

---

## 3️⃣0️⃣ Two-Group Split

```python
g1 = df.loc[df["idp"] == 1, "mdvis"].dropna().to_numpy()
g0 = df.loc[df["idp"] == 0, "mdvis"].dropna().to_numpy()
```

---

## 3️⃣1️⃣ Difference Between Two Means

```python
n1, n0 = len(g1), len(g0)
x1, x0 = g1.mean(), g0.mean()
s1, s0 = g1.std(ddof=1), g0.std(ddof=1)

diff = x1 - x0
se_diff = np.sqrt(s1**2/n1 + s0**2/n0)

ci_low = diff - 1.96 * se_diff
ci_high = diff + 1.96 * se_diff
```

---

## 3️⃣2️⃣ One-Sample Z-Test

```python
mu0 = 120
z_stat = (ds.mean - mu0) / ds.std_mean
p_value = 1 - norm.cdf(z_stat)
```

---

## 3️⃣3️⃣ One-Sample T-Test

```python
t_stat, p_value, dfree = ds.ttest_mean(
    value=120,
    alternative="larger"
)
```

---

## 3️⃣4️⃣ Decision Rule

```python
decision = "Reject H0" if p_value < 0.05 else "Fail to reject H0"
```

---

## 🧠 FINAL MEMORY (CODE + THEORY)

```
.mean() → average
.std() → spread
.choice() → sampling
DescrStatsW → mean, SE
zconfint_mean → CI
Large n → z
Small n → t
p < 0.05 → Reject
```
