from ansys.mapdl.core import launch_mapdl



class SpiralStructureModel:
    test_parametrs = {
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
            'alp':10, #угол наклона спирального ребра
        }
    def __init__(self, parametrs):
        self.mapdl = None
        self.parameters = parametrs
        self.parameters['tet'] = 360 / self.parameters['N']
        self.parameters['H'] = self.parameters['HH'] * (1 + 1 / self.parameters['m'])
        print(self.parameters['H'])
        print(self.parameters['m'])
        self.parameters['kk'] = self.parameters['H'] / self.parameters['m']
        self.keypoint_counter = 1  # Счетчик ключевых точек
        print(self.parameters['alp'])
        self.node_counter=1 #счетчик для узлов


    def run(self):
        self.test_2()

    def test_2(self):
        work_dir_path = "C:\\rb\\no\\work_dir"
        self.mapdl = launch_mapdl(run_location=work_dir_path, override=True)
        script_path = "C:\\rb\\no\\shell.txt"
        self.mapdl.input(script_path)

        print(self.mapdl.list_files())

        self.mapdl.finish()

    def test_1(self):
        try:
            self.mapdl = launch_mapdl()
            self.mapdl.clear()  # Очистка результатов прошлых расчетов

            self.mapdl.units("SI")  # Используем единицы СИ
            self.mapdl.pnum("KP", 1)  # Отключаем отображение номеров точек
            self.mapdl.pnum("LINE", 1)  # Отключаем отображение номеров линий
            self.mapdl.prep7()  # Открытие препроцессора
            self.mapdl.csys(1)  # Цилиндрическая система координат

            self.create_geometry()  # Переходим к созданию геометрии
            #self.create_node() #создание узлов
            self.create_finite_type_element() #Конечный элемент
            #self.create_finite_element()  # Конечный элемент
            #self.element_intersections()

            # Визуализация
            self.mapdl.kplot(vtk=True, show_keypoint_numbering=False, color='blue', background='white')
            self.mapdl.lplot(vtk=True, show_line_numbering=False, color='blue', background='white')
            self.mapdl.nplot(vtk=True,show_node_numbering=False, color='black',background='white')
            self.mapdl.eplot(vtk=True, show_element_numbering=False, color='black', background='white')


        except Exception as e:
            print(f"Ошибка: {e}")

    def create_geometry(self):
        """Создание всей геометрии"""
        self.create_spiral()
        self.create_shpangout()
        self.create_ring()
        self.line_intersections()
        self.create_finite_element()
       # self.element_intersections()

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

                mapdl.n(self.node_counter+1,p['d']/2,p['tet']*i,p['H']-p['H']/(p['m']+1)*0.28)
                self.node_counter += 1
                mapdl.n(1,0,0,p['H']-p['H']/(p['m']+1)*0.28)

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
                mapdl.lsel("A", "LOC", "Z", z_min_2,  z_max_2)

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


    def create_finite_type_element(self ):
        p = self.parameters
        print("Задание типа конечного элемента")
        mapdl=self.mapdl
        # 1. Определяем тип элемента
        mapdl.et(1, "BEAM4")
        mapdl.keyopt(1,6,0)
        mapdl.keyopt(1,7,0)
        mapdl.keyopt(1, 9, 0)
        mapdl.keyopt(1, 10, 0)

        mapdl.mp("EX", 1, 2.1e11)  # Модуль упругости стали ~210 ГПа
        mapdl.mp("DENS", 1, 1781)
        mapdl.mp("PRXY", 1, 0.3)
        mapdl.uimp(1,"EX","DENS","PRXY",2.1e11,1781,0.3)
        mapdl.r(1,"r1","r2","r3","r4","r5","r6")
        mapdl.rmore("r7","r8","r9")

        mapdl.r(1,p['a11']*p['b11'],(p['a11']*p['b11']*p['b11']*p['b11'])/12,(p['b11']*p['a11']*p['a11']*p['a11'])/12)
        mapdl.sectype(1, "BEAM", "RECT", "MyName", 0)  # квадратное сечение
       # mapdl.secofest("CENT")
        mapdl.secdata(p["a11"], p["b11"], 5, 5)  # Радиус круглого сечения = 0.01 м


        mapdl.et(2, "BEAM4")
        mapdl.keyopt(2, 6, 0)
        mapdl.keyopt(2, 7, 0)
        mapdl.keyopt(2, 9, 0)
        mapdl.keyopt(2, 10, 0)

        # 2. Задаем материал (модуль Юнга)
        mapdl.mp("EX", 2, 2.1e11)  # Модуль упругости стали ~210 ГПа
        mapdl.mp("DENS", 2, 1781)
        mapdl.mp("PRXY", 2, 0.3)
        mapdl.uimp(2, "EX", "DENS", "PRXY", 2.1e11, 1781, 0.3)
        mapdl.r(2, "r1", "r2", "r3", "r4", "r5", "r6")
        mapdl.rmore("r7", "r8", "r9")

        mapdl.r(2, p['a22'] * p['b22'], (p['a22'] * p['b22'] *p['b22'] * p['b22']) / 12,
                (p['b22'] * p['a22'] * p['a22'] * p['a22']) / 12)

        mapdl.sectype(2, "BEAM", "RECT", "MyName", 0)  # квадратное сечение
        #mapdl.secofest("CENT","","","","","","","")
        #SECOFFSET, Location, OFFSET1, OFFSET2, CG-Y, CG-Z, SH-Y, SH-Z
        mapdl.secdata(p["a22"], p["b22"], 5, 5)  # Радиус круглого сечения = 0.01 м


        mapdl.et(3, "BEAM4")
        mapdl.keyopt(3, 6, 0)
        mapdl.keyopt(3, 7, 0)
        mapdl.keyopt(3, 9, 0)
        mapdl.keyopt(3, 10, 0)

        mapdl.mp("EX", 3, 2.1e11)  # Модуль упругости стали ~210 ГПа
        mapdl.mp("DENS", 3, 1781)
        mapdl.mp("PRXY", 3, 0.3)
        mapdl.uimp(3, "EX", "DENS", "PRXY", 2.1e11, 1781, 0.3)
        mapdl.r(3, "r1", "r2", "r3", "r4", "r5", "r6")
        mapdl.rmore("r7", "r8", "r9")

        mapdl.r(3, p['c'] * p['d'], (p['c'] * p['d'] * p['d'] * p['d']) / 12,
                (p['d'] * p['c'] * p['c'] * p['c']) / 12)

        mapdl.sectype(3, "BEAM", "RECT", "MyName", 0)  # квадратное сечение
       # mapdl.sec ofest("CENT")
        mapdl.secdata(p["c"], p["d"], 5, 5)  # Радиус круглого сечения = 0.01 м

        mapdl.et(4, "MPC184")
        mapdl.keyopt(4, 1, 1)

    def create_finite_element(self):
        """Создание кольцевых ребер"""
        p = self.parameters
        mapdl = self.mapdl

        mapdl.lsel("S", "", "", "ALL")

        # Создание точек для кольцевых ребер
        for i in range(2, p['m'] - 1):
            for s in range(2, 2 * p['m'] ):
                # Вычисление координат для точки
                mapdl.lsel("U","LOC" ,"Z",p["H"]/(p["m"]+1)-p["H"]*0.28/(p["m"]+1))
                mapdl.lsel("U", "LOC", "Z", p['H']*s/(2*p["m"])+p["H"]/(4*p["m"]))
                mapdl.lsel("U","LOC","Z",p["H"]-p["H"]*0.28/(p["m"]+1))

                mapdl.lesize("ALL","","",5,"","")
                mapdl.latt(1,1,1,"","",1)

        for i in range(2, p['m'] - 2):
              for s in range(2, 2 * p['m']):
            # Вычисление координат для точки
                mapdl.lsel("A", "LOC", "Z", p["H"]*s / (2*p["m"]) + p["H"] / (4*p["m"]))
        mapdl.lesize("ALL", "", "", 5, "", "")
        mapdl.latt(3, 3, 3, "", "", 3)

        #mapdl.lsel("ALL")
        mapdl.lsel("NONE")
        mapdl.lsel("S", "LOC", "Z", p["H"]/ (p["m"]+1)-(p["H"]*0.28/(p["m"]+1)))
        mapdl.lsel("A","LOC","Z",p["H"]-p["H"]*0.28/(p["m"]+1))
        mapdl.lesize("ALL", "", "", 5, "", "")
        mapdl.latt(2, 2, 2, "", "", 2)
        mapdl.allsel("ALL")
        #mapdl.lmesh(1)
        #mapdl.lmesh(2)
        #mapdl.lmesh(3)

      #  for i in range(1, p['N']):
        mapdl.e("1","2","","","","","","")







