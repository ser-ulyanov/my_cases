import allure
import pytest

board_id = None


@pytest.mark.api
@allure.title("Создание проекта через API")
@allure.story("API проекта")
def test_create_board(board_api):
    global board_id

    with allure.step("Создать проект"):
        response = board_api.create_board("Тестовый проект")

    with allure.step("Проверить статус ответа"):
        assert response.status_code == 201, (
            f"Ожидался 201, получен {response.status_code}. "
            f"Ответ: {response.text}"
        )

    with allure.step("Сохранить ID проекта"):
        board_id = response.json()["id"]


@pytest.mark.api
@allure.title("Получение проекта по ID")
@allure.story("API проекта")
def test_get_board(board_api):

    assert board_id is not None, "Сначала выполни test_create_board"

    with allure.step("Получить проект"):
        response = board_api.get_board(board_id)

    with allure.step("Проверить ответ"):
        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}. "
            f"Ответ: {response.text}"
        )


@pytest.mark.api
@allure.title("Обновление названия проекта")
@allure.story("API проекта")
def test_update_board(board_api):

    assert board_id is not None, "Сначала выполни test_create_board"

    with allure.step("Изменить название проекта"):
        response = board_api.update_board(
            board_id,
            "Новое название"
        )

    with allure.step("Проверить ответ"):
        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}. "
            f"Ответ: {response.text}"
        )


@pytest.mark.api
@allure.title("Удаление проекта")
@allure.story("API проекта")
def test_delete_board(board_api):

    assert board_id is not None, "Сначала выполни test_create_board"

    with allure.step("Удалить проект"):
        response = board_api.delete_board(board_id)

    with allure.step("Проверить ответ"):
        assert response.status_code in (200, 204), (
            f"Ожидался 200 или 204, получен {response.status_code}. "
            f"Ответ: {response.text}"
        )


@pytest.mark.api
@allure.title("Проверка списка проектов")
@allure.story("API проекта")
def test_get_boards(board_api):

    with allure.step("Получить список проектов"):
        response = board_api.get_boards()

    with allure.step("Проверить ответ"):
        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}. "
            f"Ответ: {response.text}"
        )
