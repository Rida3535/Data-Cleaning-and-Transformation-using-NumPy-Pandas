# Data Warehousing & Mining Assignment

## 📌 Title: Data Cleaning and Transformation using NumPy & Pandas

**Student Name:** Rida Naseer  
**Course:** Data Warehousing & Mining  
**Instructor:** Dr. Khalid Jamal  
**Date:** April 2025

---

## 🎯 Objective

The goal of this assignment is to extract a dataset of 1000+ records, clean and transform it using Python libraries (`NumPy` and `Pandas`), and prepare the data for loading into a Data Warehouse.

---

## 🧰 Tools & Libraries Used

- **Python 3.x**
- **NumPy** – for numerical computations
- **Pandas** – for data analysis and manipulation
- *(Optional)* Matplotlib & Seaborn – for data visualization

---

## 📂 Dataset Details

- **Source:** Students Performance Dataset  
- **Format:** CSV  
- **Total Records:** 1000+

---

## 🔄 Steps Performed

### ✅ Step 1: Reading the Dataset

```python
import pandas as pd
import numpy as np

df = pd.read_csv("StudentsPerformance.csv")
print(df.head())
```

---

### ✅ Step 2: Checking for Missing Values

```python
print(df.isnull().sum())
```

**Result:** No missing values were found in the dataset.

---

### ✅ Step 3: Descriptive Statistics using NumPy

```python
math_mean = np.mean(df['math score'])
reading_max = np.max(df['reading score'])
writing_min = np.min(df['writing score'])

print("Math Mean:", math_mean)
print("Max Reading Score:", reading_max)
print("Min Writing Score:", writing_min)
```

**Results:**
- Math Mean: `66.089`
- Max Reading Score: `100`
- Min Writing Score: `10`

---

### ✅ Step 4: Data Cleaning & Transformation

Created a new column `Average` by calculating the mean of the three scores:

```python
df['Average'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
```

Filtered students with an average score greater than 70:

```python
filtered_df = df[df['Average'] > 70]
```

---

### ✅ Step 5: Exporting Processed Data

Saved the cleaned data into a new CSV file:

```python
filtered_df.to_csv("processed_students_data.csv", index=False)
```

---

### ✅ Role of Pandas & NumPy

- **Pandas** helped in loading, manipulating, and saving the data.
- **NumPy** was used for statistical calculations like mean, max, and min.

---

## ✅ Final Output

The processed data is stored in:
```
processed_students_data.csv
```

This data is cleaned and transformed, ready to be loaded into a Data Warehouse.

---

---

## 📌 Conclusion

This assignment demonstrates how we can clean and process raw data using Python libraries and prepare it for data warehousing and mining purposes.
