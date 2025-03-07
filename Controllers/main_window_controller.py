from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from Controllers.file_controller import FileController
from Controllers.mapdl_controller import MAPDLController
from Models.mesh_model import MeshModel
from Ui.main_window import Ui_MainWindow


class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.doubleSpinBox_input_R1.valueChanged.connect(self.compare_values)
        self.ui.doubleSpinBox_input_R2.valueChanged.connect(self.compare_values)

        self.default_value_for_calculated_parameters()

        # Обработчик событий
        self.ui.pushButton_save.clicked.connect(self.btn_start_pressed)
        self.ui.pushButton_generate.clicked.connect(self.btn_generate_pressed)

        self.current_mesh_model = MeshModel()

    def btn_start_pressed(self):
        automation = MAPDLController()
        automation.execute()

    def btn_save_pressed(self):
        # Заполнение геометрических параметров
        self.current_mesh_model.R1 = self.ui.doubleSpinBox_input_R1.value()
        self.current_mesh_model.R2 = self.ui.doubleSpinBox_input_R2.value()
        self.current_mesh_model.H = self.ui.doubleSpinBox_input_H.value()

        # Заполнение параметров разбиения
        self.current_mesh_model.N = self.ui.spinBox_input_N.value()
        self.current_mesh_model.m = self.ui.spinBox_input_m.value()
        self.current_mesh_model.m_shp = self.ui.spinBox_input_m_shp.value()

        # Заполнение размеров ребер
        self.current_mesh_model.a_sp = self.ui.doubleSpinBox_input_a_sp.value()
        self.current_mesh_model.b_sp = self.ui.doubleSpinBox_input_b_sp.value()
        self.current_mesh_model.a_col = self.ui.doubleSpinBox_input_a_col.value()
        self.current_mesh_model.b_col = self.ui.doubleSpinBox_input_b_col.value()
        self.current_mesh_model.a_shp = self.ui.doubleSpinBox_input_a_shp.value()
        self.current_mesh_model.b_shp = self.ui.doubleSpinBox_input_b_shp.value()

        # Заполнение механических свойств материалов для спиральных ребер
        self.current_mesh_model.material_spiral = {
            "E_x": self.ui.doubleSpinBox_input_E_x_spiral.value(),
            "E_y": self.ui.doubleSpinBox_input_E_y_spiral.value(),
            "E_z": self.ui.doubleSpinBox_input_E_z_spiral.value(),
            "G_xy": self.ui.doubleSpinBox_input_G_xy_spiral.value(),
            "G_yz": self.ui.doubleSpinBox_input_G_yz_spiral.value(),
            "G_xz": self.ui.doubleSpinBox_input_G_xz_spiral.value(),
            "v": self.ui.doubleSpinBox_input_v_spiral.value()
        }

        # Заполнение механических свойств материалов для кольцевых ребер
        self.current_mesh_model.material_ring = {
            "E_x": self.ui.doubleSpinBox_input_E_x_ring.value(),
            "E_y": self.ui.doubleSpinBox_input_E_y_ring.value(),
            "E_z": self.ui.doubleSpinBox_input_E_z_ring.value(),
            "G_xy": self.ui.doubleSpinBox_input_G_xy_ring.value(),
            "G_yz": self.ui.doubleSpinBox_input_G_yz_ring.value(),
            "G_xz": self.ui.doubleSpinBox_input_G_xz_ring.value(),
            "v": self.ui.doubleSpinBox_input_v_ring.value()
        }

        # Заполнение механических свойств материалов для шпангоутов
        self.current_mesh_model.material_shp = {
            "E_x": self.ui.doubleSpinBox_input_E_x_shp.value(),
            "E_y": self.ui.doubleSpinBox_input_E_y_shp.value(),
            "E_z": self.ui.doubleSpinBox_input_E_z_shp.value(),
            "G_xy": self.ui.doubleSpinBox_input_G_xy_shp.value(),
            "G_yz": self.ui.doubleSpinBox_input_G_yz_shp.value(),
            "G_xz": self.ui.doubleSpinBox_input_G_xz_shp.value(),
            "v": self.ui.doubleSpinBox_input_v_shp.value()
        }

        print("Данные успешно сохранены в объект MeshModel!")

    def btn_generate_pressed(self):
        # Заполнение параметров (для примера)
        self.current_mesh_model.R1 = 1.5
        self.current_mesh_model.R2 = 1.0
        self.current_mesh_model.H = 5.0
        self.current_mesh_model.N = 30
        self.current_mesh_model.m = 7
        self.current_mesh_model.m_shp = 5
        self.current_mesh_model.a_sp = 0.006
        self.current_mesh_model.b_sp = 0.03
        self.current_mesh_model.material_spiral = {
            "E_x": 70e9, "E_y": 70e9, "E_z": 70e9,
            "G_xy": 26e9, "G_yz": 26e9, "G_xz": 26e9,
            "v": 0.33
        }
        FileController.save_mesh_model_to_txt(self.current_mesh_model)
        FileController.generate_apdl_file(self.current_mesh_model)
        print("btn generate pressed")

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
