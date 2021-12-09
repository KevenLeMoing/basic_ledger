import datetime
import hashlib


class SandBlock:
    def __init__(self, id: int, ts: datetime, prev_hash: str, content: str):
        self.id = id
        self.ts = ts
        self.prev_hash = prev_hash
        self.content = content
        self.hash = self.hash_block()

    @staticmethod
    def get_hashing_method():
        return hashlib.sha256()

    @staticmethod
    def get_first_block():
        return SandBlock(id=0,
                         ts=datetime.datetime.now(),
                         prev_hash='',
                         content='This is the first block of my first blockchain')

    @staticmethod
    def get_new_block(prev_block: SandBlock):
        prev_id = prev_block.id + 1
        timestamp = d.datetime.now()
        prev_hash = prev_block.hash


    def newblock(lastblock):  # get the next block, the block that comes after the previous block (prevblock+1)
        index = lastblock.index + 1  # the id of this block will be equals to the previous block + 1, which is logic
        timestamp = d.datetime.now()  # The timestamp of the next block
        hashblock = lastblock.hash  # the hash of this block
        data = "Transaction " + str(index)  # The data or transactions containing in that block
        return Block(index, timestamp, data, hashblock)  # return the entire block

    def get_hashing_content(self):
        return str(self.id)+str(self.ts)+str(self.content)+str(self.prev_hash)

    def hash_block(self):
        hashing_method = self.get_hashing_method()
        hashing_content = self.get_hashing_content()
        hashing_method.update(hashing_content)
        return hashing_method.hexdigest()


