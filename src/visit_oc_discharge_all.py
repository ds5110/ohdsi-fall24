from utils import config, read_df, write_df, run_query
import pandas as pd
from discharge_to_concept_id import total_id

# Configurations
con, work_schema = config()
work_table = "visit_occurrence_stroke_cohort"
filter_table = "stroke_cohort_w_aphasia"
table_result = "visit_occurrence_discharge_all"

# SQL Query to fetch filtered visit occurrences
query = f"""
SELECT v.person_id, 
       v.visit_start_date,
       v.visit_source_concept_id,
       v.visit_end_date, 
       v.discharge_to_concept_id,
       f.condition_start_date
INTO {work_schema}.{table_result}
FROM {work_schema}.{work_table} v
LEFT JOIN {work_schema}.{filter_table} f
ON v.person_id = f.person_id
WHERE v.visit_end_date > f.condition_start_date;
"""

run_query(con, query)
