# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Asus\Desktop\OptiVision\GUI\Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, OptiVision):
        OptiVision.setObjectName("OptiVision")
        OptiVision.resize(852, 658)
        OptiVision.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(235, 255, 251);")
        self.centralwidget = QtWidgets.QWidget(OptiVision)
        self.centralwidget.setObjectName("centralwidget")
        self.Welcome_Label = QtWidgets.QLabel(self.centralwidget)
        self.Welcome_Label.setGeometry(QtCore.QRect(300, 0, 381, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.Welcome_Label.setFont(font)
        self.Welcome_Label.setObjectName("Welcome_Label")
        self.Email_label = QtWidgets.QLabel(self.centralwidget)
        self.Email_label.setGeometry(QtCore.QRect(371, 231, 56, 24))
        self.Email_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Email_label.setFont(font)
        self.Email_label.setObjectName("Email_label")
        self.Password_label = QtWidgets.QLabel(self.centralwidget)
        self.Password_label.setGeometry(QtCore.QRect(371, 334, 91, 24))
        self.Password_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password_label.setFont(font)
        self.Password_label.setObjectName("Password_label")
        self.EmailEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailEditBox.setGeometry(QtCore.QRect(370, 271, 221, 31))
        self.EmailEditBox.setAcceptDrops(True)
        self.EmailEditBox.setAutoFillBackground(False)
        self.EmailEditBox.setStyleSheet("QLineEdit{\n"
"    background: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    border:1px solid\n"
"}\n"
"QLineEdit:focus{\n"
"    background: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    border:1px solid #aa4f47\n"
"}\n"
"")
        self.EmailEditBox.setFrame(True)
        self.EmailEditBox.setClearButtonEnabled(False)
        self.EmailEditBox.setObjectName("EmailEditBox")
        self.PasswordEditBox = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEditBox.setGeometry(QtCore.QRect(370, 380, 221, 31))
        self.PasswordEditBox.setAcceptDrops(True)
        self.PasswordEditBox.setAutoFillBackground(False)
        self.PasswordEditBox.setStyleSheet("QLineEdit{\n"
"    background: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    border:1px solid\n"
"}\n"
"QLineEdit:focus{\n"
"    background: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    border:1px solid #aa4f47\n"
"}\n"
"")
        self.PasswordEditBox.setFrame(True)
        self.PasswordEditBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEditBox.setClearButtonEnabled(False)
        self.PasswordEditBox.setObjectName("PasswordEditBox")
        self.Login_Label = QtWidgets.QLabel(self.centralwidget)
        self.Login_Label.setGeometry(QtCore.QRect(290, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Login_Label.setFont(font)
        self.Login_Label.setObjectName("Login_Label")
        self.LogInButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogInButton.setGeometry(QtCore.QRect(410, 450, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LogInButton.setFont(font)
        self.LogInButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(246, 255, 225);\n"
"    border-radius:5px;\n"
"    border: 1px solid\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(237, 248, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Asus\\Desktop\\OptiVision\\GUI\\LoginIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LogInButton.setIcon(icon)
        self.LogInButton.setIconSize(QtCore.QSize(18, 18))
        self.LogInButton.setObjectName("LogInButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 230, 21, 16))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 330, 21, 16))
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.OptiVision_Image = QtWidgets.QLabel(self.centralwidget)
        self.OptiVision_Image.setGeometry(QtCore.QRect(10, 160, 221, 271))
        self.OptiVision_Image.setStyleSheet("background-color: rgb(246, 255, 225);")
        self.OptiVision_Image.setText("")
        self.OptiVision_Image.setPixmap(QtGui.QPixmap("C:\\Users\\Asus\\Desktop\\OptiVision\\GUI\\Colored.jpg"))
        self.OptiVision_Image.setScaledContents(True)
        self.OptiVision_Image.setObjectName("OptiVision_Image")
        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(410, 510, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RegisterButton.setFont(font)
        self.RegisterButton.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    border: 1px solid\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(237, 248, 255);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Asus\\Desktop\\OptiVision\\GUI\\RegisterIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RegisterButton.setIcon(icon1)
        self.RegisterButton.setIconSize(QtCore.QSize(18, 18))
        self.RegisterButton.setObjectName("RegisterButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, -20, 251, 781))
        self.label_9.setStyleSheet("background-color: rgb(246, 255, 225);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.ErrorMessage_label = QtWidgets.QLabel(self.centralwidget)
        self.ErrorMessage_label.setGeometry(QtCore.QRect(320, 560, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ErrorMessage_label.setFont(font)
        self.ErrorMessage_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ErrorMessage_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.ErrorMessage_label.setText("")
        self.ErrorMessage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorMessage_label.setObjectName("ErrorMessage_label")
        self.Welcome_Label.raise_()
        self.Email_label.raise_()
        self.Password_label.raise_()
        self.EmailEditBox.raise_()
        self.PasswordEditBox.raise_()
        self.Login_Label.raise_()
        self.LogInButton.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.RegisterButton.raise_()
        self.label_9.raise_()
        self.OptiVision_Image.raise_()
        self.ErrorMessage_label.raise_()
        OptiVision.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OptiVision)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
        self.menubar.setObjectName("menubar")
        OptiVision.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OptiVision)
        self.statusbar.setObjectName("statusbar")
        OptiVision.setStatusBar(self.statusbar)

        self.retranslateUi(OptiVision)
        QtCore.QMetaObject.connectSlotsByName(OptiVision)

    def retranslateUi(self, OptiVision):
        _translate = QtCore.QCoreApplication.translate
        OptiVision.setWindowTitle(_translate("OptiVision", "OptiVision"))
        self.Welcome_Label.setText(_translate("OptiVision", "Welcome!"))
        self.Email_label.setText(_translate("OptiVision", "Email:"))
        self.Password_label.setText(_translate("OptiVision", "Password:"))
        self.Login_Label.setText(_translate("OptiVision", "Login:"))
        self.LogInButton.setText(_translate("OptiVision", "Log in"))
        self.LogInButton.setShortcut(_translate("OptiVision", "Return"))
        self.label_5.setText(_translate("OptiVision", "*"))
        self.label_6.setText(_translate("OptiVision", "*"))
        self.RegisterButton.setText(_translate("OptiVision", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptiVision = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(OptiVision)
    OptiVision.show()
    sys.exit(app.exec_())