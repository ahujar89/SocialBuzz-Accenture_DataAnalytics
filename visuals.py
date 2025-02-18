import pandas as pd

# Load the cleaned dataset
file_path = "Task 3_Final Content Data set.csv"
df = pd.read_csv(file_path)

# Display first few rows
df.head()

# Count the unique categories
num_unique_categories = df["Category"].nunique()
print(f"Total Unique Categories: {num_unique_categories}")

# Group by category and sum reaction scores
category_reactions = df.groupby("Category")["Score"].sum().reset_index()

# Find the most popular category
most_popular_category = category_reactions.sort_values(by="Score", ascending=False).iloc[0]
print(f"Most Popular Category: {most_popular_category['Category']} with {most_popular_category['Score']} reactions")

# Convert 'Datetime' to datetime format
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Extract month name
df["Month"] = df["Datetime"].dt.month_name()

# Count posts per month
monthly_posts = df["Month"].value_counts()
print("Month with Most Posts:", monthly_posts.idxmax(), "with", monthly_posts.max(), "posts")

import matplotlib.pyplot as plt
import seaborn as sns

# Get top 5 categories
top_5_categories = category_reactions.sort_values(by="Score", ascending=False).head(5)

# Plot Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(top_5_categories["Score"], labels=top_5_categories["Category"], autopct="%1.1f%%", startangle=140)
plt.title("Top 5 Content Categories by Popularity")
plt.show()

# Plot Bar Chart
plt.figure(figsize=(10, 5))
sns.barplot(x="Score", y="Category", data=top_5_categories, palette="viridis")
plt.xlabel("Total Reaction Score")
plt.ylabel("Category")
plt.title("Top 5 Most Popular Content Categories")
plt.show()

# Plot posts by month
plt.figure(figsize=(10, 5))
sns.barplot(x=monthly_posts.index, y=monthly_posts.values, palette="coolwarm")
plt.xlabel("Month")
plt.ylabel("Number of Posts")
plt.title("Posts Per Month")
plt.xticks(rotation=45)
plt.show()