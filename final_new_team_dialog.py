"""
This file contains code generated from the new_team_dialog.ui file and
modifications. The file is run when you select the New Team option from the menu.
"""

from PyQt5 import QtCore, QtGui, QtWidgets

from final_dialog_box import Ui_dialog


class Ui_Dialog_new_team(object):
    def setupUi(self, Dialog_new_team):
        Dialog_new_team.setObjectName("Dialog_new_team")
        Dialog_new_team.resize(584, 122)
        Dialog_new_team.setMinimumSize(QtCore.QSize(584, 122))
        Dialog_new_team.setMaximumSize(QtCore.QSize(584, 122))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_new_team)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog_new_team)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_new_team.setWindowIcon(icon)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.team_name = QtWidgets.QLineEdit(Dialog_new_team)
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_2.addWidget(self.team_name)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(Dialog_new_team)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_new_team)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_new_team)
        stylesheet = """
        QDialog {
        border-image: url("b4.png"); 
        }
        """
        Dialog_new_team.setStyleSheet(stylesheet)
        self.pushButton_2.clicked.connect(self.team_name.clear)
        self.pushButton.clicked.connect(lambda: self.new_team_name(Dialog_new_team))
        QtCore.QMetaObject.connectSlotsByName(Dialog_new_team)

    def retranslateUi(self, Dialog_new_team):
        _translate = QtCore.QCoreApplication.translate
        Dialog_new_team.setWindowTitle(_translate("Dialog_new_team", "New Team Wizard"))
        self.label.setText(_translate("Dialog_new_team", "Enter name of your team:"))
        self.pushButton.setText(_translate("Dialog_new_team", "OK"))
        self.pushButton_2.setText(_translate("Dialog_new_team", "Reset"))

    def new_team_name(self, Dialog_new_team):
        """
        This function activates when you press the 'OK' button in the dialog.
        It checks if the name is alphanumeric and if TRUE, it accepts the input
        and sets the name variable to the given team name. If the name is not
        alphanumeric, it will display a error message.

        Parameters
        ----------
        Dialog_new_team : QtWidgets.QDialog

        Returns
        -------
        None.

        """
        name = self.team_name.text()
        if name.isalnum():
            self.name = name
            Dialog_new_team.accept()
        else:
            self.dialog_box()

    def dialog_box(self):
        """
        This displays the error message when the input name is not alphanumeric.

        Returns
        -------
        None.

        """
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_dialog()
        label = 'Team name can only contain alphanumeric characters!'
        title = 'Error'
        dialog.ui.setupUi(dialog, title, label)
        dialog.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog_new_team = QtWidgets.QDialog()
    ui = Ui_Dialog_new_team()
    ui.setupUi(Dialog_new_team)
    Dialog_new_team.show()
    sys.exit(app.exec_())
