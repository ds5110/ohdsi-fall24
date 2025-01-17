from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Establish connection and schema details
con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "procedure_occurrence"
work_table = "stroke_cohort_w_aphasia"

# Create the SQL query
query = f"""
SELECT
    sc.person_id,
    COUNT(po.visit_occurrence_id) AS total_visits,
    MIN(po.procedure_date) AS first_procedure_date,
    MAX(po.procedure_date) AS last_procedure_date
INTO {work_schema}.cohort_aphasia_speech_therapy
FROM {work_schema}.{work_table} sc
JOIN {omop_schema}.{omop_table} po
    ON sc.person_id = po.person_id
WHERE po.procedure_source_concept_id IN (2313701, 2313702, 2313707, 44816444, 44816445, 44816446, 44816447, 2313709, 2313760, 2313767, 2313768, 2313769, 2313770, 2313773, 2313774, 2313775, 2313776, 2313777, 2313778, 2313779, 2314188, 710051, 710052)
GROUP BY sc.person_id;
"""

# Run the query
run_query(con, query)
