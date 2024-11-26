from utils import config, read_df
import pandas as pd
from discharge_to_concept_id import total_id

# Configurations
con, work_schema = config()
work_table = "visit_occurrence"
filter_table = "stroke_cohort_w_aphasia"

# SQL Query to fetch filtered visit occurrences
query = f"""
SELECT v.person_id, 
       v.visit_end_date, 
       v.discharge_to_concept_id,
       f.condition_start_date
FROM omop_cdm_53_pmtx_202203.{work_table} v
LEFT JOIN {work_schema}.{filter_table} f
ON v.person_id = f.person_id
WHERE v.visit_end_date > f.condition_start_date;
"""

# Execute the query and fetch the results into a Pandas DataFrame
df = read_df(con, query)

# Ensure date columns are in datetime format
df['visit_end_date'] = pd.to_datetime(df['visit_end_date'])
df['condition_start_date'] = pd.to_datetime(df['condition_start_date'])

# Filter rows where visit_end_date is within 180 days of condition_start_date
df = df[(df['visit_end_date'] > df['condition_start_date']) &
        (df['visit_end_date'] <= df['condition_start_date'] + pd.Timedelta(days=180))]

# Filter rows where discharge_to_concept_id is in total_id
valid_concept_ids = set(total_id.keys())
df = df[df['discharge_to_concept_id'].isin(valid_concept_ids)]

# Add a row number per person_id to distinguish multiple pairs
df["pair_number"] = df.groupby("person_id").cumcount() + 1

# Pivot the table to create columns for each pair
df_wide = df.pivot(index="person_id", columns="pair_number", values=["visit_end_date", "discharge_to_concept_id"])

# Flatten the multi-level columns created by pivot
df_wide.columns = [f"{col[0]}_{col[1]}" for col in df_wide.columns]

# Reset the index for a clean output
df_wide = df_wide.reset_index()

# Check the resulting DataFrame structure
df_wide.info()

# Save the DataFrame to a CSV file
output_file = 'visit_oc_all_discharge.csv'
df_wide.to_csv(output_file, index=False)

print(f"df_wide has been saved to {output_file}")
