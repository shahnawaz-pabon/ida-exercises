<div align="center">
  <h1>:open_book: IDA Exercise Notes :open_book:</h1>
</div>

# OTHER FILES TO LOOK AT
- [IMPORTANT PYTHON CODES](./IMPORTANT-PYTHON-CODES.md)
- [QUESTIONS AND ANSWERS](./QUESTIONS-AND-ANSWERS.md)


## 1️⃣ Data Types & Plots

* **Categorical**: labels (mode, attack/benign) → **bar plot**
* **Numerical**: numbers

  * Distribution → **histogram**
  * Compare groups → **box plot**
  * Relationship (2 numeric) → **scatter plot**

---

## 2️⃣ Descriptive Statistics

**Center**

* Mean = average
* Median = middle (best for skewed data)
* Mode = most frequent

**Spread**

* Range = max − min
* SD = typical spread
* **IQR = Q3 − Q1** (middle 50%)

---

## 3️⃣ Shape of Data

* **Right-skewed**: long right tail → mean > median > mode
* **Left-skewed**: long left tail
* **Symmetric**: mean ≈ median ≈ mode
* **Kurtosis**: tail heaviness (outliers)

---

## 4️⃣ Box Plot (quick read)

* Line = median
* Box = IQR
* Whiskers = normal range
* Dots = outliers

⚠️ Can mislead for discrete, skewed, or bimodal data.

---

## 5️⃣ Outliers (IQR rule)

* Lower = Q1 − 1.5×IQR
* Upper = Q3 + 1.5×IQR
  ⚠️ Outliers ≠ errors (often real behavior).

---

## 6️⃣ Correlation

* Measures **linear** relationship (−1 to +1)
* Near 0 → weak/no linear relation
* Only for numeric data
  ⚠️ Correlation ≠ causation

---

## 7️⃣ Probability Basics

* **Experiment**: one observation
* **Sample space**: all outcomes
* **Event**: subset of outcomes

### Conditional probability

$[
P(A|B)=\frac{P(A\cap B)}{P(B)}
]$
**Meaning**: “Out of B, how many are A?”

### Bayes’ theorem

$[
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
]$
**Memory**: AND ÷ GIVEN

---

## 8️⃣ Binomial Distribution

Use when:

* Fixed n
* Two outcomes (yes/no)
* Constant p
* Independent trials

$[
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
]$

### Normal approximation (binomial)

Valid if:
$[
np\ge10 ;\text{and}; n(1-p)\ge10
]$

---

## 9️⃣ Population vs Sample

* **Population**: all data
* **Sample**: subset
* **Sample mean**: average of sample
* **Sampling distribution**: distribution of sample means

---

## 1️⃣0️⃣ Central Limit Theorem (CLT)

> As n increases, the **sampling distribution of the mean** becomes **normal** and **less variable**, regardless of original data shape.

Effects of increasing n:

* Shape → more normal
* Spread → smaller

---

## 1️⃣1️⃣ Standard Error (SE) ⭐

**Meaning**: typical error in the sample mean

$[
\boxed{SE=\frac{\sigma}{\sqrt{n}}}
]$

* σ = population SD
* Bigger n → smaller error

---

## 1️⃣2️⃣ Sampling Distribution of a Proportion

* Proportion = mean of 0/1 data
* Mean = p
* SD =
  $[
  \sqrt{\frac{p(1-p)}{n}}
  ]$

Normal approx valid if:
$[
np\ge10,; n(1-p)\ge10
]$

---

## 1️⃣3️⃣ Empirical vs Theoretical

* **Empirical**: from simulation
* **Theoretical**: from formula
  They should match when n is large.

---

## 1️⃣4️⃣ Mean vs Median

* Symmetric → **mean**
* Skewed / outliers → **median**

---

## 1️⃣5️⃣ Why normal fits fail in real data

* Skewed
* Heavy tails
* Mixed behaviors
  Better models: **log-normal, gamma, Pareto**

---

## 1️⃣6️⃣ Basic Estimates

**Mean (average)**
$[
\bar{x} = \frac{\text{sum of values}}{n}
]$

**Proportion**
$[
\hat{p} = \frac{\text{number of successes}}{n}
]$

---

