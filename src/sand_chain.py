from src.sand_block import SandBlock


class SandChain:
    def __init__(self):
        self.set_first_block = self.set_first_block()

    @staticmethod
    def set_first_block():
        return SandBlock(block_id=0,
                         prev_hash='',
                         content='This is the first block of my first blockchain')

    @staticmethod
    def get_new_block(prev_block: SandBlock):
        new_id = prev_block.block_id + 1
        prev_hash = prev_block.hash
        content = 'I am the block nbr {}'.format(new_id)
        return SandBlock(new_id, prev_hash, content)

