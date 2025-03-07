import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from Controllers.main_window_controller import MainWindowController
from Views.main_window_view import MainWindowView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindowView()
    controller = MainWindowController(view)

    view.show()
    sys.exit(app.exec())