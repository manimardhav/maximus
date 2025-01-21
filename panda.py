import pandas as pd

# Sample data for sales transactions and customer information
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}
customer_data = {
    'CustomerID': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Convert data into DataFrame
sales_df = pd.DataFrame(sales_data)
customers_df = pd.DataFrame(customer_data)

# Display Amount and Date from sales data
print("Sales Data - Amount and Date:")
print(sales_df[['Amount', 'Date']])

# Display Customer name and city from customer data
print("\nCustomer Data - Customer Name and City:")
print(customers_df[['CustomerName', 'City']])

# Display customer ids where Amount > 400
filtered_sales_df = sales_df[sales_df['Amount'] > 400]
print("\nCustomer IDs with Amount > 400:")
print(filtered_sales_df['CustomerID'])

# Show basic structure of sales_df
print("\nSales DataFrame:")
print(sales_df.head())

# Exploring the dataset (using shape and describe)
print("\nShape of sales data:", sales_df.shape)  # Get number of rows and columns
print("\nSales data statistics:")
print(sales_df.describe())  # Summary statistics


# 2. Merging data (Sales with Customer info)
merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)


# 2. Merging data (Sales with Customer info)
merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)

# 3. Accessing data using `loc` and `iloc`
print("\nAccess data using `loc` (row 1):")
print(merged_df.loc[1])

print("\nAccess data using `iloc` (row 2):")
print(merged_df.iloc[2])

# 4. Handling Missing Values
# Let's introduce some missing data for demonstration
merged_df.loc[2, 'Age'] = None  # Introduce missing value in Age column
print(merged_df)
# Check for missing values
print("\nCheck missing values (isnull):")
print(merged_df.isnull().sum())

# Fill missing values with the mean (for Age column)
merged_df['Age'].fillna(merged_df['Age'].mean(), inplace=True)
print("\nData after filling missing values:")
print(merged_df)

# 5. Aggregation: Calculate the mean sales per customer
mean_sales = merged_df.groupby('CustomerName')['Amount'].mean()
print("\nMean sales per customer:")
print(mean_sales)


# Create a Dataframe for Patient Information  and include column names as below
#1)Patient Name
#2) Age
#3) Date of oppointment
#4) Patient id
#Create a dataframe name as drag_quantity that includes column names as  drag name,quantity,patient_id
# Filter dataframe  to get Patient name and age <6

#Merge the dataframes with inner join of Patient information and drag quantity dataframe

import pandas as pd

# Create DataFrame for Patient Information
patient_data = {
    'PatientName': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
    'Age': [5, 8, 3, 7, 4],
    'DateOfAppointment': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
    'PatientID': [101, 102, 103, 104, 105]
}
patients_df = pd.DataFrame(patient_data)

# Create DataFrame for Drug Quantity
drug_quantity_data = {
    'DrugName': ['Aspirin', 'Paracetamol', 'Ibuprofen', 'Aspirin', 'Paracetamol'],
    'Quantity': [2, 3, 1, 5, 2],
    'PatientID': [101, 102, 103, 104, 105]
}
drug_quantity_df = pd.DataFrame(drug_quantity_data)

# Display the original DataFrames
print("Patient DataFrame:")
print(patients_df)

print("\nDrug Quantity DataFrame:")
print(drug_quantity_df)

# Filter Patient DataFrame where Age < 6
filtered_patients_df = patients_df[patients_df['Age'] < 6]
print("\nFiltered Patient DataFrame (Age < 6):")
print(filtered_patients_df)

# Merge the DataFrames using an inner join on 'PatientID'
merged_df = pd.merge(filtered_patients_df, drug_quantity_df, on='PatientID', how='inner')

print("\nMerged DataFrame (Inner Join on PatientID):")
print(merged_df)


