from flask import current_app
from flask import g
import psycopg2
from settings import DB_USER, DB_NAME, TEST_DB_NAME, TEST_DB_USER 

test_conn = psycopg2.connect(dbname = TEST_DB_NAME,
        user = TEST_DB_USER)
test_cursor = test_conn.cursor()

conn = psycopg2.connect(dbname = DB_NAME,
        user = DB_USER)
cursor = conn.cursor()

def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(user = current_app.config['DB_USER'],
            dbname = current_app.config['DATABASE'])
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def drop_records(cursor, conn, table_name):
    cursor.execute(f"DELETE FROM {table_name};")
    conn.commit()

def drop_tables(table_names, cursor, conn):
    for table_name in table_names:
        drop_records(cursor, conn, table_name)

def drop_all_tables(conn, cursor):
    table_names = ['venue_categories', 'venues', 'categories']
    drop_tables(table_names, cursor, conn)