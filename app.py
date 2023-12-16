from src.constants import TABLE_NAME, DATABASE_NAME
import streamlit as st
import pandas as pd
import sqlite3
from src.sql_utils import respond_with_sql_analysis
from src.streamlit_utils import cleanup
from src.lida_utils import respond_with_lida_analysis

conn = sqlite3.connect(DATABASE_NAME)
cleanup()


uploaded_file = st.file_uploader("Choose a CSV of JSON file", type=["csv", "json"])
# uploaded_file = "data/data.csv"
# uploaded_file = "sample.csv"
if uploaded_file is None:
    st.write("Please upload a valid CSV or JSON file ")
    exit()

# file_extension = "." + uploaded_file.split(".")[1]
file_extension = "." + uploaded_file.name.split(".")[1]
print(file_extension)
df = None
if file_extension.lower() == ".csv":
    df = pd.read_csv(uploaded_file)
elif file_extension.lower() == ".json":
    df = pd.read_json(uploaded_file)
else:
    print("Invalid file type!")
    exit(0)

print(df)

st.subheader("Data")
st.write(df)


user_query = st.text_input(
    "Enter your query",
    placeholder="Eg: Which merchant has the maximum transactions and by how many?",
)

if not len(user_query):
    exit()

# respond_with_lida_analysis(df, user_query)
respond_with_sql_analysis(df, conn, user_query)
