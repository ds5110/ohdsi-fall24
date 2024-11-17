from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# create connection and read configuration.
con, work_schema = config()
table_read = "stroke_cohort_w_aphasia"
table_write = "stroke_cohort_w_aphasia_TRUE"
query = f"""
SELECT *
INTO {work_schema}.{table_write}
FROM {work_schema}.{table_read}
WHERE has_aphasia=1
;
"""
run_query(con, query)
