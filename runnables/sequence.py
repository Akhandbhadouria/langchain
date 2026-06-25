from langchain_google_genai import ChatGoogleGenerativeAI #👉 This is the LLM wrapper for Gemini.....It allows LangChain to talk to Gemini API.
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("API_KEY")
)

prompt=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']

)


prompt2=PromptTemplate(
    template='explain the following joke {text}',
    input_variables=['text']

)

parser=StrOutputParser()
chain=RunnableSequence(prompt,llm,parser,prompt2,llm,parser)

print(chain.invoke({'topic':'AI'}))