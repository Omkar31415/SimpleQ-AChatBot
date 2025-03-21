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
Install Ollama application in your machine and in your terminal
```
ollama run model_name (eg: gemma2,mistral check: https://ollama.com/library for more info)
```
```
cd OllamaChatBot
```
```
streamlit run app.py
```

For RAG Document Q-A: Make sure to add your desired research paper pdf document to 'research_papers' folder
```
cd RAG Document Q-A
```
```
streamlit run app.py
```
