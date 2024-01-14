from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
import sys
from registration_ui import Ui_MainWindow
from login_ui import Ui_MainWindow2
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


class RegistrationWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Окно регистрации')
        self.login_form = LoginWidget()
        self.visibility_button.clicked.connect(self.change_visibility)  # При нажатии меняется видимость пароля
        self.copy_button.clicked.connect(self.copy)  # При нажатии пароль копируется в буфер обмена
        self.generation_button.clicked.connect(self.generation)  # При нажатии генерируется пароль
        self.reg_Button.clicked.connect(self.run)
        self.log_in_Button.clicked.connect(self.show_login_window)  # При нажатии открывается окно входа
        self.log_in_Button.clicked.connect(self.close)

    def change_visibility(self):  # Метод изменения видимости пароля
        if not self.visibility_button.isChecked():
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password.setEchoMode(QLineEdit.EchoMode.Password)

    def copy(self):  # Метод копирования пароля в буфер обмена
        QApplication.clipboard().setText(self.password.text())

    def generation(self):  # Метод генерации пароля
        symbols = ascii_lowercase + ascii_uppercase + digits
        length, password = 15, ''
        for i in range(length):
            password += choice(symbols)
        self.password.setText(password)

    def show_login_window(self):  # Метод вызова окна входа
        self.login_form.show()

    def run(self):
        pass




class LoginWidget(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Окно входа')
        self.reg_Button.clicked.connect(self.show_reg_window)
        self.reg_Button.clicked.connect(self.close)
        self.log_in_Button.clicked.connect(self.run)  # Кнопка входа в аккаунт

    def change_visibility(self):  # Метод изменения видимости пароля
        if not self.visibility_button.isChecked():
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password.setEchoMode(QLineEdit.EchoMode.Password)

    def show_reg_window(self):  # Вызывает окно регистрации
        self.reg_form = RegistrationWidget()
        self.reg_form.show()

    def run(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
