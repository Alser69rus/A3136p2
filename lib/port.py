from PyQt5.QtCore import QObject, QThread, pyqtSignal
from pymodbus.client.sync import ModbusSerialClient as SerialClient


class PortFactory():
    @staticmethod
    def create_port(config: dict):
        port_type = config.get('type', 'modbus_rtu')
        port_reg = {'modbus_rtu': ModBusRTUSerialPort}
        port = port_reg.get(port_type, ModBusRTUSerialPort)
        return port(config)


class PortHandler(QObject):
    started = pyqtSignal()
    finished = pyqtSignal()
    updated = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.thread = QThread()
        self.device = []
        self.running = False

    def connect(self, device: QObject):
        self.device.append(device)
        device.moveToThread(self.thread)

    def start(self):
        self.moveToThread(self.thread)
        self.thread.started.connect(self.run)
        self.finished.connect(self.thread.quit)
        self.finished.connect(self.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def stop(self):
        self.running = False

    def run(self):
        self.started.emit()
        self.running = True
        while self.running:
            for dev in self.device:
                dev.update()
            self.updated.emit()
            QThread.msleep(1)
        self.finished.emit()


class ModBusRTUSerialPort(PortHandler):
    def __init__(self, name: str, port: str, baud: int = 9600, timeout: float = 1.0, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.client = SerialClient(method='rtu', port=port, baudrate=baud, timeout=timeout)
