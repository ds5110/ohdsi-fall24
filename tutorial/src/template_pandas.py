import configparser
import redshift_connector
import pandas as pd


# Read the config.ini file.
config = configparser.ConfigParser()
config.read("config.ini")

# Connect to Redshift using your credentials.
con = redshift_connector.connect(
    host=config["redshift"]["host"],
    database=config["redshift"]["database"],
    port=int(config["redshift"]["port"]),
    user=config["redshift"]["user"],
    password=config["redshift"]["password"],
)
# Your work schema.
work_schema = config["redshift"]["schema"]

# Create a cursor.
cursor = con.cursor()

# Schema and table to be read.
schema_original = "omop_cdm_synpuf_110k_531"
table_name_original = "cohort"

# Execute a query.
query = f"""
SELECT *
FROM {schema_original}.{table_name_original}
LIMIT 5;
"""
cursor.execute(query)
print(f"Executed query: \n {query}")

# Create a pandas dataframe of the table read.
df = cursor.fetch_dataframe()
print(df.head())

# -----------------------------------------------------------
# Process df in here.
# -----------------------------------------------------------

# Write the pandas dataframe to a table in your schema. Table must already exists.
table_name_work = "test_new_table"
cursor.write_dataframe(df, f"{work_schema}.{table_name_work}")

# Commit the changes to the database.
con.commit()

# Close the connection.
con.close()
