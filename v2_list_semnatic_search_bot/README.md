# v2_list_semnatic_search_bot

A simple semantic search chatbot that uses sentence embeddings to match new user queries against stored training examples.

## Files
- `sematic_chatbot.py` - CLI chatbot using sentence-transformers embeddings
- `chatdata.csv` - existing `user_input` / `response_msg` pairs

## Requirements
- Python 3.8+
- `pandas`
- `numpy`
- `sentence-transformers`
- `torch` (installed automatically with sentence-transformers)

## Install
```bash
pip install pandas numpy sentence-transformers
```

## Run
```bash
python sematic_chatbot.py
```

## Notes
- The model `sentence-transformers/all-MiniLM-L6-v2` is downloaded automatically on first run.
- If the similarity score is below the threshold, the bot asks the user for a new response and updates `chatdata.csv`.
