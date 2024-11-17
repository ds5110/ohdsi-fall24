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
        timeout=60,
    )
    work_schema = config["redshift"]["schema"]
    print(f"Connection is created. Your work schema is '{work_schema}'")
    return con, work_schema


# Run SQL query.
def run_query(con, query):
    # Create a cursor.
    cursor = con.cursor()
    try:
        # Execute a query.
        cursor.execute(query)
    except Exception as e:
        print(f"Error: {e}")
    else:
        # Print executed query.
        print(f"Executed query: \n {query}")
        # Commit the changes to the database.
        con.commit()
    finally:
        # Close the connection even if error occurs.
        con.close()
        print("Connection is closed.")
    return


# Write pandas dataframe into your schema.
def write_df(con, df, work_schema, table):
    # Create a cursor.
    cursor = con.cursor()
    try:
        # Write the pandas dataframe to a table in your schema. Table must already exists.
        cursor.write_dataframe(df, f"{work_schema}.{table}")
    except Exception as e:
        print(f"Error: {e}")
    else:
        # Commit the changes to the database.
        con.commit()
    finally:
        # Close the connection even if error occurs.
        con.close()
        print("Connection is closed.")
    return


# Read a table and convert it to a pandas dataframe.
def read_df(con, query):
    # Create a cursor.
    cursor = con.cursor()
    try:
        # Execute a query.
        cursor.execute(query)
    except Exception as e:
        print(f"Error: {e}")
    else:
        # Print executed query.
        print(f"Executed query: \n {query}")
        # Create a pandas dataframe of the table read.
        df = cursor.fetch_dataframe()
        # Commit the changes to the database.
        con.commit()
        return df
    finally:
        # Close the connection even if error occurs.
        con.close()
        print("Connection is closed.")
