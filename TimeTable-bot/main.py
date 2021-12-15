#@Gadzhiyavov_Dzhamal_bot
import telebot
from telebot import types
import psycopg2, time
import sys
import traceback
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox, QInputDialog)
memory_subjects=[]
memory_teachers=[]
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="timetable_db",
                                     user="postgres",
                                     password="123456",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()


    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Расписание на верхнюю неделю")

        self.monday_gbox = QGroupBox("Понедельник")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.monday_gbox)

        self._create_monday_table()

        self.tuesday_gbox = QGroupBox("Вторник")

        self.shbox1t = QHBoxLayout()
        self.shbox2t = QHBoxLayout()

        self.svbox.addLayout(self.shbox1t)
        self.svbox.addLayout(self.shbox2t)

        self.shbox1t.addWidget(self.tuesday_gbox)

        self._create_tuesday_table()

        self.wednesday_gbox = QGroupBox("Среда")

        self.shbox1w = QHBoxLayout()
        self.shbox2w = QHBoxLayout()

        self.svbox.addLayout(self.shbox1w)
        self.svbox.addLayout(self.shbox2w)

        self.shbox1w.addWidget(self.wednesday_gbox)

        self._create_wednesday_table()

        self.thursday_gbox = QGroupBox("Четверг")

        self.shbox1th = QHBoxLayout()
        self.shbox2th = QHBoxLayout()

        self.svbox.addLayout(self.shbox1th)
        self.svbox.addLayout(self.shbox2th)

        self.shbox1th.addWidget(self.thursday_gbox)

        self._create_thursday_table()

        self.friday_gbox = QGroupBox("Пятница")

        self.shbox1f = QHBoxLayout()
        self.shbox2f = QHBoxLayout()

        self.svbox.addLayout(self.shbox1f)
        self.svbox.addLayout(self.shbox2f)

        self.shbox1f.addWidget(self.friday_gbox)

        self._create_friday_table()

        self.saturday_gbox = QGroupBox("Суббота")

        self.shbox1s = QHBoxLayout()
        self.shbox2s = QHBoxLayout()

        self.svbox.addLayout(self.shbox1s)
        self.svbox.addLayout(self.shbox2s)

        self.shbox1s.addWidget(self.saturday_gbox)

        self._create_saturday_table()

        self.add_shedule_button = QPushButton("Add")
        self.shbox2s.addWidget(self.add_shedule_button)
        self.add_shedule_button.clicked.connect(lambda: self._add_shedule(1))
        self.update_shedule_button = QPushButton("Update")
        self.shbox2s.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)


        self.shedule_tab2 = QWidget()
        self.tabs.addTab(self.shedule_tab2, "Расписание на нижнюю неделю")

        self.monday_gbox2 = QGroupBox("Понедельник")

        self.svbox2 = QVBoxLayout()
        self.shbox12 = QHBoxLayout()
        self.shbox22 = QHBoxLayout()

        self.svbox2.addLayout(self.shbox12)
        self.svbox2.addLayout(self.shbox22)

        self.shbox12.addWidget(self.monday_gbox2)

        self._create_monday_table2()

        self.tuesday_gbox2 = QGroupBox("Вторник")

        self.shbox1t2 = QHBoxLayout()
        self.shbox2t2 = QHBoxLayout()

        self.svbox2.addLayout(self.shbox1t2)
        self.svbox2.addLayout(self.shbox2t2)

        self.shbox1t2.addWidget(self.tuesday_gbox2)

        self._create_tuesday_table2()

        self.wednesday_gbox2 = QGroupBox("Среда")

        self.shbox1w2 = QHBoxLayout()
        self.shbox2w2 = QHBoxLayout()

        self.svbox2.addLayout(self.shbox1w2)
        self.svbox2.addLayout(self.shbox2w2)

        self.shbox1w2.addWidget(self.wednesday_gbox2)

        self._create_wednesday_table2()

        self.thursday_gbox2 = QGroupBox("Четверг")

        self.shbox1th2 = QHBoxLayout()
        self.shbox2th2 = QHBoxLayout()

        self.svbox2.addLayout(self.shbox1th2)
        self.svbox2.addLayout(self.shbox2th)

        self.shbox1th2.addWidget(self.thursday_gbox2)

        self._create_thursday_table2()

        self.friday_gbox2 = QGroupBox("Пятница")

        self.shbox1f2 = QHBoxLayout()
        self.shbox2f2 = QHBoxLayout()

        self.svbox2.addLayout(self.shbox1f2)
        self.svbox2.addLayout(self.shbox2f2)

        self.shbox1f2.addWidget(self.friday_gbox2)

        self._create_friday_table2()

        self.saturday_gbox2 = QGroupBox("Суббота")

        self.shbox1s2 = QHBoxLayout()
        self.shbox2s2 = QHBoxLayout()

        self.svbox2.addLayout(self.shbox1s2)
        self.svbox2.addLayout(self.shbox2s2)

        self.shbox1s2.addWidget(self.saturday_gbox2)

        self._create_saturday_table2()

        self.add_shedule_button = QPushButton("Add")
        self.shbox2s2.addWidget(self.add_shedule_button)
        self.add_shedule_button.clicked.connect(lambda: self._add_shedule(2))
        self.update_shedule_button2 = QPushButton("Update")
        self.shbox2s2.addWidget(self.update_shedule_button2)
        self.update_shedule_button2.clicked.connect(self._update_shedule)
        self.shedule_tab2.setLayout(self.svbox2)

        self.shedule_tab3 = QWidget()
        self.tabs.addTab(self.shedule_tab3, "Список предметов")

        self.subject_gbox = QGroupBox("Список:")

        self.svbox3 = QVBoxLayout()
        self.shbox13 = QHBoxLayout()
        self.shbox23 = QHBoxLayout()

        self.svbox3.addLayout(self.shbox13)
        self.svbox3.addLayout(self.shbox23)
        self.shbox13.addWidget(self.subject_gbox)
        self._create_subject_table()
        self.shedule_tab3.setLayout(self.svbox3)

        self.add_subject_button = QPushButton("Add")
        self.shbox23.addWidget(self.add_subject_button)
        self.add_subject_button.clicked.connect(lambda: self._add_subject())
        self.update_subject_button = QPushButton("Update")
        self.shbox23.addWidget(self.update_subject_button)
        self.update_subject_button.clicked.connect(self._update_shedule)


        self.shedule_tab4 = QWidget()
        self.tabs.addTab(self.shedule_tab4, "Список преподавателей")

        self.teacher_gbox = QGroupBox("Список:")

        self.svbox4 = QVBoxLayout()
        self.shbox14 = QHBoxLayout()
        self.shbox24 = QHBoxLayout()

        self.svbox4.addLayout(self.shbox14)
        self.svbox4.addLayout(self.shbox24)
        self.shbox14.addWidget(self.teacher_gbox)
        self._create_teacher_table()
        self.shedule_tab4.setLayout(self.svbox4)

        self.add_teacher_button = QPushButton("Add")
        self.shbox24.addWidget(self.add_teacher_button)
        self.add_teacher_button.clicked.connect(lambda: self._add_teacher())
        self.update_teacher_button = QPushButton("Update")
        self.shbox24.addWidget(self.update_teacher_button)
        self.update_teacher_button.clicked.connect(self._update_shedule)

    def _create_subject_table(self):
        self.subject_table = QTableWidget()

        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subject_table.setColumnCount(3)
        self.subject_table.setHorizontalHeaderLabels(["Subject", "", ""])

        self._update_subject_table()

        self.mvbox3 = QVBoxLayout()
        self.mvbox3.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.mvbox3)

    def _update_subject_table(self):
        self.cursor.execute("SELECT * FROM subject")
        records = list(self.cursor.fetchall())
        self.subject_table.setRowCount(len(records))
        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            memory_subjects.append([i,str(r[0]).encode("cp1251").decode("cp866")])
            self.subject_table.setItem(i, 0, QTableWidgetItem(str(r[0]).encode("cp1251").decode("cp866")))
            self.subject_table.setCellWidget(i, 1, joinButton[i])
            self.subject_table.setCellWidget(i, 2, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_subject_from_table(0))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_subject_from_table(1))
        except:a=0
        try:joinButton[2].clicked.connect(lambda: self._change_subject_from_table(2))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_subject_from_table(3))
        except:a=0
        try:joinButton[4].clicked.connect(lambda: self._change_subject_from_table(4))
        except:a=0
        try:joinButton[5].clicked.connect(lambda: self._change_subject_from_table(5))
        except:a=0
        try:joinButton[6].clicked.connect(lambda: self._change_subject_from_table(6))
        except:a=0
        try:joinButton[7].clicked.connect(lambda: self._change_subject_from_table(7))
        except:a=0
        try:joinButton[8].clicked.connect(lambda: self._change_subject_from_table(8))
        except:a=0
        try:joinButton[9].clicked.connect(lambda: self._change_subject_from_table(9))
        except:a=0
        try:joinButton[10].clicked.connect(lambda: self._change_subject_from_table(10))
        except:a=0
        try:joinButton[11].clicked.connect(lambda: self._change_subject_from_table(11))
        except:a=0
        try:joinButton[12].clicked.connect(lambda: self._change_subject_from_table(12))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_subject_from_table(0))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_subject_from_table(1))
        except:a=0
        try:deleteButton[2].clicked.connect(lambda: self._delete_subject_from_table(2))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_subject_from_table(3))
        except:a=0
        try:deleteButton[4].clicked.connect(lambda: self._delete_subject_from_table(4))
        except:a=0
        try:deleteButton[5].clicked.connect(lambda: self._delete_subject_from_table(5))
        except:a=0
        try:deleteButton[6].clicked.connect(lambda: self._delete_subject_from_table(6))
        except:a=0
        try:deleteButton[7].clicked.connect(lambda: self._delete_subject_from_table(7))
        except:a=0
        try:deleteButton[8].clicked.connect(lambda: self._delete_subject_from_table(8))
        except:a=0
        try:deleteButton[9].clicked.connect(lambda: self._delete_subject_from_table(9))
        except:a=0
        try:deleteButton[10].clicked.connect(lambda: self._delete_subject_from_table(10))
        except:a=0
        try:deleteButton[11].clicked.connect(lambda: self._delete_subject_from_table(11))
        except:a=0
        try:deleteButton[12].clicked.connect(lambda: self._delete_subject_from_table(12))
        except:a=0
        self.subject_table.resizeRowsToContents()



    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()

        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(4)
        self.teacher_table.setHorizontalHeaderLabels(["Name", "Subject", "", ""])

        self._update_teacher_table()

        self.mvbox4 = QVBoxLayout()
        self.mvbox4.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.mvbox4)

    def _update_teacher_table(self):
        self.cursor.execute("SELECT * FROM teacher")
        records = list(self.cursor.fetchall())
        self.teacher_table.setRowCount(len(records))
        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.teacher_table.setItem(i, 0, QTableWidgetItem(str(r[1]).encode("cp1251").decode("cp866")))
            self.teacher_table.setItem(i, 1, QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            self.teacher_table.setCellWidget(i, 2, joinButton[i])
            self.teacher_table.setCellWidget(i, 3, deleteButton[i])

        self.teacher_table.resizeRowsToContents()

    def _create_monday_table(self):
        self.monday_table = QTableWidget()

        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(4)
        self.monday_table.setHorizontalHeaderLabels(["Subject", "Time", "", ""])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)


    def _create_monday_table2(self):
        self.monday_table2 = QTableWidget()

        self.monday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table2.setColumnCount(4)
        self.monday_table2.setHorizontalHeaderLabels(["Subject", "Time", "", ""])

        self._update_monday_table2()

        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.monday_table2)
        self.monday_gbox2.setLayout(self.mvbox2)


    def _update_monday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='1.1'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.monday_table.setRowCount(len(records))
        joinButton=[]
        deleteButton=[]
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.monday_table.setCellWidget(i, 2, joinButton[i])
            self.monday_table.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "1.1"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "1.1"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "1.1"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "1.1"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "1.1"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "1.1"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "1.1"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "1.1"))
        except:a=0
        self.monday_table.resizeRowsToContents()

    def _update_monday_table2(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='1.2'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.monday_table2.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.monday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.monday_table2.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.monday_table2.setCellWidget(i, 2, joinButton[i])
            self.monday_table2.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "1.2"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "1.2"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "1.2"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "1.2"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "1.2"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "1.2"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "1.2"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "1.2"))
        except:a=0
        self.monday_table2.resizeRowsToContents()


    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()

        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(4)
        self.tuesday_table.setHorizontalHeaderLabels(["Subject", "Time", "", ""])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)


    def _create_tuesday_table2(self):
        self.tuesday_table2 = QTableWidget()

        self.tuesday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table2.setColumnCount(4)
        self.tuesday_table2.setHorizontalHeaderLabels(["Subject", "Time", "", ""])

        self._update_tuesday_table2()

        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.tuesday_table2)
        self.tuesday_gbox2.setLayout(self.mvbox2)


    def _update_tuesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='2.1'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.tuesday_table.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.tuesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.tuesday_table.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.tuesday_table.setCellWidget(i, 2, joinButton[i])
            self.tuesday_table.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "2.1"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "2.1"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "2.1"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "2.1"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "2.1"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "2.1"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "2.1"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "2.1"))
        except:a=0

        self.tuesday_table.resizeRowsToContents()


    def _update_tuesday_table2(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='2.2'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.tuesday_table2.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.tuesday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.tuesday_table2.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.tuesday_table2.setCellWidget(i, 2, joinButton[i])
            self.tuesday_table2.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "2.2"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "2.2"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "2.2"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "2.2"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "2.2"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "2.2"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "2.2"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "2.2"))
        except:a=0

        self.tuesday_table2.resizeRowsToContents()


    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.wednesday_table.setColumnCount(4)
        self.wednesday_table.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        self._update_wednesday_table()
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.mvbox)


    def _create_wednesday_table2(self):
        self.wednesday_table2 = QTableWidget()
        self.wednesday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.wednesday_table2.setColumnCount(4)
        self.wednesday_table2.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        self._update_wednesday_table2()
        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.wednesday_table2)
        self.wednesday_gbox2.setLayout(self.mvbox2)


    def _update_wednesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='3.1'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.wednesday_table.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.wednesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.wednesday_table.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.wednesday_table.setCellWidget(i, 2, joinButton[i])
            self.wednesday_table.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "3.1"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "3.1"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "3.1"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "3.1"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "3.1"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "3.1"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "3.1"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "3.1"))
        except:a=0

        self.wednesday_table.resizeRowsToContents()


    def _update_wednesday_table2(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='3.2'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.wednesday_table2.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.wednesday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.wednesday_table2.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.wednesday_table2.setCellWidget(i, 2, joinButton[i])
            self.wednesday_table2.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "3.2"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "3.2"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "3.2"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "3.2"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "3.2"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "3.2"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "3.2"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "3.2"))
        except:a=0

        self.wednesday_table2.resizeRowsToContents()


    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.thursday_table.setColumnCount(4)
        self.thursday_table.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        self._update_thursday_table()
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.mvbox)


    def _create_thursday_table2(self):
        self.thursday_table2 = QTableWidget()
        self.thursday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.thursday_table2.setColumnCount(4)
        self.thursday_table2.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        self._update_thursday_table2()
        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.thursday_table2)
        self.thursday_gbox2.setLayout(self.mvbox2)


    def _update_thursday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='4.1'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.thursday_table.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.thursday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.thursday_table.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.thursday_table.setCellWidget(i, 2, joinButton[i])
            self.thursday_table.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "4.1"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "4.1"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "4.1"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "4.1"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "4.1"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "4.1"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "4.1"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "4.1"))
        except:a=0
        self.thursday_table.resizeRowsToContents()


    def _update_thursday_table2(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='4.2'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.thursday_table2.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.thursday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.thursday_table2.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.thursday_table2.setCellWidget(i, 2, joinButton[i])
            self.thursday_table2.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "4.2"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "4.2"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "4.2"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "4.2"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "4.2"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "4.2"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "4.2"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "4.2"))
        except:a=0

        self.thursday_table2.resizeRowsToContents()


    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.friday_table.setColumnCount(4)
        self.friday_table.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        self._update_friday_table()
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.mvbox)


    def _create_friday_table2(self):
        self.friday_table2 = QTableWidget()
        self.friday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.friday_table2.setColumnCount(4)
        self.friday_table2.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        self._update_friday_table2()
        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.friday_table2)
        self.friday_gbox2.setLayout(self.mvbox2)


    def _update_friday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='5.1'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.friday_table.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.friday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.friday_table.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.friday_table.setCellWidget(i, 2, joinButton[i])
            self.friday_table.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "5.1"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "5.1"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "5.1"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "5.1"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "5.1"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "5.1"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "5.1"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "5.1"))
        except:a=0

        self.friday_table.resizeRowsToContents()


    def _update_friday_table2(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='5.2'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.friday_table2.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.friday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.friday_table2.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.friday_table2.setCellWidget(i, 2, joinButton[i])
            self.friday_table2.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "5.2"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "5.2"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "5.2"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "5.2"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "5.2"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "5.2"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "5.2"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "5.2"))
        except:a=0

        self.friday_table2.resizeRowsToContents()


    def _create_saturday_table(self):
        self.saturday_table = QTableWidget()
        self.saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.saturday_table.setColumnCount(4)
        self.saturday_table.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        self._update_saturday_table()
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.saturday_table)
        self.saturday_gbox.setLayout(self.mvbox)


    def _create_saturday_table2(self):
        self.saturday_table2 = QTableWidget()
        self.saturday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.saturday_table2.setColumnCount(4)
        self.saturday_table2.setHorizontalHeaderLabels(["Subject", "Time", "", ""])
        self._update_saturday_table2()
        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.saturday_table2)
        self.saturday_gbox2.setLayout(self.mvbox2)


    def _update_saturday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='6.1'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.saturday_table.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.saturday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.saturday_table.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.saturday_table.setCellWidget(i, 2, joinButton[i])
            self.saturday_table.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "6.1"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "6.1"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "6.1"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "6.1"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "6.1"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "6.1"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "6.1"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "6.1"))
        except:a=0

        self.saturday_table.resizeRowsToContents()


    def _update_saturday_table2(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='6.2'")
        records = list(self.cursor.fetchall())
        records.sort(key=lambda x: x[4])
        self.saturday_table2.setRowCount(len(records))

        joinButton = []
        deleteButton = []
        for i, r in enumerate(records):
            r = list(r)
            joinButton.append(QPushButton("Join"))
            deleteButton.append((QPushButton("Delete")))
            self.saturday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[2]).encode("cp1251").decode("cp866")))
            a=str(r[4]//60)+":"+str(r[4]%60)
            self.saturday_table2.setItem(i, 1,
                                      QTableWidgetItem(a))
            self.saturday_table2.setCellWidget(i, 2, joinButton[i])
            self.saturday_table2.setCellWidget(i, 3, deleteButton[i])
        try:joinButton[0].clicked.connect(lambda: self._change_day_from_table(0, "6.2"))
        except:a=0
        try:joinButton[1].clicked.connect(lambda: self._change_day_from_table(1, "6.2"))
        except:a = 0
        try:joinButton[2].clicked.connect(lambda: self._change_day_from_table(2, "6.2"))
        except:a=0
        try:joinButton[3].clicked.connect(lambda: self._change_day_from_table(3, "6.2"))
        except:a=0
        try:deleteButton[0].clicked.connect(lambda: self._delete_day_from_table(0, "6.2"))
        except:a=0
        try:deleteButton[1].clicked.connect(lambda: self._delete_day_from_table(1, "6.2"))
        except:a = 0
        try:deleteButton[2].clicked.connect(lambda: self._delete_day_from_table(2, "6.2"))
        except:a=0
        try:deleteButton[3].clicked.connect(lambda: self._delete_day_from_table(3, "6.2"))
        except:a=0

        self.saturday_table2.resizeRowsToContents()


    def _change_day_from_table(self, rowNum, day):
        row = list()
        a=[]
        if day=="1.1":
            a=self.monday_table
        elif day=="1.2":
            a=self.monday_table2
        elif day=="2.1":
            a=self.tuesday_table
        elif day=="2.2":
            a=self.tuesday_table2
        elif day=="3.1":
            a=self.wednesday_table
        elif day=="3.2":
            a=self.wednesday_table2
        elif day=="4.1":
            a=self.thursday_table
        elif day=="4.2":
            a=self.thursday_table2
        elif day=="5.1":
            a=self.friday_table
        elif day=="5.2":
            a=self.friday_table2
        elif day=="6.1":
            a=self.saturday_table
        elif day=="6.2":
            a=self.saturday_table2
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            try:
                tt=int(row[1].split(":")[0])*60+int(row[1].split(":")[1])
                if int(row[1].split(":")[1])> 59 or int(row[1].split(":")[0]) > 23:
                    return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
            except:
                return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
            cursor.execute(f"SELECT * FROM timetable WHERE day='{day}';")
            records = list(cursor.fetchall())
            records.sort(key = lambda x: x[4])
            lol=0
            cursor.execute("SELECT * FROM subject;")
            recordss = list(cursor.fetchall())
            for i in recordss:
                aa=i[0].encode("cp1251").decode("cp866")
                if row[0]==aa:
                    lol=1
            if lol==0:
                return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")

            self.cursor.execute(f"UPDATE timetable SET day='{day}', start_time={tt}, subject='{row[0].encode('cp866').decode('cp1251')}' WHERE (day='{day}' AND start_time={records[0][4]});")
            self.conn.commit()
        except Exception:
            traceback.print_exc()
            cursor.execute("ROLLBACK")
            conn.commit()
            QMessageBox.about(self, "Error", "Данные не введены или введены неверно")


    def _delete_day_from_table(self, rowNum, day):
        row = list()
        a=[]
        if day=="1.1":
            a=self.monday_table
        elif day=="1.2":
            a=self.monday_table2
        elif day=="2.1":
            a=self.tuesday_table
        elif day=="2.2":
            a=self.tuesday_table2
        elif day=="3.1":
            a=self.wednesday_table
        elif day=="3.2":
            a=self.wednesday_table2
        elif day=="4.1":
            a=self.thursday_table
        elif day=="4.2":
            a=self.thursday_table2
        elif day=="5.1":
            a=self.friday_table
        elif day=="5.2":
            a=self.friday_table2
        elif day=="6.1":
            a=self.saturday_table
        elif day=="6.2":
            a=self.saturday_table2
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            try:
                tt=int(row[1].split(":")[0])*60+int(row[1].split(":")[1])
                if int(row[1].split(":")[1])> 59 or int(row[1].split(":")[0]) > 23:
                    return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
            except:
                return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
            cursor.execute(f"SELECT * FROM timetable WHERE day='{day}';")
            self.cursor.execute(f"DELETE FROM timetable WHERE (day='{day}' AND start_time={tt});")
            self.conn.commit()
            self._update_shedule()
        except:
            print('error')



    def _change_subject_from_table(self, rowNum):
        row = list()
        a=self.subject_table
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            print(row[0],memory_subjects[rowNum][1])
            if row[0]==memory_subjects[rowNum][1]:
                return
            self.cursor.execute(f"INSERT INTO subject VALUES('{row[0].encode('cp866').decode('cp1251')}');")
            self.cursor.execute(f"UPDATE teacher SET subject='{row[0].encode('cp866').decode('cp1251')}' WHERE subject='{memory_subjects[rowNum][1].encode('cp866').decode('cp1251')}';")
            self.cursor.execute(f"UPDATE timetable SET subject='{row[0].encode('cp866').decode('cp1251')}' WHERE subject='{memory_subjects[rowNum][1].encode('cp866').decode('cp1251')}';")
            self.cursor.execute(f"DELETE FROM subject WHERE name='{memory_subjects[rowNum][1].encode('cp866').decode('cp1251')}';")
            memory_subjects.append(memory_subjects[rowNum])
            memory_subjects.remove(memory_subjects[rowNum])
            self.conn.commit()
        except Exception:
            traceback.print_exc()
            cursor.execute("ROLLBACK")
            conn.commit()
            QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
        self._update_shedule()


    def _delete_subject_from_table(self, rowNum):
        row = list()
        a = self.subject_table
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            cursor.execute(f"SELECT COUNT(*) as count FROM timetable WHERE subject='{row[0].encode('cp866').decode('cp1251')}';")
            records = list(cursor.fetchall())
            # print(records[0][0],row[0], memory_subjects[rowNum][1])
            if records[0][0]>0:
                return QMessageBox.about(self, "Error", "Нельзя удалить предмет, потому что он используется в расписании")
            cursor.execute(f"SELECT COUNT(*) as count FROM teacher WHERE subject='{row[0].encode('cp866').decode('cp1251')}';")
            records = list(cursor.fetchall())
            if records[0][0] > 0:
                return QMessageBox.about(self, "Error", "Нельзя удалить предмет, потому его все еще кто-то преподает")
            self.cursor.execute(
                f"DELETE FROM subject WHERE name='{row[0].encode('cp866').decode('cp1251')}';")
            self.conn.commit()
        except Exception:
            traceback.print_exc()
            cursor.execute("ROLLBACK")
            conn.commit()
            QMessageBox.about(self, "Error", "Нельзя удалить предмет, потому что он используется в расписании")
        self._update_shedule()



    def _update_shedule(self):
        self._update_monday_table()
        self._update_monday_table2()
        self._update_tuesday_table()
        self._update_tuesday_table2()
        self._update_wednesday_table()
        self._update_wednesday_table2()
        self._update_thursday_table()
        self._update_thursday_table2()
        self._update_friday_table()
        self._update_friday_table2()
        self._update_saturday_table()
        self._update_saturday_table2()
        self._update_subject_table()
        self._update_teacher_table()

    def _add_subject(self):
        subj, done = QInputDialog.getText(
            self, 'Добавление записи в таблицу', 'Введите название предмета')
        if subj=="" or done==False:
            return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
        try:
            self.cursor.execute(f"INSERT INTO subject VALUES ('{subj.encode('cp866').decode('cp1251')}');")
            memory_subjects.append([len(memory_subjects)+1, 'subj'])
            self.conn.commit()
            self._update_shedule()
        except:
            return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
        self._update_shedule()

    def _add_shedule(self, ned):
        den, done2 = QInputDialog.getItem(
            self, 'Добавление записи в таблицу', 'Выберете день:', ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'])
        pred, done3 = QInputDialog.getText(
            self, 'Добавление записи в таблицу', 'Введите название предмета:')
        time, done4 = QInputDialog.getText(
            self, 'Добавление записи в таблицу', 'Введите время в формате "ХХ:ХХ":')
        try:
            tt = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
            if int(time.split(":")[1]) > 59 or int(time.split(":")[0]) > 23:
                return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
        except:
            return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
        room, done5 = QInputDialog.getText(
            self, 'Добавление записи в таблицу', 'Введите номер аудитории(0, если дистанционно):')
        dd=1
        if den == "Понедельник": dd = 1
        if den == "Вторник": dd = 2
        if den == "Среда": dd = 3
        if den == "Четверг": dd = 4
        if den == "Пятница": dd = 5
        if den == "Суббота": dd = 6
        try:
            self.cursor.execute(f"INSERT INTO timetable (day, subject, room_numb, start_time) VALUES ('{dd}.{ned}', '{pred.encode('cp866').decode('cp1251')}', {room}, {tt});")
            self.conn.commit()
            self._update_shedule()
        except:
            return QMessageBox.about(self, "Error", "Данные не введены или введены неверно")
        self._update_shedule()


token = "5055933944:AAEB35DgwO08yrlNnOCW6D6gU8U1es_y7gs"
bot = telebot.TeleBot(token)

conn = psycopg2.connect(
                        database="timetable_db",
                        user="postgres",
                        password="123456",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()
def rasp(den,day):
    cursor.execute(f"SELECT * FROM timetable WHERE day='{den}'")
    records = list(cursor.fetchall())
    records.sort(key=lambda x: x[4])
    a = day+"\n----------------------------------------\n"
    for i in records:
        ii = i[2].encode("cp1251").decode("cp866")
        a += ii
        if i[3] == 0:
            a += " Дистанционно "
        else:
            a += " "+str(i[3])+"ауд. "
        a += str(i[4] // 60) + ":" + str(i[4] % 60) + " "
        c = f"SELECT * FROM teacher WHERE subject='{i[2]}';"
        cursor.execute(c)
        rec = list(cursor.fetchall())
        cc = rec[0][1].encode("cp1251").decode("cp866")
        cc = cc.split()
        a += cc[0] + " " + cc[1][0] + "." + cc[2][0] + "."
        a += "\n"
    a += "----------------------------------------"
    return a


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.max_row_keys=3
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Расписание на текущую неделю","Расписание на следующую неделю")
    bot.send_message(message.chat.id, 'Доброго времени суток. Хотите посмотреть расписание? Нажмите на кнопку ниже.', reply_markup=keyboard)


@bot.message_handler(commands=['week'])
def week(message):
    nt=int((time.time()//1-1630270800)/3600/24/7)+1
    ntt = ""
    if nt % 2 == 0:
        ntt = "Нижняя неделя"
    else:
        ntt = "Верхняя неделя"
    bot.send_message(message.chat.id, f"{ntt} №{nt}")

@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, "Официальный сайт МТУСИ – https://mtuci.ru/")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Я - бот, отображающий расписание группы БВТ2107. Вот список моих команд:\n'
                                      '/help - информация о боте\n'
                                      '/mtuci - ссылка на официальный сайт МТУСИ\n'
                                      '/week - узнать какая сейчас неделя\n'
                                      'Чтобы узнать расписание, нажимайте на кнопки на вашем экране.')


@bot.message_handler(content_types=['text'])
def answer(message):
    nt=(int((time.time()//1-1630270800)/3600/24/7)+1)
    ntt=1
    nttt=2
    if nt%2==0:
        ntt=2
        nttt=1
    else:
        ntt=1
        nttt=2

    if message.text.lower() == "понедельник":
        bot.send_message(message.chat.id, rasp(f"1.{ntt}",message.text.lower()))
    elif message.text.lower() == "вторник":
        bot.send_message(message.chat.id, rasp(f"2.{ntt}",message.text.lower()))
    elif message.text.lower() == "среда":
        bot.send_message(message.chat.id, rasp(f"3.{ntt}",message.text.lower()))
    elif message.text.lower() == "четверг":
        bot.send_message(message.chat.id, rasp(f"4.{ntt}",message.text.lower()))
    elif message.text.lower() == "пятница":
        bot.send_message(message.chat.id, rasp(f"5.{ntt}",message.text.lower()))
    elif message.text.lower() == "суббота":
        bot.send_message(message.chat.id, rasp(f"6.{ntt}",message.text.lower()))
    elif message.text.lower() == "расписание на текущую неделю":
        bot.send_message(message.chat.id, rasp(f"1.{ntt}","понедельник")+"\n"+rasp(f"2.{ntt}","вторник")+"\n"+rasp(f"3.{ntt}","среда")+"\n"+
                         rasp(f"4.{ntt}","четверг")+"\n"+rasp(f"5.{ntt}","пятница")+"\n"+rasp(f"6.{ntt}","суббота")+"\n")
    elif message.text.lower() == "расписание на следующую неделю":
        bot.send_message(message.chat.id,
                         rasp(f"1.{nttt}", "понедельник") + "\n" + rasp(f"2.{nttt}", "вторник") + "\n" + rasp(f"3.{nttt}","среда") + "\n" +
                         rasp(f"4.{nttt}", "четверг") + "\n" + rasp(f"5.{nttt}", "пятница") + "\n" + rasp(f"6.{nttt}","суббота") + "\n")
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понял.')
bot.polling()
app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())