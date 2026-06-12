# Chatbot Collection

This repository contains four versions of a Python chatbot project, each demonstrating a different conversational approach.

## Overview

- `v1_list_based_bot`: A simple rule-based chatbot using hard-coded lists and CSV data for input-output matching.
- `v2_list_semnatic_search_bot`: A keyword/semantic search-based chatbot that finds responses using a CSV dataset.
- `v3_vector_db_based_bot`: A chatbot that uses vector embeddings and a local database for semantic retrieval.
- `v4_local_llm_ollama_based_bot`: A local LLM-based chatbot built with Ollama.

Each folder includes the chatbot script and sample data required to run that version.

## Folder Contents

### `v1_list_based_bot`

A basic list-based chatbot implementation.

Files:
- `chatbot_app.py` - Main chatbot application.
- `chatbot2.py` - Alternate chatbot logic version.
- `chatbot2.1.py` - Another variant of list-based chatbot logic.
- `chatdata.csv` - CSV dataset containing user prompts and expected responses.
- `README.md` - Folder-specific notes for this version.

### `v2_list_semnatic_search_bot`

A chatbot that uses semantic search or keyword matching to find answers from CSV data.

Files:
- `sematic_chatbot.py` - Semantic search chatbot implementation.
- `chatdata.csv` - Dataset used for matching user queries.
- `README.md` - Folder-specific notes for this version.

### `v3_vector_db_based_bot`

A chatbot using vector embeddings and a local database for semantic similarity search.

Files:
- `semantic_chatbot2.py` - Vector database chatbot implementation.
- `chatdata.csv` - Text dataset used to build the vector store.
- `README.md` - Folder-specific notes for this version.
- `chat_database/` - Local vector database storage directory.

### `v4_local_llm_ollama_based_bot`

A local LLM-powered chatbot using Ollama.

Files:
- `chatbot.py` - Primary Ollama-based chatbot script.
- `requirements.txt` - Python dependencies for this version.
- `README.md` - Folder-specific notes for this version.

## Notes

- Each folder is self-contained for its respective chatbot version.
- Run the script in the folder that matches the approach you want to try.
- The repository was built as a chatbot project during an MCA course.

