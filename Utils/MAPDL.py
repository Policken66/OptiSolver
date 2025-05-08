from ansys.mapdl.core import launch_mapdl

class PyMAPDLModel:

    def __init__(self):
        self.mapdl = None

    def start_mapdl(self):
        """
                Запуск нового экземпляра MAPDL.

                :param exec_file: Путь к исполняемому файлу MAPDL.
                """
        try:
            self.mapdl = launch_mapdl()
            print("MAPDL успешно запущен.")
            # All units in (m, Kg, s)
            LENGTH = 5
            WIDTH = 2.5
            DEPTH = 0.1
            RADIUS = 0.5
            NUM = 3

            E = 2e11
            NU = 0.27

            PRESSURE = 1000

            self.mapdl.clear()
            self.mapdl.prep7()
            self.mapdl.block(0, LENGTH, 0, WIDTH, 0, DEPTH)
            for i in range(1, NUM + 1):
                self.mapdl.cyl4(i * LENGTH / (NUM + 1), WIDTH / 2, RADIUS, '', '', '', 2 * DEPTH)
            self.mapdl.vsbv(1, 'all')
            # self.mapdl.vplot('all')

            self.mapdl.lesize("ALL", 0.15, layer1=1)

            self.mapdl.mp('ex', 1, E)
            self.mapdl.mp('nuxy', 1, NU)

            self.mapdl.et(1, 'SOLID186')
            self.mapdl.mshape(1, "3D")
            self.mapdl.mshkey(0)
            self.mapdl.vmesh('all')
            self.mapdl.eplot()

            self.stop_mapdl()
        except Exception as e:
            print(f"Ошибка при запуске MAPDL: {e}")

    def stop_mapdl(self):
        """Остановка текущего экземпляра MAPDL."""
        if self.mapdl:
            self.mapdl.exit()
            print("MAPDL остановлен.")
        else:
            print("MAPDL не был запущен.")

