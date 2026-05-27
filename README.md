# Day-5
Data cleaning and pandas fundamentals assignment.
Python Pandas Assignment – Data Type Column Selection

Assignment Details

- Course: Python with Pandas
- Topic: Selecting Columns by Data Type
- Student Name: Your Name
- Assignment No: 1
- Date: May 2026

---

Introduction

In data analysis, datasets usually contain different types of data such as numbers, text, and boolean values. Before performing analysis, it is important to separate columns based on their data types.

Python’s Pandas library provides the "select_dtypes()" method, which helps users filter DataFrame columns according to their data types quickly and efficiently.

---

Objective

The objectives of this assignment are:

1. To understand DataFrame data types.
2. To learn the usage of "select_dtypes()".
3. To filter numeric, object, and boolean columns.
4. To practice data preprocessing using Pandas.

---

About select_dtypes()

The "select_dtypes()" method is used to select columns from a DataFrame based on their datatype.

Syntax

df.select_dtypes(include=None, exclude=None)

Parameters

- include → Selects specified data types.
- exclude → Removes specified data types.

---

Program

import pandas as pd

data = {
    'Name': ['Asha', 'Ravi', 'Kiran', 'Neha'],
    'Age': [21, 24, 22, 23],
    'Marks': [88.5, 76.0, 91.5, 85.0],
    'Passed': [True, True, True, True]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nNumeric Columns:")
print(df.select_dtypes(include='number'))

print("\nObject Columns:")
print(df.select_dtypes(include='object'))

print("\nBoolean Columns:")
print(df.select_dtypes(include='bool'))

print("\nNon Numeric Columns:")
print(df.select_dtypes(exclude='number'))

---

Output

Numeric Columns

- Age
- Marks

Object Columns

- Name

Boolean Columns

- Passed

---

Real-Time Usage

"select_dtypes()" is useful in:

- Data cleaning
- Machine learning preprocessing
- Filtering numeric columns for calculations
- Selecting text columns for encoding

---

Advantages

1. Easy to use
2. Saves time
3. Reduces coding complexity
4. Improves readability

---

How to Run

Install pandas:

pip install pandas

Run the program:

python main.py

---

Conclusion

The "select_dtypes()" method is very helpful for selecting DataFrame columns based on datatype. It makes data preprocessing easier, faster, and more organized in Python Pandas.
