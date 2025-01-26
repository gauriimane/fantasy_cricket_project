"""
This is the main file. This contains code generated from the game_main_window.ui
file and modifications. Run this file to launch the Fantasy Cricket app.
"""

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from final_dialog_box import Ui_dialog
from final_evaluate_teams import Ui_evaluate_team_dialog
from final_new_team_dialog import Ui_Dialog_new_team
from final_open_team import Ui_open_team_dialog


class Ui_Fantasy_Cricket_Game(object):
    def setupUi(self, Fantasy_Cricket_Game):
        Fantasy_Cricket_Game.setObjectName("Fantasy_Cricket_Game")
        Fantasy_Cricket_Game.resize(700, 604)
        Fantasy_Cricket_Game.setMinimumSize(QtCore.QSize(700, 604))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        Fantasy_Cricket_Game.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Fantasy_Cricket_Game.setWindowIcon(icon)
        Fantasy_Cricket_Game.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Fantasy_Cricket_Game)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.selection_box = QtWidgets.QGroupBox(self.centralwidget)
        self.selection_box.setFont(font)
        self.selection_box.setObjectName("selection_box")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.selection_box)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.selection_box)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.bat_num = QtWidgets.QLabel(self.selection_box)
        self.bat_num.setFont(font)
        self.bat_num.setAlignment(QtCore.Qt.AlignCenter)
        self.bat_num.setObjectName("bat_num")
        self.verticalLayout_2.addWidget(self.bat_num)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.selection_box)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.bwl_num = QtWidgets.QLabel(self.selection_box)
        self.bwl_num.setFont(font)
        self.bwl_num.setAlignment(QtCore.Qt.AlignCenter)
        self.bwl_num.setObjectName("bwl_num")
        self.verticalLayout_3.addWidget(self.bwl_num)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.selection_box)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.ar_num = QtWidgets.QLabel(self.selection_box)
        self.ar_num.setFont(font)
        self.ar_num.setAlignment(QtCore.Qt.AlignCenter)
        self.ar_num.setObjectName("ar_num")
        self.verticalLayout_4.addWidget(self.ar_num)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.selection_box)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.wk_num = QtWidgets.QLabel(self.selection_box)
        self.wk_num.setFont(font)
        self.wk_num.setAlignment(QtCore.Qt.AlignCenter)
        self.wk_num.setObjectName("wk_num")
        self.verticalLayout_5.addWidget(self.wk_num)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addWidget(self.selection_box)
        self.make_team_box = QtWidgets.QGroupBox(self.centralwidget)
        self.make_team_box.setFont(font)
        self.make_team_box.setObjectName("make_team_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.make_team_box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.make_team_box)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.points_available_label = QtWidgets.QLabel(self.make_team_box)
        self.points_available_label.setFont(font)
        self.points_available_label.setObjectName("points_available_label")
        self.horizontalLayout_6.addWidget(self.points_available_label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_bat = QtWidgets.QRadioButton(self.make_team_box)
        self.radioButton_bat.setFont(font)
        self.radioButton_bat.setObjectName("radioButton_bat")
        self.horizontalLayout_4.addWidget(self.radioButton_bat)
        self.radioButton_bwl = QtWidgets.QRadioButton(self.make_team_box)
        self.radioButton_bwl.setFont(font)
        self.radioButton_bwl.setObjectName("radioButton_bwl")
        self.horizontalLayout_4.addWidget(self.radioButton_bwl)
        self.radioButton_ar = QtWidgets.QRadioButton(self.make_team_box)
        self.radioButton_ar.setFont(font)
        self.radioButton_ar.setObjectName("radioButton_ar")
        self.horizontalLayout_4.addWidget(self.radioButton_ar)
        self.radioButton_wk = QtWidgets.QRadioButton(self.make_team_box)
        self.radioButton_wk.setMinimumSize(QtCore.QSize(0, 27))
        self.radioButton_wk.setFont(font)
        self.radioButton_wk.setObjectName("radioButton_wk")
        self.horizontalLayout_4.addWidget(self.radioButton_wk)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.list1 = QtWidgets.QListWidget(self.make_team_box)
        self.list1.setMinimumSize(QtCore.QSize(260, 300))
        self.list1.setObjectName("list1")
        self.verticalLayout_6.addWidget(self.list1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem)
        self.label_15 = QtWidgets.QLabel(self.make_team_box)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.make_team_box)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.points_used_label = QtWidgets.QLabel(self.make_team_box)
        self.points_used_label.setFont(font)
        self.points_used_label.setObjectName("points_used_label")
        self.horizontalLayout_7.addWidget(self.points_used_label)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.make_team_box)
        self.label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.team_name_label = QtWidgets.QLabel(self.make_team_box)
        self.team_name_label.setFont(font)
        self.team_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.team_name_label.setObjectName("team_name_label")
        self.horizontalLayout_3.addWidget(self.team_name_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.list2 = QtWidgets.QListWidget(self.make_team_box)
        self.list2.setMinimumSize(QtCore.QSize(260, 300))
        self.list2.setObjectName("list2")
        self.verticalLayout.addWidget(self.list2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_7.addWidget(self.make_team_box)
        Fantasy_Cricket_Game.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Fantasy_Cricket_Game)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 29))
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setFont(font)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        Fantasy_Cricket_Game.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fantasy_Cricket_Game)
        self.statusbar.setObjectName("statusbar")
        Fantasy_Cricket_Game.setStatusBar(self.statusbar)
        self.actionAdd_Team = QtWidgets.QAction(Fantasy_Cricket_Game)
        self.actionAdd_Team.setFont(font)
        self.actionAdd_Team.setObjectName("actionAdd_Team")
        self.actionOpen_Team = QtWidgets.QAction(Fantasy_Cricket_Game)
        self.actionOpen_Team.setFont(font)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(Fantasy_Cricket_Game)
        self.actionSave_Team.setFont(font)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(Fantasy_Cricket_Game)
        self.actionEvaluate_Team.setFont(font)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionAdd_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        stylesheet = """
        QMainWindow {
        border-image: url("b1.png"); 
        }
        """
        self.list1.setStyleSheet("border-image : url(b2.png); ")
        self.list2.setStyleSheet("border-image : url(b3.png); ")
        Fantasy_Cricket_Game.setStyleSheet(stylesheet)
        self.selection_box.setStyleSheet('QGroupBox:title {color: white;}')
        self.make_team_box.setStyleSheet('QGroupBox:title {color: white;}')
        self.label_3.setStyleSheet('color:white')
        self.label_5.setStyleSheet('color:white')
        self.label_7.setStyleSheet('color:white')
        self.label.setStyleSheet('color:white')
        self.retranslateUi(Fantasy_Cricket_Game)
        self.team_name_change = 0
        self.bat = 0
        self.bwl = 0
        self.ar = 0
        self.wk = 0
        self.radioButton_bat.clicked.connect(lambda: self.show_players('BAT'))
        self.radioButton_bwl.clicked.connect(lambda: self.show_players('BWL'))
        self.radioButton_ar.clicked.connect(lambda: self.show_players('AR'))
        self.radioButton_wk.clicked.connect(lambda: self.show_players('WK'))
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)
        QtCore.QMetaObject.connectSlotsByName(Fantasy_Cricket_Game)

    def retranslateUi(self, Fantasy_Cricket_Game):
        _translate = QtCore.QCoreApplication.translate
        Fantasy_Cricket_Game.setWindowTitle(_translate("Fantasy_Cricket_Game", "Fantasy Cricket Game"))
        self.selection_box.setTitle(_translate("Fantasy_Cricket_Game", "Your Selections"))
        self.label.setText(_translate("Fantasy_Cricket_Game", "Batsmen (BAT)"))
        self.bat_num.setText(_translate("Fantasy_Cricket_Game", "0"))
        self.label_3.setText(_translate("Fantasy_Cricket_Game", "Bowlers (BWL)"))
        self.bwl_num.setText(_translate("Fantasy_Cricket_Game", "0"))
        self.label_5.setText(_translate("Fantasy_Cricket_Game", "Allrounders (AR)"))
        self.ar_num.setText(_translate("Fantasy_Cricket_Game", "0"))
        self.label_7.setText(_translate("Fantasy_Cricket_Game", "Wicket-Keeper (WK)"))
        self.wk_num.setText(_translate("Fantasy_Cricket_Game", "0"))
        self.make_team_box.setTitle(_translate("Fantasy_Cricket_Game", "Make Team"))
        self.label_11.setText(_translate("Fantasy_Cricket_Game", "Points Available:"))
        self.points_available_label.setText(_translate("Fantasy_Cricket_Game", "1000"))
        self.radioButton_bat.setText(_translate("Fantasy_Cricket_Game", "BAT"))
        self.radioButton_bwl.setText(_translate("Fantasy_Cricket_Game", "BWL"))
        self.radioButton_ar.setText(_translate("Fantasy_Cricket_Game", "AR"))
        self.radioButton_wk.setText(_translate("Fantasy_Cricket_Game", "WK"))
        self.label_15.setText(_translate("Fantasy_Cricket_Game", ">"))
        self.label_14.setText(_translate("Fantasy_Cricket_Game", "Points Used:"))
        self.points_used_label.setText(_translate("Fantasy_Cricket_Game", "0"))
        self.label_9.setText(_translate("Fantasy_Cricket_Game", "Team Name:"))
        self.team_name_label.setText(_translate("Fantasy_Cricket_Game", "Team"))
        self.menuManage_Teams.setTitle(_translate("Fantasy_Cricket_Game", "Manage Teams"))
        self.actionAdd_Team.setText(_translate("Fantasy_Cricket_Game", "New Team"))
        self.actionOpen_Team.setText(_translate("Fantasy_Cricket_Game", "Open Team"))
        self.actionSave_Team.setText(_translate("Fantasy_Cricket_Game", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("Fantasy_Cricket_Game", "Evaluate Team"))

    def value_change(self):
        """
        This function calculates the current value of the selected team and
        displays the points spent and points available to the user for team
        selection.

        Returns
        -------
        total : int
            Current spent points of the selected team.

        """
        player_data = sqlite3.connect('player_database.db')
        curplayers = player_data.cursor()
        total = 0
        for i in range(self.list2.count()):
            player = self.list2.item(i).text()
            command = "SELECT value FROM stats WHERE player = '{}';".format(player)
            curplayers.execute(command)
            record = curplayers.fetchall()[0][0]
            total += record
        player_data.close()
        _translate = QtCore.QCoreApplication.translate
        if self.list2.count() > 0:
            self.points_available_label.setText(_translate("Fantasy_Cricket_Game", "{}".format(1000 - total)))
            self.points_used_label.setText(_translate("Fantasy_Cricket_Game", "{}".format(total)))
        else:
            self.points_available_label.setText(_translate("Fantasy_Cricket_Game", "1000"))
            self.points_used_label.setText(_translate("Fantasy_Cricket_Game", "0"))
        return total

    def change_ctg_count(self):
        """
        This function displays the current composition of the team, i.e. it
        displays how many players of each category are there in the team 
        currently.

        Returns
        -------
        None.

        """
        _translate = QtCore.QCoreApplication.translate
        self.bat_num.setText(_translate("Fantasy_Cricket_Game", "{}".format(self.bat)))
        self.bwl_num.setText(_translate("Fantasy_Cricket_Game", "{}".format(self.bwl)))
        self.ar_num.setText(_translate("Fantasy_Cricket_Game", "{}".format(self.ar)))
        self.wk_num.setText(_translate("Fantasy_Cricket_Game", "{}".format(self.wk)))

    def show_players(self, ctg):
        """
        This function is run when any of the category radio button is selected.
        If a team has been selected, it displays players of the selected category
        and disables the ones which are already selected. If no team is selected,
        it shows a message to the user.

        Parameters
        ----------
        ctg : str
            string representing the category selected

        Returns
        -------
        None.

        """
        if self.team_name_change == 1:
            self.ctg = ctg
            self.list1.clear()
            _translate = QtCore.QCoreApplication.translate
            player_data = sqlite3.connect('player_database.db')
            curplayers = player_data.cursor()
            command = "SELECT player FROM stats WHERE ctg = '{}';".format(ctg)
            curplayers.execute(command)
            record = curplayers.fetchall()
            __sortingEnabled = self.list1.isSortingEnabled()
            self.list1.setSortingEnabled(False)
            for i in range(len(record)):
                if self.list1.count() < len(record):
                    item = QtWidgets.QListWidgetItem()
                    self.list1.addItem(item)
                item = self.list1.item(i)
                item.setText(_translate("Fantasy_Cricket_Game", "{}".format(record[i][0])))
                temp = self.list2.findItems('{}'.format(record[i][0]), QtCore.Qt.MatchExactly)
                if temp != []:
                    item.setFlags(QtCore.Qt.NoItemFlags)
            self.list1.setSortingEnabled(__sortingEnabled)
            player_data.close()
        else:
            self.dialog_box(1)

    def menufunction(self, action):
        """
        This function handles the menu of the app.
        Depending on which option is selected, different steps are taken.
        Parameters
        ----------
        action :
            The menu option selected

        Returns
        -------
        None.

        """
        txt = action.text()  # string giving the selected menu option
        if txt == 'New Team':
            """
            If New Team is selected, a New Team Wizard from the final_new_team_dialog.py
            file is run. 
            """
            dialog = QtWidgets.QDialog()
            dialog.ui = Ui_Dialog_new_team()
            dialog.ui.setupUi(dialog)
            dialog.exec_()
            try:
                name = dialog.ui.name
                _translate = QtCore.QCoreApplication.translate
                self.team_name_label.setText(_translate("Fantasy_Cricket_Game", name))
                self.team_name_change = 1
                self.list2.clear()
                self.radioButton_bat.setChecked(True)
                self.show_players('BAT')
                self.list2_player_details()
                self.change_ctg_count()
                self.value_change()
            except:
                pass
        if txt == 'Save Team':
            if self.list2.count() == 11:
                player_data = sqlite3.connect('player_database.db')
                curplayers = player_data.cursor()
                try:
                    team_name = self.team_name_label.text()
                    curplayers.execute(('SELECT name FROM teams;'))
                    record = curplayers.fetchall()
                    team_list = []
                    for i in record:
                        team_list.append(i[0])
                    player_list = self.list2_player_details()
                    player_list = '///'.join(player_list)
                    if team_name in team_list:
                        curplayers.execute('UPDATE teams SET players = ? WHERE name = ?;', (player_list, team_name))
                    else:
                        curplayers.execute('INSERT INTO teams (name, players) VALUES (?,?);', (team_name, player_list))
                    player_data.commit()
                    player_data.close()
                except:
                    player_data.rollback()
                    player_data.close()
            else:
                if self.team_name_change == 1:
                    self.dialog_box(3)
                else:
                    self.dialog_box(1)
        if txt == 'Open Team':
            dialog = QtWidgets.QDialog()
            dialog.ui = Ui_open_team_dialog()
            dialog.ui.setupUi(dialog, )
            dialog.exec_()
            if dialog.ui.team_change_toggle:
                try:
                    selected_team = dialog.ui.selected_team
                    self.list2.clear()
                    _translate = QtCore.QCoreApplication.translate
                    player_data = sqlite3.connect('player_database.db')
                    curplayers = player_data.cursor()
                    command = "SELECT players FROM teams WHERE name = '{}';".format(selected_team)
                    curplayers.execute(command)
                    record = curplayers.fetchall()[0][0]
                    record = record.split('///')
                    font = QtGui.QFont()
                    font.setFamily("Segoe UI")
                    font.setPointSize(10)
                    font.setWeight(60)
                    font.setKerning(True)
                    __sortingEnabled = self.list2.isSortingEnabled()
                    self.list2.setSortingEnabled(False)
                    for i in range(len(record)):
                        if self.list2.count() < len(record):
                            item = QtWidgets.QListWidgetItem()
                            self.list2.addItem(item)
                        item = self.list2.item(i)
                        item.setText(_translate("evaluate_tean_dialog", "{}".format(record[i])))
                        item.setForeground(QtGui.QColor("white"))
                        item.setFont(font)
                    self.list2.setSortingEnabled(__sortingEnabled)
                    player_data.close()
                    self.team_name_label.setText(_translate("Fantasy_Cricket_Game", selected_team))
                    self.team_name_change = 1
                    self.radioButton_bat.setChecked(True)
                    self.show_players('BAT')
                    self.list2_player_details()
                    self.change_ctg_count()
                    self.value_change()
                except:
                    pass
        if txt == 'Evaluate Team':
            dialog = QtWidgets.QDialog()
            dialog.ui = Ui_evaluate_team_dialog()
            dialog.ui.setupUi(dialog)
            dialog.exec_()

    def removelist1(self, item):
        if self.list2.count() < 11:
            ctg = self.ctg
            total = self.value_change()
            player_data = sqlite3.connect('player_database.db')
            curplayers = player_data.cursor()
            player = item.text()
            command = "SELECT value FROM stats WHERE player = '{}';".format(player)
            curplayers.execute(command)
            record = curplayers.fetchall()[0][0]
            try:
                total += record
            except:
                total = 0
            player_data.close()
            if total <= 1000:
                if ctg == 'BAT' and self.bat < 4:
                    self.list2.addItem(item.text())
                    item.setFlags(QtCore.Qt.NoItemFlags)
                elif ctg == 'BWL' and self.bwl < 3:
                    self.list2.addItem(item.text())
                    item.setFlags(QtCore.Qt.NoItemFlags)
                elif ctg == 'AR' and self.ar < 3:
                    self.list2.addItem(item.text())
                    item.setFlags(QtCore.Qt.NoItemFlags)
                elif ctg == 'WK' and self.wk < 1:
                    self.list2.addItem(item.text())
                    item.setFlags(QtCore.Qt.NoItemFlags)
                else:
                    self.dialog_box(5, ctg)
            else:
                self.dialog_box(6)
            self.list2_player_details()
            self.change_ctg_count()
            self.value_change()
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setWeight(60)
            font.setKerning(True)
            try:
                item = self.list2.findItems(item.text(), QtCore.Qt.MatchExactly)
                item[0].setForeground(QtGui.QColor("white"))
                item[0].setFont(font)
            except:
                pass
        else:
            self.dialog_box(4)

    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        item = self.list1.findItems(item.text(), QtCore.Qt.MatchExactly)
        self.list2_player_details()
        self.change_ctg_count()
        self.value_change()
        try:
            item[0].setFlags(QtCore.Qt.ItemIsEnabled)
        except:
            pass

    def dialog_box(self, dialog_number, ctg='none'):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_dialog()
        title = 'Error'
        if dialog_number == 1:
            label = 'Make or open a team to start.'
            title = 'Help'
        elif dialog_number == 2:
            label = 'Team name can only contain alphanumeric characters!'
        elif dialog_number == 3:
            label = 'Your team has {} players. Select {} more to continue.'.format(self.list2.count(),
                                                                                   11 - self.list2.count())
        elif dialog_number == 4:
            label = 'Team can not have more than 11 players!'
        elif dialog_number == 5:
            if ctg == 'BAT':
                label = 'You can not have more than 4 batsmen in the team!'
            elif ctg == 'BWL':
                label = 'You can not have more than 3 bowlers in the team!'
            elif ctg == 'AR':
                label = 'You can not have more than 3 allrounders in the team!'
            elif ctg == 'WK':
                label = 'You can not have more than 1 wicket-keeper in the team!'
        elif dialog_number == 6:
            label = 'Points used can not be more than 1000!'
        dialog.ui.setupUi(dialog, title, label)
        dialog.exec_()

    def list2_player_details(self):
        self.bat = 0
        self.bwl = 0
        self.ar = 0
        self.wk = 0
        player_data = sqlite3.connect('player_database.db')
        curplayers = player_data.cursor()
        player_list = []
        for i in range(self.list2.count()):
            stats = []
            player = self.list2.item(i).text()
            player_list.append(player)
            command = "SELECT * FROM match WHERE player = '{}';".format(player)
            curplayers.execute(command)
            record = curplayers.fetchall()
            for i in record[0]:
                stats.append(i)
            command = "SELECT * FROM stats WHERE player = '{}';".format(player)
            curplayers.execute(command)
            record = curplayers.fetchall()
            for i in record[0]:
                stats.append(i)
            ctg = stats[18]
            if ctg == 'BAT':
                self.bat += 1
            elif ctg == 'BWL':
                self.bwl += 1
            elif ctg == 'AR':
                self.ar += 1
            else:
                self.wk += 1
        player_data.close()
        return player_list


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Fantasy_Cricket_Game = QtWidgets.QMainWindow()
    ui = Ui_Fantasy_Cricket_Game()
    ui.setupUi(Fantasy_Cricket_Game)
    Fantasy_Cricket_Game.show()
    sys.exit(app.exec_())
