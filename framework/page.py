from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver) -> None:
        self.driver = driver

    def check_element_exist(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(("id", locator))
            )
        except TimeoutException:
            return False
        else:
            return True

    def find_element(self, locator: tuple) -> WebElement:
        if not self.check_element_exist(locator):
            raise NoSuchElementException(f"Element {locator} does not exist")
        element = self.driver.find_element_by_id(locator)
        return element

    def click_element(self, locator: tuple) -> None:
        self.find_element(locator).click()

    def fill_field(self, locator: tuple, text: str) -> None:
        self.find_element(locator).send_keys(text)

    def back(self):
        self.driver.back()
