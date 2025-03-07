from Models.edge_model import EdgeModel


class MeshModel:
    def __init__(self):
        # Геометрические параметры
        self._R1 = 0.0  # Радиус верхней кромки [м]
        self._R2 = 0.0  # Радиус нижней кромки [м]
        self._H = 0.0  # Высота конструкции [м]

        self._spiral_edge = EdgeModel()
        self._ring_edge = EdgeModel()
        self._shpangout_edge = EdgeModel()

        self._M4 = None  # Масса обшивки [кг]
        self._M = None  # Масса всей конструкции [кг]

        self._V4 = None  # Объем обшивки [м^3]

        self._p1 = None  # Плотность материала реберной структуры [кг/м^3]
        self._p2 = None  # Плотность обшивки [кг/м^3]
