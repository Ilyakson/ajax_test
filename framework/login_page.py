from framework.element_id import LoginPageElements, HomePageElements
from framework.page import Page


class LoginPage(Page):
    def login_user(self, email: str, password: str) -> None:
        self.click_element(LoginPageElements.BUTTON_LOGIN)
        self.fill_field(LoginPageElements.INPUT_EMAIL, email)
        self.fill_field(LoginPageElements.INPUT_PASSWORD, password)
        self.click_element(LoginPageElements.BUTTON_NEXT)

    def user_on_main_page(self) -> bool:
        return self.check_element_exist(HomePageElements.BUTTON_SIDEBAR)
