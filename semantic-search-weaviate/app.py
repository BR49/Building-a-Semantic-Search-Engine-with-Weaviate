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
