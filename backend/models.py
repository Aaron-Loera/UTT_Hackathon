from langchain_ollama import OllamaEmbeddings, ChatOllama

class Models: 
    def __init__(self):
        # Snowflake embedding model, BERT arch
        self.embeddings_ollama = OllamaEmbeddings(
            model = 'snowflake-arctic-embed:22m',
        )

        self.model_ollama = ChatOllama(
            model =  'llama2:latest'
        )
