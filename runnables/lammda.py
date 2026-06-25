from langchain_google_genai import ChatGoogleGenerativeAI #👉 This is the LLM wrapper for Gemini.....It allows LangChain to talk to Gemini API.
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda
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

parser=StrOutputParser()

def cnt(data):
    return len(data)

word_runnable=RunnableLambda(cnt)

main_chain=RunnableSequence(prompt,llm,parser)

word_chain = RunnableParallel({
    "count": word_runnable,
    "joke": main_chain
})
final_chain=RunnableSequence(main_chain,word_chain)
print(final_chain.invoke({'topic':'AI'}))