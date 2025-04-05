from langchain_ollama import OllamaEmbeddings, ChatOllama

class Models:
    
    def __init__(self):
        self.embeddings_ollama = OllamaEmbeddings(model='nomic-embed-text:latest')
        self.model_ollama = ChatOllama(model='llama3.2:latest')