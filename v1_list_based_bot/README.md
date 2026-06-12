# v1_list_based_bot

A basic Python chatbot that uses `chatdata.csv` as its knowledge base.
This version includes a terminal chatbot, a Streamlit UI chatbot, and a `Bot` class example.

## Files
- `chatbot_app.py` - Streamlit chat UI that reads and writes `chatdata.csv`
- `chatbot2.py` - CLI chatbot with learning from user input
- `chatbot2.1.py` - `Bot` class implementation that reads `chatdata.csv`
- `chatdata.csv` - stored chat pairs with `user_input` and `response_msg`

## Requirements
- Python 3.8+
- `pandas`
- `streamlit` (only for `chatbot_app.py`)

## Install
```bash
pip install pandas streamlit
```

## Run
- CLI bot: `python chatbot2.py`
- Bot class example: `python -c "from chatbot2.1 import Bot; Bot().chatbot()"`
- Streamlit bot: `streamlit run chatbot_app.py`

## Notes
- Type `exit` to quit the CLI bot.
- Unknown user input is stored in `chatdata.csv` so the bot can learn.
