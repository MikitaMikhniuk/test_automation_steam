import codecs
from framework.elements.element_factory import ELEMENT_FACTORY, ElementType
from framework.utils.nav_config import Nav
from selenium.webdriver.common.by import By
import os
import json

LANG_DIR = "steam\\resources\\lang"


def load_config():
    """
    Method is used to parse project folder for lang json files.

    """
    config = {}
    for (dirpath, _, filenames) in os.walk(LANG_DIR):
        for filename in filenames:
            if filename.endswith('.json'):
                lang_name = filename.replace(".json", "")
                name = os.sep.join([dirpath, filename])
                with codecs.open(name, "r", encoding="UTF-8") as f:
                    loc = json.load(f)
                    config[lang_name] = loc
    return config


CONFIG = load_config()


def get_label(key, lang=None):
    """
    Method returns lang label for current lang.

    Input -> Key (str).

    Input (opt) -> Lang (str).
    """
    element = ELEMENT_FACTORY.get_element(ElementType.CONTAINER, (By.XPATH, "//html"))
    Nav.LANG = element.get_attribute("lang")
    l = Nav.LANG if not lang else lang
    if not l in CONFIG:
        raise Exception(f"Unsupported language {l}")
    if not key in CONFIG[l]:
        raise Exception(f"Unknown label for key {key} on language {l}")
    return CONFIG[l][key]
