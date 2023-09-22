import pandas as pd
import numpy as np
import random

# Define the list of categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']

# Number of entries (n)
n = 500

# Generate random data
data = {
    'Date': pd.date_range('2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the first few rows of the DataFrame
print("DataFrame Head:")
print(df.head())

# Print DataFrame Information
print("\nDataFrame Information:")
print(df.info())

# Print DataFrame Description
print("\nDataFrame Description:")
print(df.describe())

# Print the count of each 'Category' element
category_counts = df['Category'].value_counts()
print("\nCount of each 'Category' element:")
print(category_counts)
