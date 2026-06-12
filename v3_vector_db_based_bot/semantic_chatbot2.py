import chromadb as db
import pandas as pd

client = db.PersistentClient('./chat_database')
collection = client.get_collection('chatdata')
print('collection loaded succesfully.')

THRESHOLD = 0.25

def chatbot():
    while True:
        message = input("User: -> \n")
        if message == 'exit':
            break
        score = collection.query(query_texts=[message],n_results=1)['distances'][0][0]
        if score<=THRESHOLD:
            res = collection.query(query_texts=[message],n_results=1)['metadatas'][0][0]['response']
            print(f"Bot: -> {res}")
        else:
            res = collection.query(query_texts=[message],n_results=4)['metadatas'],collection.query(query_texts=[message],n_results=4)['distances']
            print(f"Bot:-. {res}")

chatbot()