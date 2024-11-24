from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
work_table = "stroke_cohort_w_aphasia_co"
work_table_2 = "visit_occurrence_stroke_cohort"
work_table_result = "stroke_cohort_w_aphasia_co_discharge"
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "condition_occurrence"

query = f"""
SELECT {work_schema}.{work_table}.*,
{work_schema}.{work_table_2}.discharge_to_concept_id
INTO {work_schema}.{work_table_result}
FROM {work_schema}.{work_table}
LEFT JOIN {work_schema}.{work_table_2}
ON {work_schema}.{work_table}.visit_occurrence_id
= {work_schema}.{work_table_2}.visit_occurrence_id
;
"""
run_query(con, query)
