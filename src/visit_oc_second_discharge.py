from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
work_table = "visit_occurrence_discharge"
work_table_result = "visit_occurrence_second_discharge"
query = f"""
WITH discharge_order AS
(
SELECT *,
ROW_NUMBER() OVER
 (
 PARTITION BY person_id
 ORDER BY visit_start_date ASC
 ) AS row_number
FROM {work_schema}.{work_table}
)
SELECT *
INTO {work_schema}.{work_table_result}
FROM discharge_order
WHERE row_number = 2
;
"""
run_query(con, query)
