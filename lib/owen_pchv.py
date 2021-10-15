from PyQt5.QtCore import QObject


class PCHV12(QObject):
    def __init__(self, name: str, port_handler, unit: int, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.port_handler = port_handler
        self.unit = unit
        port_handler.connect(self)
