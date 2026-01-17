<div align="center">
  <h1>:open_book: IDA Exercise Notes :open_book:</h1>
</div>

## 🔹 1. NumPy Basics

* `np.array`, `np.arange`, `np.linspace` → create arrays
* **Vectorization**: operations apply to all elements at once

  ```py
  a ** 2
  ```
* Faster than Python loops
* `np.allclose()` → compare arrays with decimals safely

---

## 🔹 2. Pandas Data Handling

* Load data:

  ```py
  df = pd.read_csv("file.csv")
  ```
* Select column:

  ```py
  df["age"]
  ```
* Filter rows:

  ```py
  df[df["age"] < 16]
  ```

---

## 🔹 3. Grouping & Aggregation

* `groupby()` → split data into groups
* `mean()` → average (also used as rate for 0/1 data)
* `agg("mean")` → aggregate with mean

Example:

```py
df.groupby("survived")["fare"].mean()
```

---

## 🔹 4. Value Counts & Most Common Value

* `value_counts()` → frequency of categories
* `idxmax()` → label with highest count

Example:

```py
df["embarked"].value_counts().idxmax()
```

---

## 🔹 5. Creating New Columns

* Use `apply()` + `lambda` for simple logic

Example:

```py
df["age_group"] = df["age"].apply(
    lambda x: "child" if x < 16 else "adult"
)
```

---

## 🔹 6. Missing Data Handling

* Fill missing values:

  ```py
  df["age"].fillna(df["age"].median(), inplace=True)
  ```
* Median is preferred when data has outliers

---

## 🔹 7. Statistics You Must Know

| Term          | Meaning            |
| ------------- | ------------------ |
| Mean          | Average            |
| Median        | Middle value       |
| Survival rate | Mean of 0/1 column |

---

## 🔹 8. Plotting

### Pandas

* Pie chart:

  ```py
  df.groupby("survived")["fare"].mean().plot.pie()
  ```

### Seaborn

* `histplot` → distribution (age, fare)
* `barplot` → compare averages

---

## 🔹 9. Titanic-Specific Columns

| Column     | Meaning                 |
| ---------- | ----------------------- |
| `survived` | 0 = died, 1 = survived  |
| `age`      | Passenger age           |
| `fare`     | Ticket price            |
| `embarked` | Boarding port (S, C, Q) |

---
