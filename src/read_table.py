from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "concept"
print("Enter the table to read info: ")
work_table = input()
query = f"""
SELECT *
FROM {work_schema}.{work_table}
;
"""
df = read_df(con, query)
print(df.info())
print(df)
