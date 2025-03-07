from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow

from Ui.main_window import Ui_MainWindow


class MainWindowView(QMainWindow):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса
        self.ui = Ui_MainWindow()  # Создаем экземпляр UI
        self.ui.setupUi(self)  # Устанавливаем интерфейс
        self.setup_QSpinBox()
        self.setup_QDoubleSpinBox()

    def setup_QSpinBox(self):

        # Количество элементов
        quantity_spinboxes = [
            self.ui.spinBox_input_N_spiral,
            self.ui.spinBox_input_N_ring,
            self.ui.spinBox_input_N_shp,
        ]

        for spinbox in quantity_spinboxes:
            spinbox.setSuffix(" шт")

    def setup_QDoubleSpinBox(self):
        """Настройка всех числовых полей с валидацией"""
        # Валидаторы
        geometry_validator = QDoubleValidator(0.0, 1e6, 3, self)
        mechanical_validator = QDoubleValidator(0.0, 1e12, 3, self)

        # Геометрические параметры (метры)
        geometry_spinboxes = [
            self.ui.doubleSpinBox_input_R1,
            self.ui.doubleSpinBox_input_R2,
            self.ui.doubleSpinBox_input_H,
            self.ui.doubleSpinBox_input_thinkness_spiral,
            self.ui.doubleSpinBox_input_height_spiral,
            self.ui.doubleSpinBox_input_thinkness_ring,
            self.ui.doubleSpinBox_input_height_ring,
            self.ui.doubleSpinBox_input_thinkness_shp,
            self.ui.doubleSpinBox_input_height_shp,
        ]

        for spinbox in geometry_spinboxes:
            spinbox.lineEdit().setValidator(geometry_validator)
            spinbox.setDecimals(3)
            spinbox.setSingleStep(0.001)
            spinbox.setSuffix(" м")

        # Физико-механические параметры
        phisical_and_mechanical_spinboxes = [
            # Спиральная кромка
            self.ui.doubleSpinBox_input_E_x_spiral,
            self.ui.doubleSpinBox_input_E_y_spiral,
            self.ui.doubleSpinBox_input_E_z_spiral,
            self.ui.doubleSpinBox_input_G_xy_spiral,
            self.ui.doubleSpinBox_input_G_yz_spiral,
            self.ui.doubleSpinBox_input_G_xz_spiral,
            self.ui.doubleSpinBox_input_v_spiral,

            # Кольцевая кромка
            self.ui.doubleSpinBox_input_E_x_ring,
            self.ui.doubleSpinBox_input_E_y_ring,
            self.ui.doubleSpinBox_input_E_z_ring,
            self.ui.doubleSpinBox_input_G_xy_ring,
            self.ui.doubleSpinBox_input_G_yz_ring,
            self.ui.doubleSpinBox_input_G_xz_ring,
            self.ui.doubleSpinBox_input_v_ring,

            # Шпангоуты
            self.ui.doubleSpinBox_input_E_x_shp,
            self.ui.doubleSpinBox_input_E_y_shp,
            self.ui.doubleSpinBox_input_E_z_shp,
            self.ui.doubleSpinBox_input_G_xy_shp,
            self.ui.doubleSpinBox_input_G_yz_shp,
            self.ui.doubleSpinBox_input_G_xz_shp,
            self.ui.doubleSpinBox_input_v_shp,
        ]

        for spinbox in phisical_and_mechanical_spinboxes:
            spinbox.lineEdit().setValidator(mechanical_validator)
            spinbox.setDecimals(3)
            spinbox.setSingleStep(0.001)

            # Специальная обработка коэффициента Пуассона
            if "v_" in spinbox.objectName():
                spinbox.setSuffix("")
                spinbox.setRange(0.0, 0.5)
                spinbox.setSingleStep(0.001)
            else:
                spinbox.setSuffix(" Па")
                spinbox.setRange(0.0, 1e12)  # До 1 триллиона Па doubleSpinBox_input_v_shp,
