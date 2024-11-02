from utils import config, run_query

con, work_schema = config()

query = f"""
--creating an intermediate table for all condition occurrences that match the stroke-related concept ids for inpatient visits
select co.condition_occurrence_id, co.person_id, co.condition_concept_id, co.condition_start_date, co.condition_end_date
into {work_schema}.inpatient_stroke --write a table name from your personal schema
from omop_cdm_53_pmtx_202203.condition_occurrence co
inner join omop_cdm_53_pmtx_202203.visit_occurrence vo 
on co.visit_occurrence_id = vo.visit_occurrence_id
where vo.visit_concept_id IN 
(
select ca.descendant_concept_id from omop_cdm_53_pmtx_202203.concept_ancestor ca 
inner join omop_cdm_53_pmtx_202203.concept c on 
ca.descendant_concept_id = c.concept_id 
where ancestor_concept_id IN (9201, 9203, 262) -- inpatient visit codes and all descendants
)
and co.condition_concept_id in 
(
select ca.descendant_concept_id from omop_cdm_53_pmtx_202203.concept_ancestor ca 
inner join omop_cdm_53_pmtx_202203.concept c on 
ca.descendant_concept_id = c.concept_id 
where ancestor_concept_id IN (372924,375557,376713,443454,441874,439847,432923) -- stroke occurrence codes and all descendants
);
"""

run_query(con, query)
