from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import discharge_to_concept_id


con, work_schema = config()
work_table = "visit_occurrence_stroke_cohort"
work_table_result = "visit_occurrence_first_discharge"

query = f"""
SELECT *
INTO {work_schema}.{work_table_result}
FROM {work_schema}.{work_table}
WHERE (person_id, visit_concept_id)
IN
(
SELECT person_id, discharge_to_concept_id
FROM {work_schema}.stroke_cohort_w_aphasia_co_discharge
)
;
"""

run_query(con, query)
