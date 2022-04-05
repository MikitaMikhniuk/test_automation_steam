from framework.utils.downloader import wait_for_download_finish
from steam.page_objects.base_steam_page import BaseSteamPage


class DownloadPage(BaseSteamPage):

    def __init__(self, driver):
        super().__init__(driver)

    INSTALL_BUTTON_XPATH = '//a[@class="about_install_steam_link"]'

    def download_installer(self, filename):
        """
        Method is used to click on "Download Steam" button.
        And wait for download finish.
        """
        install_button = self.find_element_by_xpath(self.INSTALL_BUTTON_XPATH)
        self.click_on_element(install_button)
        wait_for_download_finish(filename)
