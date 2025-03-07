class FileController:
    @staticmethod
    def save_mesh_model_to_txt(mesh_model, output_filename: str = "mesh_model.txt"):
        """
        Сохраняет параметры модели в текстовый файл
        :param mesh_model: модель сетки, которая будет сгенерирована
        :param output_filename: имя сгенерированного файла
        """

        try:

            with open("Output/" + output_filename, "w") as file:
                # Геометрические параметры
                file.write(f"R1 (Радиус верхней кромки): {mesh_model.R1}\n")
                file.write(f"R2 (Радиус нижней кромки): {mesh_model.R2}\n")
                file.write(f"H (Высота конструкции): {mesh_model.H}\n")

                # Параметры разбиения
                file.write(f"N (Число спиральных ребер): {mesh_model.N}\n")
                file.write(f"m (Число ромбических ячеек по высоте): {mesh_model.m}\n")
                file.write(f"m_shp (Число шпангоутов): {mesh_model.m_shp}\n")

                # Размеры ребер
                file.write(f"a_sp (Толщина спиральных ребер): {mesh_model.a_sp}\n")
                file.write(f"b_sp (Высота спиральных ребер): {mesh_model.b_sp}\n")
                file.write(f"a_col (Толщина кольцевых ребер): {mesh_model.a_col}\n")
                file.write(f"b_col (Высота кольцевых ребер): {mesh_model.b_col}\n")
                file.write(f"a_shp (Толщина шпангоутов): {mesh_model.a_shp}\n")
                file.write(f"b_shp (Высота шпангоутов): {mesh_model.b_shp}\n")

                # Механические свойства материалов
                file.write("Механические свойства спиральных ребер:\n")
                for key, value in mesh_model.material_spiral.items():
                    file.write(f"  {key}: {value}\n")

                file.write("Механические свойства кольцевых ребер:\n")
                for key, value in mesh_model.material_ring.items():
                    file.write(f"  {key}: {value}\n")

                file.write("Механические свойства шпангоутов:\n")
                for key, value in mesh_model.material_shp.items():
                    file.write(f"  {key}: {value}\n")

            print(f"Параметры успешно сохранены в файл: {output_filename}")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    @staticmethod
    def generate_apdl_file(mesh_model, output_filename: str = "output.apdl"):
        """
        Генерирует APDL-файл на основе данных из объекта MeshModel.

        :param mesh_model: Объект MeshModel, содержащий параметры сетки.
        :param output_filename: Имя выходного файла.
        """
        try:
            # Создание списка команд APDL
            apdl_commands = []

            # Очистка прошлых результатов и настройка единиц СИ
            apdl_commands.extend([
                "! Окончание прошлых процессов или расчетов",
                "Finish",
                "! Очистка прошлых результатов расчета",
                "/Clear, start",
                "! Использовать единицы СИ",
                "/Units, Si"
            ])

            # Геометрические параметры
            apdl_commands.extend([
                f"! Геометрические параметры спиральных ребер",
                f"a11={mesh_model.a_sp}",
                f"b11={mesh_model.b_sp}",
                f"! Геометрические параметры кольцевых ребер",
                f"c={mesh_model.a_col}",
                f"dd={mesh_model.b_col}",
                f"! Геометрические параметры шпангоутов",
                f"a22={mesh_model.a_shp}",
                f"b22={mesh_model.b_shp}"
            ])

            # Параметры разбиения
            apdl_commands.extend([
                f"! Число пар спиральных ребер",
                f"N={mesh_model.N}",
                f"! Число ромбических ячеек по высоте",
                f"m={mesh_model.m}",
                f"! Диаметр",
                f"d={2 * mesh_model.R1}",  # Диаметр = 2 * R1
                f"HH={mesh_model.H - mesh_model.H / mesh_model.m}",
                f"H={mesh_model.H}",
                f"kks={mesh_model.H / mesh_model.m}",
                f"tet=360/{mesh_model.N}",
                "! Переход в цилиндрическую систему координат",
                "CSYS,1"
            ])

            # Построение точек для спиральных ребер
            apdl_commands.append("! Начало цикла для спиральных ребер")
            apdl_commands.append("*do,i,1,N")
            apdl_commands.append("    *do,s,1,m+1")
            apdl_commands.append("        K,,d/2,tet*i,kks*(s-1) ! Построение точек")
            apdl_commands.append("    *enddo")
            apdl_commands.append("*enddo")

            # Соединение точек линиями для спиральных ребер
            apdl_commands.append("! Соединение точек линиями для спиральных ребер")
            apdl_commands.append("ii=1")
            apdl_commands.append("*do,i,1,N-1")
            apdl_commands.append("    *do,j,1,m")
            apdl_commands.append("        L,ii,ii+m+2")
            apdl_commands.append("        ii=ii+1")
            apdl_commands.append("    *enddo")
            apdl_commands.append("    ii=ii+1")
            apdl_commands.append("*enddo")

            # Дополнительные линии
            apdl_commands.extend([
                "*do,i,1,m",
                "L,i,N*(m+1)-m+i",
                "*enddo",
                "*do,i,1,m",
                "L,i+1,N*(m+1)-m-1+i",
                "*enddo"
            ])

            # Построение точек для шпангоутов
            apdl_commands.append("! Построение точек для шпангоутов")
            apdl_commands.append("*do,i,1,N")
            apdl_commands.append("    *do,s,1,m+1")
            apdl_commands.append("        K,,d/2,tet*i,H/(m+1)-(H/(m+1))*0.28")
            apdl_commands.append("        K,,d/2,tet*i,H-(H/(m+1))*0.28")
            apdl_commands.append("    *enddo")
            apdl_commands.append("*enddo")

            # Построение точек для кольцевых ребер
            apdl_commands.append("! Кольцевые ребра точки")
            apdl_commands.append("*do,i,1,N")
            apdl_commands.append("    *do,s,2,2*m")
            apdl_commands.append("        K,,d/2,tet*i,H/(2*m)*s+H/(4*m) ! Построение точек для кольцевых ребер")
            apdl_commands.append("    *enddo")
            apdl_commands.append("*enddo")

            # Разбиение пересечений линий
            apdl_commands.append("! Разбиение пересечений линий")
            apdl_commands.append("LCSL,ALL")

            # Удаление лишних точек и линий
            apdl_commands.append("! Удаление лишних точек и линий")
            apdl_commands.append("LDELE,ALL")

            # Выделение всей конструкции
            apdl_commands.append("! Выделение всей конструкции")
            apdl_commands.append("LSEL,s,,,ALL")

            # Запись команд в файл
            with open("Output/" + output_filename, "w") as file:
                file.write("\n".join(apdl_commands))

            print(f"APDL-файл успешно создан: Output/{output_filename}")

        except Exception as e:
            print(f"Ошибка при генерации APDL-файла: {e}")
