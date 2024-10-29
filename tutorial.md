# Tutorial for OHDSI database access with python
## AWS Setup
* Follow the [user guide](https://northeastern.sharepoint.com/sites/OHDSINortheastern/Shared%20Documents/Forms/AllItems.aspx?ct=1730181131359&or=OWA%2DNT%2DMail&cid=53292a02%2Da869%2D233d%2D6d85%2D6b3f16dcddb5&ga=1&id=%2Fsites%2FOHDSINortheastern%2FShared%20Documents%2FOHDSI%20Lab%20%2D%20User%20Group%2FUser%20Guide%2FLatest%2FOHDSI%20LAB%20User%20Guide%2Epdf&viewid=e9534233%2D4089%2D42ed%2D8956%2D298feac7e723&parent=%2Fsites%2FOHDSINortheastern%2FShared%20Documents%2FOHDSI%20Lab%20%2D%20User%20Group%2FUser%20Guide%2FLatest) to setup your AWS.
* When creating a workspace, make sure to select both PharMetrics Plus and OMOP CDM SynPUF. Make sure to keep the email with your Redshift credentials that you recieved when making the workspace, since we will need these credentials for any connection.
* Your operating system on the AWS is Windows Server 2019. You can check this from Settings - System - About.

## Installation of Miniconda
* Download [Miniconda installer](https://docs.anaconda.com/miniconda/miniconda-other-installer-links/) for Windows.
* Follow the [instructions](https://docs.anaconda.com/miniconda/miniconda-install/) to install miniconda.
* You must use anaconda powershell promt to run python, not Window's default powershell or cmd.

## Configuration of your Redshift credentials on python
* DO NOT put your credentials directly to your source codes. You don't want your password to be pushed on your public git repository.
* Instead, use [configparser](https://docs.python.org/3/library/configparser.html) package. This package is already installed with Miniconda as an default package.
* Create a file named 'config.ini' on your directory.
  * The credentials that you got from the email when you created the workspace will be used here.
  * The [JDBC url](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-obtain-url.html) is formatted in following format: jdbc:redshift://endpoint:port/database
  * Put your redshift username/password and info. from the JDBC url to put following content into 'config.ini':
```
[redshift]
host=<endpoint>
database=<database>
port=<port>
user=<redshift user name>
password=<redshift password>
```


## Creating connection to the Redshift database using python
* The [documantation for redshift_connector](https://docs.aws.amazon.com/redshift/latest/mgmt/python-redshift-driver.html) can be found in AWS website.
* [redshift_connector](https://docs.aws.amazon.com/redshift/latest/mgmt/python-driver-install.html) package can be installed by following command:
```
conda install -c conda-forge redshift_connector
```



* Now, we will use configparser and redshift_connector to create connection to the OHDSI-lab database:
```
import configparser
import redshift_connector

# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Connect to Redshift
con = redshift_connector.connect(
    host=config['redshift']['host'],
    database=config['redshift']['database'],
    port=int(config['redshift']['port']),
    user=config['redshift']['user'],
    password=config['redshift']['password']
)

# Create a cursor
cursor = con.cursor()

# Execute a query
query = '''
SELECT * 
FROM schema.table_name
LIMT 5;
'''
cursor.execute(query)
results = cursor.fetchall()

# Print the results
print(results)

# Close the connection
conn.close()


```
* port variable in redshift_connector.connect() needs to be an integer.

## Use Pandas to process tables read from the Redshift database
* [Install pandas](https://anaconda.org/conda-forge/pandas) package if you haven't done so yet:
```
conda install conda-forge::pandas
```


* Unfortunately, redshift_connector does not support a data structure that can be used on pandas.read_sql(). We have to use .cursor() and .execute() to create a pandas dataframe using the tables from the database.
* Use pandas to create DataFrame object:

```
import configparser
import redshift_connector
import pandas as pd

# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Connect to Redshift
con = redshift_connector.connect(
    host=config['redshift']['host'],
    database=config['redshift']['database'],
    port=int(config['redshift']['port']),
    user=config['redshift']['user'],
    password=config['redshift']['password']
)

# Create a cursor
cursor = con.cursor()

# Execute a query
query = '''
SELECT * 
FROM schema.table_name
LIMT 5;
'''
cursor.execute(query)
pd.DataFrame = cursor.fetch_dataframe()

# Close the connection
conn.close()


```
* You can find more details about [the redshift_connector API](https://docs.aws.amazon.com/redshift/latest/mgmt/python-api-reference.html).

## Write processed dataframe into your schema - To be continued
* Use cursor.write_dataframe(df, table)
