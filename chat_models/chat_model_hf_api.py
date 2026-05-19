# pyrefly: ignore [missing-import]
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("HUGGING_FACE_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-72B-Instruct',
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)