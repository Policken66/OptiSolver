from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox
from ansys.mapdl.core import launch_mapdl

from Models.edge_model import EdgeModel
from Models.mesh_model import MeshModel
from Models.spiral_structure_model import SpiralStructureModel
from Views.main_window_view import MainWindowView


class MainWindowController(QMainWindow):
    def __init__(self, view: MainWindowView):
        # Переменные
        self.view = view
        self.ui = view.ui
        self.current_mesh_model = None
        self.mapdl_model = None
        self.parametrs_for_mapdl_model = None


        # Обработка событий
        self.ui.doubleSpinBox_input_R1.valueChanged.connect(self.compare_values)
        self.ui.doubleSpinBox_input_R2.valueChanged.connect(self.compare_values)

        # Сигналы и слоты
        self.ui.pushButton_save.clicked.connect(self.pushButton_save_clicked)
        self.ui.pushButton_generate.clicked.connect(self.pushButton_generate_clicked)

        # Задание начальных данных
        self.init_first_data()

    def pushButton_save_clicked(self):
        self.current_mesh_model = self.init_mesh_model()
        # Проверяем успешность создания

        self.parametrs_for_mapdl_model = {
                            'a11': self.ui.doubleSpinBox_input_height_spiral.value(),  # Геометрический параметр спирального ребра (высота)
                            'b11': self.ui.doubleSpinBox_input_thinkness_spiral.value(),  # Геометрический параметр спирального ребра (толщина)
                            'c': self.ui.doubleSpinBox_input_height_ring.value(),  # Геометрический параметр кольцевого ребра (высота)
                            'dd': self.ui.doubleSpinBox_input_thinkness_ring.value(),  # Геометрический параметр кольцевого ребра (толщина)
                            'a22': self.ui.doubleSpinBox_input_thinkness_shp.value(),  # Геометрический параметр шпангоута (толщина)
                            'b22': self.ui.doubleSpinBox_input_height_shp.value(),  # Геометрический параметр шпангоута (высота)
                            'N': self.ui.spinBox_input_N_spiral.value(),  # Количество спиральных ребер
                            'm': int(self.ui.spinBox_input_N_ring.value()/2),  # Число ячеек по высоте (фиксированное значение, если не используется спинбокс)
                            'd': (self.ui.doubleSpinBox_input_R1.value() + self.ui.doubleSpinBox_input_R2.value()) / 2,  # Диаметр (среднее значение R1 и R2)
                            'HH': self.ui.doubleSpinBox_input_H.value(),  # Базовая высота
                            'alp':self.ui.spinBox_input_alp.value(),  # угол наклона спирального ребра
                        }



        if self.current_mesh_model:
            # Создаем QMessageBox
            message_box = QMessageBox()
            message_box.setWindowTitle("Сохранение модели")
            message_box.setWindowIcon(QIcon("Resources/Icons/satellite_icon.png"))
            message_box.setText("Модель успешно сохранена!")
            message_box.setIcon(QMessageBox.Information)
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()





    def pushButton_generate_clicked(self):
        print("PushButton generate clicked")
        if self.parametrs_for_mapdl_model is not None:
            self.mapdl_model = SpiralStructureModel(self.parametrs_for_mapdl_model)
            self.mapdl_model.run()
            self.mapdl_model.stop_mapdl()
        else:
            message_box = QMessageBox()
            message_box.setWindowTitle("Генерация")
            message_box.setWindowIcon(QIcon("Resources/Icons/satellite_icon.png"))
            message_box.setText("Сохраните параметры перед запуском!")
            message_box.setIcon(QMessageBox.Warning)
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()



    def init_mesh_model(self):
        R1 = self.ui.doubleSpinBox_input_R1.value()
        R2 = self.ui.doubleSpinBox_input_R2.value()
        H = self.ui.doubleSpinBox_input_H.value()

        spiral_edge = self.init_spiral_edge()
        ring_edge = self.init_ring_edge()
        shp_edge = self.init_shp_edge()

        # Создание объекта MeshModel с передачей всех параметров
        mesh_model = MeshModel(
            R1=R1,
            R2=R2,
            H=H,
            spiral_edge=spiral_edge,
            ring_edge=ring_edge,
            shp_edge=shp_edge
        )

        return mesh_model

    def init_spiral_edge(self):
        quantity = self.ui.spinBox_input_N_spiral.value()
        thickness = self.ui.doubleSpinBox_input_thinkness_spiral.value()
        height = self.ui.doubleSpinBox_input_height_spiral.value()
        E_x = self.ui.doubleSpinBox_input_E_x_spiral.value()
        E_y = self.ui.doubleSpinBox_input_E_y_spiral.value()
        E_z = self.ui.doubleSpinBox_input_E_z_spiral.value()
        G_xy = self.ui.doubleSpinBox_input_G_xy_spiral.value()
        G_yz = self.ui.doubleSpinBox_input_G_yz_spiral.value()
        G_xz = self.ui.doubleSpinBox_input_G_xz_spiral.value()
        v = self.ui.doubleSpinBox_input_v_spiral.value()

        # Создание объекта с передачей всех параметров
        spiral_edge = EdgeModel(
            quantity=quantity,
            thickness=thickness,
            height=height,
            E_x=E_x,
            E_y=E_y,
            E_z=E_z,
            G_xy=G_xy,
            G_yz=G_yz,
            G_xz=G_xz,
            v=v
        )
        return spiral_edge

    def init_ring_edge(self):
        quantity = self.ui.spinBox_input_N_ring.value()
        thickness = self.ui.doubleSpinBox_input_thinkness_ring.value()
        height = self.ui.doubleSpinBox_input_height_ring.value()
        E_x = self.ui.doubleSpinBox_input_E_x_ring.value()
        E_y = self.ui.doubleSpinBox_input_E_y_ring.value()
        E_z = self.ui.doubleSpinBox_input_E_z_ring.value()
        G_xy = self.ui.doubleSpinBox_input_G_xy_ring.value()
        G_yz = self.ui.doubleSpinBox_input_G_yz_ring.value()
        G_xz = self.ui.doubleSpinBox_input_G_xz_ring.value()
        v = self.ui.doubleSpinBox_input_v_ring.value()

        ring_edge = EdgeModel(
            quantity=quantity,
            thickness=thickness,
            height=height,
            E_x=E_x,
            E_y=E_y,
            E_z=E_z,
            G_xy=G_xy,
            G_yz=G_yz,
            G_xz=G_xz,
            v=v
        )
        return ring_edge

    def init_shp_edge(self):
        quantity = self.ui.spinBox_input_N_shp.value()
        thickness = self.ui.doubleSpinBox_input_thinkness_shp.value()
        height = self.ui.doubleSpinBox_input_height_shp.value()
        E_x = self.ui.doubleSpinBox_input_E_x_shp.value()
        E_y = self.ui.doubleSpinBox_input_E_y_shp.value()
        E_z = self.ui.doubleSpinBox_input_E_z_shp.value()
        G_xy = self.ui.doubleSpinBox_input_G_xy_shp.value()
        G_yz = self.ui.doubleSpinBox_input_G_yz_shp.value()
        G_xz = self.ui.doubleSpinBox_input_G_xz_shp.value()
        v = self.ui.doubleSpinBox_input_v_shp.value()

        shp_edge = EdgeModel(
            quantity=quantity,
            thickness=thickness,
            height=height,
            E_x=E_x,
            E_y=E_y,
            E_z=E_z,
            G_xy=G_xy,
            G_yz=G_yz,
            G_xz=G_xz,
            v=v
        )
        return shp_edge

    def compare_values(self):
        r1 = self.ui.doubleSpinBox_input_R1.value()
        r2 = self.ui.doubleSpinBox_input_R2.value()
        if r1 == r2:
            self.ui.label_geometric_params_model.setPixmap(QPixmap("Resources/upper_radius_equal_bottom_radius.jpg"))
        elif r1 < r2:
            self.ui.label_geometric_params_model.setPixmap(QPixmap("Resources/upper_radius_less_bottom_radius.jpg"))
        else:
            self.ui.label_geometric_params_model.setPixmap(QPixmap("Resources/upper_radius_more_bottom_radius.jpg"))

        self.ui.label_geometric_params_model.setScaledContents(True)

    def closeEvent(self, event):
        self.mapdl_model.stop_mapdl()

    def init_first_data(self):
        self.ui.doubleSpinBox_input_R1.setValue(3.5)
        self.ui.doubleSpinBox_input_R2.setValue(3.5)

        self.ui.doubleSpinBox_input_H.setValue(5.585)

        self.ui.doubleSpinBox_input_height_spiral.setValue(0.006)
        self.ui.doubleSpinBox_input_thinkness_spiral.setValue(0.03)

        self.ui.doubleSpinBox_input_height_ring.setValue(0.003)
        self.ui.doubleSpinBox_input_thinkness_ring.setValue(0.03)

        self.ui.doubleSpinBox_input_thinkness_shp.setValue(0.03)
        self.ui.doubleSpinBox_input_height_shp.setValue(0.018)

        self.ui.spinBox_input_N_spiral.setValue(30)
        self.ui.spinBox_input_N_ring.setValue(7)



