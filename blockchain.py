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
