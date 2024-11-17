from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# create connection and read configuration.
con, work_schema = config()
table_write = "stroke_ancestor"
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "concept_ancestor"
query = f"""
SELECT *
INTO {work_schema}.{table_write}
FROM {omop_schema}.{omop_table}
WHERE ancestor_concept_id
IN (372924,375557,376713,443454,441874,439847,432923)
;
"""
# we will write all the descandant concept id from the 7 stroke codes.
run_query(con, query)
