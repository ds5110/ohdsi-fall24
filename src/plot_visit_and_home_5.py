from utils import config, read_df, write_df, run_query
import pandas as pd
from discharge_to_concept_id import total_id
import discharge_to_concept_id
from visit_and_home_df import visit_and_home_df
import seaborn as sns
import matplotlib.pyplot as plt

visit_dataframes, at_home = visit_and_home_df()

# Iterate through visit_n DataFrames
for name, df in visit_dataframes.items():
    print(f"DataFrame: {name}")
    print(df.head())
    print(f"Shape: {df.shape}")
    print(f"Info: {df.info}")

# Check the at_home DataFrame
print("At Home DataFrame:")
print(at_home.head())
print(f"Shape: {df.shape}")
print(f"Info: {df.info}")
print(f"T")


# create copy of visit_dataframe
visit_df_copy = visit_dataframes.copy()

#add visit_num column
for name, df in visit_df_copy.items():
    df['visit_num'] = name
    #df["discharge_grouped"] = df["discharge_to_concept_id"].map(
    #discharge_to_concept_id.group_mapping)

combined_df = pd.concat(visit_df_copy.values(), ignore_index=True)

visit = sns.FacetGrid(combined_df, col="visit_num", height=5.0, aspect=2.0, hue="visit_num", palette="ocean")
visit.map_dataframe(sns.histplot, x="discharge_to_concept_id", binwidth=3)
visit.figure.suptitle("Distribution of discharge groups by discharge number", fontsize=12, y=1.0)
visit.set_titles(col_template="{col_name}", row_template="{row_name}")
for ax in visit.axes.flat:
    ax.set_yscale('log'),
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
visit.tight_layout()
plt.savefig("figs/discharge_5_plots.png")
plt.show()

# countplot - needs works
visit_bar_plot = sns.FacetGrid(combined_df, col="visit_num", hue="visit_num")
visit_bar_plot.map_dataframe(sns.countplot, x="discharge_to_concept_id")
plt.savefig("figs/discharge_5_plots_countplot.png")
plt.show()
