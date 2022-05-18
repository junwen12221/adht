import asyncio

from adht.common.crypto import Crypto
from adht.common.network import Network, NetworkPackage
from adht.common.network_service import NetworkService
from adht.common.peer import Peer
from adht.handler.echo import EchoHandler


def test_echo_network():
    crypto = Crypto(b'')
    network = Network()
    echo_handler = EchoHandler(network)
    dummy_address = object()
    peer = Peer(dummy_address, crypto=crypto)

    echo_pkg = NetworkPackage(peer, b'echo me', False)
    echo_handler.handle(echo_pkg)

    echo_back_pkg = network.get_send_queue().get()

    assert echo_pkg == echo_back_pkg


def test_echo_network_service():
    port = 9123
    addr = ('127.0.0.1', port)
    crypto = Crypto(b'')
    network = Network()
    peer = Peer(addr, crypto=crypto)
    peer_dict = {addr: peer}

    echo_pkg = NetworkPackage(peer, b'echo me', False)

    loop = asyncio.get_event_loop()
    t = loop.create_datagram_endpoint(lambda: NetworkService(peer_dict, network, crypto), local_addr=('0.0.0.0', port))

    loop.run_until_complete(t)
    network.send(echo_pkg)
    loop.run_until_complete(asyncio.sleep(10))

    echo_back_pkg = network.recv()
    assert echo_pkg == echo_back_pkg
