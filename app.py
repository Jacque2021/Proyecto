import sys
from PySide6.QtWidgets import QApplication
from controllers.main_window import MainWindowsForm
if __name__ == '__main__':
    app = QApplication()
    window = MainWindowsForm()
    window.show()
    sys.exit(app.exec())