# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# generate embedding
result = model.encode("Delhi is the capital of India")

print(result)