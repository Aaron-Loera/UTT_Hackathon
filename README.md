# Swoop Advisor

By: [Aaron Loera](https://www.linkedin.com/in/aaronloera324/), [Matthew Emanuel](https://www.linkedin.com/in/matthew-emanuel-1b168a340/), [Melusi Senzanje](https://www.linkedin.com/in/melusi-senzanje-5b26102a4/) 

## Overview

This project leverages the power of **Langchain**, **Ollama**, and **Chroma** to create a document-based question answering system. It uses a vector database to store document chunks and retrieves relevant information based on user queries. The system is capable of ingesting CSV files, splitting them into manageable chunks, and embedding them into a vector space for efficient search and retrieval. The assistant, acting as a college advisor, answers questions by leveraging the stored data and the underlying models.

## Components

This project consists of three main Python scripts:

### chat.py
This script sets up the Langchain framework to initialize the models, the vector store (Chroma), and the retrieval chain. It also defines a prompt template to guide the assistant's responses.
### ingest.py
This script ingests CSV files from a given directory, splits them into smaller chunks, embeds them, and stores them into a vector database using Chroma. It checks for new documents at regular intervals.
### model.py
This script defines the Models class, which initializes the embedding and language models using Ollama’s APIs.
Setup and Installation

## To run this project, you will need to have the following dependencies installed:

Python 3.7+
pip for package management
Required Python Packages:
langchain
langchain_core
langchain_chroma
langchain_text_splitters
langchain_community
dotenv
uuid
time
os
Ollama (to get access to OllamaEmbeddings and ChatOllama)
You can install these dependencies by running:

`pip install langchain langchain_core langchain_chroma langchain_text_splitters langchain_community dotenv uuid`
You will also need access to Ollama’s models and APIs to use OllamaEmbeddings and ChatOllama.

## Example Interaction

Assistant: Ask anything

Human: Return a list of professors who teach computer science
Assistant: Assistant: Okay, based on the data provided, here’s a list of professors who teach Computer Science:

*   David Alger
*   Timothy Nix
*   Stephen Rainwater
*   Tom Roberts

Human: Who has the best ratings in the English Department
Assistant: Okay, based on the data provided, I would recommend **Matthew Kelly** as the best choice in the English department.

Here’s my reasoning:

*   **Highest Rating:** Matthew Kelly has the highest rating of 4.6.
*   **Lowest Retake Percentage:** He also has the lowest retake percentage at 93%, suggesting he grasped the material effectively.

While Mark Sidey has a decent rating of 3.0, and Emily Standridge has a respectable 3.2, Matthew Kelly’s superior rating and lower retake percentage make him the strongest candidate according to this data.


## Future Plans
Support for More File Formats: Expand the ingestion process to support additional file formats (e.g., PDFs, Word Documents).
Optimized Retrieval: Implement more advanced retrieval techniques to improve the relevance of returned documents.
User Feedback: Incorporate a feedback loop to allow the system to learn from user interactions.
License

Contact:[Aaron Loera](https://www.linkedin.com/in/aaronloera324/), [Matthew Emanuel](https://www.linkedin.com/in/matthew-emanuel-1b168a340/), [Melusi Senzanje](https://www.linkedin.com/in/melusi-senzanje-5b26102a4/) 

For further questions or contributions, please feel free to open an issue.
