from PyQt5 import QtCore, QtGui, QtWidgets
import resource, sys
import sqlite3
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(940, 680)
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
        self.logo.setGeometry(QtCore.QRect(0, 0, 380, 600))
        self.logo.setStyleSheet("border-image:url(:/images/logo.png);\n"
                                "border-top-left-radius:30px;\n"
                                "border-bottom-left-radius:30px;\n"
                                "\n"
                                "background-color: gba(0, 0, 0,80);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.white_label = QtWidgets.QLabel(self.widget)
        self.white_label.setGeometry(QtCore.QRect(379, -1, 520, 600))
        self.white_label.setStyleSheet("\n"
                                       "background-color: rgb(255, 255, 240);\n"
                                       "\n"
                                       "    border-bottom-right-radius: 30px;\n"
                                       "    border-top-right-radius: 30px;")
        self.white_label.setText("")
        self.white_label.setObjectName("white_label")
        self.register_2 = QtWidgets.QLabel(self.widget)
        self.register_2.setGeometry(QtCore.QRect(540, 30, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(22)
        self.register_2.setFont(font)
        self.register_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.register_2.setStyleSheet("color: rgba(0, 0, 0,200);     ")
        self.register_2.setObjectName("register_2")
        self.first_name = QtWidgets.QLineEdit(self.widget)
        self.first_name.setGeometry(QtCore.QRect(420, 100, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        self.first_name.setFont(font)
        self.first_name.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
                                      "    \n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.first_name.setText("")
        self.first_name.setObjectName("first_name")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(420, 160, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                 "border:none;\n"
                                 "border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
                                 "    \n"
                                 "color:rgba(0, 0, 0, 240);\n"
                                 "padding-bottom:7px;")
        self.email.setText("")
        self.email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.email.setReadOnly(False)
        self.email.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.email.setObjectName("email")
        self.last_name = QtWidgets.QLineEdit(self.widget)
        self.last_name.setGeometry(QtCore.QRect(630, 100, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        self.last_name.setFont(font)
        self.last_name.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                     "border:none;\n"
                                     "border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
                                     "    \n"
                                     "color:rgba(0, 0, 0, 240);\n"
                                     "padding-bottom:7px;")
        self.last_name.setText("")
        self.last_name.setObjectName("last_name")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(420, 220, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
                                    "    \n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px;")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.cfpassword = QtWidgets.QLineEdit(self.widget)
        self.cfpassword.setGeometry(QtCore.QRect(630, 220, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        self.cfpassword.setFont(font)
        self.cfpassword.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
                                      "    \n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.cfpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cfpassword.setObjectName("cfpassword")
        self.selectuser = QtWidgets.QComboBox(self.widget)
        self.selectuser.setGeometry(QtCore.QRect(420, 300, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(11)
        font.setItalic(False)
        self.selectuser.setFont(font)
        self.selectuser.setStyleSheet("QComboBox {\n"
                                      "    border: 1px solid #fffff0; \n"
                                      "    border-radius: 5px; /* Border radius to create curved edges */\n"
                                      "    padding: 5px;\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(12, 112, 117, 255), stop:0.5 rgba(9, 113, 114, 255), stop:1 rgba(101, 161, 185, 255));\n"
                                      "    selection-background-color: #45a059; /* Background color when selected */\n"
                                      "    color: white; /* Text color */\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down {\n"
                                      "    subcontrol-origin: padding;\n"
                                      "    subcontrol-position: top right;\n"
                                      "    width: 15px;\n"
                                      "    border-left-width: 0px;\n"
                                      "    border-left-color: darkgray;\n"
                                      "    border-left-style: solid; /* creates triangle */\n"
                                      "    border-top-right-radius: 5px; /* Adjust as needed for curved corner */\n"
                                      "    border-bottom-right-radius: 5px; /* Adjust as needed for curved corner */\n"
                                      "    margin-right: 5px; /* Move arrow a little bit to the left */\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::down-arrow {\n"
                                      "    image:url(:/images/down-arrow.png); /* Custom arrow icon */\n"
                                      "    height:25px;\n"
                                      "    width: 30px;\n"
                                      "    margin-right: 7px;\n"
                                      "    margin-top: 7px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::down-arrow:on {\n"
                                      "    /* Rotate arrow when dropdown is opened */\n"
                                
                                      "}\n"
                                      "\n"
                                      "QComboBox::item {\n"
                                      "    height: 25px;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::item:selected {\n"
                                      "    background-color: #45a059;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "")
        self.selectuser.setEditable(False)
        self.selectuser.setMaxVisibleItems(3)
        self.selectuser.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.selectuser.setDuplicatesEnabled(False)
        self.selectuser.setObjectName("selectuser")
        self.selectuser.addItem("")
        self.selectuser.addItem("")
        self.selectuser.addItem("")
        self.selectuser.addItem("")
        self.selectuser.setItemText(3, "")
        self.selectuser.setCurrentIndex(0)
        self.line = QtWidgets.QLabel(self.widget)
        self.line.setGeometry(QtCore.QRect(420, 340, 381, 20))
        self.line.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                "border:none;\n"
                                "border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
                                "    \n"
                                "color:rgba(0, 0, 0, 240);\n"
                                "padding-bottom:7px;")
        self.line.setText("")
        self.line.setObjectName("line")
        self.resgister_button = QtWidgets.QPushButton(self.widget)
        self.resgister_button.setGeometry(QtCore.QRect(420, 390, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.resgister_button.setFont(font)
        self.resgister_button.setStyleSheet("QPushButton#resgister_button {\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(44, 42, 42, 255), stop:0.5 rgba(7, 46, 51, 255), stop:1 rgba(12, 112, 117, 255));\n"
                                            "    color: rgba(255, 255, 255, 210);\n"
                                            "    border-radius: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#resgister_button:hover {\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(12, 112, 117, 255), stop:0.5 rgba(9, 113, 114, 255), stop:1 rgba(101, 161, 185, 255));\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#resgister_button:pressed {\n"
                                            "    padding-left: 5px;\n"
                                            "    padding-top: 5px;\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(101, 161, 185, 255), stop:0.5 rgba(40, 77, 95, 255), stop:1 rgba(44, 42, 42, 255));\n"
                                            "}\n"
                                            "")

        self.resgister_button.setObjectName("resgister_button")
        self.alregister = QtWidgets.QLabel(self.widget)
        self.alregister.setGeometry(QtCore.QRect(420, 440, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        self.alregister.setFont(font)
        self.alregister.setObjectName("alregister")
        self.logdirect = QtWidgets.QLabel(self.widget)
        self.logdirect.setGeometry(QtCore.QRect(550, 440, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(12)
        self.logdirect.setFont(font)
        self.logdirect.setObjectName("logdirect")
        '''self.logdirect.mousePressEvent = self.redirect_to_login'''

        # Add minimize and close buttons
        self.minimize_button = QtWidgets.QPushButton(Form)
        self.minimize_button.setGeometry(QtCore.QRect(870, 10, 30, 30))
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setText("-")
        self.minimize_button.clicked.connect(Form.showMinimized)
        self.minimize_button.setStyleSheet("""
    QPushButton#minimize_button {
        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(12, 112, 117, 255), stop:0.5 rgba(9, 113, 114, 255), stop:1 rgba(101, 161, 185, 255));
        color: rgba(255, 255, 255, 210);
        border-radius: 5px;
    }
    QPushButton#minimize_button:hover {
        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(12, 112, 117, 255), stop:0.5 rgba(9, 113, 114, 255), stop:1 rgba(101, 161, 185, 255));
    }
    QPushButton#minimize_button:pressed {
        padding-left: 5px;
        padding-top: 5px;
        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(101, 161, 185, 255), stop:0.5 rgba(40, 77, 95, 255), stop:1 rgba(44, 42, 42, 255));
    }
""")

        self.close_button = QtWidgets.QPushButton(Form)
        self.close_button.setGeometry(QtCore.QRect(900, 10, 30, 30))
        self.close_button.setObjectName("close_button")
        self.close_button.setText("x")
        self.close_button.clicked.connect(Form.close)
        self.close_button.setStyleSheet("""
    QPushButton#close_button {
        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(12, 112, 117, 255), stop:0.5 rgba(9, 113, 114, 255), stop:1 rgba(101, 161, 185, 255));
        color: rgba(255, 255, 255, 210);
        border-radius: 5px;
    }
    QPushButton#close_button:hover {
        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(12, 112, 117, 255), stop:0.5 rgba(9, 113, 114, 255), stop:1 rgba(101, 161, 185, 255));
    }
    QPushButton#close_button:pressed {
        padding-left: 5px;
        padding-top: 5px;
        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(101, 161, 185, 255), stop:0.5 rgba(40, 77, 95, 255), stop:1 rgba(44, 42, 42, 255));
    }
""")
        self.white_label.raise_()
        self.logo.raise_()
        self.register_2.raise_()
        self.first_name.raise_()
        self.email.raise_()
        self.last_name.raise_()
        self.password.raise_()
        self.cfpassword.raise_()
        self.selectuser.raise_()
        self.line.raise_()
        self.resgister_button.raise_()
        self.alregister.raise_()
        self.logdirect.raise_()

        self.logo.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0 ,yOffset=0))
        self.resgister_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0 ,yOffset=0))
        self.widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3 ,yOffset=3))

        self.retranslateUi(Form)
        self.selectuser.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.register_2.setText(_translate("Form", "REGISTER"))
        self.first_name.setPlaceholderText(_translate("Form", "First Name"))
        self.email.setPlaceholderText(_translate("Form", "Your Email ID"))
        self.last_name.setPlaceholderText(_translate("Form", "Last Name"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.cfpassword.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.selectuser.setCurrentText(_translate("Form", "Select User type"))
        self.selectuser.setItemText(0, _translate("Form", "Select User type"))
        self.selectuser.setItemText(1, _translate("Form", "Faculty"))
        self.selectuser.setItemText(2, _translate("Form", "Student"))
        self.resgister_button.setText(_translate("Form", "R E G I S T E R"))
        self.alregister.setText(_translate("Form", "Already registered?"))
        self.logdirect.setText(_translate("Form", " Log In"))

'''  def redirect_to_login(self, event):
        # Function to redirect to login page
        login_window = LoginWindow()
        Form.hide()
        login_window.show()'''
 
# Add the register_button.clicked.connect method to call the register_user function
    def register_user(self):
        # Function to register a new user
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        email = self.email.text()
        password = self.password.text()
        confirm_password = self.cfpassword.text()
        user_type = self.selectuser.currentText()  # Assuming 'Faculty' or 'Student'

        # Check if any field is empty
        if not (first_name and last_name and email and password and confirm_password):
            QtWidgets.QMessageBox.warning(self.widget, "Error", "Please fill in all fields.")
            return

        # Check if password and confirm password match
        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self.widget, "Error", "Passwords do not match.")
            return

        # Connect to the database
        conn = sqlite3.connect('timetable.db')
        cursor = conn.cursor()

        try:
            # Insert user data into the database
            cursor.execute('''
                INSERT INTO Users (username, password_hash, first_name, last_name, email)
                VALUES (?, ?, ?, ?, ?)
            ''', (email, password, first_name, last_name, email))

            # Commit changes
            conn.commit()

            # Optionally, display a message box indicating successful registration
            QtWidgets.QMessageBox.information(self.widget, "Success", "Registration successful!")

            # Clear input fields after registration
            self.first_name.clear()
            self.last_name.clear()
            self.email.clear()
            self.password.clear()
            self.cfpassword.clear()

            # Optionally, switch to the login window after successful registration
            # login_window = LoginWindow()  # Assuming LoginWindow is defined somewhere
            # self.Form.hide()
            # login_window.show()

        except sqlite3.Error as e:
            # Handle database errors
            QtWidgets.QMessageBox.warning(self.widget, "Error", "Database error: " + str(e))

        finally:
            # Close the database connection
            conn.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
