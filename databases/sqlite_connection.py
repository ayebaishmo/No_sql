import sqlite3
import queries as q
import pandas as pd

def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()


if __name__=="__main__":
    conn = connect_to_db()
    # results = execute_q(conn, q.GET_CHARACTERS)
    print(execute_q(conn, q.GET_CHARACTERS)[:2])

    # # change the tuples to dataframes
    # df = pd.DataFrame(results)
    # # Lets name the columns
    # df.columns = ['name', 'average_item_weight']
    # # turn the dataframe and save it to csv file
    # df.to_csv('rpg_db.csv', index=False)
    # print(df.head())