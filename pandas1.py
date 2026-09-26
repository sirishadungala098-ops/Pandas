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
result = df[df["Salary"] > 30000] 
print(result)
result = df[ (df["Salary"] > 30000) & (df["Department"] == "IT") ]                  
print(result) 
result = df[df["City"].isin(["Hyderabad", "Chennai"])] 
print(result) 
print(df["Department"].value_counts()) 
df.drop("Age",axis=1, inplace=True)
print(df)
