# --- Базовые типы с ограничениями ---
from pathlib import Path
from typing import Annotated, List, Literal

from pydantic import Field, BaseModel, ConfigDict, model_validator

Meter = Annotated[float, Field(gt=0)]  # м > 0
MeterInt = Annotated[int, Field(ge=1)]  # целое >= 1
ElasticMod = Annotated[float, Field(gt=0)]  # Па > 0
DensityT = Annotated[float, Field(gt=0)]  # кг/м^3 > 0
PoissonT = Annotated[float, Field(gt=0, lt=0.5)]  # 0 <= v < 0.5
ForceT = float  # H
MomentT = float  # Н * м
FreqT = Annotated[float, Field(gt=0)]  # Гц > 0


class MetaData(BaseModel):
    model_config = ConfigDict(extra="forbid")
    project_name: str
    author: str | None
    date: str


class Geometry(BaseModel):
    model_config = ConfigDict(extra="forbid")
    # размеры
    a11: Meter
    b11: Meter
    c: Meter
    dd: Meter
    a22: Meter
    b22: Meter
    # конфигурация
    N: MeterInt
    m: MeterInt
    d: Meter
    HH: Meter
    nn: Meter

    @model_validator(mode="after")
    def _business_rules(self):
        if self.N < 3:
            raise ValueError("Geometry.N должно быть >= 3.")
        if self.m < 1:
            raise ValueError("Geometry.m должно быть >= 1.")
        # Дальше можно также задавать правила на все параметры под нужные задачи
        # ...
        # ...
        return self


class Material(BaseModel):
    model_config = ConfigDict(extra="forbid")
    E1: ElasticMod
    E2: ElasticMod
    PoissonRatio: PoissonT
    Density: DensityT


class Loads(BaseModel):
    model_config = ConfigDict(extra="forbid")
    MZ: MomentT
    FZ: ForceT


class Constraints(BaseModel):
    model_config = ConfigDict(extra="forbid")
    sigma_eq_max: ElasticMod
    u_max: Meter
    f_min: FreqT
    lambda_buckle_min: Annotated[float, Field(gt=0)]


class Solver(BaseModel):
    model_config = ConfigDict(extra="forbid")
    analyses: List[Literal["static", "modal", "buckle"]]
    timeout_sec: Annotated[int, Field(ge=1)]
    retries: Annotated[int, Field(ge=0)]

    @model_validator(mode="after")
    def _check_analyses(self):
        if not self.analyses:
            raise ValueError("Список Solver.analyses не должен быть пустым.")
        return self


class Paths(BaseModel):
    model_config = ConfigDict(extra="forbid")
    work_dir: Path
    template_dir: Path
    results_dir: Path

    @model_validator(mode="after")
    def _paths_are_strings(self):
        return self


class ConfigModel(BaseModel):
    """
    Агрегирующая модель конфигурации.
    Все поля обязательны; лишние ключи запрещены.
    """
    model_config = ConfigDict(extra="forbid")
    metadata: MetaData
    geometry: Geometry
    material: Material
    loads: Loads
    constraints: Constraints
    solver: Solver
    paths: Paths
