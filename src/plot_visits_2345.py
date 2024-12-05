import matplotlib.pyplot as plt
import seaborn as sns
from utils import config, read_df, write_df, run_query
import pandas as pd
from discharge_to_concept_id import total_id
from visit_and_home_df import visit_and_home_df

# Step 1: Define the mapping function
def map_discharge_to_group(value):
    if  value.startswith("2:"):
        return "Skilled Nursing"
    elif value.startswith("3:"):
        return "Acute Care"
    elif value.startswith("4:"):
        return "Inpatient Rehab"
    elif value.startswith("5:"):
        return "Other"
    else:
        return "Unknown"

# Step 2: Load the data
visit_dataframes, at_home = visit_and_home_df()

# Access specific DataFrames
visit_2 = visit_dataframes["visit_2"]
visit_3 = visit_dataframes["visit_3"]
visit_4 = visit_dataframes["visit_4"]
visit_5 = visit_dataframes["visit_5"]

# Step 3: Apply the mapping function to each DataFrame
for visit_df in [visit_2, visit_3, visit_4, visit_5]:
    visit_df['grouped_discharge'] = visit_df['discharge_to_previous'].apply(map_discharge_to_group)

# Step 4: Define the plotting function
def plot_visit_data(df, title, ax):
    # Count the occurrences of each grouped category
    category_counts = df['grouped_discharge'].value_counts()
    
    # Define consistent order of categories
    grouped_categories = ["Skilled Nursing", "Acute Care", "Inpatient Rehab", "Other"]
    category_counts = category_counts.reindex(grouped_categories, fill_value=0)
    
    # Create the bar plot
    sns.barplot(x=category_counts.index, y=category_counts.values, palette="tab10", ax=ax)
    
    # Set title and labels
    ax.set_title(title)
    ax.set_ylabel("Number of Patients")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Step 5: Plot the data
fig, axes = plt.subplots(2, 2, figsize=(16, 12))  # 2x2 grid for 4 plots
axes = axes.flatten()

# Plot each visit's data
plot_visit_data(visit_2, "Location 2", axes[0])
plot_visit_data(visit_3, "Location 3", axes[1])
plot_visit_data(visit_4, "Location 4", axes[2])
plot_visit_data(visit_5, "Location 5", axes[3])

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
