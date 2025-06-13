import hashlib
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + self.previous_hash
            + str(self.nonce)
        )
        return hashlib.sha256(value.encode()).hexdigest()

    def __str__(self):
        return f"Block {self.index}:\nData: {self.data}\nHash: {self.hash}\nPrevHash: {self.previous_hash}\n"


# Create and link three blocks in the chain
# Each block contains its data, hash, and previous hash
block0 = Block(0, time.time(), "Genesis Block")
block1 = Block(1, time.time(), "Second Block", block0.hash)
block2 = Block(2, time.time(), "Third Block", block1.hash)

# Print the blocks and their hashes
print("--- Initial Blockchain State ---")
print("Each block contains its data, hash, and previous hash.")
print(block0)
print(block1)
print(block2)

# Tamper with block1's data and recalculate its hash
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()
print("\n--- After Tampering Block 1 ---")
print("Block 1's data was changed and its hash recalculated.")
print(
    "Notice: Block 2's previous hash still points to the old hash, breaking the chain."
)
print(block1)
print(block2)
