"""
This file is the UI code generated from the open_team.ui file with modifications.
This file is run when you select the Open Team option from the menu.
"""

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from final_dialog_box import Ui_dialog


class Ui_open_team_dialog(object):
    def setupUi(self, open_team_dialog):
        open_team_dialog.setObjectName("open_team_dialog")
        open_team_dialog.resize(440, 110)
        open_team_dialog.setMinimumSize(QtCore.QSize(440, 110))
        open_team_dialog.setMaximumSize(QtCore.QSize(440, 110))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        open_team_dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(open_team_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(open_team_dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.team_select_dropdown = QtWidgets.QComboBox(open_team_dialog)
        self.team_select_dropdown.setObjectName("team_select_dropdown")
        self.team_select_dropdown.addItem("")
        self.horizontalLayout.addWidget(self.team_select_dropdown)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(open_team_dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(open_team_dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(open_team_dialog)
        stylesheet = """
        QDialog {
        border-image: url("b4.png"); 
        }
        """
        open_team_dialog.setStyleSheet(stylesheet)
        self.team_change_toggle = False
        self.team_select_dropdown.model().item(0).setEnabled(False)
        self.populate_teams()
        self.selected_team = ''
        self.team_select_dropdown.activated['QString'].connect(self.team_changed)
        self.pushButton.clicked.connect(lambda: self.ok_pressed(open_team_dialog))
        self.pushButton_2.clicked.connect(open_team_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(open_team_dialog)

    def retranslateUi(self, open_team_dialog):
        _translate = QtCore.QCoreApplication.translate
        open_team_dialog.setWindowTitle(_translate("open_team_dialog", "Open Teams"))
        self.label.setText(_translate("open_team_dialog", "Select your team:"))
        self.team_select_dropdown.setItemText(0, _translate("open_team_dialog", "Teams"))
        self.pushButton.setText(_translate("open_team_dialog", "OK"))
        self.pushButton_2.setText(_translate("open_team_dialog", "Cancel"))

    def ok_pressed(self, open_team_dialog):
        """
        This function activates when 'OK' button is pressed in the dialog.
        If a team is selected it accepts the input and changes the selected_team
        variable to the team name selected otherwise it shows an error dialog.

        Parameters
        ----------
        open_team_dialog : QtWidgets.QDialog

        Returns
        -------
        None.

        """
        if self.team_change_toggle:
            self.selected_team = self.team_select_dropdown.currentText()
            open_team_dialog.accept()
        else:
            self.dialog_box()

    def dialog_box(self):
        """
        This is the error message dialog displayed when no team is selected.

        Returns
        -------
        None.

        """
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_dialog()
        label = 'Please select a team.'
        title = 'Error'
        dialog.ui.setupUi(dialog, title, label)
        dialog.exec_()

    def team_changed(self):
        """
        This function changes the state of team_change_toggle variable to
        TRUE if a team is selected.

        Returns
        -------
        None.

        """
        self.team_change_toggle = True

    def populate_teams(self):
        """
        This function populates the team_select_dropdown with names of the teams
        saved previously.

        Returns
        -------
        None.

        """
        player_data = sqlite3.connect('player_database.db')
        curplayers = player_data.cursor()
        command = "SELECT name FROM teams ;"
        curplayers.execute(command)
        record = curplayers.fetchall()
        _translate = QtCore.QCoreApplication.translate
        for i in range(len(record)):
            self.team_select_dropdown.addItem("")
            self.team_select_dropdown.setItemText(i + 1, _translate("evaluate_team_dialog", "{}".format(record[i][0])))
        player_data.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    open_team_dialog = QtWidgets.QDialog()
    ui = Ui_open_team_dialog()
    ui.setupUi(open_team_dialog)
    open_team_dialog.show()
    sys.exit(app.exec_())
