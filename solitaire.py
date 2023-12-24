from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from solitaire_ui import Ui_Form


class SolitaireMenu(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Настройки косынки')