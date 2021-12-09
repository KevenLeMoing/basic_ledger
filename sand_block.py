import datetime
import hashlib


class SandBlock:
    def __init__(self, id: str, ts: datetime, prev_hash: str, content: str):
        self.id = id
        self.ts = ts
        self.prev_hash = prev_hash
        self.content = content
        self.hash = self.hash_block()

    def hash_block(self):
        pass
