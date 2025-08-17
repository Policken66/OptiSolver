from Preprocessor.config.schema import ConfigModel


class NormalizationError(Exception):
    pass


def to_si(cfg: ConfigModel) -> ConfigModel:
    """
    Приводит значения конфигурации к СИ (сейчас pass-through).
    Если в будущем появятся поля с единицами, выполняем конвертацию здесь.
    :param cfg:
    :return:
    """

    return cfg
