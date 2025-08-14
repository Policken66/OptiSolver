#   Задачи модуля loader.py
#   1. Принять путь к конфигу (YAML или JSON)
#   2. Прочитать и распарсить в Python-структуру с учетом формата
#   3. Выдать данные в стандартизованном виде следующему шагу (валидации)

def load_config(path: str) -> dict:
    """
    Загружает конфигурацию из YAML или JSON файла и возвращает как словарь Python.

    :param path: Путь к файлу конфигурации (.yaml, .yml, .json).
    :return: Словарь с данными конфигурации.
    :raises FileNotFoundError: Если файл не найден.
    :raises ValueError: Если формат файла не поддерживается или данные некорректны.
    :raises yaml.YAMLError / json.JSONDecodeError: Если парсинг не удался.
    """


def detect_format(path: str) -> str:
    """
    Определяет формат конфигурационного файла по расширению.

    :param path: Путь к файлу конфигурации.
    :return: 'yaml' или 'json'.
    :raises: ValueError: Если расширение неизвестно.
    """


def read_yaml(path: str) -> dict:
    """
    Читает YAML файл и возвращает данные как словарь.

    :param path: Путь к YAML файлу.
    :return: Словарь.
    :raises yaml.YAMLError: Если ошибка парсинга.
    """


def read_json(path: str) -> dict:
    """
    Читает JSON файл и возвращает данные как словарь.

    :param path: Путь к JSON файлу.
    :return: Словарь.
    :raises json.JSONDecodeError: Если ошибка парсинга.
    """