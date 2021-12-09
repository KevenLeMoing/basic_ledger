from src.sand_block import SandBlock


class SandChain:
    def __init__(self, ledger_length: int):
        self.ledger = [self.set_first_block]
        self.ledger_length = ledger_length

    @staticmethod
    def set_first_block() -> SandBlock:
        return SandBlock(block_id=0,
                         prev_hash='',
                         content='This is the first block of my first blockchain')

    def get_new_block(self, prev_block: SandBlock):
        new_id = prev_block.block_id + 1
        prev_hash = prev_block.hash
        content = 'I am the block nbr {}'.format(new_id)
        self.ledger.append(SandBlock(new_id, prev_hash, content))

    def print_chain_info(self):
        for block in len(self.ledger):
            self.ledger[block].print_block_info()
