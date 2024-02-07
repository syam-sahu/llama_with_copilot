import os
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

PERSIST_DIR = "./storage"

if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)

if __name__ == "__main__":
    print("Key: ",os.environ["OPENAI_API_KEY"])