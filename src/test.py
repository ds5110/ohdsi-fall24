from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "concept"
# work_table = "stroke_cohort_w_aphasia"
query = f"""
SELECT *
FROM {omop_schema}.{omop_table}
LIMIT 5
"""
# run_query(con, query)
df = read_df(con, query)

print(df.info())
print(df)
