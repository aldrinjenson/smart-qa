from src.constants import TABLE_NAME


import requests
import json

def execute_with_ollama(query):
    print({"Query: ", query})
    payload = {
        "model": "mistral",
        "format": "json",
        "stream": False,
        "messages": [
            {"role": "user", "content": query}
        ]
    }

    payload_json = json.dumps(payload)
    url = 'http://localhost:11434/api/chat'

    try:
        response = requests.post(url, data=payload_json)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['message']['content']
        else:
            print(f"LLM Request failed with status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request exception: {e}")
        return None

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
    llm_response = execute_with_ollama(llm_query)

    llm_response = json.loads(llm_response)
    print(llm_response["sql"])
    return llm_response["sql"]


def get_nlp_result_for(user_query, sql_query, db_result):
    print(user_query, db_result)
    llm_query = f"""You are an intelligent assistant. 
    After running an SQL query of {sql_query}, the result of {db_result}  was obtained. 
    Based on this, in natural language answer the question: {user_query}. 
    If you cannot answer based on this, directly say so. Don't mention anything about SQL. 
    Directly answer the user to the point.
"""
    nlp_result = execute_with_ollama(llm_query)
    print(nlp_result)
    nlp_result = json.loads(nlp_result)
    return nlp_result