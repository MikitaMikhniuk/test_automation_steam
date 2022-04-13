from framework.elements.element_factory import ELEMENT_FACTORY, ElementType
from framework.utils.downloader import wait_for_download_finish
from framework.utils.lang_utils import get_label
from steam.page_objects.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By


class DownloadPage(BaseSteamPage):

    def __init__(self):
        super().__init__(self.AVAILABE_PLATFORMS, get_label("DownloadPageAnchor"))

    AVAILABE_PLATFORMS = (By.XPATH, "//div[@class='available_platforms']")
    INSTALL_BUTTON_XPATH = (By.XPATH, '//a[@class="about_install_steam_link"]')

    def download_installer(self, filename):
        """
        Method is used to click on "Download Steam" button.
        And wait for download finish.
        """
        button = ELEMENT_FACTORY.get_element(ElementType.BUTTON, self.INSTALL_BUTTON_XPATH)
        button.click()
        wait_for_download_finish(filename)
