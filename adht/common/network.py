
import queue
from typing import Optional

from adht.common.peer import Peer


class NetworkPackage:
    def __init__(self, msg: bytes, peer: Peer):
        self.msg = msg
        self.peer = peer


class Network:
    def __init__(self):
        self.send_queue: queue.Queue[NetworkPackage] = queue.Queue()
        self.recv_queue: queue.Queue[NetworkPackage] = queue.Queue()

    def get_send_queue(self):
        return self.send_queue

    def get_recv_queue(self):
        return self.recv_queue

    def send(self, pkg: NetworkPackage):
        self.get_send_queue().put(pkg)

    def recv(self) -> Optional[NetworkPackage]:
        try:
            return self.get_recv_queue().get(block=False)
        except queue.Empty:
            return None
