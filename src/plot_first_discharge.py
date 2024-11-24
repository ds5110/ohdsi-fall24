from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import discharge_to_concept_id
import numpy as np


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "concept"
work_table = "stroke_cohort_w_aphasia_co_discharge"
query = f"""
SELECT *
FROM {work_schema}.{work_table}
;
"""
# run_query(con, query)
df = read_df(con, query)
print(df.info())
df["discharge_to_concept_id"] = df["discharge_to_concept_id"].map(
    discharge_to_concept_id.total_id
)
first_discharge = np.sort(df["discharge_to_concept_id"].unique())
print(f"First discharge concept IDs are: {first_discharge}")
print(f"There are {len(first_discharge)} types of discharge")

# Plot.
fig, ax = plt.subplots()
sns.histplot(data=df, x="discharge_to_concept_id", shrink=0.9)
ax.tick_params(axis="x", rotation=90)
plt.tight_layout()
plt.savefig("figs/first_discharge.png")
plt.show()
