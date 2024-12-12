import json
import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.load_chain()

    def create_genesis_block(self):
        # The first block in the chain (genesis block)
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, data):
        last_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, last_block.hash)
        self.chain.append(new_block)
        self.save_chain()

    def get_latest_block(self):
        return self.chain[-1]

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def save_chain(self):
        with open('blockchain_data.json', 'w') as file:
            json.dump([block.__dict__ for block in self.chain], file, default=str)

    def load_chain(self):
        try:
            with open('blockchain_data.json', 'r') as file:
                chain_data = json.load(file)
                self.chain = [Block(**block) for block in chain_data]
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is empty, start with the genesis block
            self.chain = [self.create_genesis_block()]
