import math
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

    # Расчет из файла MathCAD
    N_sp = cfg.geometry.N
    N_kol = N_sp / 2
    N_shp = 2
    alp = tet
    R = cfg.geometry.d / 2
    H = HH + HH / float(m)
    a = [cfg.geometry.a11, cfg.geometry.c, cfg.geometry.a22]
    b = [cfg.geometry.b11, cfg.geometry.dd, cfg.geometry.b22]

    V1 = H / (math.cos(alp) * 2 * N_sp * a[1] * b[1])
    V2 = N_kol * math.pi * 2 * R * a[2] * b[2]
    V3 = N_shp * math.pi * 2 * R * a[3] * b[3]
    V = V1 + V2 + V3

    for name, val in {"tet": tet, "H": H}.items():
        if not isfinite(val):
            raise DerivationError(f"Невалидное значение {name}: {val}")

    return {"tet": tet, "H": H}