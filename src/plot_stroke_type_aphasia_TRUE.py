from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
table_main = "stroke_cohort_w_aphasia_TRUE"
table_ancestor = "stroke_ancestor"
query = f"""
SELECT *
FROM {work_schema}.{table_main}
LEFT JOIN {work_schema}.{table_ancestor}
ON {work_schema}.{table_main}.condition_concept_id
={work_schema}.{table_ancestor}.descendant_concept_id
;
"""
# run_query(con, query)
df = read_df(con, query)

# Print info of the table.
print(df.info())

# Convert the data type to str for plotting purpose.
df["ancestor_concept_id"] = df["ancestor_concept_id"].apply(str)

# Plot.
fig, ax = plt.subplots(2, 1, figsize=(12, 15))
sns.histplot(data=df, x="ancestor_concept_id", hue="ancestor_concept_id", palette="ocean", shrink=0.9, ax=ax[0])
sns.histplot(data=df, x="ancestor_concept_id", hue="ancestor_concept_id", palette="ocean", shrink=0.9, ax=ax[1])

#plot 1 
ax[0].set_title("Regular", weight="bold", fontsize=14, pad=20)
ax[0].set_xlabel("Condition Concept Id", fontsize=14, labelpad=20)
ax[0].set_ylabel("Count", fontsize=14, labelpad=15)

#plot 2 - log 
ax[1].set_yscale("log")
ax[1].set_title("Log", weight="bold", fontsize=14, pad=15)
ax[1].set_xlabel("Condition Concept Id", fontsize=14, labelpad=20)
ax[1].set_ylabel("Count", fontsize=14, labelpad=15)

#plot - all 
ax[1].set_yscale("log")
fig.suptitle("7 Stroke Types for Stroke Cohort with Aphasia", fontsize=16, weight="heavy")
plt.subplots_adjust(bottom=0.1, hspace=0.9)

plt.savefig("figs/stroke_type_aphasia_TRUE.png", bbox_inches="tight")
plt.show()
