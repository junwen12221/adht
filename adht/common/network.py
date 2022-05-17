
import queue
from typing import Optional

from adht.common.peer import Peer


class NetworkPackage:
    def __init__(self, peer: Peer, msg: bytes, encoded: bool):
        self.peer = peer
        if not encoded:
            self.encoded_msg = self.peer.crypto.process_with_public_key(msg)
        else:
            self.encoded_msg = msg


class Network:
    def __init__(self):
        self.send_queue: queue.Queue[NetworkPackage] = queue.Queue()
        self.recv_queue: queue.Queue[NetworkPackage] = queue.Queue()
        self.send_cb = None

    def register_send_cb(self, cb):
        self.send_cb = cb

    def get_send_queue(self):
        return self.send_queue

    def get_recv_queue(self):
        return self.recv_queue

    def send(self, pkg: NetworkPackage):
        if self.send_cb:
            self.send_cb(pkg)
        else:
            self.get_send_queue().put(pkg)

    def recv(self) -> Optional[NetworkPackage]:
        try:
            return self.get_recv_queue().get(block=False)
        except queue.Empty:
            return None
