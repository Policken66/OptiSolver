from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from Ui.main_window import Ui_MainWindow


class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.doubleSpinBox_input_R1.valueChanged.connect(self.compare_values)
        self.ui.doubleSpinBox_input_R2.valueChanged.connect(self.compare_values)

        self.default_value_for_calculated_parameters()



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
