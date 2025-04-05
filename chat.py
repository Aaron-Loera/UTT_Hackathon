from models import Models
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma as CDb

# Initialize both LLM model and Embedding model
models =  Models()
embeddings  = models.embeddings_ollama
llm = models.model_ollama

# Storing location for vector database
vector_store = CDb(
    collection_name="documents",
    embedding_function=embeddings,
    persist_directory="./db/chroma_langchain_db"  # Vector store location
)

# Template used to guide response
prompt = ChatPromptTemplate.from_messages([("system", "You are a knowledgable and helpful college advisor. Answer the questions using \
                                            the provided context. If the context is not sufficient, say I need more information to \
                                            answer this. Do not make up information."),
                                           
                                            ("human", "Use the user input {input} to answer question. Use {context} to answer question.")])

# Define the retrieval chain
# Retriver from our vector store. To find and retrieve relevent docs
retriever = vector_store.as_retriever(search_kwargs={"k":10}) # 10 most relevant docs
combine_docs_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)


# Main loop
def main():
    while True:
        query = input("Please provide a question you need help with. Otherwise enter 'q' or 'quit' to end the conversation: ")
        if query.lower() in ['q', 'quit']:
            break
        result = retrieval_chain.invoke({"input": query})
        print(f"Retrieved Context: {result["context"]}\n")
        print(f"Assistant: {result.get("answer", "Sorry, I couldn't find a helpful response.")} \n\n")

# Run main loop
if __name__ ==  "__main__":
    main()
