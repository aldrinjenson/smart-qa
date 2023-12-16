
from io import BytesIO
import streamlit as st
from lida import Manager, llm, TextGenerationConfig
from src.constants import LLM_MODEL, OPENAI_API_KEY
from PIL import Image
import base64



model = None
if LLM_MODEL == 'openai':
    model = llm(
        provider="openai",
        api_key= OPENAI_API_KEY
    )
elif LLM_MODEL == 'ollama':
    model = llm(
        provider="openai",
        api_base="http://localhost:8000",
        api_key="EMPTY"
    )


lida = Manager(text_gen = model)
textgen_config = TextGenerationConfig(n=1, temperature=0.5, model="gpt-3.5-turbo-1106", use_cache=True)

def respond_with_lida_analysis(csv_file, user_query):
    summary = lida.summarize(csv_file, textgen_config=textgen_config)
    print(summary)
    print("Summary done")

    charts = lida.visualize(summary, user_query, textgen_config=textgen_config)
    base64_image_string = charts[0].raster
    print(charts[0])
    chart_code = charts[0].code
    explanation = lida.explain(code=chart_code,textgen_config=textgen_config)

    image_bytes = base64.b64decode(base64_image_string)
    image = Image.open(BytesIO(image_bytes))
    st.image(image, use_column_width=True)
    image.save("image.png")

    st.write(explanation[0][0]["explanation"])



