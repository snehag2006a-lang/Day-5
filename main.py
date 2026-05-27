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