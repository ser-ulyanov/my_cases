from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config_provider import ConfigProvider
from config.data_provider import DataProvider


class MainPage:
    """Класс для UI-работы с проектами YouGile."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.config = ConfigProvider()
        self.data = DataProvider()
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.project_card = (
            By.CSS_SELECTOR,
            "[data-testid='project-card']"
        )
        self.project_title = (
            By.CSS_SELECTOR,
            "[data-testid='project-title']"
        )
        self.menu_button = (
            By.CSS_SELECTOR,
            "[data-testid='project-card-menu-button']"
        )
        self.menu_item_edit = (
            By.CSS_SELECTOR,
            "[data-testid='menu-item-edit']"
        )
        self.menu_item_archive = (
            By.CSS_SELECTOR,
            "[data-testid='menu-item-archive']"
        )
        self.menu_item_delete = (
            By.CSS_SELECTOR,
            "[data-testid='menu-item-remove']"
        )
        self.edit_title_input = (
            By.CSS_SELECTOR,
            "input[data-testid='project-title-input']"
        )
        self.save_button = (
            By.CSS_SELECTOR,
            "button[data-testid='save-project-btn']"
        )
        self.create_button = (
            By.XPATH,
            "//span[text()='Добавить проект с задачами']"
        )
        self.board_name_input = (
            By.XPATH,
            "//input[@placeholder='Введите название проекта…']"
        )
        self.save_board_button = (
            By.XPATH,
            "//div[text()='Добавить проект с задачами']"
        )
        self.confirm_delete = (
            By.XPATH,
            "//div[contains(@class,'w-full') and text()='Удалить']"
        )
        self.project_id = (
            By.CSS_SELECTOR,
            ".text-secondary.px-4.bg-background-subtask-open"
        )

    def create_board(self, board_name: str) -> bool:
        """Создать новый проект."""
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.create_button)
            ).click()
            field = self.wait.until(
                EC.presence_of_element_located(self.board_name_input)
            )
            field.clear()
            field.send_keys(board_name)
            self.wait.until(
                EC.element_to_be_clickable(self.save_board_button)
            ).click()

            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{board_name}')]")
                )
            )
            return True
        except Exception as e:
            print(f"Ошибка при создании проекта: {e}")
            return False

    def _get_project_card(self, identifier: str, by_title: bool = True):
        """Найти карточку проекта по названию или ID."""
        try:
            cards = self.wait.until(
                EC.presence_of_all_elements_located(self.project_card)
            )
            for card in cards:
                if by_title:
                    title = card.find_element(*self.project_title).text
                    if title == identifier:
                        return card
                else:
                    try:
                        project_id = card.find_element(*self.project_id).text
                        if project_id == identifier:
                            return card
                    except Exception:
                        continue
            return None
        except TimeoutException:
            return None

    def _open_menu(self, board_name: str) -> None:
        """Открыть меню проекта."""
        menu_btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@data-testid='project-title' "
                    f"and contains(text(), '{board_name}')]"
                    f"/ancestor::div[@data-testid='project-card']"
                    f"//div[@data-testid='project-card-menu-button']"
                )
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            menu_btn
        )
        self.driver.execute_script(
            "arguments[0].click();",
            menu_btn
        )

    def update_board(self, identifier: str, new_title: str,
                     by_id: bool = False) -> bool:
        """Обновить название проекта."""
        try:
            card = self._get_project_card(identifier, not by_id)
            if not card:
                print(f"Проект '{identifier}' не найден")
                return False

            card.find_element(*self.menu_button).click()
            self.wait.until(
                EC.element_to_be_clickable(self.menu_item_edit)
            ).click()

            title_input = self.wait.until(
                EC.presence_of_element_located(self.edit_title_input)
            )
            title_input.clear()
            title_input.send_keys(new_title)
            self.wait.until(
                EC.element_to_be_clickable(self.save_button)
            ).click()

            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element(
                    self.project_title,
                    new_title
                )
            )
            return True
        except Exception as e:
            print(f"Ошибка при обновлении проекта: {e}")
            return False

    def archive_board(self, board_name: str) -> bool:
        """Переместить проект в архив."""
        try:
            self._open_menu(board_name)
            self.wait.until(
                EC.element_to_be_clickable(self.menu_item_archive)
            ).click()
            return True
        except Exception as e:
            print(f"Ошибка при архивации проекта: {e}")
            return False

    def delete_board(self, board_name: str) -> bool:
        """Удалить проект."""
        try:
            self._open_menu(board_name)
            self.wait.until(
                EC.element_to_be_clickable(self.menu_item_delete)
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(self.confirm_delete)
            ).click()

            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{board_name}')]")
                )
            )
            return True
        except Exception as e:
            print(f"Ошибка при удалении проекта: {e}")
            return False

    def get_project_title(self, board_name: str) -> str:
        """Получить название проекта."""
        try:
            card = self._get_project_card(board_name)
            if card:
                return card.find_element(*self.project_title).text
            return ""
        except Exception as e:
            print(f"Ошибка при получении названия: {e}")
            return ""

    def is_board_exists(self, board_name: str) -> bool:
        """Проверить существование проекта."""
        return board_name in self.driver.page_source
