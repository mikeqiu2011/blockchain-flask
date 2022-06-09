import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')  # create genisis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'prev_hash': previous_hash
        }

        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1

        while True:
            payload = str(new_proof**2 - previous_proof**2).encode()
            hash_value = hashlib.sha256(payload).hexdigest()
            print(f'hash value is:', hash_value)

            if hash_value[:4] == '0000':
                return new_proof
            else:
                new_proof +=1
