import datetime
import hashlib


class SandBlock:
    def __init__(self, block_id: int, prev_hash: str, content: str):
        self.block_id = block_id
        self.ts = datetime.datetime.now()
        self.content = content
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    @staticmethod
    def get_hashing_method():
        return hashlib.sha256()

    def get_hashing_content(self) -> str:
        return str(self.block_id)+str(self.ts)+str(self.content)+str(self.prev_hash)

    def hash_block(self):
        hashing_method = self.get_hashing_method()
        hashing_content = self.get_hashing_content()
        hashing_method.update(hashing_content.encode('utf-8'))
        return hashing_method.hexdigest()

    def print_block_info(self):
        print('Block ID: {}'.format(self.block_id))
        print('Block timestamp: {}'.format(self.ts))
        print('Block content: {}'.format(self.content))
        print('Block hash: {}'.format(self.hash))
        print('Prev block hash: {}'.format(self.prev_hash))
