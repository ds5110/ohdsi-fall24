import configparser
import redshift_connector


# Configuration setup.
def config():
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
    work_schema = config["redshift"]["schema"]
    return con, work_schema


# Run SQL query.
def run_query(con, query):
    # Create a cursor.
    cursor = con.cursor()

    # Execute a query.
    cursor.execute(query)
    print(f"Executed query: \n {query}")

    # Commit the changes to the database.
    con.commit()

    # Close the connection.
    con.close()
    return


# Read and convert to pandas df.
def read_df(con, query):
    # Create a cursor.
    cursor = con.cursor()

    # Execute a query.
    cursor.execute(query)
    print(f"Executed query: \n {query}")

    # Create a pandas dataframe of the table read.
    df = cursor.fetch_dataframe()

    # Commit the changes to the database.
    con.commit()

    # Close the connection.
    con.close()
    return df


# Write pandas df into database.
def write_df(con, df, work_schema, table):
    # Create a cursor.
    cursor = con.cursor()

    # Write the pandas dataframe to a table in your schema. Table must already exists.
    cursor.write_dataframe(df, f"{work_schema}.{table}")

    # Commit the changes to the database.
    con.commit()

    # Close the connection.
    con.close()

    return
