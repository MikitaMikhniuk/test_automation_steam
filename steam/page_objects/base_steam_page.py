from framework.base.base_element import BaseElement
from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.utils.browser import Browser
from framework.utils.nav_config import Nav


class BaseSteamPage(BasePage, BaseElement):
    """
    Base Steam page class.

    Contains basic methods available for all Steam pages.

    """

    def __init__(self):
        super().__init__()

    LANG_DROPDOWN_ID = "language_pulldown"
    MAIN_CONTENT_XPATH = (By.XPATH, '//div[@class="responsive_page_frame with_header"]')
    INSTALL_BTN_XPATH = '//a[@class="header_installsteam_btn_content"]'

    def get_current_appid_from_url(self):
        """
        Methond is used to get app id of the current app page URL.

        Returns -> app id (str).
        """
        browser = Browser()
        url = browser.get_current_url()
        url_splitted = url.split("/")
        app_index = url_splitted.index("app")
        app_id = url_splitted[app_index + 1]
        return app_id

    def get_current_appid_from_link(self, url):
        """
        Methond is used to get app id from any link.

        Input -> URL (str).

        Returns -> app id (str).
        """
        url_splitted = url.split("/")
        app_index = url_splitted.index("app")
        app_id_raw = url_splitted[app_index + 1]
        app_id_splitted = app_id_raw.split("?")
        app_id = app_id_splitted[0]
        return app_id

    def get_lang_locator(self, lang): # Соединить с метдом ниже
        """
        Methond is used to generate a lang locator.

        Input -> Lang (str). Example: "russian", "english"

        Returns -> Lang Locator (str).
        """
        part = f"ChangeLanguage( '{lang}' )"
        part_x = f'"{part}"'
        lang_locator = f"//a[contains(@onclick, {part_x})]"
        return lang_locator

    def change_lang_to(self, lang):
        """
        Complex methond is used to change language on the page.

        Input -> Lang (str). Example: "russian", "english"
        """
        lang_drop = self.find_element_by_id(self.LANG_DROPDOWN_ID)
        self.click_on_element(lang_drop)
        lang_locator = self.get_lang_locator(lang)
        lang_btn = self.find_element_by_xpath(lang_locator)
        self.click_on_element(lang_btn)

    def check_for_current_lang(self, desired_lang_code, desired_lang_full):
        """
        Complex methond is used to check language on the page.

        Input -> Desired Lang code (str). Example: "en", "ru".
        Input -> Desired Lang full (str). Example: "english", "russian".
        """
        if Nav.LANG != desired_lang_code:
            self.change_lang_to(desired_lang_full)
            browser = Browser()
            browser.page_reload()
        else:
            pass

    def navigate_to_download_page(self):
        """
        Help method is used to click on Global header download button.
        """
        btn = self.find_element_by_xpath(self.INSTALL_BTN_XPATH)
        self.click_and_wait(btn)
