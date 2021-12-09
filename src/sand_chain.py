import datetime

from src.sand_block import SandBlock


class SandChain:
    def __init__(self):
        self.set_first_block = self.set_first_block()

    @staticmethod
    def set_first_block():
        return SandBlock(id=0,
                         ts=datetime.datetime.now(),
                         prev_hash='',
                         content='This is the first block of my first blockchain')