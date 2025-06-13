import hashlib
import time


class Block:
    # Block represents a single block in the blockchain
    def __init__(self, index, data, previous_hash=""):
        # Initialize block with index, data, and previous hash
        self.index = index
        self.timestamp = time.time()  # Store the creation time of the block
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = ""

    def calc_hash(self):
        # Calculate the SHA-256 hash of the block's contents
        s = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(s.encode()).hexdigest()

    def mine(self, difficulty):
        # Mine the block by finding a hash with a certain number of leading zeros
        prefix = "0" * difficulty
        print("Mining block...")
        start = time.time()
        while True:
            self.hash = self.calc_hash()
            if self.hash.startswith(prefix):
                break
            self.nonce += 1
        print(
            f"Block mined: {self.hash}\nNonce: {self.nonce}\nTime: {round(time.time() - start, 2)}s"
        )


# Create a block and mine it with difficulty 4
block = Block(1, "Some transaction data")  # Create a new block
block.mine(difficulty=4)  # Start mining process
