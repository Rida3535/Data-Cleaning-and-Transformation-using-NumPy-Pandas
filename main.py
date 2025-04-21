# Import necessary libraries
import pandas as pd
import numpy as np

# Read data (Load the dataset)
df = pd.read_csv("StudentsPerformance.csv")

# Refer to the data warehouse (simulated by loading dataset here)
print("Initial Data Preview:\n")
print(df.head())

# Extract / Clean / Transform (ECT)
# Check for missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Rename columns for easier access
df.rename(columns={
    'math score': 'Math_scr',
    'reading score': 'Read_scr',
    'writing score': 'Write_scr',
    'race/ethnicity': 'ethnicity_grp',
    'parental level of education': 'Parent_edu_level',
    'test preparation course': 'Test_prep_crs'
}, inplace=True)

# Add a new column: average score
df['Average'] = df[['Math_scr', 'Read_scr', 'Write_scr']].mean(axis=1)

# Use NumPy and Pandas
math_mean = np.mean(df['Math_scr'])
reading_max = np.max(df['Read_scr'])
writing_min = np.min(df['Write_scr'])

print("\nStatistics:")
print(f"Math Mean: {math_mean}")
print(f"Max Reading Score: {reading_max}")
print(f"Min Writing Score: {writing_min}")

# Apply NumPy and Pandas to prepare the final dataset
filtered_df = df[df['Average'] > 70]

# Display the cleaned and filtered data
print("\nFiltered Data (Average > 70):\n")
print(filtered_df.head())

# Save the final processed dataset
filtered_df.to_csv("processed_students_data.csv", index=False)
print("\nFinal processed data saved as 'processed_students_data.csv'")
