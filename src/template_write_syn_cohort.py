import configparser
import redshift_connector


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

# Table name to be created.
table_name_work = "test_new_table_1"

# Execute a query.
query = f"""
SELECT *
INTO {work_schema}.{table_name_work}
FROM {schema_original}.{table_name_original}
LIMIT 5;
"""
cursor.execute(query)
print(f"Executed query: \n {query}")

# Commit the changes to the database.
con.commit()

# Close the connection.
con.close()
