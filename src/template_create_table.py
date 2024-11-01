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

# Name of the new table in your schema to be created.
new_table_name = "test_new_table"

# Execute a query.
query = f"""CREATE TABLE {work_schema}.{new_table_name}
(cohort_definition_id int4 NOT NULL,
subject_id int4 NOT NULL,
cohort_start_date date NOT NULL,
cohort_end_date date NOT NULL);"""
cursor.execute(query)
print(f"Executed query: \n {query}")

# Commit the changes to the database.
con.commit()

# Close the connection.
con.close()
