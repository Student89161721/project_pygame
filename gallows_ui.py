# Form implementation generated from reading ui file 'gallows_ui.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Form.resize(402, 302)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 9, 401, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.theme_comboBox = QtWidgets.QComboBox(parent=Form)
        self.theme_comboBox.setGeometry(QtCore.QRect(200, 130, 191, 31))
        self.theme_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.theme_comboBox.setObjectName("theme_comboBox")
        self.theme_comboBox.addItem("")
        self.theme_comboBox.addItem("")
        self.theme_comboBox.addItem("")
        self.theme_comboBox.addItem("")
        self.theme_comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 240, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 111, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAccessibleDescription("")
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_3.setMidLineWidth(11)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 111, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAccessibleDescription("")
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_4.setMidLineWidth(11)
        self.label_4.setObjectName("label_4")
        self.difficulty_comboBox = QtWidgets.QComboBox(parent=Form)
        self.difficulty_comboBox.setGeometry(QtCore.QRect(200, 190, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.difficulty_comboBox.setFont(font)
        self.difficulty_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.difficulty_comboBox.setObjectName("difficulty_comboBox")
        self.difficulty_comboBox.addItem("")
        self.difficulty_comboBox.addItem("")
        self.difficulty_comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Виселица"))
        self.label_2.setText(_translate("Form", "Настройки"))
        self.theme_comboBox.setItemText(0, _translate("Form", "Случайная"))
        self.theme_comboBox.setItemText(1, _translate("Form", "Природа"))
        self.theme_comboBox.setItemText(2, _translate("Form", "Еда"))
        self.theme_comboBox.setItemText(3, _translate("Form", "Страны"))
        self.theme_comboBox.setItemText(4, _translate("Form", "Животные"))
        self.pushButton.setText(_translate("Form", "Играть"))
        self.label_3.setText(_translate("Form", "Тема"))
        self.label_4.setText(_translate("Form", "Сложность"))
        self.difficulty_comboBox.setItemText(0, _translate("Form", "Легкая (4-5 букв)"))
        self.difficulty_comboBox.setItemText(1, _translate("Form", "Нормальная (6-8 букв)"))
        self.difficulty_comboBox.setItemText(2, _translate("Form", "Сложная (9-11 букв)"))
