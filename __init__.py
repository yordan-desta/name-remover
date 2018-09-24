import sys
from PyQt4 import QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import nameRemoverUi
import commonLib
import nameRemover

path = ""

width = 500
height = 300

class RenamerApp(QtGui.QDialog, nameRemoverUi.Ui_Dialog):
    def __init__(self):

        super(self.__class__, self).__init__()

        self.setupUi(self)

        self.setWindowTitle("Yoni's name remover (by pyordan)")

        self.setFixedSize(width, height)

        self.filePathEditText.lineWrapMode()

        self.connect(self.selectDir, SIGNAL("clicked()"), self.selectDirClicked)

        self.connect(self.selectFile, SIGNAL("clicked()"), self.selectFileClicked)

    def selectDirClicked(self):

        directory = QtGui.QFileDialog.getExistingDirectory()

        print directory

        if commonLib.isFileOrDir(directory):
            self.filePathEditText.setText(directory)

    def selectFileClicked(self):

        global path

        _file = QtGui.QFileDialog.getOpenFileNameAndFilter()

        print _file[0]

        if commonLib.isFileOrDir(_file[0]):
            self.filePathEditText.setText(_file[0])

    def accept(self):

        global path

        if QString.isNull(self.filePathEditText.toPlainText()) or QString.isEmpty(self.filePathEditText.toPlainText()):
            QMessageBox.about(self, "Error", "path doesn't exist")
            return

        if QString.isNull(self.keyEditText.toPlainText()) or QString.isEmpty(self.keyEditText.toPlainText()):
            QMessageBox.about(self, "Error", "key can not be empty")
            return

        path = str(self.filePathEditText.toPlainText())

        key = str(self.keyEditText.toPlainText())

        select_flag = -1

        if QRadioButton.isChecked(self.leftMatchRB):
            select_flag = nameRemover.CONST.LEFT()

        elif QRadioButton.isChecked(self.rightMatchRB):
            select_flag = nameRemover.CONST.RIGHT()

        elif QRadioButton.isChecked(self.exactMatchRB):
            select_flag = nameRemover.CONST.EXACT()

        if select_flag == -1:
            QMessageBox.about(self, "Error", "please select one of the options: left, right or exact")
            return

        if commonLib.isDir(path):
            nameRemover.removeFileFromDir(path, key, select_flag)

        elif commonLib.isFile(path):
            nameRemover.removeNameFromFile(path, key, select_flag)

        sys.exit(0)


def main():
    app = QtGui.QApplication(sys.argv)
    form = RenamerApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
