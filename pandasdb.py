## Importing module sqlalchemy inorder to connect mssql database. If package is not installed in your environment, use command "pip install sqlachemy" on command line interface to download package.

import sqlalchemy.create_engine
import pandas as pd

## Creating a dataframe of 5 records.

df=pd.DataFrame([["Kiran","IT",20000],["Arun","IT",80000],["Pawan","IT",40000],["Hari","HR",40000],["Akhil","HR",90000]])

## Field names provided below should match with field names in database tables. Even if one  is different, it will throw an error. So before you perform load operation,verify the column names as well as datatypes with  database table column defintions.

df.columns=["name","dept","salary"]

## Create an odbc connection for your database server so as to perform actions on database tables. Here we are going to connect to odbc(already created) using below line of code.

connection=sqlalchemy.create_engine("mssql+pyodbc://mydb:saistuff576@sqlserver")

## Connection string provided above is in format "mssql+pyodbc://{username}:{password}@{odbc_name}". This may vary for other databases,so please check in sqlalchemy documentation for any queries.

## Here is the final step of loading data from dataframe to sql table.

df.to_sql('employee',schema='test_db',con=connection,if_exists='replace',index=False)


