from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOllama

chat = ChatOllama(model="qwen2.5-coder:1.5b", temperature=0.7)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=chat, memory=memory, verbose=False)

print("Local LangChain Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Bye!")
        break

    response = conversation.predict(input=user_input)
    print(f"Bot: {response}")
