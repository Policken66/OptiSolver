#   Задачи модуля loader.py
#   1. Принять путь к файлу конфигурации (YAML или JSON)
#   2. Прочитать и распарсить в Python-структуру с учетом формата
#   3. Выдать данные в стандартизованном виде следующему шагу (валидации)
import json
import pathlib
from typing import Dict, Any

try:
    import yaml  # PyYAML
except ImportError as e:
    yaml = None  # позволим импортировать модуль без PyYAML, но сообщим об этом при чтении .yaml


class ConfigFormatError(ValueError):
    """Неподдерживаемый формат или ошибка определения формата."""


class ConfigReadError(RuntimeError):
    """Ошибка чтения/парсинга конфигурационного файла."""


SUPPORTED_EXTENSIONS = {".yaml", ".yml", ".json"}


def detect_format(path: str | pathlib.Path) -> str:
    """
    Определяет формат конфигурационного файла по расширению.

    :param path: Путь к файлу конфигурации.
    :return: 'yaml' или 'json'.
    :raises: ConfigFormatError: Если расширение неизвестно/неподдерживаемое.
    """
    ext = pathlib.Path(path).suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise ConfigFormatError(
            f"Неподдерживаемое расширение '{ext}'. Допустимо: {','.join(sorted(SUPPORTED_EXTENSIONS))}."
        )

    return "yaml" if ext in {".yaml", ".yml"} else "json"


def read_yaml(path: str | pathlib.Path) -> Dict[str, Any]:
    """
    Читает YAML файл и возвращает данные как словарь.

    :param path: Путь к YAML-файлу.
    :return: Словарь с данными конфигурации.
    :raises ConfigReadError: Если PyYAML не установлен или парсинг завершился с ошибкой.
    """
    if yaml is None:
        raise ConfigReadError(
            "Пакет PyYAML не установлен. Установите 'pyyaml' или используйте JSON."
        )
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise ConfigReadError(f"Ошибка чтения YAML '{path}': {e}") from e

    if data is None:
        # пустой файл корректен для YAML, но нам нужен объект-словарь
        data = {}
    if not isinstance(data, dict):
        raise ConfigReadError(
            f"Ожидался объект верхнего уровня(mapping) в YAML '{path}', получено: {type(data).__name__}."
        )
    return data


def read_json(path: str | pathlib.Path) -> Dict[str, Any]:
    """
    Читает JSON файл и возвращает данные как словарь.

    :param path: Путь к JSON-файлу.
    :return: Словарь с данными конфигурации.
    :raises ConfigReadError: Если парсинг завершился с ошибкой или верхний уровень не объект.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise e
    except json.JSONDecodeError as e:
        raise ConfigReadError(
            f"Ошибка парсинга JSON '{path}' (строка {e.lineno}, столбец {e.colno}): {e.msg}"
        ) from e
    except Exception as e:
        raise ConfigReadError(f"Ошибка чтения JSON '{path}': {e}") from e

    if not isinstance(data, dict):
        raise ConfigReadError(
            f"Ожидался объект верхнего уровня (object) в JSON '{path}', получено: {type(data).__name__}."
        )
    return data


def load_config(path: str | pathlib.Path) -> Dict[str, Any]:
    """
    Загружает конфигурацию из YAML/JSON и возвращает словарь Python.

    :param path: Путь к файлу конфигурации (.yaml, .yml, .json).
    :return: Словарь конфигурации (как есть, без валидации и нормализации).
    :raises FileNotFoundError: Если файл не найден.
    :raises ConfigFormatError: Если формат не поддержан.
    :raises ConfigReadError: Ошибки парсинга/чтения.
    """
    path = pathlib.Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Файл конфигурации не найден: {path}")

    fmt = detect_format(path)
    if fmt == "yaml":
        return read_yaml(path)
    elif fmt == "json":
        return read_json(path)
    else:
        raise ConfigFormatError(f"Неизвестный формат: {fmt}")
