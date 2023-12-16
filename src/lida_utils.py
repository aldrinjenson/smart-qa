from io import BytesIO
import streamlit as st
from lida import Manager, llm, TextGenerationConfig
from src.constants import LLM_MODEL, OPENAI_API_KEY
from PIL import Image
import base64


model = None
if LLM_MODEL == "openai":
    model = llm(provider="openai", api_key=OPENAI_API_KEY)
elif LLM_MODEL == "ollama":
    model = llm(provider="openai", api_base="http://localhost:8000", api_key="EMPTY")


def generate_chart_and_explanation(chart):
    chart_code = chart.code
    base64_image_string = chart.raster

    image_bytes = base64.b64decode(base64_image_string)
    image = Image.open(BytesIO(image_bytes))
    explanation_obj = lida.explain(code=chart_code, textgen_config=textgen_config)
    explanation_string = explanation_obj[0][0]["explanation"]

    st.image(image, caption=explanation_string, use_column_width=True)


lida = Manager(text_gen=model)
textgen_config = TextGenerationConfig(
    n=1, temperature=0.5, model="gpt-3.5-turbo-1106", use_cache=True
)


def respond_with_lida_analysis(csv_file, user_query):
    summary = lida.summarize(csv_file, textgen_config=textgen_config)
    print(summary)
    print("Summary done")

    charts = lida.visualize(summary, user_query, textgen_config=textgen_config)
    print(charts)
    print(len(charts))
    generate_chart_and_explanation(charts[0])
    # infographics = lida.infographics(visualization=base64_image_string n=2, style_prompt="line art")
    # infographics = lida.infographics(visualization = base64_image_string, n=3, style_prompt="line art")
    # print(infographics)

    # recommendations = lida.recommend(code=charts[0].code, summary=summary, n=2,  textgen_config=textgen_config)
    # for recommendation in recommendations:
    #     generate_chart_and_explanation(recommendation)
