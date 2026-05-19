# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
import os

load_dotenv()  

api_key = os.getenv("API_KEY")

# pyrefly: ignore [missing-import]
from langchain_groq import ChatGroq

llm=ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant" ,
   temperature=1.2
    )
response = llm.invoke("write 5 line summary on cricket")
print(response.content)