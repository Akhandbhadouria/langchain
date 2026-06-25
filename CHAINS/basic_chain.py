from langchain_core.prompts import PromptTemplate #👉 This is used to create dynamic prompts.
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI #👉 This is the LLM wrapper for Gemini.....It allows LangChain to talk to Gemini API.
from langchain_core.output_parsers import StrOutputParser # type: ignore
import os

load_dotenv()
api_key = os.getenv("API_KEY")


prompt=PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(
    api_key=api_key,
    model="gemini-2.5-flash"
)

parser=StrOutputParser()

chain=prompt |model |parser
result =chain.invoke({'topic':'cricket'})
print(result)