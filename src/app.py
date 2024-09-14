from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store for simplicity
data_store = {}

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item), 200

@app.route('/items/<item_id>', methods=['POST'])
def create_item(item_id):
    if item_id in data_store:
        return jsonify({'error': 'Item already exists'}), 400
    data_store[item_id] = request.json
    return jsonify(data_store[item_id]), 201

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in data_store:
        return jsonify({'error': 'Item not found'}), 404
    data_store[item_id] = request.json
    return jsonify(data_store[item_id]), 200

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in data_store:
        return jsonify({'error': 'Item not found'}), 404
    del data_store[item_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
