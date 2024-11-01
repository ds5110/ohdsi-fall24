# How to use the templates.
* There are 4 templates available to learn how to access the OHDSI database using python.
  * 'config_template.ini'
  * 'template_create_table.py'
  * 'template_delete_table.py'
  * 'template_pandas.py'
  * 'template_write_syn_cohort.py'

## config_template.ini
* This is [a template file](src/config_template.ini) to show you how to store all your credential for the redshift OHDSI database you recieved by an email into your 'config.ini.
* You MUST add your 'config.ini' into your '.gitignore'. NEVER push your credentials to a public repo.

## template_create_table.py
* You need a valid 'config.ini' file on your repo.
* Following command runs this file:
```
make test_create_table
```
* [This template](src/template_create_table.py) is currently creating an empty table called 'test_new_table' into your work schema.
* Change your SQL command in 'query' or your new table name in 'new_table_name'.
* Note that you will see an error if there is already a table with a same name exists in your work schema.

## template_delete_table.py
* You need a valid 'config.ini' file on your repo.
* Following command runs this file:
```
make test_delete_table
```
* [This template](src/template_delete_table.py) is currently deleting a table 'test_new_table' from your work schema.
* Change 'new_table_name' variable into the table name you want to delete.
* Note that you will see an error if a table you want to delete does not exisst in your work schema.

## template_pandas.py
* You need a valid 'config.ini' file on your repo.
* Following command runs this file:
```
make test_pandas
```
* [This template](src/template_pandas.py) creates a Pandas DataFrame that you can process with python.
* Currently, this template is creating a dataframe using 'cohort' table from 'omop_cdm_synpuf_110k_531' schema, and then writing it into a table 'test_new_table' in your own schema.
* 'schema_original' defines a database you choose to read a table out of. 'table_name_original' defines a table that you want to read from 'schema_original'.
* Process 'df' with any python commands you want to use.
* 'table_name_work' defines a table in your work space you want to store your final dataframe 'df'.
* Note that you will see an error if the tables do not exists in each schemas, or your data frame format does not match your schema table (column's data type does not match, etc.).
## template_write_syn_cohort.py
* You need a valid 'config.ini' file on your repo.
* Following command runs this file:
```
make test_create_table
```
* [This template](src/template_write_syn_cohort.py) is reading a table 'cohort' from a schema 'omop_cdm_synpuf_110k_531' and writing it into a table 'test_new_table_1' in your workr schema.
* Note that you will see an error if you already have a table with a same name 'test_new_table_1' in your work schema.