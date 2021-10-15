from PyQt5.QtCore import QObject


class OwenDevice(QObject):
    def __init__(self, name: str, port_handler, unit: int, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.port_handler = port_handler
        self.unit = unit
        self.port_handler.connect(self)


class AI8(OwenDevice):
    def __init__(self, name: str, port_handler, unit: int, parent=None):
        super().__init__(name=name, port_handler=port_handler, unit=unit, parent=parent)


class DI16(OwenDevice):
    def __init__(self, name: str, port_handler, unit: int, parent=None):
        super().__init__(name=name, port_handler=port_handler, unit=unit, parent=parent)


class DO32(OwenDevice):
    def __init__(self, name: str, port_handler, unit: int, parent=None):
        super().__init__(name=name, port_handler=port_handler, unit=unit, parent=parent)


class AO8I(OwenDevice):
    def __init__(self, name: str, port_handler, unit: int, parent=None):
        super().__init__(name=name, port_handler=port_handler, unit=unit, parent=parent)
