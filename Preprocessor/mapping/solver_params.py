from typing import Dict, Any

from Preprocessor.config.schema import ConfigModel

REQUIRED_NAMES = (
    "a11", "b11", "c", "dd", "a22", "b22",
    "N", "m", "d", "HH", "nn",
    "E1", "E2", "PoissonRatio", "Density",
    "MZ", "FZ"
)


class MappingError(Exception):
    pass


def build_solver_params(cfg: ConfigModel, drv: Dict[str, float]) -> Dict[str, Any]:
    """
    Формирует плоский словарь переменных для подстановки в APDL.
    Принимает валидированную конфигурацию и набор производных параметров.
    Возвращает ровно те ключи, которые ждет шаблон 1.txt/
    :param cfg:
    :param drv:
    :return:
    """

    g, mat, loads = cfg.geometry, cfg.material, cfg.loads

    params: Dict[str, Any] = {
        # геометрия
        "a11": g.a11, "b11": g.b11, "c": g.c, "dd": g.dd, "a22": g.a22, "b22": g.b22,
        "N": g.N, "m": g.m, "d": g.d, "HH": g.HH, "nn": g.nn,
        # материал
        "E1": mat.E1, "E2": mat.E2, "PoissonRatio": mat.PoissonRatio, "Density": mat.Density,
        # нагрузки
        "MZ": loads.MZ, "FZ": loads.FZ,
    }

    # проверка полноты - на случай опечаток
    missing = [k for k in REQUIRED_NAMES if k not in params]
    if missing:
        raise MappingError(f"Отсутствуют обязательные параметры для решателя: {', '.join(missing)}")

    return params
