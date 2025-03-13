from ansys.mapdl.core import launch_mapdl
import numpy as np


class SpiralStructureModel:
    def __init__(self):
        self.mapdl = None
        self.parameters = {
            'a11': 0.006,  # Геометрический параметр спирального ребра
            'b11': 0.03,  # Геометрический параметр спирального ребра
            'c': 0.003,  # Геометрический параметр кольцевого ребра
            'dd': 0.03,  # Геометрический параметр кольцевого ребра
            'a22': 0.03,  # Геометрический параметр шпангоута
            'b22': 0.018,  # Геометрический параметр шпангоута
            'N': 30,  # Количество спиральных ребер
            'm': 7,  # Число ячеек по высоте
            'd': 2.560,  # Диаметр
            'HH': 5.585,  # Базовая высота
        }
        self.parameters['tet'] = 360 / self.parameters['N']
        self.parameters['H'] = self.parameters['HH'] * (1 + 1 / self.parameters['m'])
        self.parameters['kk'] = self.parameters['H'] / self.parameters['m']
        self.keypoint_counter = 1  # Счетчик ключевых точек

    def run(self):
        try:
            self.mapdl = launch_mapdl()
            self.mapdl.clear()  # Очистка результатов прошлых расчетов

            self.mapdl.units("SI")  # Используем единицы СИ
            self.mapdl.pnum("KP", 0)  # Отключаем отображение номеров точек
            self.mapdl.pnum("LINE", 0)  # Отключаем отображение номеров линий
            self.mapdl.prep7()  # Открытие препроцессора
            self.mapdl.csys(1)  # Цилиндрическая система координат

            self.create_geometry()  # Переходим к созданию геометрии

            # Визуализация
            #self.mapdl.kplot(vtk=True, show_keypoint_numbering=True)
            self.mapdl.lplot(vtk=True, show_line_numbering=False, color='blue')

        except Exception as e:
            print(f"Ошибка: {e}")

    def create_geometry(self):
        """Создание всей геометрии"""
        self.create_spiral()
        self.create_shpangout()
        self.create_ring()
        self.line_intersections()

    def create_spiral(self):
        """Создание спиральных ребер"""
        p = self.parameters
        mapdl = self.mapdl

        # Создание точек спирали
        for i in range(1, p['N'] + 1):
            for s in range(1, p['m'] + 2):
                x = p['d'] / 2
                y = p['tet'] * i
                z = p['kk'] * (s - 1)

                mapdl.k(self.keypoint_counter, x, y, z)
                self.keypoint_counter += 1

        # Соединение точек спирали линиями
        ii = 1  # Инициализация счетчика для номеров точек
        # Первый цикл для соединения точек
        for i in range(1, p['N']):
            for j in range(1, p['m'] + 1):
                # Создание линии между точками ii и ii + m + 2
                mapdl.l(ii, ii + p['m'] + 2)
                ii += 1
            ii += 1

        if mapdl.klist():  # Проверяем наличие точек
            print("Точки созданы. Начинаем соединение...")
        else:
            print("Ошибка: точки не созданы!")

        # Второй цикл для соединения точек
        for i in range(1, p['m'] + 1):
            # Создаем линию между точками i и N*(m+1)-m+i
            start_point = i
            end_point = p['N'] * (p['m'] + 1) - p['m'] + i
            mapdl.l(start_point, end_point)

        # Третий цикл для соединения точек
        for i in range(1, p['m'] + 1):
            # Создаем линию между точками i+1 и N*(m+1)-m-1+i
            start_point = i + 1
            end_point = p['N'] * (p['m'] + 1) - p['m'] - 1 + i
            mapdl.l(start_point, end_point)

        # Четвертый цикл для соединения точек
        ii = 2
        for i in range(1, p['N']):
            for j in range(1, p['m'] + 1):
                # Создаем линию между точками ii и ii+m
                mapdl.l(ii, ii + p['m'])
                ii += 1
            ii += 1

    def create_shpangout(self):
        """Создание шпангоутов"""
        p = self.parameters
        mapdl = self.mapdl

        self.keypoint_counter += 1
        for i in range(1, p['N'] + 1):
            for s in range(1, p['m'] + 2):
                # Вычисление координат для нижнего шпангоута
                z_lower = p['H'] / (p['m'] + 1) - (p['H'] / (p['m'] + 1)) * 0.28
                mapdl.k(self.keypoint_counter, p['d'] / 2, p['tet'] * i, z_lower)
                self.keypoint_counter += 1

                # Вычисление координаты для верхнего шпангоута
                z_upper = p['H'] - (p['H'] / (p['m'] + 1)) * 0.28
                mapdl.k(self.keypoint_counter, p['d'] / 2, p['tet'] * i, z_upper)
                self.keypoint_counter += 1

    def create_ring(self):
        """Создание кольцевых ребер"""
        p = self.parameters
        mapdl = self.mapdl

        # Создание точек для кольцевых ребер
        for i in range(1, p['N'] + 1):
            for s in range(2, 2 * p['m'] + 1):
                # Вычисление координат для точки
                z = p['H'] / (2 * p['m']) * s + p['H'] / (4 * p['m'])
                mapdl.k(self.keypoint_counter, p['d'] / 2, p['tet'] * i, z)
                self.keypoint_counter += 1

        total_keypoints = mapdl.klist().strip().split("\n")
        print(f"Создано точек: {len(total_keypoints)}")

        # Соединение точек линиями
        for i in range(1, p['N']):
            for ii in range(1, 2 * p['m'] - 2):
                for iii in range(1, 3):
                    # Линия между точками
                    start_point_1 = p['N'] * (p['m'] + 1) * 3 + 1 + (i - 1) * (p['m'] * 2 - 1) + ii - 1
                    end_point_1 = p['N'] * (p['m'] + 1) * 3 + 1 + i * (p['m'] * 2 - 1) + ii - 1
                    mapdl.l(start_point_1, end_point_1)

                    start_point_2 = p['N'] * (p['m'] + 1) * 3 + 1 + ii - 1
                    end_point_2 = p['N'] * (p['m'] + 1) * 3 + 1 + (p['N'] - 1) * (p['m'] * 2 - 1) + ii - 1
                    mapdl.l(start_point_2, end_point_2)

                    start_point_3 = p['N'] * (p['m'] + 1) + 2 + (i - 1) * (p['m'] * 2 + 2) + iii - 1
                    end_point_3 = p['N'] * (p['m'] + 1) + 2 + i * (p['m'] * 2 + 2) + iii - 1
                    mapdl.l(start_point_3, end_point_3)

                    start_point_4 = p['N'] * (p['m'] + 1) + 2 + (i - 1) * (p['m'] * 2 + 2) + iii - 1
                    end_point_4 = p['N'] * (p['m'] + 1) + 2 + (p['N'] - 1) * (p['m'] * 2 + 2) + iii - 1
                    mapdl.l(start_point_4, end_point_4)

                    start_point_5 = p['N'] * (p['m'] + 1) + 2 + iii - 1
                    end_point_5 = p['N'] * (p['m'] + 1) + 2 + (p['N'] - 1) * (p['m'] * 2 + 2) + iii - 1
                    mapdl.l(start_point_5, end_point_5)


    def line_intersections(self):
        p = self.parameters
        mapdl = self.mapdl

        # --- Часть 1: Разбиение пересечений линий ---
        print("Разбиение пересечений линий...")
        mapdl.lcsl("ALL")  # Разбиваем все пересечения линий

        # --- Часть 2: Выбор линий по координате Z ---
        print("Выбор линий по координате Z...")

        # Внешний цикл (i от 1 до 2)
        for i in range(1, 3):
            # Внутренний цикл (s от 2 до 2*m)
            for s in range(2, 2 * p['m'] + 1):
                # Выбор линий в диапазоне Z
                z_min_1 = p['H'] - (p['H'] / (p['m'] + 1)) * 0.25
                z_max_1 = p['H']
                mapdl.lsel("S", "LOC", "Z", z_min_1, z_max_1)

                z_min_2 = 0
                z_max_2 = p['H'] / (p['m'] + 1) - (p['H'] / (p['m'] + 1)) * 0.3
                mapdl.lsel("A", "LOC", "Z", z_min_2, z_max_2)

        # --- Часть 3: Удаление лишних точек и линий ---
        print("Удаление лишних точек и линий...")
        mapdl.ldele("ALL")  # Удаляем все выбранные линии

        # --- Часть 4: Выделение всей конструкции ---
        print("Выделение всей конструкции...")
        mapdl.lsel("S", "", "", "ALL")  # Выделяем все линии


    def stop_mapdl(self):
        if self.mapdl:
            self.mapdl.exit()
            print("MAPDL успешно остановлен.")
        else:
            print("MAPDL не был запущен.")
