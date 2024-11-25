from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import discharge_to_concept_id
import numpy as np

con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "concept"
work_table = "speech_11_24_943"
work_table_2 = "stroke_cohort_w_aphasia"
query = f"""
SELECT DISTINCT {work_schema}.{work_table}.person_id
FROM {work_schema}.{work_table}
LEFT JOIN {work_schema}.{work_table_2}
ON {work_schema}.{work_table}.person_id
= {work_schema}.{work_table_2}.person_id
WHERE 
;
"""
# run_query(con, query)
df = read_df(con, query)
print(df.info())
print(len(df["person_id"].unique()))
col = "condition_concept_id"
df[col] = df[col].astype(str)
first_discharge = df[col].unique()
print(f"First discharge concept IDs are: {first_discharge}")
print(f"There are {len(first_discharge)} types of discharge")

# Plot.
fig, ax = plt.subplots()
sns.histplot(data=df, x=col, shrink=0.9)
ax.tick_params(axis="x", rotation=90)
plt.tight_layout()
plt.show()
