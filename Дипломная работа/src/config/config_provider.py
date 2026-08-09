import configparser


class ConfigProvider:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read("config.ini", encoding="utf-8")

    def get(self, section: str, key: str) -> str:
        return self.config[section][key]
