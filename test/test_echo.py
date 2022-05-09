from adht.common.network import Network, NetworkPackage
from adht.common.peer import Peer
from adht.handler.echo import EchoHandler


def test_echo():
    network = Network()
    echo_handler = EchoHandler(network)
    dummy_address = object()
    peer = Peer(dummy_address, pub_key=b'')

    echo_pkg = NetworkPackage(b'echo me', peer)
    echo_handler.handle(echo_pkg)

    echo_back_pkg = network.get_send_queue().get()

    assert echo_pkg == echo_back_pkg
