from PyQt5.QtCore import QObject


class Button(QObject):
    def __init__(self, name: str, device, pin: int = 0, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.device = device
        self.pin = pin
