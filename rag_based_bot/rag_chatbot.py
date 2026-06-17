from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
# from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_ollama.chat_models import ChatOllama
import chromadb as db
import os

chat = ChatOllama(model="qwen2.5-coder:1.5b", temperature=0.7)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=chat, memory=memory, verbose=True)

client = db.PersistentClient('../vectordb/chatdatabase')
print('client loaded successfully.')