from src.sand_chain import SandChain


def add_blocks(blockchain: SandChain, nb_blocks: int) -> SandChain:
    for i in range(nb_blocks):
        blockchain.get_new_block(blockchain.ledger[i-1])
    return blockchain


my_blockchain = add_blocks(SandChain(10), 10)
my_blockchain.print_chain_info()

