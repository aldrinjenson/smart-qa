from src.constants import TABLE_NAME

def get_sql_for(user_query, table_info_string ):
    llm_query= f"""
    I have an SQL tabled called {TABLE_NAME},
    having the following structure:\n {table_info_string}
    ---
    Please generate only the SQL based on this table for the following query:
    {user_query}
    """
    print(llm_query)

    # connect with llm and get sql_query

    dummy_sql_query = f"""
        SELECT merchant, COUNT(*) AS transaction_count
        FROM {TABLE_NAME}
        GROUP BY merchant
        ORDER BY transaction_count DESC
        LIMIT 1
    """

    return dummy_sql_query


def get_nlp_result_for(user_query, db_result):
    print(user_query, db_result)
    return db_result[0]