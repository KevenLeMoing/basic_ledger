from src.sand_chain import SandChain
from src.sand_block import SandBlock


def add_blocks(blockchain) -> SandChain:
    for i in range (1,5):
        blockchain.get_new_block(blockchain.ledger[i-1])
    return blockchain

#chain = SandChain(10)
#my_blockchain = add_blocks()
#my_blockchain.print_chain_info()

block = SandBlock(block_id=0, prev_hash='', content='This is the first block of my first blockchain')
block.print_block_info()
