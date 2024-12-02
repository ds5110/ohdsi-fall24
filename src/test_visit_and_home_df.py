from utils import config, read_df, write_df, run_query
import pandas as pd
from discharge_to_concept_id import total_id
from visit_and_home_df import visit_and_home_df

visit_dataframes, at_home = visit_and_home_df()

# Iterate through visit_n DataFrames
for name, df in visit_dataframes.items():
    print(f"DataFrame: {name}")
    print(df.head())
    print(f"Shape: {df.shape}")
    print(f"Info: {df.info}")

# Check the at_home DataFrame
print("At Home DataFrame:")
print(at_home.head())
print(f"Shape: {df.shape}")
print(f"Info: {df.info}")
