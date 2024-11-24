# Tutorial for OHDSI database access with python
## Intro
* This is a step by step tutorial to setup a safe environment to access OHDSI redshift database using python.
* There is also a [git repo](https://github.com/aws/amazon-redshift-python-driver/tree/master) from AWS where you can find a tutorial from AWS. This includes more general cases than ours such as using different Identity Provider plugins, using Numpy instead of Pandas, etc.
* Pandas dataframe object will be used to process data. SQL is only used to read the original data tables from the database and write data tables that are processed by Pandas into your own schema.

## AWS Setup
* Follow the [user guide](https://northeastern.sharepoint.com/sites/OHDSINortheastern/Shared%20Documents/Forms/AllItems.aspx?ct=1730181131359&or=OWA%2DNT%2DMail&cid=53292a02%2Da869%2D233d%2D6d85%2D6b3f16dcddb5&ga=1&id=%2Fsites%2FOHDSINortheastern%2FShared%20Documents%2FOHDSI%20Lab%20%2D%20User%20Group%2FUser%20Guide%2FLatest%2FOHDSI%20LAB%20User%20Guide%2Epdf&viewid=e9534233%2D4089%2D42ed%2D8956%2D298feac7e723&parent=%2Fsites%2FOHDSINortheastern%2FShared%20Documents%2FOHDSI%20Lab%20%2D%20User%20Group%2FUser%20Guide%2FLatest) to setup your AWS.
* When creating a workspace, make sure to select both PharMetrics Plus and OMOP CDM SynPUF.
* Make sure to keep the email with your Redshift credentials that you recieved when making the workspace, since we will need these credentials for any connection.
* Your operating system on the AWS is Windows Server 2019. You can check this from Settings - System - About.
* You should use AWS virtual environment, but not use your local machine directly to access the database. Direct access to the database from your local machine is not possible, and even if it was, it is not safe to have raw data stored in your local machine at any time.

## Installation of Miniconda
* Download [Miniconda installer](https://docs.anaconda.com/miniconda/miniconda-other-installer-links/) for Windows.
* Follow the [instructions](https://docs.anaconda.com/miniconda/miniconda-install/) to install miniconda.
* You must use Anaconda PowerShell Prompt to run python, not Window's default powershell or cmd.

## Setup your python environment
* You can use Notepad++, [VScode](https://code.visualstudio.com/) or any other tool you like to write your python scripts.
* Following commands are all supposed to be ran on Anaconda PowerShell Prompt.
* Check your channels with following command:
```
conda config --show channels
```
* [conda-forge](https://conda-forge.org/) is very useful when installing different python packages. Add it to your channel:
```
conda config --add channels conda-forge
```

## Setup your git environment
* You need git to use github. Read [tutorials for git](https://www.atlassian.com/git) if you don't have any experience with it. Install [git](https://anaconda.org/conda-forge/git) package with following commad:
```
conda install conda-forge::git
```


* To use git more easily, you need to generate an SSH. Install [openssh](https://anaconda.org/conda-forge/openssh) with following command:
```
conda install conda-forge::openssh
```

* Use following command to generate a ssh key:
```
ssh-keygen
```

* You will now have '.ssh' directory on your home (D:\Users\your_name\.ssh). Open copy the content of 'id_ed25519.pub' in the directory, and paste it to your github SSH keys (Setting - SSH and GPG keys - New SSH Keys).

* Add your ssh key to the ssh-agent. You need to open windowns powershell as an administrator. Use following [commands](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent):
```
Get-Service -Name ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent

ssh-add D:/Users/your_name/.ssh/id_ed25519
```

* Set your user name and email by following command:
```
git config --global user.email your_name@email.com
git config --global user.name your_name
```

## Setup make
* [Make](https://www.gnu.org/software/make/manual/make.html) is a useful tool regarding reproducibility. Install [make](https://anaconda.org/conda-forge/make/) pckage with following command:
```
conda install conda-forge::make
```

* Create 'Makefile' on a directory where you want to use the make command. Following command in 'Makefile' is an example of running a python script 'src/example.py' with a command 'make example':
```
example:
	python -B src/example.py
```



## Configuration of your Redshift credentials on python
* DO NOT put your credentials directly to your source codes. You don't want your password to be pushed on your public git repository.
* Instead, use [configparser](https://docs.python.org/3/library/configparser.html) package. This package is already installed with Miniconda as an default package.
* Create a file named 'config.ini' on your repo. You can do this by simply changing the context of your 'config_template.ini' file. This file should be in your project directory, but not in any of the sub-directories. If you want to change its location, you MUST make sure the new location is included in your .gitignore.
  * Make sure this file is listed on your .gitignore first, so it will never be pushed to your git repository.
  * The credentials that you got from the email when you created the workspace will be used here.
  * The [JDBC url](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-obtain-url.html) is formatted in a following way: jdbc:redshift://endpoint:port/database
  * Note that 'JDBC url' and 'url' are different things. endpoint, host and url all refers to a same thing. You can separate this further with cluster, region, etc., but it is not necessary in here.
  * Write your redshift username/password and information from the JDBC url to 'config.ini' in the following format:
```
[redshift]
host=<endpoint>
database=<database>
port=<port>
user=<redshift user name>
password=<redshift password>
schema=<your redshift work schema>
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

# Read the config.ini file.
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

# Create a cursor.
cursor = con.cursor()

# Execute a query.
query = '''
SELECT * 
FROM schema.table_name
LIMIT 5;
'''
cursor.execute(query)
results = cursor.fetchall()

# Print the results.
print(results)

# Close the connection.
con.close()
```
* port variable in redshift_connector.connect() needs to be an integer.

## Use Pandas to process tables read from the Redshift database


* Install [pandas](https://anaconda.org/conda-forge/pandas) package with following command:
```
conda install pandas
```

* Unfortunately, redshift_connector does not support a data structure that can be used on pandas.read_sql(). We have to use .cursor() and .execute() to create a pandas dataframe using the tables from the database.
* Use cursor.fetch_dataframe() to create a DataFrame object:

```
import pandas as pd

# Create a Pandas dataframe.
df = cursor.fetch_dataframe()
```
* Now you have a Pandas dataframe object that can be used as if any other Pandas dataframe.
* You can find more details about [the redshift_connector API](https://docs.aws.amazon.com/redshift/latest/mgmt/python-api-reference.html).

## Write processed dataframe into your schema
* [Create table](https://www.w3schools.com/sql/sql_create_table.asp) using SQL command and cursor.execute() method.
```
cursor.execute("CREATE TABLE your_schema.your_table(col_ID int, col_name varchar);")
```
* Use cursor.write_dataframe(df, table) method to save processed dataframe df, into the table created on your schema. Your column should match the table.
```
cursor.write_dataframe(df, "your_schema.yourtable")
```
* Check if you can read the written table properly.

```
cursor.execute("SELECT * FROM your_schema.yourtable")
result = cursor.fetchall()
```
* If you want the changes in the python script to be updated to the database, you have to use .commit() method. If you don't use this command, all of the changes done in the python script will not be updated to the database:
```
redshift_connector.connection.commit()
```
* If you want to autocommit your changes, you can use [.autocommit](https://docs.aws.amazon.com/redshift/latest/mgmt/python-connect-examples.html) method.
```
# Run a rollback
con.rollback()
# Turn on autocommit
con.autocommit = True
# Turn off autocommit
con.autocommit = False
```

## Use pre-defined functions
* While you can understand and practice with the templates and above examples, we have created pre-defined functions that can be used in 'utils.py' file. You can use following 4 functions to process data in pandas data frame, and read and write tables in and out of your schema. Only reading is allowed for the omop schema.
  * config()
  * run_query()
  * write_df()
  * read_df()
* 'src/test.py' can be used as a template of using these functions. It can be ran by following command:
```
make test
```

* There are also utility commands that you can input a name of tables in your work schema in the command line. You can read a table or drop(delete) a table from your work schema using following commands:
```
make read_table
make drop_table
```