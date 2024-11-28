from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import discharge_to_concept_id
import numpy as np


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "concept"
work_table = "stroke_cohort_w_aphasia_co_vo"
query = f"""
SELECT *
FROM {work_schema}.{work_table}
WHERE has_aphasia = 1
;
"""
# run_query(con, query)
df = read_df(con, query)

# create copy of discharge_to column
df["discharge_grouped"] = df["discharge_to_concept_id"].copy()

# print(df.info())
df["discharge_to_concept_id"] = df["discharge_to_concept_id"].map(
    discharge_to_concept_id.total_id
)
first_discharge = np.sort(df["discharge_to_concept_id"].unique())
print(f"First discharge concept IDs are: {first_discharge}")
print(
    f"There are {len(first_discharge)} types of discharge types for stroke patients with aphasia"
)

# discharged grouped column mapped
df["discharge_grouped"] = df["discharge_grouped"].map(
    discharge_to_concept_id.group_mapping)

# Plot 1
plt.figure(figsize=(12,10))
sns.histplot(data=df, x="discharge_to_concept_id", color="#2292B5", shrink=0.9)
plt.xticks(rotation=90)
plt.xlabel("Discharge to Concept Id", fontsize=14, labelpad=20)
plt.ylabel("Count", fontsize=14, labelpad=20)
plt.title("First discharge paths of stroke patients with aphasia", fontsize=16, weight="bold", pad=15, loc="center")
plt.tight_layout()
plt.savefig("figs/first_discharge_aphasia_TRUE.png", bbox_inches="tight")
plt.show()


# Plot 2 - Grouped
plt.figure(figsize=(10,10))
sns.histplot(data=df, x="discharge_grouped", hue="discharge_grouped", palette="ocean", shrink=0.9)
plt.xticks(rotation=90)
plt.xlabel("Discharge_to by Categories", fontsize=14, labelpad=20)
plt.ylabel("Count", fontsize=14, labelpad=20)
plt.title("Grouped by category", fontsize=16, weight="bold", pad=15, loc="center")
plt.savefig("figs/first_discharge_aphasia_TRUE_grouped.png", bbox_inches="tight")
plt.show()

