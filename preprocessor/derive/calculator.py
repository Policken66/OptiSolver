from math import isfinite
from typing import Dict

from preprocessor.config.schema import ConfigModel


class DerivationError(Exception):
    pass


def compute(cfg: ConfigModel) -> Dict[str, float]:
    """
    Возвращает словарь DerivedParam.
    Здесь считаем только, то что пользователь НЕ вводит.
    :param cfg:
    :return:
    """
    N = cfg.geometry.N
    m = cfg.geometry.m
    HH = cfg.geometry.HH

    if N <= 0 or m <= 0:
        raise DerivationError("Параметры N и m должны быть положительными.")

    tet = 360.0 / float(N) # град
    H = HH + HH / float(m)
    kk = H / float(m)

    for name, val in {"tet": tet, "H": H, "kk": kk}.items():
        if not isfinite(val):
            raise DerivationError(f"Невалидное значение {name}: {val}")

    return {"tet": tet, "H": H, "kk": kk}