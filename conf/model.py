from collections import namedtuple

from PyQt5.QtCore import QObject

from lib.controls import Button as Btn
from lib.electropribor import SH02P
from lib.generator import Generator
from lib.icpdas import M7084
from lib.owen_io import AI8, DI16, DO32, AO8I
from lib.owen_pchv import PCHV12
from lib.port import ModBusRTUSerialPort as PortHandler

Dev = QObject


class Model(QObject):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        Port = namedtuple('Port', 'owen pchv gen freq')
        self.port = Port(
            owen=PortHandler('Ввод-вывод', 'COM1', 38400, timeout=0.1),
            pchv=PortHandler('ПЧВ', 'COM2', 38400, timeout=0.1),
            gen=PortHandler('Генератор', 'COM4', 115200, timeout=0.1),
            freq=PortHandler('Частотомер', 'COM7', 38400, timeout=0.1),
        )

        Device = namedtuple('Device', 'ai di do1 do2 ao pchv gen freq')
        self.device = Device(
            ai=AI8('Аналоговый ввод', self.port.owen, 8),
            di=DI16('Дискретный ввод', self.port.owen, 9),
            do1=DO32('Дискретный вывод 1', self.port.owen, 1),
            do2=DO32('Дискретный вывод 2', self.port.owen, 5),
            ao=AO8I('Аналоговый вывод', self.port.owen, 6),
            pchv=PCHV12('ПЧВ', self.port.pchv, 2),
            gen=Generator('Генератор', self.port.gen, 100),
            freq=M7084('Частотомер', self.port.freq, 3)
        )

        AnalogDevice = namedtuple('AnalogDevice', 'pv1 pv2 pa1 pa2 pa3')
        self.analog_device = AnalogDevice(
            pv1=SH02P('PV1', self.port.owen, 11),
            pv2=SH02P('PV2', self.port.owen, 12),
            pa1=SH02P('PA1', self.port.owen, 21),
            pa2=SH02P('PA2', self.port.owen, 22),
            pa3=SH02P('PA3', self.port.owen, 23),
        )
        Button = namedtuple('Button', 'up down back yes')
        self.button = Button(
            up=Btn('ВВЕРХ', self.device.di, 4),
            down=Btn('ВНИЗ', self.device.di, 7),
            back=Btn('НАЗАД', self.device.di, 6),
            yes=Btn('ДА', self.device.di, 5),
        )
