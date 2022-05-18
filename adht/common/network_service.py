import asyncio
import socket

from adht.common.crypto import Crypto
from adht.common.network import Network, NetworkPackage
from adht.common.peer import Peer


class NetworkService(asyncio.DatagramProtocol):
    def __init__(self, peer_dict: {(str, int): Peer}, network: Network, crypto: Crypto):
        super().__init__()
        self.transport = None
        self.peer_dict: {(str, int): Peer} = peer_dict
        self.network = network
        self.crypto: Crypto = crypto
        self.network.register_send_cb(self.send_cb)

    def connection_made(self, transport) -> "Used by asyncio":
        print('connection made.')
        self.transport = transport

    def datagram_received(self, data, addr) -> "Main entrypoint for processing message":
        # Here is where you would push message to whatever methods/classes you want.
        print(f"Received Syslog message: {data}")
        decoded_data = self.crypto.process_with_private_key(data)
        if addr in self.peer_dict:
            peer = self.peer_dict[addr]
        else:
            peer = Peer.unknown_peer(addr)
        self.network.recv_queue.put(NetworkPackage(peer, decoded_data, True), block=True, timeout=1)

    @staticmethod
    def send_cb(packet):
        print(f"resume_writing.")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        sock.sendto(packet.encoded_msg, packet.peer.address)
