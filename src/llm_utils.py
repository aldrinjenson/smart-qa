from src.constants import TABLE_NAME, LLM_MODEL
from src.llm_models import execute_with_openai, execute_with_ollama


def execute_with_llm(query):
    print({"Query: ", query})

    if LLM_MODEL == 'openai':
        response = execute_with_openai(query)
    elif LLM_MODEL == 'mistral':
        response = execute_with_ollama(query)
    else:
        return Exception("Invalid model specified")
    return response


def get_sql_for(user_query, table_info_string, first_few_entries ):
    llm_query= f"""
    Please generate only the simplest SQL to find answer to the query:{user_query}

    Here is the SQL table strucuture: 
    {table_info_string}

    ---
    Here are the first few entries:
    {first_few_entries}

    ---

    Table name is {TABLE_NAME}
    ---

    Output only SQL in json format.
    eg: {{
        "sql": "SELECT * FROM {TABLE_NAME}"
        "error": null
    }}
    """
    llm_response = execute_with_llm(llm_query)

    print(llm_response["sql"])
    return llm_response["sql"]


def get_nlp_result_for(user_query, sql_query, db_result):
    print(user_query, db_result)
    llm_query = f"""You are an intelligent assistant. 
    After running an SQL query of {sql_query}, the result of {db_result}  was obtained. 
    Based on this, in natural language answer the question: {user_query}. 
    If you cannot answer based on this, directly say so. Don't mention anything about SQL. 
    Directly answer the user to the point Output in the following json format
    {{response: <your response>}}.
"""
    nlp_result = execute_with_llm(llm_query)
    print(nlp_result)
    return nlp_result