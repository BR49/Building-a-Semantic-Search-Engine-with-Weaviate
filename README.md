# Building-a-Semantic-Search-Engine-with-Weaviate

This project aims to build a semantic search engine using Weaviate, leveraging BERT embeddings, and the arXiv dataset. The search engine allows users to find relevant documents based on semantic similarity, making it useful for information retrieval tasks.

# Features
Semantic Search: Find documents based on semantic similarity rather than keyword matching.

BERT Embeddings: Utilize BERT pre-trained embeddings for capturing semantic information.

Weaviate Integration: Store and search documents efficiently using Weaviate's vector-based search capabilities.

Scalability: Demonstrates scalability for handling large datasets.

# Requirements

Python 3.x

Transformers library (for BERT embeddings)
Pandas

Weaviate Python client

Flask (optional for API)

# Installation
Clone the repository:

git clone https://github.com/br49/semantic-search-weaviate.git

cd semantic-search-weaviate

Install dependencies:

pip install -r requirements.txt

Download the arXiv dataset from Kaggle and place it in the project directory.

Ensure Weaviate server is running locally at http://localhost:8080 (or update the URL accordingly).

# Usage
Data Preprocessing and Embedding Generation: Run data_preprocessing.py to clean and preprocess the dataset and generate BERT embeddings.

Weaviate Integration: Run weaviate_integration.py to integrate the preprocessed data with Weaviate.

Semantic Search Implementation: Run semantic_search.py to perform semantic search based on user queries.

User Interface (Optional): Run app.py to start a Flask server for performing searches via API.

# Evaluation
Evaluation metrics such as precision, recall, and F1 score are calculated in evaluation.py.

# Results
Precision: 0.75

Recall: 0.75

F1 Score: 0.75

# Insights

Accuracy: The search engine achieved balanced precision and recall, indicating effective performance.

Improvements: Suggestions for fine-tuning BERT on domain-specific data and optimizing hyperparameters are provided.

Scalability: Weaviate efficiently handled the dataset, demonstrating scalability for large datasets.

# Conclusion
This project demonstrates advanced skills in machine learning, data preprocessing, and integration with Weaviate to build a functional semantic search engine.
