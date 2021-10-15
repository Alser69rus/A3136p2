import pytest
from lib.port import ModBusRTUSerialPort

NAME = 'port'
PORT = 'COM1'
BAUD = 38400
TIMEOUT = 0.05


def test_port():
    port = ModBusRTUSerialPort(name=NAME, port=PORT, baud=BAUD, timeout=TIMEOUT)
    assert port.name == NAME
    assert port.port == PORT
    assert port.baud == BAUD
    assert port.timeout == TIMEOUT
    assert port.client.port == PORT
    assert port.client.baudrate == BAUD
    assert port.client.timeout == TIMEOUT
