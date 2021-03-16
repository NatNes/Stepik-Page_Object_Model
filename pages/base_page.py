class BasePage():
    def __init__(self, browser, url):   #конструктор — метод, который вызывается, когда мы создаем объект.
                                        # В него в качестве параметров передаем экземпляр драйвера и url адрес.
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
