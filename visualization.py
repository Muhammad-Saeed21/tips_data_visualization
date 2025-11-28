# ------------------------------------------------------------
# Data Visualization Project
# Dataset Used: Tips Dataset (Seaborn Built-in)
# Author: Muhammad Saeed
# Description: Basic visual analysis of tipping trends,
#              gender distribution, and smoking effect.
# ------------------------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------
df = sns.load_dataset("tips")
print("Dataset Loaded Successfully!\n")
print(df.head())   # Display first few rows

# ------------------------------------------------------------
# Bar Chart: Average Tip Per Day
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
sns.barplot(x='day', y='tip', data=df, estimator=lambda x: sum(x)/len(x))
plt.title("Average Tip Per Day")
plt.xlabel("Day of Week")
plt.ylabel("Average Tip Amount")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Pie Chart: Gender Distribution
# ------------------------------------------------------------
gender_counts = df['sex'].value_counts()

plt.figure(figsize=(5,5))
plt.pie(gender_counts,
        labels=gender_counts.index,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Gender Distribution of Customers")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Line Chart: Tip Trend Based on Total Bill
# ------------------------------------------------------------
df_sorted = df.sort_values("total_bill")

plt.figure(figsize=(7,4))
plt.plot(df_sorted['total_bill'], df_sorted['tip'])
plt.title("Tip Trend Based on Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Tip Amount")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Box Plot: Smokers vs Non-Smokers (Tip Comparison)
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(x='smoker', y='tip', data=df)
plt.title("Tip Comparison: Smokers vs Non-Smokers")
plt.xlabel("Smoker?")
plt.ylabel("Tip Amount")
plt.tight_layout()
plt.show()
