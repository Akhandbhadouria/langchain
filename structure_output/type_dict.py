# pyrefly: ignore [missing-import]
from typing import TypedDict
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from langchain_groq import ChatGroq
import os



load_dotenv()

api_key = os.getenv("API_KEY")


model=ChatGroq(api_key=api_key,model='llama-3.1-8b-instant')

class Review(TypedDict):
    """Review object."""
    summary:str
    sentiment:str

str_model=model.with_structured_output(Review)

result=str_model.invoke(""" I had high expectations from this product, but it turned out to be a complete letdown. The build quality feels cheap and nowhere near what was advertised. Within a few days of use, I started noticing performance issues—lags, inconsistent behavior, and overall unreliability.

What’s even more frustrating is the poor customer support. Getting any meaningful help was slow and unproductive. For the price I paid, I expected much better durability and functionality.

Honestly, this feels like a product that looks good on paper but fails in real-world usage. I wouldn’t recommend it unless significant improvements are made.""")


print(result)
print(result['summary'])
