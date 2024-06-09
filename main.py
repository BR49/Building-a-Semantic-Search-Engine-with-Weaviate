{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPN1ksSM+hlR0C8+L/VbGlr"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Bk7pImbswgLx"
      },
      "outputs": [],
      "source": [
        "pip install pandas transformers torch weaviate-client scikit-learn"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import re\n",
        "\n",
        "# Load dataset\n",
        "data = pd.read_csv('arxiv-metadata-oai-snapshot.csv')\n",
        "\n",
        "# Clean text\n",
        "def clean_text(text):\n",
        "    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags\n",
        "    text = re.sub(r'[^a-zA-Z\\s]', '', text)  # Remove special characters\n",
        "    text = text.lower()  # Convert to lowercase\n",
        "    return text\n",
        "\n",
        "data['abstract'] = data['abstract'].apply(clean_text)\n",
        "data = data[['title', 'abstract']].dropna()  # Select relevant columns and drop NaNs\n"
      ],
      "metadata": {
        "id": "RHwCivr1wnr5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from transformers import BertModel, BertTokenizer\n",
        "import torch\n",
        "\n",
        "model = BertModel.from_pretrained('bert-base-uncased')\n",
        "tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')\n",
        "\n",
        "def get_embedding(text):\n",
        "    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)\n",
        "    outputs = model(**inputs)\n",
        "    return outputs.last_hidden_state.mean(dim=1).detach().numpy().tolist()\n",
        "\n",
        "data['embedding'] = data['abstract'].apply(get_embedding)\n"
      ],
      "metadata": {
        "id": "lzU_lPMTwwAg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import weaviate\n",
        "\n",
        "client = weaviate.Client(\"http://localhost:8080\")\n",
        "\n",
        "schema = {\n",
        "    \"classes\": [\n",
        "        {\n",
        "            \"class\": \"Document\",\n",
        "            \"properties\": [\n",
        "                {\"name\": \"title\", \"dataType\": [\"string\"]},\n",
        "                {\"name\": \"abstract\", \"dataType\": [\"string\"]},\n",
        "                {\"name\": \"embedding\", \"dataType\": [\"blob\"]},\n",
        "            ]\n",
        "        }\n",
        "    ]\n",
        "}\n",
        "client.schema.create(schema)\n",
        "\n",
        "for index, row in data.iterrows():\n",
        "    client.data_object.create({\n",
        "        \"title\": row['title'],\n",
        "        \"abstract\": row['abstract'],\n",
        "        \"embedding\": row['embedding']\n",
        "    }, \"Document\")\n"
      ],
      "metadata": {
        "id": "oqJ4jhKlw1sw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def query_embedding(query):\n",
        "    return get_embedding(query)\n",
        "\n",
        "query_vector = query_embedding(\"machine learning in healthcare\")\n",
        "response = client.query.get(\"Document\", [\"title\", \"abstract\"]).with_near_vector({\n",
        "    \"vector\": query_vector\n",
        "}).do()\n",
        "\n",
        "for result in response['data']['Get']['Document']:\n",
        "    print(result['title'], result['abstract'])\n"
      ],
      "metadata": {
        "id": "qFbDk2vxxAO1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import precision_score, recall_score, f1_score\n",
        "\n",
        "# Assuming we have true labels and predicted labels for evaluation\n",
        "true_labels = [...]  # True relevance labels\n",
        "predicted_labels = [...]  # Predicted relevance labels\n",
        "\n",
        "precision = precision_score(true_labels, predicted_labels, average='weighted')\n",
        "recall = recall_score(true_labels, predicted_labels, average='weighted')\n",
        "f1 = f1_score(true_labels, predicted_labels, average='weighted')\n",
        "print(f\"Precision: {precision}, Recall: {recall}, F1 Score: {f1}\")\n"
      ],
      "metadata": {
        "id": "gWiBI7oPxW6D"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from flask import Flask, request, jsonify\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n",
        "@app.route('/search', methods=['GET'])\n",
        "def search():\n",
        "    query = request.args.get('query')\n",
        "    query_vector = query_embedding(query)\n",
        "    response = client.query.get(\"Document\", [\"title\", \"abstract\"]).with_near_vector({\n",
        "        \"vector\": query_vector\n",
        "    }).do()\n",
        "    return jsonify(response['data']['Get']['Document'])\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run(debug=True)"
      ],
      "metadata": {
        "id": "f4-UBD_3yG4O"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}