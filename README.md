To run:

```
conda create -p venv python==3.10 -y
```

```
conda activate venv\
```

```
pip install -r requirements.txt
```

Add LANGCHAIN_API_KEY, OPENAI_API_KEY in .env

For OpenAI ChatBot:
```
cd OpenAIChatBot
```
```
streamlit run app.py
```

For Ollama ChatBot:
```
cd OllamaChatBot
```
```
streamlit run app.py
```