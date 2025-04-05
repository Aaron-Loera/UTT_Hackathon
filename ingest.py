import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma  import Chroma as CDb
from models import Models
from uuid import uuid4

# Initialize the models
models = Models()
embeddings  = models.embeddings_ollama
llm = models.model_ollama

# Define constants
knowledge_base = "./knowledge_base"  # TODO: Add relevant textbook to vector store
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 50
CHECK_INTERVAL = 10

# Chroma vector store
vector_store = CDb(collection_name = "documents",
                   embedding_function = embeddings,
                   persist_directory = "./db/chroma_langchain_db") # Storing vector space locally

# Ingest file, load and split file
def ingest_file(file_path):
    '''
    Processes file from inputted file path, extracts its content, chunks the data, and stores it
    a vector database.
    '''
    print(f'Ingesting: {file_path}')
    loader =  PyPDFLoader(file_path)
    
    # Load and extract text from file
    loaded_docs =  loader.load()
    
    # Parse File
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = CHUNK_SIZE,
                                                   chunk_overlap = CHUNK_OVERLAP,
                                                   separators= ['\n', " ", ""])

    documents = text_splitter.split_documents(loaded_docs)
    uuids = [str(uuid4()) for _ in range(len(documents))]
    print(f'Adding {len(documents)} chunks to vector space')
    
    # Add chunks to CDb
    vector_store.add_documents(documents=documents, ids=uuids)
    print(f'Ingested: {file_path}')


# Main Loop
def main():
    while True:
        for filename in os.listdir(knowledge_base):
            if not filename.startswith('_'):
                # To prevent adding same document twice
                file_path = os.path.join(knowledge_base, filename) 
                ingest_file(file_path)
                new_filename  = '_' + filename
                new_filepath = os.path.join(knowledge_base, new_filename)
                os.rename(file_path, new_filepath)
            time.sleep(CHECK_INTERVAL) # Check every period for new documents


# Run main loop
if __name__ == "__main__":
    main()