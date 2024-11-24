from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
work_table = "stroke_cohort_w_aphasia"
work_table_result = "stroke_cohort_w_aphasia_co"
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "condition_occurrence"

# add columns from condition occurance table on the stroke cohort table.
query = f"""
SELECT {work_schema}.{work_table}.*,
{omop_schema}.{omop_table}.visit_occurrence_id,
{omop_schema}.{omop_table}.visit_detail_id,
{omop_schema}.{omop_table}.provider_id
INTO {work_schema}.{work_table_result}
FROM {work_schema}.{work_table}
LEFT JOIN {omop_schema}.{omop_table}
ON {work_schema}.{work_table}.condition_occurrence_id
= {omop_schema}.{omop_table}.condition_occurrence_id
AND {work_schema}.{work_table}.person_id
= {omop_schema}.{omop_table}.person_id
;
"""
run_query(con, query)
