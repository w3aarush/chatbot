from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOllama
import chromadb as db
import os

chat = ChatOllama(model="qwen2.5-coder:1.5b", temperature=0.7)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=chat, memory=memory, verbose=True)

client = db.PersistentClient('../vectordb/chatdatabase')
print('client loaded successfully.')
# print(client.list_collections())
collection = client.get_collection('chat_collection')
print('collection loaded successfully.')

THRESHOLD = 0.25

def chatbot():
    while True:
        message = input("User: -> \n")
        if message == 'exit':
            break
        results = collection.query(query_texts=[message],n_results=1)
        response_msg = results['metadatas'][0][0]['response_msg']
        reply = conversation.predict(input=message, output=response_msg)
        print(reply)
        # print(f"Bot: => {response_msg} (sim={best_score:.2f})")
        # if best_score >= THRESHOLD:
        #     print(f"Bot: => {response_msg} (sim={best_score:.2f})")
        # else:
        #     print("Sorry, didn't get that")
        #     print("please tell me, what should have been my response here.")
        #     new_response = input()
        #     conversation.predict(input=message, output=new_response)
        #     print("thanks buddy, now I know. Try asking my again.")
chatbot()
