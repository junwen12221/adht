class Crypto:
    def __init__(self, public_key, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    @classmethod
    def load_from_file(cls, public_path, private_path=None):
        with open(public_path, 'wb') as pub_f:
            pub_key = pub_f.read()
        if private_path is not None:
            with open(private_path, 'wb') as pri_f:
                pri_key = pri_f.read()
        else:
            pri_key = None

        return cls(pub_key, pri_key)

    @classmethod
    def load_from_generate(cls):
        pub_k = b''
        pri_k = b''
        return cls(pub_k, pri_k)

    def process_with_public_key(self, data: bytes) -> bytes:
        assert self
        return data

    def process_with_private_key(self, data: bytes) -> bytes:
        assert self
        return data
