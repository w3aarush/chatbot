import os
import chromadb
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Determine robust path to ChromaDB vector database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "../vectordb/chatdatabase"))

def load_vector_db(db_path: str):
    """Load ChromaDB client and collection."""
    try:
        client = chromadb.PersistentClient(path=db_path)
        collection = client.get_collection(name="chat_collection")
        print(f"✅ Connected to ChromaDB collection 'chat_collection' at '{db_path}'.")
        return collection
    except Exception as e:
        print(f"⚠️ Could not load ChromaDB collection: {e}")
        return None

def query_knowledge_base(collection, user_query: str, top_k: int = 2) -> str:
    """Retrieve top-k relevant knowledge items from ChromaDB."""
    if not collection:
        return "No vector database context available."
    
    try:
        results = collection.query(query_texts=[user_query], n_results=top_k)
        contexts = []
        if results and 'documents' in results and results['documents']:
            docs = results['documents'][0]
            metas = results['metadatas'][0] if 'metadatas' in results and results['metadatas'] else []
            distances = results['distances'][0] if 'distances' in results and results['distances'] else []
            
            for i in range(len(docs)):
                doc_text = docs[i]
                meta = metas[i] if i < len(metas) else {}
                dist = distances[i] if i < len(distances) else None
                
                resp = meta.get('response_msg', '')
                if resp:
                    dist_str = f" (Distance: {dist:.4f})" if dist is not None else ""
                    contexts.append(f"- Matched Question: '{doc_text}' -> Expected Answer: '{resp}'{dist_str}")
                else:
                    contexts.append(f"- Document Context: {doc_text}")
        
        return "\n".join(contexts) if contexts else "No closely matching context found."
    except Exception as e:
        return f"Error retrieving context: {e}"

def run_rag_chatbot():
    collection = load_vector_db(DB_PATH)
    
    print("🤖 Initializing Local LLM (qwen2.5-coder:1.5b)...")
    llm = ChatOllama(model="qwen2.5-coder:1.5b", temperature=0.7)
    
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful and intelligent AI chatbot assistant.\n"
            "Use the following retrieved context from the knowledge base (if relevant) to inform your response.\n"
            "If the context is relevant, prioritize it. Otherwise, use your general knowledge while remaining concise and clear.\n\n"
            "Retrieved Knowledge Context:\n{context}"
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    chain = prompt | llm
    chat_history = []

    print("\n==========================================================")
    print("🚀 RAG Chatbot is Ready! Type 'exit', 'quit', or 'bye' to stop.")
    print("==========================================================\n")
    
    while True:
        try:
            user_input = input("User: -> ").strip()
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Bot: Goodbye! Take care.")
                break
            
            # 1. Retrieve knowledge base context
            retrieved_context = query_knowledge_base(collection, user_input)
            
            # 2. Predict response with RAG prompt + chat history
            response = chain.invoke({
                "context": retrieved_context,
                "history": chat_history,
                "input": user_input
            })
            
            response_text = response.content.strip()
            print(f"\nBot: -> {response_text}\n")
            
            # 3. Update conversation history
            chat_history.append(HumanMessage(content=user_input))
            chat_history.append(AIMessage(content=response_text))
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break

if __name__ == "__main__":
    run_rag_chatbot()