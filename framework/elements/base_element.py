
from selenium.webdriver.common.action_chains import ActionChains



class BaseElement:
    def __init__(self, driver, element):
        self.driver = driver
        self.element = element

    # def find_element_by_xpath(self, xpath):
    #     element = self.driver.find_element(By.XPATH, xpath)
    #     return element

    # def find_elements_by_xpath(self, xpath):
    #     elements = self.driver.find_elements(By.XPATH, xpath)
    #     return elements

    # def find_element_by_id(self, id):
    #     element = self.driver.find_element(By.ID, id)
    #     return element

    # def find_elements_by_id(self, id):
    #     elements = self.driver.find_elements(By.ID, id)
    #     return elements

    def click(self):
        self.element.click()

    def click_and_wait(self):
        self.click()
        # move to Browser
        page_state = self.driver.execute_script("return document.readyState;")
        try:
            assert page_state == "complete"
        except AssertionError:
            print("Page was not loaded after click event")

    def scroll_to_element(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.element)

    def move_cursor_to_element(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element)

    def send_keys(self, keys):
        self.element.send_keys(keys)
    
    def get_text(self):
        return self.element.text

    def get_attribute(self, attribute):
        return self.element.get_attribute(attribute)
