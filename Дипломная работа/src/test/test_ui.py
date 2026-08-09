import allure
import pytest


@pytest.mark.ui
@allure.title("Авторизация пользователя")
@allure.story("Авторизация")
def test_login(auth_page):
    with allure.step("Открыть страницу авторизации"):
        auth_page.open()
    with allure.step("Выполнить авторизацию"):
        auth_page.login()


@pytest.mark.ui
@allure.title("Создание проекта")
@allure.story("Работа с проектами")
def test_create_board(auth_page, main_page):
    with allure.step("Авторизоваться"):
        auth_page.open()
        auth_page.login()
    with allure.step("Создать проект"):
        main_page.create_board("Тестовый проект")
    with allure.step("Проверить создание проекта"):
        assert main_page.is_board_exists("Тестовый проект")


@pytest.mark.ui
@allure.title("Переименование проекта")
@allure.story("Работа с проектами")
def test_rename_board(auth_page, main_page):
    with allure.step("Авторизоваться"):
        auth_page.open()
        auth_page.login()
    with allure.step("Переименовать проект"):
        pass


@pytest.mark.ui
@allure.title("Перемещение проекта в архив")
@allure.story("Работа с проектами")
def test_archive_board(auth_page, main_page):
    with allure.step("Авторизоваться"):
        auth_page.open()
        auth_page.login()
    with allure.step("Переместить проект в архив"):
        main_page.archive_board("Тестовый проект")


@pytest.mark.ui
@allure.title("Удаление проекта")
@allure.story("Работа с проектами")
def test_delete_board(auth_page, main_page):
    with allure.step("Авторизоваться"):
        auth_page.open()
        auth_page.login()
    with allure.step("Удалить проект"):
        main_page.delete_board("Тестовый проект")
