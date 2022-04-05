from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from framework.utils.downloader import set_up_download_folder
from framework.utils import config_reader


class Browser:

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_current_page_title(self):
        current_page_title = self.driver.title()
        return current_page_title

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(self.driver.window_handles[window_handle])

    def page_reload(self):
        self.driver.execute_script("window.location.reload()")

    @staticmethod
    def browser_setup():
        factory_config = config_reader.get_factory_config()
        if factory_config["USE_DOWNLOADER"] == "True":
            default_download_path = set_up_download_folder()
        else:
            default_download_path = "\\"
        # весь иф сунуть в driver_factory, а потом юзать driver_factory тут
        if factory_config["BROWSER"] == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("--safebrowsing-disable-download-protection")
            file_prefs = {"download.default_directory": default_download_path,
                          "download.prompt_for_download": False,
                          "safebrowsing.enabled": True}
            options.add_experimental_option("prefs", file_prefs)
            if factory_config["HEADLESS_MODE"] == "True":
                options.add_argument("--headless")
            s = ChromeService(ChromeDriverManager().install())
        elif factory_config["BROWSER"] == "Firefox":
            options = FirefoxOptions()
            options.set_preference("browser.download.folderList", 2)
            options.set_preference(
                "browser.download.dir", default_download_path)
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference(
                "browser.download.viewableInternally.enabledTypes", "")
            options.set_preference(
                "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            options.set_preference(
                "browser.download.manager.showWhenStarting", False)
            if factory_config["HEADLESS_MODE"] == "True":
                options.headless = True
            s = FirefoxService(GeckoDriverManager().install())
        return s, options

    @staticmethod
    def tear_down(driver):
        """
        Driver tear down.
        """
        if (driver != None):
            print("Cleanup of test environment!")
            driver.close()
            driver.quit()
