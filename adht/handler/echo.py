from adht.common.event_handler import EventHandler
from adht.common.network import NetworkPackage, Network


class EchoHandler(EventHandler):
    def __init__(self, network: Network):
        super().__init__(network)

    def handle(self, pkg: NetworkPackage):
        self.network.send(pkg)
