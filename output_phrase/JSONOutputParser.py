from langchain_core.prompts import PromptTemplate #👉 This is used to create dynamic prompts.
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI #👉 This is the LLM wrapper for Gemini.....It allows LangChain to talk to Gemini API.

import os

load_dotenv()
api_key = os.getenv("API_KEY")

#creating the llm object 
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("API_KEY")
)

parser=JsonOutputParser()

template=PromptTemplate(
    template='give me the name , age of the fictional character {formate_instruction}',
    input_variables=[],
    partial_variables={'formate_instruction':parser.get_format_instructions()}
)

chain = template | llm | parser

result =  chain.invoke({})
print( result)