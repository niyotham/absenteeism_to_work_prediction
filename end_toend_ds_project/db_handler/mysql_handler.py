import sys
# from os.path import dirname, abspath 
# d= dirname(dirname(abspath(__file__)))
# # sys.path.append('/Users/apple/Desktop/end_toend_ds_project/')
# sys.path.append(d)
from sqlalchemy import text
from sqlalchemy import create_engine
import pandas as pd

PREDICT_SCHEMA = 'mysql_schema.sql'
engine = create_engine('mysql+pymysql://{username}:{password}@localhost:3306/predicted_outputs')
df_path= 'df_new_obs.csv'
df=pd.read_csv(df_path)


def create_table():
    try:
        with engine.connect() as conn:
            with open(f'./{PREDICT_SCHEMA}', 'r') as file:
                query= text(file.read())
                # print(query)
                conn.execute(query)
        print("Table created sucessfully!")
    except Exception as e:
        print("Error creating table", e)
        sys.exit(e)

# create_table()   

def insert_to_table(df):
    """
    df: A dataframe containing columns to insert into the database.
    """
    try:
        insert_query = 'INSERT INTO predicted_outputs VALUES '
        for i in range(df.shape[0]):
            insert_query += '(' 
            
            for j in range(df.shape[1]):
                insert_query += str(df[df.columns.values[j]][i]) + ', '
            
            insert_query = insert_query[:-2] + '), '
        
        # build a slq compatible query
        insert_query = insert_query[:-2] + ';'
        with engine.connect() as conn:
            conn.execute(insert_query)
        print('Insert into database was perfomed suscessfull')
        # print(insert_query)

    except Exception as e:
        print(f"error while inserting to table: {e}")  
        sys.exit(e)
    

insert_to_table(df)


