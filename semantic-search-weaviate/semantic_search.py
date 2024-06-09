def query_embedding(query):
    return get_embedding(query)

query_vector = query_embedding("machine learning in healthcare")
response = client.query.get("Document", ["title", "abstract"]).with_near_vector({
    "vector": query_vector
}).do()

for result in response['data']['Get']['Document']:
    print(result['title'], result['abstract'])

