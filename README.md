# PaperQuery

## Overview
PaperQuery is a FastAPI-based application that allows users to load models in a ZILLIZ cluster and ask questions based on research papers. The system processes research papers by generating embeddings and storing them in a vector database for efficient retrieval. This allows users to perform semantic searches and retrieve relevant information quickly.

## Features
- Load and process research papers in PDF format.
- Generate embeddings using OpenAI, Google Generative AI, or Ollama.
- Store embeddings in a ZILLIZ vector database for efficient retrieval.
- Query and retrieve relevant answers based on user input.
- Provides context for answers, including document source information.

## Installation

### 1. Clone the Repository
   ```sh
   git clone <repo-url>
   cd PaperQuery
   ```

### 2. Install Dependencies
   ```sh
   pip install -r requirements.txt
   ```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and set your required environment variables:
   ```
   ZILLIZ_ENDPOINT=<your_zilliz_endpoint>
   ZILLIZ_TOKEN=<your_zilliz_token>
   GOOGLE_API_KEY=<your_google_api_key>
   ```

### 4. Prepare Research Papers
All research papers should be placed in the `papers/` directory before processing. Ensure that they are in PDF format for proper extraction and embedding generation.

### 5. Generate Embeddings
Run the following command to extract text, create embeddings, and store them in the vector database:
   ```sh
   python document_ingestion.py
   ```
This script will:
- Load all research papers from the `papers/` directory.
- Split the text into manageable chunks.
- Generate embeddings using the configured model.
- Store the embeddings in the ZILLIZ vector database for retrieval.

### 6. Start the FastAPI Server
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

### 1. Retrieve Homepage
- **Endpoint:** `GET /`
- **Description:** Returns the homepage.
- **Response:** Serves `index.html` from the `static/` directory.

### 2. Ask a Question
- **Endpoint:** `POST /chat`
- **Description:** Accepts a user query and returns a relevant answer along with the source context.
- **Request Format:**
   ```json
   {
       "message": "What is the main finding of the research paper?"
   }
   ```
- **Response Format:**
   ```json
   {
       "context": "Relevant excerpts from research papers",
       "answer": "Summarized response based on the retrieved content"
   }
   ```

## Usage
1. Ensure all research papers are placed in the `papers/` directory.
2. Run `document_ingestion.py` to process and store embeddings.
3. Start the FastAPI server using `uvicorn`.
4. Use the `/chat` endpoint to ask questions and receive AI-generated answers based on research papers.

## Future Enhancements
- Implement additional LLM models for embeddings.
- Improve document preprocessing and filtering mechanisms.
- Optimize query performance using advanced retrieval techniques.
- Expand support for other document formats beyond PDF.
- Implement a user-friendly web interface for interactive querying.


