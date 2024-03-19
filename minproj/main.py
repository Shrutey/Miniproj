from PyQt5 import QtWidgets, QtCore
import sys, resource
from registerUI import Ui_Form as RegisterUi
from loginUI import Ui_Form as LoginUi

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create the Form object
        self.Form = QtWidgets.QWidget()
        self.Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Initialize the UI components
        self.register_ui = RegisterUi()
        self.register_ui.setupUi(self.Form)

        self.login_ui = LoginUi()
        self.login_ui.setupUi(self.Form)

        # Initially hide the login page
        self.login_ui.widget.hide()

        # Connect signals
        self.register_ui.logdirect.mousePressEvent = self.show_login_page
        self.login_ui.regdirect.mousePressEvent = self.show_register_page

    def show_login_page(self, event):
        self.register_ui.widget.hide()
        self.login_ui.widget.show()

    def show_register_page(self, event):
        self.register_ui.widget.show()
        self.login_ui.widget.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.Form.show()  # Show the Form object instead of main_window directly
    sys.exit(app.exec_())
