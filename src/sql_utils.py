
import sqlite3

def run_query(conn, query):
    query = query.replace('\\', '')
    try:
        cursor = conn.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print("Error executing SQL query:", e)