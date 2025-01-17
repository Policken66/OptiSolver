# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(965, 638)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 30, 251, 25))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_N = QLabel(self.horizontalLayoutWidget_4)
        self.label_N.setObjectName(u"label_N")

        self.horizontalLayout_4.addWidget(self.label_N)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.spinBox_input_N = QSpinBox(self.horizontalLayoutWidget_4)
        self.spinBox_input_N.setObjectName(u"spinBox_input_N")

        self.horizontalLayout_4.addWidget(self.spinBox_input_N)

        self.horizontalLayoutWidget_5 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(9, 60, 251, 25))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_m = QLabel(self.horizontalLayoutWidget_5)
        self.label_m.setObjectName(u"label_m")

        self.horizontalLayout_5.addWidget(self.label_m)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.spinBox_input_m = QSpinBox(self.horizontalLayoutWidget_5)
        self.spinBox_input_m.setObjectName(u"spinBox_input_m")

        self.horizontalLayout_5.addWidget(self.spinBox_input_m)

        self.horizontalLayoutWidget_6 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 90, 251, 25))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_m_shp = QLabel(self.horizontalLayoutWidget_6)
        self.label_m_shp.setObjectName(u"label_m_shp")

        self.horizontalLayout_6.addWidget(self.label_m_shp)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.spinBox_input_m_shp = QSpinBox(self.horizontalLayoutWidget_6)
        self.spinBox_input_m_shp.setObjectName(u"spinBox_input_m_shp")

        self.horizontalLayout_6.addWidget(self.spinBox_input_m_shp)


        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)

        self.pushButton_generate = QPushButton(self.centralwidget)
        self.pushButton_generate.setObjectName(u"pushButton_generate")

        self.gridLayout.addWidget(self.pushButton_generate, 3, 1, 1, 1)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.gridLayout.addWidget(self.pushButton_save, 2, 1, 1, 1)

        self.geometric_params_groupBox = QGroupBox(self.centralwidget)
        self.geometric_params_groupBox.setObjectName(u"geometric_params_groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.geometric_params_groupBox.sizePolicy().hasHeightForWidth())
        self.geometric_params_groupBox.setSizePolicy(sizePolicy1)
        self.geometric_params_groupBox.setMinimumSize(QSize(300, 0))
        self.label_geometric_params_model = QLabel(self.geometric_params_groupBox)
        self.label_geometric_params_model.setObjectName(u"label_geometric_params_model")
        self.label_geometric_params_model.setGeometry(QRect(60, 150, 171, 121))
        self.horizontalLayoutWidget = QWidget(self.geometric_params_groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 281, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_R1 = QLabel(self.horizontalLayoutWidget)
        self.label_R1.setObjectName(u"label_R1")

        self.horizontalLayout.addWidget(self.label_R1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.doubleSpinBox_input_R1 = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox_input_R1.setObjectName(u"doubleSpinBox_input_R1")

        self.horizontalLayout.addWidget(self.doubleSpinBox_input_R1)

        self.horizontalLayoutWidget_2 = QWidget(self.geometric_params_groupBox)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 60, 281, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_R2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_R2.setObjectName(u"label_R2")

        self.horizontalLayout_2.addWidget(self.label_R2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.doubleSpinBox_input_R2 = QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.doubleSpinBox_input_R2.setObjectName(u"doubleSpinBox_input_R2")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_input_R2)

        self.horizontalLayoutWidget_3 = QWidget(self.geometric_params_groupBox)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 100, 281, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_H = QLabel(self.horizontalLayoutWidget_3)
        self.label_H.setObjectName(u"label_H")

        self.horizontalLayout_3.addWidget(self.label_H)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.doubleSpinBox_input_H = QDoubleSpinBox(self.horizontalLayoutWidget_3)
        self.doubleSpinBox_input_H.setObjectName(u"doubleSpinBox_input_H")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_input_H)


        self.gridLayout.addWidget(self.geometric_params_groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(630, 300))
        self.layoutWidget = QWidget(self.groupBox_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 591, 261))
        self.horizontalLayout_34 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.layoutWidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy2)
        self.groupBox_7.setMinimumSize(QSize(200, 0))
        self.layoutWidget1 = QWidget(self.groupBox_7)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 181, 231))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_E_x_spiral = QLabel(self.layoutWidget1)
        self.label_E_x_spiral.setObjectName(u"label_E_x_spiral")

        self.horizontalLayout_13.addWidget(self.label_E_x_spiral)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.doubleSpinBox_input_E_x_spiral = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_input_E_x_spiral.setObjectName(u"doubleSpinBox_input_E_x_spiral")

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_input_E_x_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_E_y_spiral = QLabel(self.layoutWidget1)
        self.label_E_y_spiral.setObjectName(u"label_E_y_spiral")

        self.horizontalLayout_14.addWidget(self.label_E_y_spiral)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)

        self.doubleSpinBox_input_E_y_spiral = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_input_E_y_spiral.setObjectName(u"doubleSpinBox_input_E_y_spiral")

        self.horizontalLayout_14.addWidget(self.doubleSpinBox_input_E_y_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_E_z_spiral = QLabel(self.layoutWidget1)
        self.label_E_z_spiral.setObjectName(u"label_E_z_spiral")

        self.horizontalLayout_15.addWidget(self.label_E_z_spiral)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.doubleSpinBox_input_E_z_spiral = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_input_E_z_spiral.setObjectName(u"doubleSpinBox_input_E_z_spiral")

        self.horizontalLayout_15.addWidget(self.doubleSpinBox_input_E_z_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_G_xy_spiral = QLabel(self.layoutWidget1)
        self.label_G_xy_spiral.setObjectName(u"label_G_xy_spiral")

        self.horizontalLayout_16.addWidget(self.label_G_xy_spiral)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)

        self.doubleSpinBox_input_G_xy_spiral = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_input_G_xy_spiral.setObjectName(u"doubleSpinBox_input_G_xy_spiral")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_input_G_xy_spiral.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_input_G_xy_spiral.setSizePolicy(sizePolicy3)

        self.horizontalLayout_16.addWidget(self.doubleSpinBox_input_G_xy_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_G_yz_spiral = QLabel(self.layoutWidget1)
        self.label_G_yz_spiral.setObjectName(u"label_G_yz_spiral")

        self.horizontalLayout_17.addWidget(self.label_G_yz_spiral)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.doubleSpinBox_input_G_yz_spiral = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_input_G_yz_spiral.setObjectName(u"doubleSpinBox_input_G_yz_spiral")

        self.horizontalLayout_17.addWidget(self.doubleSpinBox_input_G_yz_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_G_xz_spiral = QLabel(self.layoutWidget1)
        self.label_G_xz_spiral.setObjectName(u"label_G_xz_spiral")

        self.horizontalLayout_18.addWidget(self.label_G_xz_spiral)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)

        self.doubleSpinBox_input_G_xz_spiral = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_input_G_xz_spiral.setObjectName(u"doubleSpinBox_input_G_xz_spiral")

        self.horizontalLayout_18.addWidget(self.doubleSpinBox_input_G_xz_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_v_spiral = QLabel(self.layoutWidget1)
        self.label_v_spiral.setObjectName(u"label_v_spiral")

        self.horizontalLayout_19.addWidget(self.label_v_spiral)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.doubleSpinBox_input_v_spiral = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_input_v_spiral.setObjectName(u"doubleSpinBox_input_v_spiral")

        self.horizontalLayout_19.addWidget(self.doubleSpinBox_input_v_spiral)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_34.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.layoutWidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy4)
        self.layoutWidget2 = QWidget(self.groupBox_8)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 171, 231))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_E_x_ring = QLabel(self.layoutWidget2)
        self.label_E_x_ring.setObjectName(u"label_E_x_ring")

        self.horizontalLayout_20.addWidget(self.label_E_x_ring)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.doubleSpinBox_input_E_x_ring = QDoubleSpinBox(self.layoutWidget2)
        self.doubleSpinBox_input_E_x_ring.setObjectName(u"doubleSpinBox_input_E_x_ring")

        self.horizontalLayout_20.addWidget(self.doubleSpinBox_input_E_x_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_E_y_ring = QLabel(self.layoutWidget2)
        self.label_E_y_ring.setObjectName(u"label_E_y_ring")

        self.horizontalLayout_21.addWidget(self.label_E_y_ring)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)

        self.doubleSpinBox_input_E_y_ring = QDoubleSpinBox(self.layoutWidget2)
        self.doubleSpinBox_input_E_y_ring.setObjectName(u"doubleSpinBox_input_E_y_ring")

        self.horizontalLayout_21.addWidget(self.doubleSpinBox_input_E_y_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_E_z_ring = QLabel(self.layoutWidget2)
        self.label_E_z_ring.setObjectName(u"label_E_z_ring")

        self.horizontalLayout_22.addWidget(self.label_E_z_ring)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_22)

        self.doubleSpinBox_input_E_z_ring = QDoubleSpinBox(self.layoutWidget2)
        self.doubleSpinBox_input_E_z_ring.setObjectName(u"doubleSpinBox_input_E_z_ring")

        self.horizontalLayout_22.addWidget(self.doubleSpinBox_input_E_z_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_G_xy_ring = QLabel(self.layoutWidget2)
        self.label_G_xy_ring.setObjectName(u"label_G_xy_ring")

        self.horizontalLayout_23.addWidget(self.label_G_xy_ring)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_23)

        self.doubleSpinBox_input_G_xy_ring = QDoubleSpinBox(self.layoutWidget2)
        self.doubleSpinBox_input_G_xy_ring.setObjectName(u"doubleSpinBox_input_G_xy_ring")

        self.horizontalLayout_23.addWidget(self.doubleSpinBox_input_G_xy_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_G_yz_ring = QLabel(self.layoutWidget2)
        self.label_G_yz_ring.setObjectName(u"label_G_yz_ring")

        self.horizontalLayout_24.addWidget(self.label_G_yz_ring)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_24)

        self.doubleSpinBox_input_G_yz_ring = QDoubleSpinBox(self.layoutWidget2)
        self.doubleSpinBox_input_G_yz_ring.setObjectName(u"doubleSpinBox_input_G_yz_ring")

        self.horizontalLayout_24.addWidget(self.doubleSpinBox_input_G_yz_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_G_xz_ring = QLabel(self.layoutWidget2)
        self.label_G_xz_ring.setObjectName(u"label_G_xz_ring")

        self.horizontalLayout_25.addWidget(self.label_G_xz_ring)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_25)

        self.doubleSpinBox_input_G_xz_ring = QDoubleSpinBox(self.layoutWidget2)
        self.doubleSpinBox_input_G_xz_ring.setObjectName(u"doubleSpinBox_input_G_xz_ring")

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_input_G_xz_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_v_ring = QLabel(self.layoutWidget2)
        self.label_v_ring.setObjectName(u"label_v_ring")

        self.horizontalLayout_26.addWidget(self.label_v_ring)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_26)

        self.doubleSpinBox_input_v_ring = QDoubleSpinBox(self.layoutWidget2)
        self.doubleSpinBox_input_v_ring.setObjectName(u"doubleSpinBox_input_v_ring")

        self.horizontalLayout_26.addWidget(self.doubleSpinBox_input_v_ring)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_34.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.layoutWidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy4.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy4)
        self.layoutWidget3 = QWidget(self.groupBox_9)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 171, 231))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_E_x_shp = QLabel(self.layoutWidget3)
        self.label_E_x_shp.setObjectName(u"label_E_x_shp")

        self.horizontalLayout_27.addWidget(self.label_E_x_shp)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_27)

        self.doubleSpinBox_input_E_x_shp = QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox_input_E_x_shp.setObjectName(u"doubleSpinBox_input_E_x_shp")

        self.horizontalLayout_27.addWidget(self.doubleSpinBox_input_E_x_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_E_y_shp = QLabel(self.layoutWidget3)
        self.label_E_y_shp.setObjectName(u"label_E_y_shp")

        self.horizontalLayout_28.addWidget(self.label_E_y_shp)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_28)

        self.doubleSpinBox_input_E_y_shp = QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox_input_E_y_shp.setObjectName(u"doubleSpinBox_input_E_y_shp")

        self.horizontalLayout_28.addWidget(self.doubleSpinBox_input_E_y_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_E_z_shp = QLabel(self.layoutWidget3)
        self.label_E_z_shp.setObjectName(u"label_E_z_shp")

        self.horizontalLayout_29.addWidget(self.label_E_z_shp)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_29)

        self.doubleSpinBox_input_E_z_shp = QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox_input_E_z_shp.setObjectName(u"doubleSpinBox_input_E_z_shp")

        self.horizontalLayout_29.addWidget(self.doubleSpinBox_input_E_z_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_G_xy_shp = QLabel(self.layoutWidget3)
        self.label_G_xy_shp.setObjectName(u"label_G_xy_shp")

        self.horizontalLayout_30.addWidget(self.label_G_xy_shp)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_30)

        self.doubleSpinBox_input_G_xy_shp = QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox_input_G_xy_shp.setObjectName(u"doubleSpinBox_input_G_xy_shp")

        self.horizontalLayout_30.addWidget(self.doubleSpinBox_input_G_xy_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_G_yz_shp = QLabel(self.layoutWidget3)
        self.label_G_yz_shp.setObjectName(u"label_G_yz_shp")

        self.horizontalLayout_31.addWidget(self.label_G_yz_shp)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_31)

        self.doubleSpinBox_input_G_yz_shp = QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox_input_G_yz_shp.setObjectName(u"doubleSpinBox_input_G_yz_shp")

        self.horizontalLayout_31.addWidget(self.doubleSpinBox_input_G_yz_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_G_xz_shp = QLabel(self.layoutWidget3)
        self.label_G_xz_shp.setObjectName(u"label_G_xz_shp")

        self.horizontalLayout_32.addWidget(self.label_G_xz_shp)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_33)

        self.doubleSpinBox_input_G_xz_shp = QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox_input_G_xz_shp.setObjectName(u"doubleSpinBox_input_G_xz_shp")

        self.horizontalLayout_32.addWidget(self.doubleSpinBox_input_G_xz_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_v_shp = QLabel(self.layoutWidget3)
        self.label_v_shp.setObjectName(u"label_v_shp")

        self.horizontalLayout_33.addWidget(self.label_v_shp)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_32)

        self.doubleSpinBox_input_v_shp = QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox_input_v_shp.setObjectName(u"doubleSpinBox_input_v_shp")

        self.horizontalLayout_33.addWidget(self.doubleSpinBox_input_v_shp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_34.addWidget(self.groupBox_9)


        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 3)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(300, 300))
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 30, 251, 80))
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 20, 231, 25))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_a_sp = QLabel(self.horizontalLayoutWidget_7)
        self.label_a_sp.setObjectName(u"label_a_sp")

        self.horizontalLayout_7.addWidget(self.label_a_sp)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.doubleSpinBox_input_a_sp = QDoubleSpinBox(self.horizontalLayoutWidget_7)
        self.doubleSpinBox_input_a_sp.setObjectName(u"doubleSpinBox_input_a_sp")

        self.horizontalLayout_7.addWidget(self.doubleSpinBox_input_a_sp)

        self.horizontalLayoutWidget_8 = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 50, 231, 25))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_b_sp = QLabel(self.horizontalLayoutWidget_8)
        self.label_b_sp.setObjectName(u"label_b_sp")

        self.horizontalLayout_8.addWidget(self.label_b_sp)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.doubleSpinBox_input_b_sp = QDoubleSpinBox(self.horizontalLayoutWidget_8)
        self.doubleSpinBox_input_b_sp.setObjectName(u"doubleSpinBox_input_b_sp")

        self.horizontalLayout_8.addWidget(self.doubleSpinBox_input_b_sp)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 120, 251, 80))
        self.horizontalLayoutWidget_9 = QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 20, 231, 25))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_a_col = QLabel(self.horizontalLayoutWidget_9)
        self.label_a_col.setObjectName(u"label_a_col")

        self.horizontalLayout_9.addWidget(self.label_a_col)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.doubleSpinBox_input_a_col = QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_input_a_col.setObjectName(u"doubleSpinBox_input_a_col")

        self.horizontalLayout_9.addWidget(self.doubleSpinBox_input_a_col)

        self.horizontalLayoutWidget_10 = QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(10, 50, 231, 25))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_b_col = QLabel(self.horizontalLayoutWidget_10)
        self.label_b_col.setObjectName(u"label_b_col")

        self.horizontalLayout_10.addWidget(self.label_b_col)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.doubleSpinBox_input_b_col = QDoubleSpinBox(self.horizontalLayoutWidget_10)
        self.doubleSpinBox_input_b_col.setObjectName(u"doubleSpinBox_input_b_col")

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_input_b_col)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 210, 251, 80))
        self.horizontalLayoutWidget_11 = QWidget(self.groupBox_6)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(10, 20, 231, 25))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_a_shp = QLabel(self.horizontalLayoutWidget_11)
        self.label_a_shp.setObjectName(u"label_a_shp")

        self.horizontalLayout_11.addWidget(self.label_a_shp)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.doubleSpinBox_input_a_shp = QDoubleSpinBox(self.horizontalLayoutWidget_11)
        self.doubleSpinBox_input_a_shp.setObjectName(u"doubleSpinBox_input_a_shp")

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_input_a_shp)

        self.horizontalLayoutWidget_12 = QWidget(self.groupBox_6)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(10, 50, 231, 25))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_b_shp = QLabel(self.horizontalLayoutWidget_12)
        self.label_b_shp.setObjectName(u"label_b_shp")

        self.horizontalLayout_12.addWidget(self.label_b_shp)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.doubleSpinBox_input_b_shp = QDoubleSpinBox(self.horizontalLayoutWidget_12)
        self.doubleSpinBox_input_b_shp.setObjectName(u"doubleSpinBox_input_b_shp")

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_input_b_shp)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 3, 1)

        self.groupBox_10 = QGroupBox(self.centralwidget)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy1.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy1)
        self.groupBox_10.setMinimumSize(QSize(0, 315))
        self.widget = QWidget(self.groupBox_10)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 27, 141, 91))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_M1 = QLabel(self.widget)
        self.label_M1.setObjectName(u"label_M1")

        self.horizontalLayout_35.addWidget(self.label_M1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_34)

        self.label_value_M_1 = QLabel(self.widget)
        self.label_value_M_1.setObjectName(u"label_value_M_1")

        self.horizontalLayout_35.addWidget(self.label_value_M_1)


        self.verticalLayout.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_M2 = QLabel(self.widget)
        self.label_M2.setObjectName(u"label_M2")

        self.horizontalLayout_36.addWidget(self.label_M2)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_35)

        self.label_value_M_2 = QLabel(self.widget)
        self.label_value_M_2.setObjectName(u"label_value_M_2")

        self.horizontalLayout_36.addWidget(self.label_value_M_2)


        self.verticalLayout.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_M3 = QLabel(self.widget)
        self.label_M3.setObjectName(u"label_M3")

        self.horizontalLayout_37.addWidget(self.label_M3)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_36)

        self.label_value_M_3 = QLabel(self.widget)
        self.label_value_M_3.setObjectName(u"label_value_M_3")

        self.horizontalLayout_37.addWidget(self.label_value_M_3)


        self.verticalLayout.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_M4 = QLabel(self.widget)
        self.label_M4.setObjectName(u"label_M4")

        self.horizontalLayout_38.addWidget(self.label_M4)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_37)

        self.label_value_M_4 = QLabel(self.widget)
        self.label_value_M_4.setObjectName(u"label_value_M_4")

        self.horizontalLayout_38.addWidget(self.label_value_M_4)


        self.verticalLayout.addLayout(self.horizontalLayout_38)

        self.widget1 = QWidget(self.groupBox_10)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 130, 141, 91))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_V1 = QLabel(self.widget1)
        self.label_V1.setObjectName(u"label_V1")

        self.horizontalLayout_39.addWidget(self.label_V1)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_38)

        self.label_value_V_1 = QLabel(self.widget1)
        self.label_value_V_1.setObjectName(u"label_value_V_1")

        self.horizontalLayout_39.addWidget(self.label_value_V_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_V2 = QLabel(self.widget1)
        self.label_V2.setObjectName(u"label_V2")

        self.horizontalLayout_40.addWidget(self.label_V2)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_39)

        self.label_value_V_2 = QLabel(self.widget1)
        self.label_value_V_2.setObjectName(u"label_value_V_2")

        self.horizontalLayout_40.addWidget(self.label_value_V_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_V3 = QLabel(self.widget1)
        self.label_V3.setObjectName(u"label_V3")

        self.horizontalLayout_41.addWidget(self.label_V3)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_40)

        self.label_value_V_3 = QLabel(self.widget1)
        self.label_value_V_3.setObjectName(u"label_value_V_3")

        self.horizontalLayout_41.addWidget(self.label_value_V_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_V4 = QLabel(self.widget1)
        self.label_V4.setObjectName(u"label_V4")

        self.horizontalLayout_42.addWidget(self.label_V4)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_41)

        self.label_value_V_4 = QLabel(self.widget1)
        self.label_value_V_4.setObjectName(u"label_value_V_4")

        self.horizontalLayout_42.addWidget(self.label_value_V_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_42)

        self.widget2 = QWidget(self.groupBox_10)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 220, 141, 51))
        self.verticalLayout_6 = QVBoxLayout(self.widget2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_p1 = QLabel(self.widget2)
        self.label_p1.setObjectName(u"label_p1")

        self.horizontalLayout_43.addWidget(self.label_p1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_42)

        self.label_value_p_1 = QLabel(self.widget2)
        self.label_value_p_1.setObjectName(u"label_value_p_1")

        self.horizontalLayout_43.addWidget(self.label_value_p_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_p2 = QLabel(self.widget2)
        self.label_p2.setObjectName(u"label_p2")

        self.horizontalLayout_44.addWidget(self.label_p2)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_43)

        self.label_value_p_2 = QLabel(self.widget2)
        self.label_value_p_2.setObjectName(u"label_value_p_2")

        self.horizontalLayout_44.addWidget(self.label_value_p_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_44)

        self.widget3 = QWidget(self.groupBox_10)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 280, 141, 22))
        self.horizontalLayout_45 = QHBoxLayout(self.widget3)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_M = QLabel(self.widget3)
        self.label_M.setObjectName(u"label_M")

        self.horizontalLayout_45.addWidget(self.label_M)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_44)

        self.label_value_M = QLabel(self.widget3)
        self.label_value_M.setObjectName(u"label_value_M")

        self.horizontalLayout_45.addWidget(self.label_value_M)


        self.gridLayout.addWidget(self.groupBox_10, 1, 2, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OptiSolver", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0439 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438", None))
        self.label_N.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u0441\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0445 \u0440\u0435\u0431\u0435\u0440", None))
        self.label_m.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u043a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0445 \u0440\u0435\u0431\u0435\u0440", None))
        self.label_m_shp.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u043b\u043e \u0448\u043f\u0430\u043d\u0433\u043e\u0443\u0442\u043e\u0432", None))
        self.pushButton_generate.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.geometric_params_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_geometric_params_model.setText("")
        self.label_R1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u0432\u0435\u0440\u0445\u043d\u0435\u0439 \u043a\u0440\u043e\u043c\u043a\u0438", None))
        self.label_R2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u043d\u0438\u0436\u043d\u0435\u0439 \u043a\u0440\u043e\u043c\u043a\u0438", None))
        self.label_H.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u0437\u0438\u043a\u043e-\u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_E_x_spiral.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_E_y_spiral.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_E_z_spiral.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_G_xy_spiral.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_G_yz_spiral.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_G_xz_spiral.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_spiral.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_E_x_ring.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_E_y_ring.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_E_z_ring.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_G_xy_ring.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_G_yz_ring.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_G_xz_ring.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_ring.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043f\u0430\u043d\u0433\u043e\u0443\u0442", None))
        self.label_E_x_shp.setText(QCoreApplication.translate("MainWindow", u"E_x", None))
        self.label_E_y_shp.setText(QCoreApplication.translate("MainWindow", u"E_y", None))
        self.label_E_z_shp.setText(QCoreApplication.translate("MainWindow", u"E_z", None))
        self.label_G_xy_shp.setText(QCoreApplication.translate("MainWindow", u"G_xy", None))
        self.label_G_yz_shp.setText(QCoreApplication.translate("MainWindow", u"G_yz", None))
        self.label_G_xz_shp.setText(QCoreApplication.translate("MainWindow", u"G_xz", None))
        self.label_v_shp.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0440\u0435\u0431\u0435\u0440\u043d\u043e\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_a_sp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_sp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u044c\u0446\u0435\u0432\u044b\u0435 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_a_col.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_col.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043f\u0430\u043d\u0433\u043e\u0443\u0442", None))
        self.label_a_shp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.label_b_shp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0440\u0435\u0431\u0440\u0430", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_M1.setText(QCoreApplication.translate("MainWindow", u"M_1", None))
        self.label_value_M_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M2.setText(QCoreApplication.translate("MainWindow", u"M_2", None))
        self.label_value_M_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M3.setText(QCoreApplication.translate("MainWindow", u"M_3", None))
        self.label_value_M_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M4.setText(QCoreApplication.translate("MainWindow", u"M_4", None))
        self.label_value_M_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V1.setText(QCoreApplication.translate("MainWindow", u"V_1", None))
        self.label_value_V_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V2.setText(QCoreApplication.translate("MainWindow", u"V_2", None))
        self.label_value_V_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V3.setText(QCoreApplication.translate("MainWindow", u"V_3", None))
        self.label_value_V_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_V4.setText(QCoreApplication.translate("MainWindow", u"V_4", None))
        self.label_value_V_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p1.setText(QCoreApplication.translate("MainWindow", u"p_1", None))
        self.label_value_p_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p2.setText(QCoreApplication.translate("MainWindow", u"p_2", None))
        self.label_value_p_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_value_M.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

