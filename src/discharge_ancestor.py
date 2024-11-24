from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import discharge_to_concept_id
import numpy as np

con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "concept_ancestor"
work_table_result = "discharge_ancestor"
discharge_code = list(discharge_to_concept_id.total_id.keys())
discharge_code = ", ".join(str(x) for x in discharge_code)

query = f"""
SELECT *
INTO {work_schema}.{work_table_result}
FROM {omop_schema}.{omop_table}
WHERE ancestor_concept_id
IN ({discharge_code})
;
"""
run_query(con, query)
