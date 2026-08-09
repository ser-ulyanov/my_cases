from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_provider import ConfigProvider
from config.data_provider import DataProvider


class AuthPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.config = ConfigProvider()
        self.data = DataProvider()

        self.ui_auth_url = self.config.get("UI", "ui_auth_url")

        # Локаторы полей — по placeholder
        self.username_input = (
            By.CSS_SELECTOR, 'input[placeholder="example@mail.ru"]'
            )
        self.password_input = (
            By.CSS_SELECTOR, 'input[placeholder="Введите пароль"]'
            )

        # Локатор кнопки — div с ролью button и классом hint__cnt
        self.login_button = (By.CSS_SELECTOR, 'div[role="button"].hint__cnt')

        # Таймаут ожидания
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.ui_auth_url)

    def enter_email(self):
        field = self.wait.until(
            EC.presence_of_element_located(self.username_input)
        )
        field.clear()
        field.send_keys(self.data.get("email"))

    def enter_password(self):
        field = self.wait.until(
            EC.presence_of_element_located(self.password_input)
        )
        field.clear()
        field.send_keys(self.data.get("password"))

    def click_login(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )
        button.click()

    def login(self):
        self.open()
        self.enter_email()
        self.enter_password()
        self.click_login()
