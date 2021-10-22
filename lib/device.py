import lib.electropribor, lib.icpdas, lib.owen_pchv, lib.owen_io, lib.generator


class DeviceFactory:
    @staticmethod
    def create_device(port, config: dict):
        device_type = config.get('type', 'unknown')
        device_reg = {
            'unknown': DeviceUnknown,
            'щ02п': lib.electropribor.SH02P,
            'ген_1': lib.generator.Generator,
            'm7084': lib.icpdas.M7084,
            'пчв12': lib.owen_pchv.PCHV12,
            'мв110_8ас': lib.owen_io.AI8,
            'мв110_16д': lib.owen_io.DI16,
            'мв110_32р': lib.owen_io.DO32,
            'мв110_8и': lib.owen_io.AO8I,
        }
        device = device_reg.get(device_type,DeviceUnknown)
        return device(port=port, config=config)


class DeviceUnknown:
    def __init__(self, config):
        self.config = config
