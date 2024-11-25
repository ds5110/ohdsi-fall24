from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "procedure_occurrence"
work_table = "stroke_cohort_w_aphasia"
query = f"""
SELECT person_id,
       procedure_source_concept_id,
       visit_occurrence_id,
       procedure_date
INTO {work_schema}.speech_11_24_943
FROM {omop_schema}.{omop_table}
WHERE procedure_source_concept_id IN (2313701);
"""
run_query(con, query)
