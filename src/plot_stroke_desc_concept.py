from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
table = "stroke_cohort_w_aphasia"

# SQL query.
query = f"""
SELECT *
FROM {work_schema}.{table}
;
"""

# Convert the table read by the SQL query as a pandas dataframe.
df = read_df(con, query)

# Print info of the table.
print(df.info())

# Print distinct condition_concept_id.
print(
    f"Descendant concept ID in the stroke cohort is: \n{df['condition_concept_id'].unique()}"
)

# Convert the data type to str for plotting purpose.
df["condition_concept_id"] = df["condition_concept_id"].apply(str)

# Plot.
fig, ax = plt.subplots(2, 1, figsize=(12, 22))
sns.histplot(data=df, x="condition_concept_id", color="#2292B5", legend=False, ax=ax[0])
sns.histplot(data=df, x="condition_concept_id", color="#00246D", legend=False, ax=ax[1])

#plot 1 - reg
ax[0].tick_params(axis="x", rotation=90)
ax[0].set_title("Descendant Concept Id of the Stroke Cohort", weight="bold", pad=15)
ax[0].set_xlabel("Condition Concept Id", fontsize=12, labelpad=20)
ax[0].set_ylabel("Count", fontsize=12, labelpad=15)

#plot 2 - log
ax[1].set_title("Descendant Concept Id of the Stroke Cohort - Log", weight="bold", pad=15)
ax[1].tick_params(axis="x", rotation=90)
ax[1].set_xlabel("Condition Concept Id", fontsize=12, labelpad=20)
ax[1].set_ylabel("Count", fontsize=12, labelpad=15)
ax[1].set_yscale("log")

#plot - all 
plt.subplots_adjust(bottom=0.2, hspace=1)
plt.savefig("figs/stroke_desc_concept_id.png", bbox_inches="tight")
plt.show()
