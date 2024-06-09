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
