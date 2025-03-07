from ansys.mapdl.core import launch_mapdl


class MAPDLController:
    def __init__(self):
        self.mapdl = None

    def execute(self):
        try:
            # Шаг 1: Запуск ANSYS MAPDL
            self._launch_ansys()

            # Шаг 2: Настройка среды
            self._setup_environment()

            # Шаг 3: Генерация простой геометрии (блок)
            self._generate_simple_geometry()

            # Шаг 4: Разбиение на сетку
            self._meshing()

            print("Простой сценарий успешно выполнен.")

        finally:
            # Закрытие ANSYS
            self._close_ansys()

    def _launch_ansys(self):
        """
        Запускает ANSYS MAPDL.
        """
        print("Запуск ANSYS...")
        self.mapdl = launch_mapdl()
        print("ANSYS успешно запущен.")

    def _setup_environment(self):
        """
        Настройка рабочей среды ANSYS.
        """
        print("Настройка среды...")
        self.mapdl.clear()  # Очистка предыдущих данных
        self.mapdl.units("SI")  # Установка единиц СИ
        self.mapdl.prep7()  # Вход в препроцессор

    def _generate_simple_geometry(self):
        """
        Генерация простой геометрии (блок).
        """
        print("Генерация геометрии...")
        # Создание блока размером 1x1x1 м
        self.mapdl.block(0, 1, 0, 1, 0, 1)

    def _meshing(self):
        """
        Разбиение модели на сетку.
        """
        print("Разбиение на сетку...")
        self.mapdl.esize(0.1)  # Размер элемента (например, 0.1 м)
        self.mapdl.vmesh("ALL")  # Разбиение всех объемов на сет

    def _close_ansys(self):
        """
        Закрытие соединения с ANSYS.
        """
        print("Закрытие ANSYS...")
        if self.mapdl:
            self.mapdl.exit()