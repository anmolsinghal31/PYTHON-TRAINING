import pandas as pd

# 1. Setup the initial DataFrame based on your screenshot
data = {
    'Employee': ['John', 'Alice', 'Bob', 'Eva', 'Mark'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Salary': [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

# --- TASK 1: Filter all employees from the "IT" department ---
it_employees = df[df['Department'] == 'IT']

# --- TASK 2: Find the average salary per department ---
# We group by Department and calculate the mean of the Salary column
avg_salary_dept = df.groupby('Department')['Salary'].mean()

# --- TASK 3: Add a new column "Salary_Adjusted" (10% increase) ---
# Formula: Original Salary * 1.10
df['Salary_Adjusted'] = df['Salary'] * 1.10

# --- Print Results ---
print("1. IT Employees:")
print(it_employees)

print("\n2. Average Salary per Department:")
print(avg_salary_dept)

print("\n3. Updated DataFrame with Adjusted Salary:")
print(df)