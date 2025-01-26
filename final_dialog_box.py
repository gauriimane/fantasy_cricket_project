"""
This file contains code from dialog_box.ui file with modifications.
When this file is called through the app, it is supplied with the dialog message
and title which is then displayed in the dialog box.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog, title, label):
        dialog.setObjectName("dialog")
        dialog.resize(615, 120)
        dialog.setMinimumSize(QtCore.QSize(615, 120))
        dialog.setMaximumSize(QtCore.QSize(615, 120))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialog, title, label)
        stylesheet = """
        QDialog {
        border-image: url("b4.png"); 
        }
        """
        dialog.setStyleSheet(stylesheet)
        self.pushButton.clicked.connect(dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog, title, label):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "{}".format(title)))
        self.label.setText(_translate("dialog", "{}".format(label)))
        self.pushButton.setText(_translate("dialog", "OK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog, 'change title', 'change label')
    dialog.show()
    sys.exit(app.exec_())
