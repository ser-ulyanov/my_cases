import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from api.project_api import ProjectApi


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def board_api():
    """Фикстура для работы с API проектов."""
    return ProjectApi()
