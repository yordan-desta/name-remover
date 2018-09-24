# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nameRemover.ui'
#
# Created: Tue May 16 09:24:10 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(500, 265)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.filePathEditText = QtGui.QTextEdit(Dialog)
        self.filePathEditText.setGeometry(QtCore.QRect(10, 30, 371, 30))
        self.filePathEditText.setObjectName(_fromUtf8("filePathEditText"))
        self.keyEditText = QtGui.QTextEdit(Dialog)
        self.keyEditText.setGeometry(QtCore.QRect(110, 80, 281, 31))
        self.keyEditText.setObjectName(_fromUtf8("keyEditText"))
        self.selectDir = QtGui.QPushButton(Dialog)
        self.selectDir.setGeometry(QtCore.QRect(390, 10, 98, 27))
        self.selectDir.setObjectName(_fromUtf8("selectDir"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 90, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.selectFile = QtGui.QPushButton(Dialog)
        self.selectFile.setGeometry(QtCore.QRect(390, 40, 98, 27))
        self.selectFile.setObjectName(_fromUtf8("selectFile"))
        self.leftMatchRB = QtGui.QRadioButton(Dialog)
        self.leftMatchRB.setGeometry(QtCore.QRect(60, 140, 116, 22))
        self.leftMatchRB.setObjectName(_fromUtf8("leftMatchRB"))
        self.rightMatchRB = QtGui.QRadioButton(Dialog)
        self.rightMatchRB.setGeometry(QtCore.QRect(180, 140, 116, 22))
        self.rightMatchRB.setObjectName(_fromUtf8("rightMatchRB"))
        self.exactMatchRB = QtGui.QRadioButton(Dialog)
        self.exactMatchRB.setGeometry(QtCore.QRect(310, 140, 116, 22))
        self.exactMatchRB.setObjectName(_fromUtf8("exactMatchRB"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.selectDir.setText(_translate("Dialog", "select Dir", None))
        self.label.setText(_translate("Dialog", "Text key", None))
        self.selectFile.setText(_translate("Dialog", "select File", None))
        self.leftMatchRB.setText(_translate("Dialog", "left match", None))
        self.rightMatchRB.setText(_translate("Dialog", "right match", None))
        self.exactMatchRB.setText(_translate("Dialog", "exact match", None))

