from Models.edge_model import EdgeModel


class MeshModel:
    def __init__(
        self,
        R1: float = 0.0,  # Радиус верхней кромки [м]
        R2: float = 0.0,  # Радиус нижней кромки [м]
        H: float = 0.0,   # Высота конструкции [м]
        spiral_edge: EdgeModel = EdgeModel(),  # Параметры спиральной кромки
        ring_edge: EdgeModel = EdgeModel(),    # Параметры кольцевой кромки
        shp_edge: EdgeModel = EdgeModel(),     # Параметры шпангоутов
    ):
        # Геометрические параметры
        self._R1 = R1
        self._R2 = R2
        self._H = H

        # Кромки
        self._spiral_edge = spiral_edge
        self._ring_edge = ring_edge
        self._shp_edge = shp_edge

        # Рассчитываемые параметры (инициализируются позже)
        self._p1 = None  # Плотность реберной структуры [кг/м³]
        self._p2 = None  # Плотность обшивки [кг/м³]
        self._M4 = None  # Масса обшивки
        self._M = None   # Общая масса
        self._V4 = None  # Объем обшивки