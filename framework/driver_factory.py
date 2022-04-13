from selenium import webdriver
from framework.utils import json_reader
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from framework.utils.downloader import set_up_download_folder
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

CONFIG_PATH = "steam\\resources\\factory_config.json"


class DriverFactory:
    """
    Creates a webdriver instance based on factory_config.json

    """

    @staticmethod
    def get_driver():
        factory_config = json_reader.get_json(CONFIG_PATH)
        if factory_config["USE_DOWNLOADER"] == "True":
            default_download_path = set_up_download_folder()
        else:
            default_download_path = "\\"
        if factory_config["BROWSER"] == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--safebrowsing-disable-download-protection")
            file_prefs = {
                "download.default_directory": default_download_path,
                "download.prompt_for_download": False,
                "safebrowsing.enabled": True,
            }
            options.add_experimental_option("prefs", file_prefs)
            if factory_config["HEADLESS_MODE"] == "True":
                options.add_argument("--headless")
            s = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=s, options=options)
        elif factory_config["BROWSER"] == "Firefox":
            options = FirefoxOptions()
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.dir", default_download_path)
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference(
                "browser.download.viewableInternally.enabledTypes", ""
            )
            options.set_preference(
                "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream"
            )
            options.set_preference("browser.download.manager.showWhenStarting", False)
            if factory_config["HEADLESS_MODE"] == "True":
                options.headless = True
            s = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=s, options=options)
        else:
            raise Exception("I don't know such driver yet!")
        return driver
