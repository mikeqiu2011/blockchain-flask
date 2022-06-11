import datetime
import hashlib
import json


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
            hash_value = self.get_hash(new_proof, previous_proof)
            print(f'hash value is:', hash_value)

            if hash_value[:4] == '0000':
                return new_proof

            new_proof += 1

    def get_hash(self, new_proof, previous_proof):
        payload = str(new_proof ** 2 - previous_proof ** 2).encode()
        hash_value = hashlib.sha256(payload).hexdigest()
        return hash_value

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        prev_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            cur_block = self.chain[block_index]

            # 1. check if previous block's hash is valid
            if cur_block['prev_hash'] != self.hash(prev_block):
                return False

            # 2. check if previous block's proof of work is valid
            prev_proof = prev_block['proof']
            cur_proof = cur_block['proof']
            hash_value = self.get_hash(cur_proof, prev_proof)
            print(f'hash value is:', hash_value)

            if hash_value[:4] != '0000':
                return False

            prev_block = cur_block
            block_index += 1

        return True

    def mine_block(self):
        prev_block = self.get_last_block()
        pow = self.proof_of_work(prev_block['proof'])
        prev_hash = self.hash(prev_block)
        block = self.create_block(pow, prev_hash)

        return block



