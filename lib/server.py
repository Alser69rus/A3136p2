from PyQt5.QtCore import QObject
from lib.port import PortFactory
from lib.device import DeviceFactory


class Server(QObject):
    def __init__(self, config, parent=None):
        super().__init__(parent=parent)

        self.port = {}
        for key, value in config['port'].items():
            self.port[key] = PortFactory.create_port(value)

        self.device = {}
        for key, value in config['device'].items():
            port = self.port.get(value['port'], 'None')
            self.device[key] = DeviceFactory(port=port, config=value)
