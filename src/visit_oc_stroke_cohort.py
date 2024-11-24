from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import discharge_to_concept_id


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "visit_occurrence"
discharge_code = list(discharge_to_concept_id.total_id.keys())
discharge_code = ", ".join(str(x) for x in discharge_code)

# create visit_occurrence table with only stroke cohorts with discharge.
query = f"""
SELECT *
INTO {work_schema}.visit_occurrence_stroke_cohort
FROM {omop_schema}.{omop_table}
WHERE person_id
IN
(
SELECT person_id
FROM {work_schema}.stroke_cohort_w_aphasia
)
;
"""

run_query(con, query)
