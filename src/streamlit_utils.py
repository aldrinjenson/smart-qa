import streamlit as st

def cleanup():
    st.set_page_config(
        page_title="Smart QA",
        page_icon="✨",
    )

    st.title("Smart QA - Smart Question Answering system on CSV data")
    st.write(
        "Web application that uses AI tech to answer questions on you data using just natural language"
    )

