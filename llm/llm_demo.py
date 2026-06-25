# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
import os

load_dotenv()  

api_key = os.getenv("API_KEY")

# pyrefly: ignore [missing-import]
from langchain_google_genai import ChatGoogleGenerativeAI #👉 This is the LLM wrapper for Gemini.....It allows LangChain to talk to Gemini API.

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("API_KEY")
)
response = llm.invoke("write 5 line summary on cricket")
print(response.content)