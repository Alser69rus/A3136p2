import pytest
from conf.model import Model


def test_model():
    model = Model()
    assert model.port.owen.name == 'Ввод-вывод'

