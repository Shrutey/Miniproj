
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, resource

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 583)
        self.widget = QtWidgets.QWidget(Form)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Center the window
        qr = Form.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        Form.move(qr.topLeft())
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 50, 900, 600))

        self.widget.setObjectName("widget")
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setGeometry(QtCore.QRect(40, 30, 281, 430))
        self.logo.setStyleSheet("border-image:url(:/images/logo.png);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;\n"
"\n"
"background-color: gba(0, 0, 0,80);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.whitebg = QtWidgets.QLabel(self.widget)
        self.whitebg.setGeometry(QtCore.QRect(318, 30, 291, 430))
        self.whitebg.setStyleSheet("\n"
"background-color: rgb(255, 255, 240);\n"
"    border-bottom-right-radius: 30px;\n"
"    border-top-right-radius: 30px;")
        self.whitebg.setText("")
        self.whitebg.setObjectName("whitebg")
        self.llabe = QtWidgets.QLabel(self.widget)
        self.llabe.setGeometry(QtCore.QRect(420, 80, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(22)
        self.llabe.setFont(font)
        self.llabe.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.llabe.setStyleSheet("color: rgba(0, 0, 0,200);     ")
        self.llabe.setObjectName("llabe")
        self.lusername = QtWidgets.QLineEdit(self.widget)
        self.lusername.setGeometry(QtCore.QRect(370, 159, 190, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        self.lusername.setFont(font)
        self.lusername.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
"    \n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lusername.setObjectName("lusername")
        self.lpassword = QtWidgets.QLineEdit(self.widget)
        self.lpassword.setGeometry(QtCore.QRect(370, 210, 190, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        self.lpassword.setFont(font)
        self.lpassword.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
"    \n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lpassword.setObjectName("lpassword")
        self.login_button = QtWidgets.QPushButton(self.widget)
        self.login_button.setGeometry(QtCore.QRect(370, 261, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton#login_button {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#login_button:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(12, 112, 117, 255), stop:0.5 rgba(9, 113, 114, 255), stop:1 rgba(101, 161, 185, 255));\n"
"}\n"
"\n"
"QPushButton#login_button:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(101, 161, 185, 255), stop:0.5 rgba(40, 77, 95, 255), stop:1 rgba(44, 42, 42, 255));\n"
"}\n"
"")

# Error labels for invalid username and password
        self.invalid_username_label = QtWidgets.QLabel(self.widget)
        self.invalid_username_label.setGeometry(QtCore.QRect(370, 190, 190, 20))
        self.invalid_username_label.setStyleSheet("color: red;")
        self.invalid_username_label.setObjectName("invalid_username_label")
        self.invalid_username_label.setVisible(False)

        self.invalid_password_label = QtWidgets.QLabel(self.widget)
        self.invalid_password_label.setGeometry(QtCore.QRect(370, 240, 190, 20))
        self.invalid_password_label.setStyleSheet("color: red;")
        self.invalid_password_label.setObjectName("invalid_password_label")
        self.invalid_password_label.setVisible(False)
        
        self.login_button.setObjectName("login_button")
        self.forgot = QtWidgets.QLabel(self.widget)
        self.forgot.setGeometry(QtCore.QRect(370, 312, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.forgot.setFont(font)
        self.forgot.setStyleSheet("color:rgb(97, 97, 97)")
        self.forgot.setObjectName("forgot")
        self.lalregister = QtWidgets.QLabel(self.widget)
        self.lalregister.setGeometry(QtCore.QRect(370, 420, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.lalregister.setFont(font)
        self.lalregister.setObjectName("lalregister")
        self.regdirect = QtWidgets.QLabel(self.widget)
        self.regdirect.setGeometry(QtCore.QRect(500, 420, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(11)
        self.regdirect.setFont(font)
        self.regdirect.setObjectName("regdirect")
        self.whitebg.raise_()
        self.logo.raise_()
        self.llabe.raise_()
        self.lusername.raise_()
        self.lpassword.raise_()
        self.login_button.raise_()
        self.forgot.raise_()
        self.lalregister.raise_()
        self.regdirect.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.llabe.setText(_translate("Form", "LOGIN"))
        self.lusername.setPlaceholderText(_translate("Form", "Username"))
        self.lpassword.setPlaceholderText(_translate("Form", "Password"))
        self.login_button.setText(_translate("Form", "L O G I N"))
        self.forgot.setText(_translate("Form", "Forgot your Username or Password?"))
        self.lalregister.setText(_translate("Form", "Already registered?"))
        self.regdirect.setText(_translate("Form", "Register"))

if __name__== "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui=Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

