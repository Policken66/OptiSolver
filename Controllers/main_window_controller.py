from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from Controllers.file_controller import FileController
from Controllers.mapdl_controller import MAPDLController
from Models.edge_model import EdgeModel
from Models.mesh_model import MeshModel
from Views.main_window_view import MainWindowView


class MainWindowController(QMainWindow):
    def __init__(self, view: MainWindowView):
        self.view = view
        self.ui = view.ui

        self.ui.doubleSpinBox_input_R1.valueChanged.connect(self.compare_values)
        self.ui.doubleSpinBox_input_R2.valueChanged.connect(self.compare_values)

        self.default_value_for_calculated_parameters()

        # Обработчик событий
        self.ui.pushButton_save.clicked.connect(self.pushButton_save_clicked)
        self.ui.pushButton_generate.clicked.connect(self.pushButton_generate_clicked)

        # Переменные
        self.current_mesh_model = None

    def pushButton_save_clicked(self):
        self.current_mesh_model = self.init_mesh_model()

    def pushButton_start_clicked(self):
        print("PushButton start clicked")
        # automation = MAPDLController()
        # automation.execute()

    def pushButton_generate_clicked(self):
        print("PushButton generate clicked")

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

    def default_value_for_calculated_parameters(self):
        self.ui.label_value_M_1.setText("Не рассчитано")
        self.ui.label_value_M_2.setText("Не рассчитано")
        self.ui.label_value_M_3.setText("Не рассчитано")
        self.ui.label_value_M_4.setText("Не рассчитано")
        self.ui.label_value_M_1.setStyleSheet("color: red;")
        self.ui.label_value_M_2.setStyleSheet("color: red;")
        self.ui.label_value_M_3.setStyleSheet("color: red;")
        self.ui.label_value_M_4.setStyleSheet("color: red;")

        self.ui.label_value_V_1.setText("Не рассчитано")
        self.ui.label_value_V_2.setText("Не рассчитано")
        self.ui.label_value_V_3.setText("Не рассчитано")
        self.ui.label_value_V_4.setText("Не рассчитано")
        self.ui.label_value_V_1.setStyleSheet("color: red;")
        self.ui.label_value_V_2.setStyleSheet("color: red;")
        self.ui.label_value_V_3.setStyleSheet("color: red;")
        self.ui.label_value_V_4.setStyleSheet("color: red;")

        self.ui.label_value_p_1.setText("Не рассчитано")
        self.ui.label_value_p_2.setText("Не рассчитано")
        self.ui.label_value_p_1.setStyleSheet("color: red;")
        self.ui.label_value_p_2.setStyleSheet("color: red;")

        self.ui.label_value_M.setText("Не рассчитано")
        self.ui.label_value_M.setStyleSheet("color: red;")
