from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):   #конструктор — метод, который вызывается, когда мы создаем объект.
                                                    # В него в качестве параметров передаем экземпляр драйвера и url адрес.
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # неявное ожидание

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
