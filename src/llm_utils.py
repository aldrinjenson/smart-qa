# from src.constants import TABLE_NAME
TABLE_NAME = "tb"


import requests
import json

def execute_with_ollama(query):
    print({"Query: ", query})
    payload = {
        "model": "mistral",
        "format": "json",
        "stream": False,
        "messages": [
            {"role": "user", "content": query + "\nOutput only SQL in JSON"}
        ]
    }

    payload_json = json.dumps(payload)
    url = 'http://localhost:11434/api/chat'

    try:
        response = requests.post(url, data=payload_json)

        if response.status_code == 200:
            response_data = response.json()
            print("Reponse data = ", response_data)
            return response_data['message']['content']
        else:
            print(f"LLM Request failed with status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request exception: {e}")
        return None

# query = "why is the sky blue? Respond to the point in JSON"
# result = execute_with_ollama(query)
# print("Response:", result)


def get_sql_for(user_query, table_info_string, first_few_entries ):
    llm_query= f"""
    I have an SQL tabled called {TABLE_NAME},
    having the following structure: 
    {table_info_string}
    ---
    Here are the first few entries:
    {first_few_entries}
    ---
    Please generate only the simplest SQL based on this table for the following query. Here is the query::
    {user_query}

    ---

    eg: {{
        "sql": "SELECT * FROM {TABLE_NAME}"
        "error": null
    }}
    """
    llm_response = execute_with_ollama(llm_query)
    print("LLM resopnse = ", llm_response)

    # connect with llm and get sql_query

    dummy_sql_query = f"""
        SELECT merchant, COUNT(*) AS transaction_count
        FROM {TABLE_NAME}
        GROUP BY merchant
        ORDER BY transaction_count DESC
        LIMIT 1
    """

    print(type(llm_response))
    print(type(json.loads(llm_response)))
    llm_response = json.loads(llm_response)
    print("JSON response= ", llm_response)
    print(llm_response["sql"])
    # return dummy_sql_query
    return llm_response["sql"]


def get_nlp_result_for(user_query, db_result):
    print(user_query, db_result)
    return db_result[0][0]