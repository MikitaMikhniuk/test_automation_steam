from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.browser import BROWSER
from framework.elements.element_factory import ELEMENT_FACTORY, ElementType
from framework.utils.nav_config import Nav


class BaseSteamPage(BasePage):
    """
    Base Steam page class.

    Contains basic methods available for all Steam pages.

    """

    def __init__(self, locator, title):
        super().__init__(locator, title)

    LANG_DROPDOWN_ID = (By.ID, "language_pulldown")
    INSTALL_BTN_XPATH = (By.XPATH, '//a[@class="header_installsteam_btn_content"]')

    def get_current_appid_from_url(self):
        """
        Methond is used to get app id of the current app page URL.

        Returns -> app id (str).
        """
        url = BROWSER.get_current_url()
        url_splitted = url.split("/")
        app_index = url_splitted.index("app")
        app_id = url_splitted[app_index + 1]
        return app_id

    def change_lang_to(self, lang):
        """
        Complex methond is used to change language on the page.

        Input -> Lang (str). Example: "russian", "english"
        """
        lang_drop = ELEMENT_FACTORY.get_element(
            ElementType.BUTTON, self.LANG_DROPDOWN_ID
        )
        lang_drop.click()
        part = f"ChangeLanguage( '{lang}' )"
        part_x = f'"{part}"'
        lang_locator = f"//a[contains(@onclick, {part_x})]"
        lang_btn = ELEMENT_FACTORY.get_element(
            ElementType.BUTTON, (By.XPATH, lang_locator)
        )
        lang_btn.click_and_wait()

    def check_for_current_lang(self, desired_lang):
        """
        Complex methond is used to check language on the page.

        Input -> Desired Lang code (str). Example: "en", "ru".
        Input -> Desired Lang full (str). Example: "english", "russian".
        """
        if Nav.LANG != desired_lang[:1]:
            self.change_lang_to(desired_lang)

    def navigate_to_download_page(self):
        """
        Help method is used to click on Global header download button.
        """
        btn = ELEMENT_FACTORY.get_element(ElementType.BUTTON, self.INSTALL_BTN_XPATH)
        btn.click_and_wait()
