import pandas as pd
import streamlit as st
import sqlite3
from src.llm_utils import get_sql_for, get_nlp_result_for
from src.constants import TABLE_NAME


def run_query(conn, query):
    query = query.replace("\\", "")
    try:
        cursor = conn.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print("Error executing SQL query:", e)


def respond_with_sql_analysis(df, conn, user_query):
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

    table_info = run_query(conn, f"PRAGMA table_info({TABLE_NAME})")
    filtered_info = [(col[1], col[2]) for col in table_info]
    columns = ["Column Name", "Data Type"]
    df_table_info = pd.DataFrame(filtered_info, columns=columns)
    print("df info: ", df_table_info)
    table_info_string = df_table_info.to_string(index=False)

    first_few_entries = df.head(2).to_string()
    sql_query = get_sql_for(user_query, table_info_string, first_few_entries)

    db_result = run_query(conn, sql_query)
    print("db res = ", db_result)
    st.write(db_result)
    nlp_result = get_nlp_result_for(user_query, sql_query, db_result)

    st.write(nlp_result)
