from typing import Dict
import requests
from config.config_provider import ConfigProvider
from config.data_provider import DataProvider


class ProjectApi:
    """Класс для работы с проектами YouGile через API."""

    def __init__(self) -> None:
        self.config = ConfigProvider()
        self.data = DataProvider()

        self.base_url: str = self.config.get("API", "api_base_url")
        self.token: str = self.data.get("token")

        self.headers: Dict[str, str] = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_board(self, title: str) -> requests.Response:
        """
        Создать новый проект.
        POST /projects
        """
        payload = {"title": title}
        response = requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers
        )
        return response

    def get_board(self, board_id: str) -> requests.Response:
        """
        Получить проект по ID.
        GET /projects/{id}
        """
        response = requests.get(
            f"{self.base_url}/projects/{board_id}",
            headers=self.headers
        )
        return response

    def get_boards(self) -> requests.Response:
        """
        Получить список всех проектов.
        GET /projects
        """
        response = requests.get(
            f"{self.base_url}/projects",
            headers=self.headers
        )
        return response

    def update_board(self, board_id: str, title: str) -> requests.Response:
        """
        Обновить название проекта.
        PUT /projects/{id}
        """
        payload = {"title": title}
        response = requests.put(
            f"{self.base_url}/projects/{board_id}",
            json=payload,
            headers=self.headers
        )
        return response

    def delete_board(self, board_id: str) -> requests.Response:
        """
        Удалить проект (софт-удаление через PUT).
        PUT /projects/{id}
        """
        payload = {"deleted": True}
        response = requests.put(
            f"{self.base_url}/projects/{board_id}",
            json=payload,
            headers=self.headers
        )
        return response
