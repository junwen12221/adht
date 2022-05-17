from adht.common.crypto import Crypto


class Peer:
    def __init__(self, address, crypto: Crypto):
        self.address = address
        self.crypto = crypto


