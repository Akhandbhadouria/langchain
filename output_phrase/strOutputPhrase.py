from langchain_core.prompts import PromptTemplate #👉 This is used to create dynamic prompts.
from langchain_core.output_parsers import StrOutputParser
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

parser = StrOutputParser()

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary of the following text:\n{text}',
    input_variables=['text']
)

# 🔥 Proper chain
chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({'topic': 'black hole'})

print(result)



# 🔥 LangChain Flow (with example)
# Chain:
# template1 | llm | parser | template2 | llm | parser
# 🧠 Step-by-step execution
# 1️⃣ Input
# {"topic": "black hole"}

# 2️⃣ template1 (PromptTemplate)
# "Write a detailed report on black hole"

# 3️⃣ llm (Gemini model)
# AIMessage(content="Black holes are regions in space where gravity is extremely strong...")

# 4️⃣ parser (StrOutputParser)
# "Black holes are regions in space where gravity is extremely strong..."

# 5️⃣ template2 (PromptTemplate)

# Auto-mapping happens:

# "long report..." → {"text": "long report..."}

# Output:

# "Write a 5 line summary of the following text:
# Black holes are regions in space where gravity is extremely strong..."
# 6️⃣ llm (Gemini model)
# AIMessage(content="Black holes have strong gravity. They form from dying stars...")
# 7️⃣ parser (StrOutputParser)
# "Black holes have strong gravity. They form from dying stars..."
# ✅ Final Output
# "Black holes have strong gravity. They form from dying stars..."