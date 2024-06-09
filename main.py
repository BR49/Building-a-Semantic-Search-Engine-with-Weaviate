import pandas as pd
import re

# Load dataset
data = pd.read_csv('arxiv-metadata-oai-snapshot.csv')

# Clean text
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    return text

data['abstract'] = data['abstract'].apply(clean_text)
data = data[['title', 'abstract']].dropna()  # Select relevant columns and drop NaNs

from transformers import BertModel, BertTokenizer
import torch

model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy().tolist()

data['embedding'] = data['abstract'].apply(get_embedding)

import weaviate

client = weaviate.Client("http://localhost:8080")

schema = {
    "classes": [
        {
            "class": "Document",
            "properties": [
                {"name": "title", "dataType": ["string"]},
                {"name": "abstract", "dataType": ["string"]},
                {"name": "embedding", "dataType": ["blob"]},
            ]
        }
    ]
}
client.schema.create(schema)

for index, row in data.iterrows():
    client.data_object.create({
        "title": row['title'],
        "abstract": row['abstract'],
        "embedding": row['embedding']
    }, "Document")
    
def query_embedding(query):
    return get_embedding(query)

query_vector = query_embedding("machine learning in healthcare")
response = client.query.get("Document", ["title", "abstract"]).with_near_vector({
    "vector": query_vector
}).do()

for result in response['data']['Get']['Document']:
    print(result['title'], result['abstract'])

from sklearn.metrics import precision_score, recall_score, f1_score

# Assuming we have true labels and predicted labels for evaluation
true_labels = [...]  # True relevance labels
predicted_labels = [...]  # Predicted relevance labels

precision = precision_score(true_labels, predicted_labels, average='weighted')
recall = recall_score(true_labels, predicted_labels, average='weighted')
f1 = f1_score(true_labels, predicted_labels, average='weighted')
print(f"Precision: {precision}, Recall: {recall}, F1 Score: {f1}")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    query_vector = query_embedding(query)
    response = client.query.get("Document", ["title", "abstract"]).with_near_vector({
        "vector": query_vector
    }).do()
    return jsonify(response['data']['Get']['Document'])

if __name__ == '__main__':
    app.run(debug=True)

