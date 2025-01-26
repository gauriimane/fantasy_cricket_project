"""
This file contains code generated from the evaluate_teams.ui file and the
modifications. This file is run you select the Evaluate Team option from the
menu.
"""

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

import point_calculation
from final_dialog_box import Ui_dialog


class Ui_evaluate_team_dialog(object):
    def setupUi(self, evaluate_team_dialog):
        evaluate_team_dialog.setObjectName("evaluate_team_dialog")
        evaluate_team_dialog.resize(600, 465)
        evaluate_team_dialog.setMinimumSize(QtCore.QSize(600, 465))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(evaluate_team_dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(evaluate_team_dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        evaluate_team_dialog.setWindowIcon(icon)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.team_select_dropdown = QtWidgets.QComboBox(evaluate_team_dialog)
        self.team_select_dropdown.setObjectName("team_select_dropdown")
        self.team_select_dropdown.addItem("")
        self.horizontalLayout_4.addWidget(self.team_select_dropdown)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.match_select_dropdown = QtWidgets.QComboBox(evaluate_team_dialog)
        self.match_select_dropdown.setObjectName("match_select_dropdown")
        self.match_select_dropdown.addItem("")
        self.match_select_dropdown.addItem("")
        self.match_select_dropdown.addItem("")
        self.match_select_dropdown.addItem("")
        self.match_select_dropdown.addItem("")
        self.match_select_dropdown.addItem("")
        self.horizontalLayout_4.addWidget(self.match_select_dropdown)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 2)
        self.horizontalLayout_4.setStretch(3, 4)
        self.horizontalLayout_4.setStretch(4, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(evaluate_team_dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(evaluate_team_dialog)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.player_list = QtWidgets.QListWidget(evaluate_team_dialog)
        self.player_list.setObjectName("player_list")
        self.verticalLayout_2.addWidget(self.player_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(evaluate_team_dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.total_points = QtWidgets.QLabel(evaluate_team_dialog)
        self.total_points.setObjectName("total_points")
        self.horizontalLayout.addWidget(self.total_points)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.point_list = QtWidgets.QListWidget(evaluate_team_dialog)
        self.point_list.setObjectName("point_list")
        self.verticalLayout.addWidget(self.point_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.calc_score_button = QtWidgets.QPushButton(evaluate_team_dialog)
        self.calc_score_button.setObjectName("calc_score_button")
        self.verticalLayout_4.addWidget(self.calc_score_button)

        self.retranslateUi(evaluate_team_dialog)
        stylesheet = """
        QDialog {
        border-image: url("b1.png"); 
        }
        """
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.total_points.setFont(font)
        evaluate_team_dialog.setStyleSheet(stylesheet)
        self.player_list.setStyleSheet("border-image : url(b2.png); ")
        self.point_list.setStyleSheet("border-image : url(b3.png); ")
        self.match_select_dropdown.activated['QString'].connect(self.match_change_toggle)
        self.retranslateUi(evaluate_team_dialog)
        self.team_select_dropdown.model().item(0).setEnabled(False)
        self.match_select_dropdown.model().item(0).setEnabled(False)
        self.populate_teams()
        self.team_list = []
        self.team_change = False
        self.match_change = False
        self.team_select_dropdown.activated['QString'].connect(self.fill_player_list)
        self.calc_score_button.clicked.connect(self.fill_scores)
        QtCore.QMetaObject.connectSlotsByName(evaluate_team_dialog)

    def retranslateUi(self, evaluate_team_dialog):
        _translate = QtCore.QCoreApplication.translate
        evaluate_team_dialog.setWindowTitle(_translate("evaluate_team_dialog", "Evaluate Teams"))
        self.label.setText(_translate("evaluate_team_dialog", "Evaluate the performance of your Fantasy Team"))
        self.team_select_dropdown.setItemText(0, _translate("evaluate_team_dialog", "Select Team"))
        self.match_select_dropdown.setItemText(0, _translate("evaluate_team_dialog", "Select Match"))
        self.match_select_dropdown.setItemText(1, _translate("evaluate_team_dialog", "Match 1"))
        self.match_select_dropdown.setItemText(2, _translate("evaluate_team_dialog", "Match 2"))
        self.match_select_dropdown.setItemText(3, _translate("evaluate_team_dialog", "Match 3"))
        self.match_select_dropdown.setItemText(4, _translate("evaluate_team_dialog", "Match 4"))
        self.match_select_dropdown.setItemText(5, _translate("evaluate_team_dialog", "Match 5"))
        self.label_2.setText(_translate("evaluate_team_dialog", "Players in your team:"))
        self.label_3.setText(_translate("evaluate_team_dialog", "Points:"))
        self.total_points.setText(_translate("evaluate_team_dialog", "0"))
        self.calc_score_button.setText(_translate("evaluate_team_dialog", "Calculate Score"))

    def match_change_toggle(self):
        """
        Changes state of match_change variable to TRUE if a match is selected
        from the match_select_dropdown.

        Returns
        -------
        None.

        """
        self.match_change = True

    def populate_teams(self):
        """
        This function populates the team_select_dropdown with the names of the
        teams saved previously.

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

    def fill_player_list(self):
        """
        This function is run when you select a team from the dropdown. It shows
        the names of players of the selected team in the player_list. It also
        chnages the state of the team_change variable to TRUE.

        Returns
        -------
        None.

        """
        selected_team = self.team_select_dropdown.currentText()
        self.team_change = True
        _translate = QtCore.QCoreApplication.translate
        player_data = sqlite3.connect('player_database.db')
        curplayers = player_data.cursor()
        command = "SELECT players FROM teams WHERE name = '{}';".format(selected_team)
        curplayers.execute(command)
        record = curplayers.fetchall()[0][0]
        record = record.split('///')
        self.team_list = record
        __sortingEnabled = self.player_list.isSortingEnabled()
        self.player_list.setSortingEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(60)
        font.setKerning(True)
        for i in range(len(record)):
            if self.player_list.count() < len(record):
                item = QtWidgets.QListWidgetItem()
                self.player_list.addItem(item)
            item = self.player_list.item(i)
            item.setText(_translate("evaluate_tean_dialog", "{}".format(record[i])))
            item.setForeground(QtGui.QColor("white"))
            item.setFont(font)
        self.player_list.setSortingEnabled(__sortingEnabled)
        player_data.close()

    def fill_scores(self):
        """
        This function is run when Calculate Score button is pressed. If both a 
        team and a match has been selected, it displays the respective points 
        of each player in the team and also the total score of the team. If
        either one is not selected, it will display an error message.

        Returns
        -------
        None.

        """
        if self.team_change and self.match_change:
            selected_team = self.team_list
            scores = point_calculation.get_team_score(selected_team)
            _translate = QtCore.QCoreApplication.translate
            __sortingEnabled = self.point_list.isSortingEnabled()
            self.point_list.setSortingEnabled(False)
            for i in range(len(scores)):
                if self.point_list.count() < len(scores):
                    item = QtWidgets.QListWidgetItem()
                    self.point_list.addItem(item)
                item = self.point_list.item(i)
                item.setText(_translate("evaluate_tean_dialog", "{}".format(scores[i])))
            self.point_list.setSortingEnabled(__sortingEnabled)
            total = sum(scores)
            self.total_points.setText(_translate("evaluate_team_dialog", "{}".format(total)))
        else:
            self.dialog_box()

    def dialog_box(self):
        """
        This function displays a error message if Calculate Score button is
        pressed before selecting a team or a match.

        Returns
        -------
        None.

        """
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_dialog()
        label = 'Please select a team and a match!'
        title = 'Error'
        dialog.ui.setupUi(dialog, title, label)
        dialog.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    evaluate_team_dialog = QtWidgets.QDialog()
    ui = Ui_evaluate_team_dialog()
    ui.setupUi(evaluate_team_dialog)
    evaluate_team_dialog.show()
    sys.exit(app.exec_())
