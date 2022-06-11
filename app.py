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
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'prev_hash': block['prev_hash']
    }

    return jsonify(resp), 201


@app.route('/chain', methods=['GET'])
def get_chain():
    resp = {
        'chain': blockchain.get_chain(),
        'length': len(blockchain.get_chain())
    }

    return jsonify(resp), 200


# run the app
app.run(host='0.0.0.0', port=5000)
