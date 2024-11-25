from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "procedure_occurrence"
work_table = "stroke_cohort_w_aphasia"
work_table_2 = "speech_11_24_943"
work_table_result = "speech_stroke_cohort"
query = f"""
SELECT *
INTO {work_schema}.{work_table_result}
FROM {work_schema}.{work_table_2}
WHERE person_id
IN
(
SELECT person_id
FROM {work_schema}.{work_table}
);
"""
run_query(con, query)
