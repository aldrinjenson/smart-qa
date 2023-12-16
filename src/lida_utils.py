
from lida import Manager, llm

# model = llm(
#     provider="openai",
#     api_key="sk-***"
# )
model = llm(
    provider="openai",
    api_base="http://localhost:8000",
    api_key="EMPTY"
)

lida = Manager(text_gen = model)
summary = lida.summarize("sample.csv")
goals = lida.goals(summary, n=3) 
print(goals)
charts = lida.visualize(summary=summary, goal=goals[1])
print(charts)


