from utils import config, read_df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

con, work_schema = config()
table = "stroke_cohort_w_aphasia"
omop_schema = "omop_cdm_53_pmtx_202203"


query = f"""
SELECT *
FROM {omop_schema}.visit_detail AS visit_detail
INNER JOIN {work_schema}.{table} AS aphasia
on visit_detail.person_id = aphasia.person_id
;
"""
df = read_df(con, query)

print(df.info())
print(df["care_site_id"].unique())
print(len(df["care_site_id"].unique()))



query = f"""
SELECT *
FROM {omop_schema}.visit_occurrence AS visit_occurrence
INNER JOIN {work_schema}.{table} AS aphasia
on visit_occurrence.person_id = aphasia.person_id
;
"""

con, work_schema = config()
df = read_df(con, query)

print(df.info())
print(df["care_site_id"].unique())
print(len(df["care_site_id"].unique()))



# care-site non-null
# provider: 0
# visit_detail: 193/2000
# visit_occurrence: 272/2000
# person: 0
# ------------------------
# location non-null
# care_site: 0
# person: 1914/2000

# 7584 care_site_id from visit detail.  2333343 entries total
# 