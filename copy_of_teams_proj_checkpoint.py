# -*- coding: utf-8 -*-
"""Copy of Teams proj-checkpoint.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12JCAvru8aeqQ5elqysI_XPmZ4ztYLHIh
"""

import pandas as pd

# reading the data from csv file
try:
    # Attempt to read a file
    with open("/content/sample_data/california_housing_test.csv", 'r') as file:
        content = file.read()
    print("File read successfully!")
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# to display the loaded data
dataset = pd.read_csv("/content/sample_data/california_housing_test.csv")
dataset

# importing the matpltlib library
import matplotlib.pyplot as plt

# viewing the columns
dataset.columns

# cheking for empty values
dataset.isnull().sum()

# importing seaborn
import seaborn as sns

sns.barplot(x='median_income', y='population', data=dataset, palette='coolwarm', legend = False)
plt.title('Median Income vs the population')
plt.xlabel('the median_icome')
plt.ylabel('population')
plt.show()

dataset.describe()

grouped_mean = dataset.groupby("population").mean()
grouped_mean

# plotting a line graph
sns.lineplot(x='median_income', y='population', data=dataset, palette='coolwarm')

# Customizing the plot
plt.title('Median Income vs Population')
plt.xlabel('Median Income')
plt.ylabel('Population')
plt.show()

# plotting a bar graph
# defining the lenght which is  (10, 6)
plt.figure(figsize=(10, 6))
sns.barplot(x='median_income', y='population', data=dataset, palette='coolwarm')

# Adding labels and title
plt.title('Median Income vs Population', fontsize=16)
plt.xlabel('Median Income', fontsize=12)
plt.ylabel('Population', fontsize=12)

# Rotating x-axis labels if needed
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()  # Ensures labels/titles fit within the figure
plt.show()

# drwaing a histigram to show the realtionship between the population and median income columns
plt.figure(figsize=(10, 6))
sns.histplot(dataset['median_income'], bins=20, kde=True, color='blue', edgecolor='black')

# Adding labels and title
plt.title('Distribution of Median Income', fontsize=16)
plt.xlabel('Median Income', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Show plot
plt.tight_layout()
plt.show()

# plotting a scatter plotter for my data to visualize the realtionship between the income and the populatiomn
plt.figure(figsize=(10, 6))
sns.scatterplot(x='median_income', y='population', data=dataset, color='purple', alpha=0.7)

# Adding labels and title
plt.title('Scatter Plot: Median Income vs Population', fontsize=16)
plt.xlabel('Median Income', fontsize=12)
plt.ylabel('Population', fontsize=12)

# Showing the plot
plt.tight_layout()
plt.show()

