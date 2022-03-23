import json

CONFIG_PATH = "framework\\resources\\factory_config.json"

def get_factory_config():
    config_file = open(CONFIG_PATH)
    factory_config = json.load(config_file)
    return factory_config