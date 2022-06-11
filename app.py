from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/mine_block', methods=['POST'])
def mine_block():
    block = blockchain.mine_block()
    resp = {
        'message': 'Congratulations, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestampe'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(resp), 201
