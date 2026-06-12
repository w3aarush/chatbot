# v4_local_llm_ollama_based_bot

A local LLM chatbot using LangChain Classic and Ollama for offline model access.

## Files
- `chatbot.py` - CLI local LLM chatbot using `ChatOllama`
- `requirements.txt` - Python package dependencies

## Requirements
- Python 3.8+
- Local Ollama installed and running
- Ollama model `qwen2.5-coder:1.5b` available locally
- `langchain==1.2.0`
- `langchain-classic==1.0.0`
- `langchain-community==0.4.1`

## Install
```bash
pip install -r requirements.txt
```

## Run
```bash
python chatbot.py
```

## Notes
- The script uses `ChatOllama` from `langchain_community`.
- Make sure your local Ollama service is running before starting the chatbot.
- Type `exit`, `quit`, or `bye` to end the conversation.
