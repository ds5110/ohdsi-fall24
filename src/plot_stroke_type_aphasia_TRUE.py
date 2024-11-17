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
fig, ax = plt.subplots(2, 1, figsize=(10, 10))
sns.histplot(data=df, x="ancestor_concept_id", ax=ax[0])
sns.histplot(data=df, x="ancestor_concept_id", ax=ax[1])
ax[1].set_yscale("log")
fig.suptitle("7 stroke types for stroke cohorts with aphasia")
plt.savefig("figs/stroke_type_aphasia_TRUE.png", bbox_inches="tight")
plt.tight_layout()
plt.show()
