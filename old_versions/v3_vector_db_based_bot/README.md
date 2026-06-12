# v3_vector_db_based_bot

A vector database chatbot that uses ChromaDB to retrieve the best matching response from embedded chat pairs.

## Files
- `semantic_chatbot2.py` - CLI chatbot using ChromaDB
- `chatdata.csv` - stored chat example pairs
- `chat_database/` - persistent ChromaDB database folder

## Requirements
- Python 3.8+
- `chromadb`
- `pandas`

## Install
```bash
pip install chromadb pandas
```

## Run
```bash
python semantic_chatbot2.py
```

## Notes
- This script expects `chat_database/` to be initialized with a ChromaDB collection named `chatdata`.
- Type `exit` to stop the chatbot.
