import psycopg2
from queries import GET_CHARACTERS, DROP_CHARACTER_TABLE, INSERT_RYAN, CREATE_CHARACTER_TABLE
from sqlite_connection import connect_to_db, execute_q

# Postgress connection Credetials

# User and default database from ELEphant sql
DBNAME = 'pjksxssb'
USER = 'pjksxssb'
# pssword from elephant sql
PASSWORD = 'wK01rRzqfi2AHOcB0wHEQRlzwCK4sj0X'
# server from elephant sql
HOST = 'jelani.db.elephantsql.com'

def connect_to_pg(dbname =DBNAME, user=USER, password = PASSWORD, host = HOST):
    pg_conn = psycopg2.connect(dbname =DBNAME, user=USER, password = PASSWORD, host = HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def modify_db(conn, curs, query):
    curs.execute(query)
    conn.commit()


if __name__=="__main__":

    # GET data from sqlite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)
    
    # create destination table within postgress
    pg_conn, pg_curs = connect_to_pg()
    modify_db(pg_conn, pg_curs, DROP_CHARACTER_TABLE)
    modify_db(pg_conn, pg_curs, CREATE_CHARACTER_TABLE)


    # Loop over characyer and insert in to postgresssql
    for character in sl_characters:
        modify_db(pg_conn, pg_curs,
            f'''
            INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dextrity", "wisdom")
            VALUES ('{character[1]}', {character[2]}, {character[3]}, {character[4]}, {character[5]}, {character[6]}, {character[7]}, {character[8]});
    '''
        )



    # pg_curs.execute(INSERT_RYAN)
    # pg_conn.commit()

