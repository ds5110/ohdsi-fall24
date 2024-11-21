from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# create connection and read configuration.
con, work_schema = config()
#table_read = "stroke_cohort_w_aphasia"
#table_write = "Alex_first_discharge_table"

query = f"""
create table {work_schema}.intermed_table_1 as 
select co.person_id, co.condition_occurrence_id, co.condition_concept_id, co.visit_occurrence_id, vo.visit_end_date, vo.discharge_to_concept_id 
from omop_cdm_53_pmtx_202203.condition_occurrence co 
join omop_cdm_53_pmtx_202203.visit_occurrence vo  
on co.visit_occurrence_id = vo.visit_occurrence_id
where co.person_id = vo.person_id
and co.condition_occurrence_id in 
(select co2.condition_occurrence_id from omop_cdm_53_pmtx_202203.condition_occurrence co2
inner join work_corcoran_al215.stroke_cohort_w_aphasia scwa 
on scwa.condition_occurrence_id = co2.condition_occurrence_id 
)
order by co.person_id;
"""
'''query = f"""select co.person_id, co.condition_occurrence_id, co.condition_concept_id, co.visit_occurrence_id, vo.visit_end_date, vo.discharge_to_concept_id 
into {work_schema}.discharge1_inter_table
from omop_cdm_53_pmtx_202203.condition_occurrence co 
join omop_cdm_53_pmtx_202203.visit_occurrence vo  
on co.visit_occurrence_id = vo.visit_occurrence_id
where co.person_id = vo.person_id;
"""'''

'''query = f"""
SELECT co.person_id, co.condition_occurrence_id, vo.visit_occurrence_id, vo.discharge_to_concept_id 
INTO {work_schema}.{table_write}
FROM omop_cdm_53_pmtx_202203.condition_occurrence co 
INNER JOIN omop_cdm_53_pmtx_202203.visit_occurrence vo 
ON co.visit_occurrence_id = vo.visit_occurrence_id
WHERE co.condition_occurrence_id in
(SELECT co2.condition_occurrence_id FROM omop_cdm_53_pmtx_202203.condition_occurrence co2
INNER JOIN work_corcoran_al215.stroke_cohort_w_aphasia scwa
ON scwa.condition_occurrence_id = co2.condition_occurrence_id 
)
ORDER BY co.person_id;
"""'''
run_query(con, query)