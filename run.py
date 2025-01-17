import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from Controllers.main_window_controller import MainWindowController


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindowController()
    main_window.show()
    sys.exit(app.exec())