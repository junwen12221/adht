from adht.common.network import Network, NetworkPackage


class EventHandler:
    def __init__(self, network: Network):
        self.network = network

    def handle(self, pkg: NetworkPackage):
        pass
