from src.sand_chain import SandChain
from src.sand_block import SandBlock


def add_blocks(blockchain) -> SandChain:
    for i in range (1,5):
        blockchain.add_new_block(blockchain.ledger[i-1])
    return blockchain

chain = SandChain()
my_blockchain = add_blocks(chain)
my_blockchain.print_chain_info()
