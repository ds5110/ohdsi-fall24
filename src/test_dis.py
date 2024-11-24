from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import discharge_to_concept_id
import numpy as np

con, work_schema = config()
work_table = "stroke_cohort_w_aphasia_co_discharge"
work_table_result = "visit_occurrence_stroke_cohort"

query = f"""
SELECT DISTINCT person_id
FROM {work_schema}.{work_table}
WHERE (person_id, visit_concept_id)
IN
(
SELECT person_id, discharge_to_concept_id
FROM {work_schema}.stroke_cohort_w_aphasia_co_discharge
)
;
"""

query = f"""
SELECT DISTINCT visit_concept_id
FROM {work_schema}.visit_occurence_first_discharge
"""

df = read_df(con, query)
print(df.info())
print(df)

df["visit_concept_id"] = df["visit_concept_id"].map(discharge_to_concept_id.total_id)
first_discharge = df["visit_concept_id"].unique()
print(f"First discharge concept IDs are: {first_discharge}")
print(f"There are {len(first_discharge)} types of discharge")
