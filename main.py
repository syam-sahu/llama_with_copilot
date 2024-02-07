from dotenv import load_dotenv
import os

from llama_index import VectorStoreIndex, SimpleDirectoryReader


load_dotenv()

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
