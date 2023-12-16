import streamlit as st
import pandas as pd
import sqlite3
from src.constants import TABLE_NAME, DATABASE_NAME
from src.sql_utils import run_query
from src.llm_utils import get_sql_for, get_nlp_result_for
from src.streamlit_utils import cleanup

conn = sqlite3.connect(DATABASE_NAME) 
cleanup()


# uploaded_file = st.file_uploader("Choose a CSV file", type=["CSV"])
uploaded_file = "data/data.csv"
if uploaded_file is None:
    st.write("Please upload a valid CSV file ")
    exit()

df = pd.read_csv(uploaded_file)
st.subheader("Head data")
st.write(df.head())

df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)

user_query = st.text_input(
    "Enter your query",
    placeholder="Eg: Which merchant has the maximum transactions and by how many?",
)

print(user_query)


# sql_query = f"SELECT AVG(cc_num) FROM {TABLE_NAME}"  

table_info = run_query(conn, f"PRAGMA table_info({TABLE_NAME})")
table_info_string = pd.DataFrame(table_info, columns=["Column Index","Column Name", "Data Type", "Nullable", "Default Value", "Primary Key"]).to_string(index=False)
sql_query = get_sql_for(user_query, table_info_string)

db_result = run_query(conn, sql_query)
nlp_result = get_nlp_result_for(user_query, db_result)
print(type(nlp_result))

st.write(nlp_result)

