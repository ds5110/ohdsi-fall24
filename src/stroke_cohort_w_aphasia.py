from utils import config, run_query

con, work_schema = config()

# This SQL query belongs to Casey Tilton.
query = f"""
-- creating a cohort with aphasia indicator
with first_stroke_occurrence as 
(
  -- Select all stroke occurrences and assign row numbers for each person based on the condition_start_date
  select condition_occurrence_id, 
         person_id, 
         condition_concept_id, 
         condition_start_date, 
         condition_end_date, 
         row_number() over(partition by person_id order by condition_start_date asc) as row_num
  from {work_schema}.inpatient_stroke
),
distinct_stroke_occurrence as 
(
  -- Select distinct stroke occurrences by condition_start_date and rank them
  select condition_occurrence_id, 
         person_id, 
         condition_concept_id, 
         condition_start_date, 
         condition_end_date, 
         dense_rank() over(partition by person_id order by condition_start_date asc) as distinct_rank
  from first_stroke_occurrence
),
multiple_stroke_occurrence as
(
  -- Select person_ids with more than one distinct occurrence within 180 days// can use SELECT DISTINCT
  select f1.person_id
  from distinct_stroke_occurrence f1
  join distinct_stroke_occurrence f2 -- probably need to delete join, and replace it with a (,)
    on f1.person_id = f2.person_id 
   and f1.distinct_rank = 1  -- First distinct stroke// should this be after where command?
   and f2.distinct_rank = 2  -- Second distinct stroke// should this be after where command?
  where datediff(day, f1.condition_start_date, f2.condition_start_date) <= 180
  group by f1.person_id
),
stroke_cohort as
(
  -- Select first stroke occurrence and filter based on observation period
  select f.*, 
         op.observation_period_start_date, 
         op.observation_period_end_date, 
         op.observation_period_id 
  from first_stroke_occurrence f
  inner join omop_cdm_53_pmtx_202203.observation_period op 
    on op.person_id = f.person_id
  where f.person_id in (select person_id from multiple_stroke_occurrence)
    and f.row_num = 1  -- Select only the first stroke occurrence for each person
    and f.condition_start_date >= dateadd(day, 180, op.observation_period_start_date)
    and op.observation_period_end_date >= dateadd(day, 180, f.condition_start_date)
),
aphasia_occurrence as
(
  -- Find aphasia occurrences for each person (aphasia concept ids: 440424, 40480002)
  select condition_occurrence_id, 
         person_id, 
         condition_start_date, 
         dense_rank() over(partition by person_id order by condition_start_date asc) as aphasia_rank
  from omop_cdm_53_pmtx_202203.condition_occurrence
  where condition_concept_id in (440424, 40480002)
),
valid_aphasia_occurrence as
(
  -- Select person_ids where aphasia occurrence is on or after the stroke occurrence date
  select ao.person_id
  from stroke_cohort sc
  join aphasia_occurrence ao 
    on sc.person_id = ao.person_id
    and ao.condition_start_date >= sc.condition_start_date
  group by ao.person_id
),
multiple_aphasia_occurrence as
(
  -- Select person_ids with more than one distinct aphasia occurrence on different days
  select f1.person_id
  from aphasia_occurrence f1
  join aphasia_occurrence f2 
    on f1.person_id = f2.person_id 
   and f1.aphasia_rank = 1  -- First distinct aphasia occurrence
   and f2.aphasia_rank = 2  -- Second distinct aphasia occurrence
  group by f1.person_id
),
aphasia_indicator as
(
  -- Combine the valid aphasia and multiple aphasia occurrences into a binary indicator
  select sc.person_id,
         case when va.person_id is not null and ma.person_id is not null then 1 else 0 end as has_aphasia
  from stroke_cohort sc
  left join valid_aphasia_occurrence va on sc.person_id = va.person_id
  left join multiple_aphasia_occurrence ma on sc.person_id = ma.person_id
)
-- Final select to return the cohort with the aphasia binary indicator
select sc.*, ai.has_aphasia into {work_schema}.stroke_cohort_w_aphasia --write a table name from your personal schema
from stroke_cohort sc
left join aphasia_indicator ai 
  on sc.person_id = ai.person_id;
"""

run_query(con, query)
