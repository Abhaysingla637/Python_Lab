import pandas as pd

# Taking file name from user
file_name = "D:\\crime.csv"

# Reading the CSV file
df = pd.read_csv(file_name)

# Display basic information
print("\nCSV File Information")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nSummary Statistics")
print(df.describe(include="all"))

# Filtering
column = input("\nEnter column name for filtering: ")

if column in df.columns:
    value = input("Enter value to filter: ")

    filtered_df = df[df[column].astype(str) == value]

    print("\nFiltered Data")
    print(filtered_df)

    # Export filtered data
    output_file = "D:\\output.csv"
    filtered_df.to_csv(output_file, index=False)

    print("Filtered data saved successfully.")

else:
    print("Column not found.")