import bombOg as b
import getpass
from PyQt5 import QtCore, QtGui, QtWidgets
un_=getpass.getuser()
def sendUserInfo(un_):
    user=b.getUserDetails(un_)
    return user
def startBombing(pn,cc,n,un):
    if b.checkConnectivity():
        if b.ifExists(un):
            if b.checkQuota(b.getUserDetails(un)):
                if b.blackList(pn):
                    b.startBombing(pn,cc,n,un)
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Error!")
                    msg.setText("This number has been blacklisted")
                    x = msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("You have exhausted your daily quota\nSubscribe premium to get unlimited msg")
                x = msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("You have not registered for the service\nRun setup.py to register")
            x = msg.exec_()
    else:
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Check your internet Connection")
        x = msg.exec_()
