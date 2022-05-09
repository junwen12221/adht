from adht.common.peer import Peer


class PeerPool:
    def __init__(self):
        self.pub_key_to_peer = {}

    def update_peer(self, peer: Peer):
        self.pub_key_to_peer[peer.pub_key] = peer

    def remove_peer(self, pub_key):
        del self.pub_key_to_peer[pub_key]
        