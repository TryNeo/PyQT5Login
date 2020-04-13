import sys
import mysql.connector
from PyQt5 import uic
from py_rc import passowrd_rc, user_rc, user_profile_rc, login_rc
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox)


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("login.ui", self)
        self.setMinimumSize(294, 461)
        self.setMaximumSize(294, 461)
        self.inicio.clicked.connect(self.login)

    #########Connection Mysql###########
    def connecting(self):
        try:
            self.mydb = mysql.connector.connect(host='localhost',
                                                user='root',
                                                passwd='root',
                                                db='login')
            self.mysqlcursor = self.mydb.cursor()
        except mysql.connector.errors.ProgrammingError as error:
            print("Review the Error -->", error)

    def login(self):
        self.connecting()
        user_name = self.usuario.text()
        password = self.contrasena.text()
        if user_name == "" and password == "":
            QMessageBox.warning(self, "Login", "Fill in the data", QMessageBox.Ok)
        else:
            get_data = (user_name, password)
            query = "SELECT * FROM usuarios WHERE username = %s and password = %s"
            self.mysqlcursor.execute(query, get_data)
            validate = self.mysqlcursor.fetchall()
            if validate:
                QMessageBox.about(self, 'Login Successful', 'Correct username and password', QMessageBox.Ok)
                QMainWindow.destroy()
            else:
                QMessageBox.warning(self, "Login Incorrect", "Incorrect user or password", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    app.exec_()
