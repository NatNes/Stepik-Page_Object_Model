from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):    # В аргументы больше не надо передавать экземпляр браузера, мы его передаем
                                   # и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент
                                   # self , чтобы иметь доступ к атрибутам и методам класса
        # login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK),\
            "Login link is not presented"
