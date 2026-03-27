import pandas as pd
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],

    'Age': [25, 30, 35, 40, 45],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df.head())  # Display the first few rows of the DataFrame
print("\nDataFrame Info:")
print(df.info())  # Display information about the DataFrame
print("\nDataFrame Description:")   
print(df.describe())  # Display statistical summary of the DataFrame
# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]    
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)  # Display the filtered DataFrame


read_csv = pd.read_csv('dataset/Dataset.csv')  # Read a CSV file into a DataFrame
print("\nDataFrame from CSV:")  
print(read_csv.head())  # Display the first few rows of the DataFrame from CSV

Read_pass = read_csv[read_csv['Result'] == 'Pass']  # Filter rows where 'Result' is 'Pass'
print("\nFiltered DataFrame (Result == 'Pass'):")
print(Read_pass)  # Display the filtered DataFrame where 'Result' is 'Pass'