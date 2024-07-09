import pandas as pd

# Create a sample dictionary
data = {
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Tom'],
    'Age': [30, 25, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [50000, 60000, 45000, 55000, 65000]
}

# Create the DataFrame from the dictionary
df = pd.DataFrame(data)

balue = "City"
def update_salary(row):
    row["Salary"] = row["Salary"] + 10000
    return row

df = df.apply(update_salary, axis=1)

print(df)