## 1️⃣7️⃣ Uncertainty (VERY IMPORTANT)

### Standard Error (SE)

How uncertain an estimate is.
$[
SE_{\text{mean}} = \frac{s}{\sqrt{n}}
]$

---

### Margin of Error (MOE)

How wrong the estimate could be.
$[
MOE = z \times SE \quad \text{or} \quad t \times SE
]$

---

### Confidence Interval (CI)

Range for the true value.
$[
CI = \text{estimate} \pm MOE
]$

**95% CI meaning:**
95 out of 100 such intervals contain the true value.

---

## 1️⃣8️⃣ Sample Size Effect

* Bigger **n** → smaller SE
* Bigger **n** → smaller MOE
* Bigger **n** → narrower CI

$[
MOE \propto \frac{1}{\sqrt{n}}
]$

---

## 1️⃣9️⃣ Interpreting Confidence Intervals (EXAM GOLD)

| CI Example      | Meaning             |
| --------------- | ------------------- |
| `[0.3, 1.2]`    | Group 1 > Group 0   |
| `[-0.8, -0.2]`  | Group 1 < Group 0   |
| `[-0.01, 0.02]` | No clear difference |

**Rule:**
CI includes **0** → no difference
CI excludes **0** → difference exists

---

## 2️⃣0️⃣ Hypothesis Testing

### Hypotheses

* **H0 (Null):** default claim
* **H1 (Alternative):** what we test

---

### One-sided vs Two-sided

* “Greater than / Less than” → **One-sided**
* “Different from” → **Two-sided**

---

### Alpha (α)

* Usually **0.05**
* 5% chance of being wrong

---

### p-value

Chance result happened by luck **if H0 is true**.

**Decision rule:**

* p < 0.05 → **Reject H0**
* p ≥ 0.05 → **Fail to reject H0**

---

### Reject vs Fail to Reject

* **Reject H0:** strong evidence against H0
* **Fail to reject H0:** not enough evidence

❗Fail to reject ≠ H0 is true

---

## 2️⃣1️⃣ z-test vs t-test

| Situation             | Test   |
| --------------------- | ------ |
| Large sample (n ≥ 30) | z-test |
| Small sample (n < 30) | t-test |

---

## 2️⃣2️⃣ Degrees of Freedom (dfree)

How many values can vary freely.
[
df = n - 1
]

Example: n = 15 → df = 14

---

## 2️⃣3️⃣ Test Statistics

### z-statistic
$[
z = \frac{\bar{x} - \mu_0}{SE}
]$

### t-statistic

Same formula, but uses **t distribution** and df.

---

## 2️⃣4️⃣ Difference Between Two Means

**Estimate**
$[
\hat{\Delta} = \bar{x}_1 - \bar{x}_0
]$

**Standard Error**
$[
SE = \sqrt{\frac{s_1^2}{n_1} + \frac{s_0^2}{n_0}}
]$

**95% CI**
$[
\hat{\Delta} \pm 1.96 \times SE
]$

---

## 2️⃣5️⃣ Sampling Variability

* Different samples → different results
* Even with same sample size
* This is normal randomness

---

## 🧠 SOME IMPORTANT HACKS

* **CLT**:
  “As n increases, the sampling distribution of the mean becomes more normal and less variable due to the Central Limit Theorem.”

* **Variability**:
  “Variability decreases with increasing sample size because averaging cancels randomness.”

* **Proportion**:
  “The normal approximation is reasonable when both np and n(1−p) are sufficiently large.”

* **Standard Error**:
  “Standard error decreases with √n, enabling more precise estimates with larger samples.”

---

## 🔑 10-SECOND MEMORY BLOCK

* Mean → CLT → bell curve
* Bigger n → tighter
* **SE = σ / √n**
* Proportion = average of 0/1
* Outliers ≠ errors

---

## 🧠 MASTER MEMORY BLOCK

```
Mean → SE → MOE → CI
Big sample → z-test
Small sample → t-test
df = n − 1
p < 0.05 → Reject H0
CI includes 0 → No difference
```

---

## ✍️ EXAM CONCLUSION TEMPLATE FOR REJECT HYPOTHESIS

> At the 5% significance level, we [reject / fail to reject] H0.
> The data [do / do not] provide evidence for the stated claim.