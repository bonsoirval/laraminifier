# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laraminifier.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog

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

class Ui_Laraminifier(object):
    def setupUi(self, Laraminifier):
        Laraminifier.setObjectName(_fromUtf8("Laraminifier"))
        Laraminifier.resize(491, 300)
        self.widget = QtGui.QWidget(Laraminifier)
        self.widget.setGeometry(QtCore.QRect(60, 60, 372, 172))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.browse_folder_btn = QtGui.QPushButton(self.widget)
        self.browse_folder_btn.setObjectName(_fromUtf8("browse_folder_btn"))
        self.horizontalLayout.addWidget(self.browse_folder_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.browse_folder_btn_2 = QtGui.QPushButton(self.widget)
        self.browse_folder_btn_2.setObjectName(_fromUtf8("browse_folder_btn_2"))
        self.horizontalLayout_2.addWidget(self.browse_folder_btn_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.radioButton = QtGui.QRadioButton(self.widget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_2.addWidget(self.radioButton)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Laraminifier)
        #self.browse_folder_btn_2.clicked.connect(self.selectFile(self.lineEdit))
        QtCore.QObject.connect(self.browse_folder_btn, QtCore.SIGNAL(_fromUtf8("clicked()")),self.selectFile(self.lineEdit))
        QtCore.QMetaObject.connectSlotsByName(Laraminifier)

    def selectFile(self,item):
        #create an instance of QFileDialog
        fileDlg = QFileDialog()
        #Sets the field text as the selected file path
        item.setText(fileDlg.getOpenFileName())

    def retranslateUi(self, Laraminifier):
        Laraminifier.setWindowTitle(_translate("Laraminifier", "Laraminifier", None))
        self.label.setText(_translate("Laraminifier", "Choose Folder", None))
        self.browse_folder_btn.setText(_translate("Laraminifier", "Browser Folder", None))
        self.label_2.setText(_translate("Laraminifier", "Choose Destination", None))
        self.lineEdit_2.setPlaceholderText(_translate("Laraminifier", "Empty to use default", None))
        self.browse_folder_btn_2.setText(_translate("Laraminifier", "Destination Folder", None))
        self.radioButton.setText(_translate("Laraminifier", "Minify .php files", None))
        self.pushButton.setText(_translate("Laraminifier", "Cancel", None))
        self.pushButton_2.setText(_translate("Laraminifier", "Minify", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Laraminifier = QtGui.QDialog()
    ui = Ui_Laraminifier()
    ui.setupUi(Laraminifier)
    Laraminifier.show()
    sys.exit(app.exec_())
