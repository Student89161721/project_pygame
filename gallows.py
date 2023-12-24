from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from gallows_ui import Ui_Form


class GallowsMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Настройки виселицы')