import json
import pytest


def test_config():
    with open(r'conf/config.json', 'r') as file:
        config = json.load(file)
        assert config
        assert config['port']
        assert config['device']
        assert config['controls']

