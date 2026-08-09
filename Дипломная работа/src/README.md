# Дипломная работа по проекту YouGile для автоматизации тестирования на Python

Автоматизация UI- и API-тестов проекта **YouGile** на Python.

В рамках дипломной работы реализованы:
- UI-тесты с использованием Selenium;
- API-тесты с использованием requests;
- отчётность через Allure;
- архитектура Page Object Model;
- хранение конфигурации и тестовых данных отдельно от кода.

---

## Шаги

### 1. Склонировать проект
git clone https://github.com/ser-ulyanov/Diplom_rabota.git

### 2. Перейти в папку проекта

cd Diplom_rabota

### 3. Установить зависимости
pip install -r requirements.txt

# Стек

- **pytest** — тестовый фреймворк;
- **selenium** — автоматизация UI-тестирования;
- **requests** — автоматизация API-тестирования;
- **allure-pytest** — генерация отчётов;
- **configparser** — работа с конфигурацией;
- **Page Object Model** — архитектура UI-тестов.

---

# Структура проекта

```
├── api/                       # хелперы для работы с API
│   └── project_api.py
│
├── config/                    # конфигурация проекта
│   ├── config_provider.py
│   └── data_provider.py
│
├── pages/                     # описание страниц приложения
│   ├── auth_page.py
│   └── main_page.py
│
├── test/                      # автотесты
│   ├── test_ui.py
│   └── test_api.py
│
├── conftest.py                # фикстуры pytest
├── config.ini                 # настройки окружения
├── test_data.json             # тестовые данные
├── pytest.ini                 # настройки pytest
└── requirements.txt           # зависимости проекта
```
---

# Запуск тестов

## Запуск UI-тестов
```
pytest -m "ui"
```
## Запуск API-тестов
```
pytest -m "api"
```
## Запуск всех тестов
```
pytest
```
---

# Allure отчёт

После запуска тестов результаты сохраняются в папку:
```
allure-files
```
Для просмотра отчёта выполнить:

```
allure serve allure-files
```
---

# Полезные ссылки

- [Подсказка по Markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файлов .gitignore](https://www.toptal.com/developers/gitignore)