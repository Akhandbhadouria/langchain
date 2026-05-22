from langchain_core.prompts import PromptTemplate #👉 This is used to create dynamic prompts.
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI #👉 This is the LLM wrapper for Gemini.....It allows LangChain to talk to Gemini API.
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
import os

load_dotenv()
api_key = os.getenv("API_KEY")

#creating the llm object 
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("API_KEY")
)




schema=[
    ResponseSchema(name='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='fact 3 about the topic'),
    ]


parser=StructuredOutputParser.from_response_schemas(schema)


template=PromptTemplate(
    template='give 3fact about the {topic}\n {formate_instruction}',
    input_variables=['topic'],
    partial_variables={'formate_instruction':parser.get_format_instructions()}
)
chain=template | llm |parser
result=chain.invoke({'topic':'black hole'})
print(result)