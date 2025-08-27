from typing import Dict, Any

from pydantic import ValidationError

from preprocessor.config.schema import ConfigModel


class ConfigValidationError(Exception):
    """Человекочитаемая ошибка валидации входной конфигурации."""


def validate_config(data: Dict[str, Any]) -> ConfigModel:
    """
    Преобразует сырые данные (из loader.load_config) в типизированный объект ConfigModel.
    Поднимает подробную ошибку при несоответствии структуры/типов/ограничений.
    :param data:
    :return:
    """
    try:
        return ConfigModel.model_validate(data)
    except ValidationError as e:
        # Сформируем полезный и компактный текст для отчета/лога
        msgs = []
        for err in e.errors():
            loc = ".".join(str(x) for x in err.get("loc", []))
            msg = err.get("msg", "invalid value")
            typ = err.get("type", "")
            msgs.append(f"- {loc}: {msg} ({typ})")
        text = "Конфигурация не прошла валидацию:\n" + "\n".join(msgs)
        raise ConfigValidationError(text) from e
