import datetime
import hashlib


class SandBlock:
    def __init__(self, id: str, ts: datetime, prev_hash: str, content: str):
        self.id = id
        self.ts = ts
        self.prev_hash = prev_hash
        self.content = content
        self.hash = self.hash_block()

    @staticmethod
    def get_hashing_method():
        return hashlib.sha256()

    def get_hashing_content(self):
        return str(self.id)+str(self.ts)+str(self.content)+str(self.prev_hash)

    def hash_block(self):
        hashing_method = self.get_hashing_method()
        hashing_content = self.get_hashing_content()
        hashing_method.update(hashing_content)
        return hashing_method.hexdigest()
