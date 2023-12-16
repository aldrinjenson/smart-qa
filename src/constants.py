from dotenv import load_dotenv
load_dotenv()
import os

TABLE_NAME = "tb"
DATABASE_NAME = "db.db"

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
# LLM_MODEL="ollama"
LLM_MODEL="openai"
