from langchain_google_genai import ChatGoogleGenerativeAI #👉 This is the LLM wrapper for Gemini.....It allows LangChain to talk to Gemini API.
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("API_KEY")
)

prompt=PromptTemplate(
    input_variables=['topic'],
    template="write a blog on {topic} in 5 lines"
)

topic=input("enter the topic")

formatted_prompt=prompt.format(topic=topic)

response = llm.invoke(formatted_prompt)

print(response.content)