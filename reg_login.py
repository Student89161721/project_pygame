from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
import sys
from registration_ui import Ui_MainWindow
from successful_registration import Ui_Form
from login_ui import Ui_MainWindow2
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
import sqlite3
global nickname_
global score_


class PasswordError(Exception):
    pass


class NoPasswordError(PasswordError):  # Вызывается, если пароль не введен
    pass


class PasswordLenError(PasswordError):  # Вызывается, если длина пароля не более 8 символов
    pass


class NicknameError(Exception):
    pass


class NoNicknameError(NicknameError):  # Вызывается, если номер телефона не введен
    pass


class NicknameFormatError(NicknameError):  # Вызывается, если формат номера неверный
    pass


class NicknameLenError(NicknameError):  # Вызывается, если длина номера (без +7 и 8) не равна десяти
    pass


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
        self.second_form = SuccessfulRegistration()

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
        
    def run(self):  # Метод, вызываемый при нажатии кнопки 'Зарегистрироваться'
        nickname = self.name.text()  # Проверка на корректность номера телефона и вывод ошибок
        try:
            if not nickname:
                raise NoNicknameError('Введите пароль')
            else:
                self.name_error_Label.setText('')
        except NoNicknameError:
            self.name_error_Label.setText('Введите номер телефона')

        password = self.password.text()  # Проверка на корректность пароля и вывод ошибок
        try:
            if not password:
                raise NoPasswordError
            elif len(password) < 9:
                raise PasswordLenError
            else:
                self.password_error_Label.setText('')
        except NoPasswordError:
            self.password_error_Label.setText('Введите пароль')
        except PasswordLenError:
            self.password_error_Label.setText('Длина пароля должна превышать 8 символов')

        if not self.password_error_Label.text() and not self.name_error_Label.text():  # Проверка есть ли ошибки
            connection = sqlite3.connect('gallowsdir/database.db')
            cursor = connection.cursor()
            try:  # Если данных в базе нет, то сработает try, а если есть - except
                cursor.execute('BEGIN')
                cursor.execute('INSERT INTO users (nickname, password, score) VALUES (?, ?, ?)',
                               (nickname, password, 0))
                cursor.execute('COMMIT')
                self.password.setText('')
                self.name.setText('')
                self.second_form.show()
                self.registration_error_Label.setText('')
            except sqlite3.IntegrityError:
                cursor.execute('ROLLBACK')
                self.registration_error_Label.setText(
                    '''Эти данные уже есть в базе. Нажмите на кнопку 'Войти' и введите их''')
            connection.close()
        self.close()


class SuccessfulRegistration(QWidget, Ui_Form):  # Окно успешной регистрации
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Успешная регистрация!')
        self.OK_Button.clicked.connect(self.close)


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
        nickname = self.name.text()
        password = self.password.text()
        try:  # Проверка, введены ли данные
            if not nickname:
                raise NoNicknameError
            else:
                self.name_error_Label.setText('')
            if not password:
                raise NoPasswordError
            else:
                self.password_error_Label.setText('')
        except NoNicknameError:
            self.name_error_Label.setText('Введите номер телефона')
        except NoPasswordError:
            self.password_error_Label.setText('Введите пароль')

        if not self.password_error_Label.text() and not self.name_error_Label.text():
            connection = sqlite3.connect('gallowsdir/database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()

            for el in users:
                if el[1] == nickname:
                    if el[2] == password:
                        id_ = cursor.execute('''SELECT * FROM users WHERE nickname=?''',
                                                  (nickname,)).fetchall()
                        global nickname_
                        nickname_ = id_[0][1]
                        global score_
                        score_ = id_[0][3]
                        self.password.setText('')
                        self.name.setText('')
                        self.name_error_Label.setText('')
                        self.close()
                        break
                    else:
                        self.password_error_Label.setText('Неверный пароль')
                        break
            else:
                self.password_error_Label.setText(
                    '''Ваших данных нет в базе. Нажмите на кнопку 'Зарегистрироваться' и введите их''')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
