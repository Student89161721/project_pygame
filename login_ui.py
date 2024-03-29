# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 560)
        self.reg_widget = QtWidgets.QWidget(parent=MainWindow)
        self.reg_widget.setObjectName("reg_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.reg_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.text_Layout = QtWidgets.QVBoxLayout()
        self.text_Layout.setObjectName("text_Layout")
        self.frame_3 = QtWidgets.QFrame(parent=self.reg_widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.registration = QtWidgets.QLabel(parent=self.frame_3)
        self.registration.setGeometry(QtCore.QRect(10, 10, 571, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registration.sizePolicy().hasHeightForWidth())
        self.registration.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(36)
        self.registration.setFont(font)
        self.registration.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.registration.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.registration.setObjectName("registration")
        self.text_Layout.addWidget(self.frame_3)
        self.verticalLayout_6.addLayout(self.text_Layout)
        self.name_Layout = QtWidgets.QVBoxLayout()
        self.name_Layout.setObjectName("name_Layout")
        self.frame_4 = QtWidgets.QFrame(parent=self.reg_widget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.name = QtWidgets.QLineEdit(parent=self.frame_4)
        self.name.setGeometry(QtCore.QRect(20, 50, 561, 41))
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 41))
        self.label.setObjectName("label")
        self.name_error_Label = QtWidgets.QLabel(parent=self.frame_4)
        self.name_error_Label.setGeometry(QtCore.QRect(20, 90, 691, 21))
        self.name_error_Label.setStyleSheet("QLabel {\n"
"color: #ff0000\n"
"}")
        self.name_error_Label.setText("")
        self.name_error_Label.setObjectName("name_error_Label")
        self.name_Layout.addWidget(self.frame_4)
        self.verticalLayout_6.addLayout(self.name_Layout)
        self.password_Layout = QtWidgets.QVBoxLayout()
        self.password_Layout.setObjectName("password_Layout")
        self.frame = QtWidgets.QFrame(parent=self.reg_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.password = QtWidgets.QLineEdit(parent=self.frame)
        self.password.setGeometry(QtCore.QRect(20, 50, 511, 41))
        self.password.setText("")
        self.password.setObjectName("password")
        self.visibility_button = QtWidgets.QPushButton(parent=self.frame)
        self.visibility_button.setGeometry(QtCore.QRect(540, 50, 41, 41))
        self.visibility_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/visibility_on.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("data/visibility_off.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.visibility_button.setIcon(icon)
        self.visibility_button.setCheckable(True)
        self.visibility_button.setChecked(False)
        self.visibility_button.setObjectName("visibility_button")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 271, 41))
        self.label_3.setObjectName("label_3")
        self.password_error_Label = QtWidgets.QLabel(parent=self.frame)
        self.password_error_Label.setGeometry(QtCore.QRect(20, 95, 601, 16))
        self.password_error_Label.setStyleSheet("QLabel {\n"
"color: #ff0000\n"
"}")
        self.password_error_Label.setText("")
        self.password_error_Label.setObjectName("password_error_Label")
        self.password_Layout.addWidget(self.frame)
        self.verticalLayout_6.addLayout(self.password_Layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=self.reg_widget)
        self.widget.setObjectName("widget")
        self.log_in_Button = QtWidgets.QPushButton(parent=self.widget)
        self.log_in_Button.setGeometry(QtCore.QRect(20, 0, 561, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_in_Button.sizePolicy().hasHeightForWidth())
        self.log_in_Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.log_in_Button.setFont(font)
        self.log_in_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.log_in_Button.setObjectName("log_in_Button")
        self.reg_Button = QtWidgets.QPushButton(parent=self.widget)
        self.reg_Button.setGeometry(QtCore.QRect(290, 70, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        self.reg_Button.setFont(font)
        self.reg_Button.setObjectName("reg_Button")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(100, 70, 171, 51))
        self.label_4.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_4.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.login_error_Label = QtWidgets.QLabel(parent=self.widget)
        self.login_error_Label.setGeometry(QtCore.QRect(20, 50, 561, 21))
        self.login_error_Label.setStyleSheet("QLabel {\n"
"color: #ff0000\n"
"}")
        self.login_error_Label.setText("")
        self.login_error_Label.setObjectName("login_error_Label")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.reg_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registration.setText(_translate("MainWindow", "Войти"))
        self.label.setText(_translate("MainWindow", "Введите имя пользователя:"))
        self.label_3.setText(_translate("MainWindow", "Введите пароль:"))
        self.log_in_Button.setText(_translate("MainWindow", "Войти"))
        self.reg_Button.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.label_4.setText(_translate("MainWindow", "Ещё не зарегистрированы?"))
