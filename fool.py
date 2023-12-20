from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from fool_menu_ui import Ui_Form


class FoolMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки дурака')