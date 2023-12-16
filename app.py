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
first_few_entries = df.head(2)
print(first_few_entries)
st.subheader("Data")
st.write(df)

df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)


table_info = run_query(conn, f"PRAGMA table_info({TABLE_NAME})")
filtered_info = [(col[1], col[2]) for col in table_info]
columns = ["Column Name", "Data Type"]
df_table_info = pd.DataFrame(filtered_info, columns=columns)
print("df info: ", df_table_info)
table_info_string = df_table_info.to_string(index=False)

user_query = st.text_input(
    "Enter your query",
    placeholder="Eg: Which merchant has the maximum transactions and by how many?",
)

print(user_query)
if not len(user_query):
    exit()





sql_query = get_sql_for(user_query, table_info_string, first_few_entries)

db_result = run_query(conn, sql_query)
print("db res = ", db_result)
nlp_result = get_nlp_result_for(user_query, db_result)
print(type(nlp_result))

st.write(nlp_result)

