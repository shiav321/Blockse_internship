import random

# Proof of Work (PoW)
# Each miner has a random power value. The miner with the highest power wins.
print("[PoW] The miner with the highest power wins the right to add the next block.")
miners = {"A": random.randint(10, 100), "B": random.randint(10, 100)}
print(f"Miners and their power: {miners}")
pow_winner = max(miners, key=miners.get)
print(f"[PoW] Winner: {pow_winner} with power {miners[pow_winner]}")

# Proof of Stake (PoS)
# Each staker has a random stake value. The staker with the highest stake is selected.
print(
    "\n[PoS] The staker with the highest stake is selected to validate the next block."
)
stakers = {"X": random.randint(100, 1000), "Y": random.randint(100, 1000)}
print(f"Stakers and their stake: {stakers}")
pos_winner = max(stakers, key=stakers.get)
print(f"[PoS] Winner: {pos_winner} with stake {stakers[pos_winner]}")

# Delegated Proof of Stake (DPoS)
# Delegates are voted by accounts. The one with the most votes is chosen.
print(
    "\n[DPoS] Delegates are voted by accounts; the one with the most votes is chosen as the block producer."
)
delegates = ["D1", "D2", "D3"]
votes = {"D1": 2, "D2": 3, "D3": 1}
print(f"Delegates and their votes: {votes}")
most_voted = max(votes, key=votes.get)
print(f"[DPoS] Delegate Elected: {most_voted} with {votes[most_voted]} votes")
