from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import discharge_to_concept_id


con, work_schema = config()
work_table = "condition_occurrence_stroke_cohort"
work_table_2 = "stroke_cohort_w_aphasia_co_vo"
work_table_result = "condition_occurrence_discharge"

query = f"""
SELECT {work_schema}.{work_table}.*
INTO {work_schema}.{work_table_result}
FROM {work_schema}.{work_table}
LEFT JOIN {work_schema}.{work_table_2}
ON {work_schema}.{work_table}.person_id
= {work_schema}.{work_table_2}.person_id
WHERE {work_schema}.{work_table}.condition_start_date
> {work_schema}.{work_table_2}.condition_start_date
;
"""

run_query(con, query)
