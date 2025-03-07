class EdgeModel:
    def __init__(
            self,
            quantity: int = 0,
            thickness: float = 0.0,
            height: float = 0.0,
            E_x: float = 0.0,
            E_y: float = 0.0,
            E_z: float = 0.0,
            G_xy: float = 0.0,
            G_yz: float = 0.0,
            G_xz: float = 0.0,
            v: float = 0.0
    ):
        self._quantity = quantity  # Количество ребер [шт.]
        self._thickness = thickness  # Толщина ребра [м]
        self._height = height  # Высота ребра [м]
        self._E_x = E_x  # Модуль упругости в направлении оси x [Па]
        self._E_y = E_y  # Модуль упругости в направлении оси y [Па]
        self._E_z = E_z  # Модуль упругости в направлении оси z [Па]
        self._G_xy = G_xy
        self._G_yz = G_yz
        self._G_xz = G_xz
        self._v = v  # Коэффициент Пуассона

        self._M = None  # Масса ребер [кг]
        self._V = None  # Объем ребер [м^3]
