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
