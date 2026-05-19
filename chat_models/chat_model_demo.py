# pyrefly: ignore [missing-import]
from langchain_groq import ChatGroq
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

chat_model=ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)

result=chat_model.invoke("what is the capital of india?")

print(result)
