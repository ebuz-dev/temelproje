# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Listofpeople.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Listofpeople(object):
    def setupUi(self, Listofpeople):
        Listofpeople.setObjectName("Listofpeople")
        Listofpeople.resize(240, 320)
        self.buttonBox = QtWidgets.QDialogButtonBox(Listofpeople)
        self.buttonBox.setGeometry(QtCore.QRect(-30, 270, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.il = QtWidgets.QComboBox(Listofpeople)
        self.il.setGeometry(QtCore.QRect(10, 110, 211, 20))
        self.il.setObjectName("il")
        self.ilce = QtWidgets.QComboBox(Listofpeople)
        self.ilce.setGeometry(QtCore.QRect(10, 150, 211, 20))
        self.ilce.setObjectName("ilce")
        self.isim = QtWidgets.QLineEdit(Listofpeople)
        self.isim.setGeometry(QtCore.QRect(12, 30, 211, 20))
        self.isim.setObjectName("isim")
        self.soyisim = QtWidgets.QLineEdit(Listofpeople)
        self.soyisim.setGeometry(QtCore.QRect(12, 70, 211, 20))
        self.soyisim.setObjectName("soyisim")

        self.retranslateUi(Listofpeople)
        self.buttonBox.accepted.connect(Listofpeople.accept)
        self.buttonBox.rejected.connect(Listofpeople.reject)
        QtCore.QMetaObject.connectSlotsByName(Listofpeople)

    def retranslateUi(self, Listofpeople):
        _translate = QtCore.QCoreApplication.translate
        Listofpeople.setWindowTitle(_translate("Listofpeople", "Dialog"))
        self.il.setToolTip(_translate("Listofpeople", "<html><head/><body><p>İL</p></body></html>"))
        self.ilce.setToolTip(_translate("Listofpeople", "<html><head/><body><p>İlçe</p></body></html>"))
        self.isim.setToolTip(_translate("Listofpeople", "<html><head/><body><p>Kullanıcı adını giriniz</p></body></html>"))
        self.soyisim.setToolTip(_translate("Listofpeople", "<html><head/><body><p>Kullanıcı soyadını giriniz</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Listofpeople = QtWidgets.QDialog()
    ui = Ui_Listofpeople()
    ui.setupUi(Listofpeople)
    Listofpeople.show()
    sys.exit(app.exec_())