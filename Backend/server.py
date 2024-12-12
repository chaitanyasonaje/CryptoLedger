from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from blockchain import Blockchain

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Create a blockchain instance
blockchain = Blockchain()

@app.route('/get_chain', methods=['GET'])
def get_chain():
    chain_data = [
        {
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "hash": block.hash
        }
        for block in blockchain.chain
    ]
    response = {
        "chain": chain_data,
        "length": len(chain_data)
    }
    return jsonify(response), 200

@app.route('/add_block', methods=['POST'])
def add_block():
    json_data = request.get_json()
    data = json_data.get('data', '')

    if not data:
        return jsonify({"message": "Data for the block is missing."}), 400

    blockchain.add_block(data)
    response = {
        "message": "Block added successfully.",
        "new_block": {
            "index": blockchain.get_latest_block().index,
            "timestamp": blockchain.get_latest_block().timestamp,
            "data": blockchain.get_latest_block().data,
            "previous_hash": blockchain.get_latest_block().previous_hash,
            "hash": blockchain.get_latest_block().hash
        }
    }
    return jsonify(response), 201

@app.route('/is_chain_valid', methods=['GET'])
def is_chain_valid():
    is_valid = blockchain.is_chain_valid()
    response = {
        "is_valid": is_valid,
        "message": "The blockchain is valid." if is_valid else "The blockchain is not valid."
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
