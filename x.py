import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, difficulty=4):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    def compute_hash(self):
        block_content = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }
        block_string = json.dumps(block_content, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self):
        """Basic Proof-of-Work: Find a hash with a certain number of leading zeros."""
        while True:
            hash_attempt = self.compute_hash()
            if hash_attempt[:self.difficulty] == '0' * self.difficulty:
                return hash_attempt
            self.nonce += 1

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Creates the first block in the blockchain."""
        genesis_block = Block(0, "Genesis Block", "0", self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        """Adds a new block to the chain."""
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, last_block.hash, self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Validates the blockchain by checking hashes."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def tamper_with_chain(self, block_index, new_data):
        """Simulates tampering by modifying a block's data."""
        if 0 < block_index < len(self.chain):
            self.chain[block_index].transactions = new_data
            self.chain[block_index].hash = self.chain[block_index].compute_hash()
        else:
            print("Invalid block index")

    def print_chain(self):
        """Displays the blockchain in a readable format."""
        for block in self.chain:
            print(json.dumps({
                'index': block.index,
                'timestamp': block.timestamp,
                'transactions': block.transactions,
                'previous_hash': block.previous_hash,
                'hash': block.hash
            }, indent=4))

# Testing the Blockchain
if __name__ == "__main__":
    my_blockchain = Blockchain()
    my_blockchain.add_block(["Alice pays Bob 10 BTC", "Charlie pays Dave 5 BTC"])
    my_blockchain.add_block(["Eve pays Frank 2 BTC"])
    
    print("\nBlockchain before tampering:")
    my_blockchain.print_chain()
    
    print("\nIs blockchain valid?", my_blockchain.is_chain_valid())
    
    # Tamper with a block
    my_blockchain.tamper_with_chain(1, ["Alice pays Bob 100 BTC"])
    
    print("\nBlockchain after tampering:")
    my_blockchain.print_chain()
    
    print("\nIs blockchain valid?", my_blockchain.is_chain_valid())
