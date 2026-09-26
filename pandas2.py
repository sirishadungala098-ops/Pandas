import pandas as pd 
data = { 
    "Name": ["Vyshu", "Ramya", "Karthika", "Sita", "Raghu"],
    "Age": [22, 25, 21, 24, 27],
    "City": ["Rajahmundry", "Hyderabad", "Chennai", "Rajahmundry", "Hyderabad"], 
    "Salary": [25000, 45000, 30000, 35000, 55000], 
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
     }
df = pd.DataFrame(data) 
print(df) 
df.rename(columns={"Salary":"Employee Salary"}, inplace=True)
print(df)

df.rename(columns={"Name":"Employee Name"}, inplace=True)
print(df)
print(df.isnull()) 
print(df.isnull().sum())
print(df.loc[0])
print(df.loc[0:2])
print(df.iloc[0])
print(df.fillna(0))