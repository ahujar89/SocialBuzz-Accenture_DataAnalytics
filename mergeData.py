import pandas as pd

# Loading datasets
content_df = pd.read_csv("Content.csv")
reactions_df = pd.read_csv("Reactions.csv")
reaction_types_df = pd.read_csv("ReactionTypes.csv")

# Dropping unnecessary columns
content_df = content_df.drop(columns=["Unnamed: 0", "Unnamed: 2"], errors="ignore")
reactions_df = reactions_df.drop(columns=["Unnamed: 0", "Unnamed: 2"], errors="ignore")
reaction_types_df = reaction_types_df.drop(columns=["Unnamed: 0"], errors="ignore")

# Merging reactions with content to add category information
merged_df = reactions_df.merge(content_df, on="Content ID", how="left")

# Merging with reaction types to get popularity scores
final_df = merged_df.merge(reaction_types_df, left_on="Reaction Type", right_on="Reaction Type", how="left")

# Dropping the redundant "Type" column from ReactionTypes
final_df = final_df.drop(columns=["Reaction Type"])

# Saving the final merged dataset
final_df.to_csv("final_merged_dataset.csv", index=False)

# Grouping by category and sum the scores
category_scores = final_df.groupby("Category")["Score"].sum().reset_index()

# Sorting to get top 5
top_5_categories = category_scores.sort_values(by="Score", ascending=False).head(5)

# Displaying the results
print(top_5_categories)