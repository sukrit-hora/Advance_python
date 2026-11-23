import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create Employee DataFrame
data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohit',
             'Neha', 'Vikas', 'Pooja', 'Anjali', 'Karan'],
    'Age': [25, 30, 28, 35, 27, 32, 40, 26, 29, 31],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR',
                   'IT', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [30000, 40000, 35000, 50000, 45000,
               38000, 60000, 32000, 42000, 200000]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

# 2. Calculate Mean, Median and Standard Deviation
mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()
std_salary = df['Salary'].std()

print("\nMean Salary:", mean_salary)
print("Median Salary:", median_salary)
print("Standard Deviation:", std_salary)

# 3. Detect and Remove Outliers using IQR
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Detect Outliers
outliers = df[(df['Salary'] < lower_limit) |
              (df['Salary'] > upper_limit)]

print("\nOutliers:")
print(outliers)

# Remove Outliers
df_clean = df[(df['Salary'] >= lower_limit) &
              (df['Salary'] <= upper_limit)]

print("\nData After Removing Outliers:")
print(df_clean)

# 4. Plot Salary Distribution

# Boxplot
plt.figure(figsize=(6, 4))
plt.boxplot(df_clean['Salary'])
plt.title("Salary Boxplot")
plt.ylabel("Salary")
plt.show()

# Histogram
plt.figure(figsize=(6, 4))
plt.hist(df_clean['Salary'], bins=5, edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()