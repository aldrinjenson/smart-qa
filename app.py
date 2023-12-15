import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('db.db') 
TABLE_NAME = "tb"

# uploaded_file = st.file_uploader("Choose a CSV file")
uploaded_file = "data/data.csv"
if uploaded_file is None:
    st.write("Please upload a valid CSV file ")
    exit()

df = pd.read_csv(uploaded_file)
df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
st.write(df)

def run_query(query):
    try:
        cursor = conn.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print("Error executing SQL query:", e)


sql_query = f"SELECT AVG(cc_num) FROM {TABLE_NAME}"  
result = run_query(sql_query)
print(result)
st.write(result)
