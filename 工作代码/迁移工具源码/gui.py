# -*- coding: GBK -*-
import pymssql
import _mssql
import uuid
import decimal
import os,sys
from ui_gui import Ui_Form
from PyQt4 import QtCore, QtGui
import time,datetime
from array import array
import decimal

class Cao(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Cao, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 各类单击信号：
        #整机迁移
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.zjInsert)  # 插入SQL
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.zjcs)  # 查询PlanID
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.zjcse)  # 查询EDB
        # 普通迁移
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.ptInsert)  # 插入SQL
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.ptcs)  # 查询PlanID
        QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL("clicked()"), self.ptcse)  # 查询EDB
        #升级独享
        QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.dxInsert)  # 插入SQL
        QtCore.QObject.connect(self.ui.pushButton_8, QtCore.SIGNAL("clicked()"), self.dxcs)  # 查询PlanID
        QtCore.QObject.connect(self.ui.pushButton_9, QtCore.SIGNAL("clicked()"), self.dxcse)  # 查询EDB

    #整机迁移部分
    # 插入操作的函数
    def zjInsert(self):
        con = pymssql.connect(host=', port=, user=, password=,database='')
        cur = con.cursor()
        PlanExecTime2 = self.ui.dateTimeEdit_2.dateTime()
        PlanExecTime3 = PlanExecTime2.toPyDateTime()
        PlanExecTime1 = PlanExecTime3.strftime("%Y-%m-%d %H:%M:%S")
        SourceVIP1 = str(self.ui.lineEdit_2.text())
        TargetVIP1 = str(self.ui.lineEdit_3.text())
        SourceVIPWeb1 = str(self.ui.lineEdit_4.text())
        TargetVIPWeb1 = str(self.ui.lineEdit_5.text())
        SourceSerAdd1 = str(self.ui.lineEdit_6.text())
        TargetSerAdd1 = str(self.ui.lineEdit_7.text())
        isUseDiff1 = str(self.ui.lineEdit_8.text())
        cur.executemany(
            "Insert into MigrationPlan(PlanExecTime,SourceVIP,TargetVIP,SourceVIPWeb,TargetVIPWeb,SourceSerAdd,TargetSerAdd,PlanType,NetType,isUseDiff)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);SELECT @@IDENTITY",
            [(PlanExecTime1, SourceVIP1, TargetVIP1, SourceVIPWeb1, TargetVIPWeb1, SourceSerAdd1, TargetSerAdd1,
              '整机迁移', '公网',isUseDiff1)]
        )
        con.commit()
        cur.execute('SELECT @@IDENTITY')
        a = cur.fetchall()
        x = a[0][0]
        dec = decimal.Decimal(x)
        y = str(dec)
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setHorizontalHeaderLabels(['PlanID'])
        newItem = QtGui.QTableWidgetItem(y)
        self.ui.tableWidget.setItem(0, 0, newItem)
        cur.close()
        con.close()

    def zjcs(self):
        con = pymssql.connect(host=', port=, user=, password=,
                              database='EdbMigration')
        cur = con.cursor()
        PlanId = int(str(self.ui.lineEdit_9.text()))
        cur.execute('Select * from MigrationPlan where planid >= %d'% PlanId )
        a = cur.fetchall()
        b = len(a)
        self.ui.tableWidget_2.setRowCount(b)
        self.ui.tableWidget_2.setColumnCount(24)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(
            ['PlanID', 'PlanExecTime', 'PlanType', 'NetType', 'SourceEDBA', 'SourceVIP', 'TargetVIP',
             'SourceStatus', 'TargetStatus', 'SourceVIPWeb', 'TargetVIPWeb', 'SourceSerAdd', 'TargetSerAdd',
             'SouceEDBVersion', 'TargetEDBVersion', 'SourceFreeDisk', 'TargetFreeDisk', 'SourceDBSizeTotal',
             'PlanCheckResult', 'isLinked', 'isOver', 'isEnable', 'SourceXLS', 'isUesDiff'])

        for y, x in enumerate(a):
            # self.MyTable.insertRow(y)
            newItem = QtGui.QTableWidgetItem(str(x[0]))
            self.ui.tableWidget_2.setItem(y, 0, newItem)
            newItem = QtGui.QTableWidgetItem(x[2].strftime("%Y-%m-%d %H:%M:%S"))
            self.ui.tableWidget_2.setItem(y, 1, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[3]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_2.setItem(y, 2, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[4]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_2.setItem(y, 3, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[5]))
            self.ui.tableWidget_2.setItem(y, 4, newItem)
            newItem = QtGui.QTableWidgetItem(x[6])
            self.ui.tableWidget_2.setItem(y, 5, newItem)
            newItem = QtGui.QTableWidgetItem(x[7])
            self.ui.tableWidget_2.setItem(y, 6, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[8]))
            self.ui.tableWidget_2.setItem(y, 7, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[9]))
            self.ui.tableWidget_2.setItem(y, 8, newItem)
            newItem = QtGui.QTableWidgetItem(x[10])
            self.ui.tableWidget_2.setItem(y, 9, newItem)
            newItem = QtGui.QTableWidgetItem(x[11])
            self.ui.tableWidget_2.setItem(y, 10, newItem)
            newItem = QtGui.QTableWidgetItem(x[12])
            self.ui.tableWidget_2.setItem(y, 11, newItem)
            newItem = QtGui.QTableWidgetItem(x[13])
            self.ui.tableWidget_2.setItem(y, 12, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[14]))
            self.ui.tableWidget_2.setItem(y, 13, newItem)
            newItem = QtGui.QTableWidgetItem(x[15])
            self.ui.tableWidget_2.setItem(y, 14, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[16]))
            self.ui.tableWidget_2.setItem(y, 15, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[17]))
            self.ui.tableWidget_2.setItem(y, 16, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[18]))
            self.ui.tableWidget_2.setItem(y, 17, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[19]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_2.setItem(y, 18, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[20]))
            self.ui.tableWidget_2.setItem(y, 19, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[21]))
            self.ui.tableWidget_2.setItem(y, 20, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[22]))
            self.ui.tableWidget_2.setItem(y, 21, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[23]))
            self.ui.tableWidget_2.setItem(y, 22, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[24]))
            self.ui.tableWidget_2.setItem(y, 23, newItem)
        cur.close()
        con.close()

    # MigEDB的显示设计:
    def zjcse(self):
        con = pymssql.connect(host=', port=, user=, password=,
                              database='')
        cur = con.cursor()
        PlanId = int(str(self.ui.lineEdit_10.text()))
        cur.execute('Select * from MigrationEDB where planid >= %d' % PlanId )
        j = cur.fetchall()
        b = len(j)
        self.ui.tableWidget_3.setRowCount(b)
        self.ui.tableWidget_3.setColumnCount(11)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(
            ['EdbID', 'PlanID', 'SourceVIP', 'TargetVIP', 'SourceEDB', 'SourceDBSize', 'ZipDbSize',
             'SourceStatus', 'TargetStatus', 'ZipDiffsize', 'isBackDiff'])
        for y, x in enumerate(j):
            newItem = QtGui.QTableWidgetItem(str(x[0]))
            self.ui.tableWidget_3.setItem(y, 0, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[1]))
            self.ui.tableWidget_3.setItem(y, 1, newItem)
            newItem = QtGui.QTableWidgetItem(x[2])
            self.ui.tableWidget_3.setItem(y, 2, newItem)
            newItem = QtGui.QTableWidgetItem(x[3])
            self.ui.tableWidget_3.setItem(y, 3, newItem)
            newItem = QtGui.QTableWidgetItem(x[4])
            self.ui.tableWidget_3.setItem(y, 4, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[5]))
            self.ui.tableWidget_3.setItem(y, 5, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[6]))
            self.ui.tableWidget_3.setItem(y, 6, newItem)
            newItem = QtGui.QTableWidgetItem(x[7])
            self.ui.tableWidget_3.setItem(y, 7, newItem)
            newItem = QtGui.QTableWidgetItem(x[8])
            self.ui.tableWidget_3.setItem(y, 8, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[9]))
            self.ui.tableWidget_3.setItem(y, 9, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[10]))
            self.ui.tableWidget_3.setItem(y, 10, newItem)
        cur.close()
        con.close()

    #普通迁移部分：
    # 插入操作的函数
    def ptInsert(self):
        con = pymssql.connect(host=', port=, user=, password=,
                              database=')
        cur = con.cursor()
        PlanExecTime2 = self.ui.dateTimeEdit_3.dateTime()
        PlanExecTime3 = PlanExecTime2.toPyDateTime()
        PlanExecTime1 = PlanExecTime3.strftime("%Y-%m-%d %H:%M:%S")
        SourceEDBA1 = str(self.ui.lineEdit_11.text())
        SourceVIP1 = str(self.ui.lineEdit_12.text())
        TargetVIP1 = str(self.ui.lineEdit_13.text())
        SourceVIPWeb1 = str(self.ui.lineEdit_14.text())
        TargetVIPWeb1 = str(self.ui.lineEdit_15.text())
        SourceSerAdd1 = str(self.ui.lineEdit_16.text())
        TargetSerAdd1 = str(self.ui.lineEdit_17.text())
        isUseDiff1 = str(self.ui.lineEdit_18.text())
        cur.executemany(
            "Insert into MigrationPlan(PlanExecTime,SourceEDBA,SourceVIP,TargetVIP,SourceVIPWeb,TargetVIPWeb,SourceSerAdd,TargetSerAdd,PlanType,NetType,isUseDiff)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);SELECT @@IDENTITY",
            [(PlanExecTime1,SourceEDBA1, SourceVIP1, TargetVIP1, SourceVIPWeb1, TargetVIPWeb1, SourceSerAdd1, TargetSerAdd1,
              '普通迁移', '公网',isUseDiff1)]
        )
        con.commit()
        cur.execute('SELECT @@IDENTITY')
        a = cur.fetchall()
        x = a[0][0]
        dec = decimal.Decimal(x)
        y = str(dec)
        self.ui.tableWidget_4.setRowCount(1)
        self.ui.tableWidget_4.setColumnCount(1)
        self.ui.tableWidget_4.setHorizontalHeaderLabels(['PlanID'])
        newItem = QtGui.QTableWidgetItem(y)
        self.ui.tableWidget_4.setItem(0, 0, newItem)
        cur.close()
        con.close()

    def ptcs(self):
        con = pymssql.connect(host=', port=, user=, password=,
                              database=')
        cur = con.cursor()
        PlanId = int(str(self.ui.lineEdit.text()))
        cur.execute('Select * from MigrationPlan where planid >= %d'% PlanId )
        a = cur.fetchall()
        b = len(a)
        self.ui.tableWidget_5.setRowCount(b)
        self.ui.tableWidget_5.setColumnCount(24)
        self.ui.tableWidget_5.setHorizontalHeaderLabels(
            ['PlanID', 'PlanExecTime', 'PlanType', 'NetType', 'SourceEDBA', 'SourceVIP', 'TargetVIP',
             'SourceStatus', 'TargetStatus', 'SourceVIPWeb', 'TargetVIPWeb', 'SourceSerAdd', 'TargetSerAdd',
             'SouceEDBVersion', 'TargetEDBVersion', 'SourceFreeDisk', 'TargetFreeDisk', 'SourceDBSizeTotal',
             'PlanCheckResult', 'isLinked', 'isOver', 'isEnable', 'SourceXLS', 'isUesDiff'])

        for y, x in enumerate(a):
            # self.MyTable.insertRow(y)
            newItem = QtGui.QTableWidgetItem(str(x[0]))
            self.ui.tableWidget_5.setItem(y, 0, newItem)
            newItem = QtGui.QTableWidgetItem(x[2].strftime("%Y-%m-%d %H:%M:%S"))
            self.ui.tableWidget_5.setItem(y, 1, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[3]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_5.setItem(y, 2, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[4]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_5.setItem(y, 3, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[5]))
            self.ui.tableWidget_5.setItem(y, 4, newItem)
            newItem = QtGui.QTableWidgetItem(x[6])
            self.ui.tableWidget_5.setItem(y, 5, newItem)
            newItem = QtGui.QTableWidgetItem(x[7])
            self.ui.tableWidget_5.setItem(y, 6, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[8]))
            self.ui.tableWidget_5.setItem(y, 7, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[9]))
            self.ui.tableWidget_5.setItem(y, 8, newItem)
            newItem = QtGui.QTableWidgetItem(x[10])
            self.ui.tableWidget_5.setItem(y, 9, newItem)
            newItem = QtGui.QTableWidgetItem(x[11])
            self.ui.tableWidget_5.setItem(y, 10, newItem)
            newItem = QtGui.QTableWidgetItem(x[12])
            self.ui.tableWidget_5.setItem(y, 11, newItem)
            newItem = QtGui.QTableWidgetItem(x[13])
            self.ui.tableWidget_5.setItem(y, 12, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[14]))
            self.ui.tableWidget_5.setItem(y, 13, newItem)
            newItem = QtGui.QTableWidgetItem(x[15])
            self.ui.tableWidget_5.setItem(y, 14, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[16]))
            self.ui.tableWidget_5.setItem(y, 15, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[17]))
            self.ui.tableWidget_5.setItem(y, 16, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[18]))
            self.ui.tableWidget_5.setItem(y, 17, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[19]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_5.setItem(y, 18, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[20]))
            self.ui.tableWidget_5.setItem(y, 19, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[21]))
            self.ui.tableWidget_5.setItem(y, 20, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[22]))
            self.ui.tableWidget_5.setItem(y, 21, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[23]))
            self.ui.tableWidget_5.setItem(y, 22, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[24]))
            self.ui.tableWidget_5.setItem(y, 23, newItem)
        cur.close()
        con.close()

    # MigEDB的显示设计:
    def ptcse(self):
        con = pymssql.connect(host=', port=, user=, password=,
                              database='')
        cur = con.cursor()
        PlanId = int(str(self.ui.lineEdit_19.text()))
        cur.execute('Select * from MigrationEDB where planid >= %d' % PlanId)
        j = cur.fetchall()
        b = len(j)
        self.ui.tableWidget_6.setRowCount(b)
        self.ui.tableWidget_6.setColumnCount(11)
        self.ui.tableWidget_6.setHorizontalHeaderLabels(
            ['EdbID', 'PlanID', 'SourceVIP', 'TargetVIP', 'SourceEDB', 'SourceDBSize', 'ZipDbSize',
             'SourceStatus', 'TargetStatus', 'ZipDiffsize', 'isBackDiff'])
        for y, x in enumerate(j):
            newItem = QtGui.QTableWidgetItem(str(x[0]))
            self.ui.tableWidget_6.setItem(y, 0, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[1]))
            self.ui.tableWidget_6.setItem(y, 1, newItem)
            newItem = QtGui.QTableWidgetItem(x[2])
            self.ui.tableWidget_6.setItem(y, 2, newItem)
            newItem = QtGui.QTableWidgetItem(x[3])
            self.ui.tableWidget_6.setItem(y, 3, newItem)
            newItem = QtGui.QTableWidgetItem(x[4])
            self.ui.tableWidget_6.setItem(y, 4, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[5]))
            self.ui.tableWidget_6.setItem(y, 5, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[6]))
            self.ui.tableWidget_6.setItem(y, 6, newItem)
            newItem = QtGui.QTableWidgetItem(x[7])
            self.ui.tableWidget_6.setItem(y, 7, newItem)
            newItem = QtGui.QTableWidgetItem(x[8])
            self.ui.tableWidget_6.setItem(y, 8, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[9]))
            self.ui.tableWidget_6.setItem(y, 9, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[10]))
            self.ui.tableWidget_6.setItem(y, 10, newItem)
        cur.close()
        con.close()

    #升级独享部分：
    # 插入操作的函数
    def dxInsert(self):
        con = pymssql.connect(host=', port=, user=, password=,
                              database='')
        cur = con.cursor()
        PlanExecTime2 = self.ui.dateTimeEdit_4.dateTime()
        PlanExecTime3 = PlanExecTime2.toPyDateTime()
        PlanExecTime1 = PlanExecTime3.strftime("%Y-%m-%d %H:%M:%S")
        SourceEDBA1 = str(self.ui.lineEdit_20.text())
        SourceVIP1 = str(self.ui.lineEdit_21.text())
        TargetVIP1 = str(self.ui.lineEdit_22.text())
        SourceVIPWeb1 = str(self.ui.lineEdit_23.text())
        TargetVIPWeb1 = str(self.ui.lineEdit_24.text())
        SourceSerAdd1 = str(self.ui.lineEdit_25.text())
        TargetSerAdd1 = str(self.ui.lineEdit_26.text())
        isUseDiff1 = str(self.ui.lineEdit_27.text())
        cur.executemany(
            "Insert into MigrationPlan(PlanExecTime,SourceEDBA,SourceVIP,TargetVIP,SourceVIPWeb,TargetVIPWeb,SourceSerAdd,TargetSerAdd,PlanType,NetType,isUseDiff)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);SELECT @@IDENTITY",
            [(PlanExecTime1,SourceEDBA1, SourceVIP1, TargetVIP1, SourceVIPWeb1, TargetVIPWeb1, SourceSerAdd1, TargetSerAdd1,
              '升级独享', '公网',isUseDiff1)]
        )
        con.commit()
        cur.execute('SELECT @@IDENTITY')
        a = cur.fetchall()
        x = a[0][0]
        dec = decimal.Decimal(x)
        y = str(dec)
        self.ui.tableWidget_7.setRowCount(1)
        self.ui.tableWidget_7.setColumnCount(1)
        self.ui.tableWidget_7.setHorizontalHeaderLabels(['PlanID'])
        newItem = QtGui.QTableWidgetItem(y)
        self.ui.tableWidget_7.setItem(0, 0, newItem)
        cur.close()
        con.close()

    def dxcs(self):
        con = pymssql.connect(host=', port=, user=, password=,
                              database='')
        cur = con.cursor()
        PlanId = int(str(self.ui.lineEdit_28.text()))
        cur.execute('Select * from MigrationPlan where planid >= %d'% PlanId )
        a = cur.fetchall()
        b = len(a)
        self.ui.tableWidget_8.setRowCount(b)
        self.ui.tableWidget_8.setColumnCount(24)
        self.ui.tableWidget_8.setHorizontalHeaderLabels(
            ['PlanID', 'PlanExecTime', 'PlanType', 'NetType', 'SourceEDBA', 'SourceVIP', 'TargetVIP',
             'SourceStatus', 'TargetStatus', 'SourceVIPWeb', 'TargetVIPWeb', 'SourceSerAdd', 'TargetSerAdd',
             'SouceEDBVersion', 'TargetEDBVersion', 'SourceFreeDisk', 'TargetFreeDisk', 'SourceDBSizeTotal',
             'PlanCheckResult', 'isLinked', 'isOver', 'isEnable', 'SourceXLS', 'isUesDiff'])

        for y, x in enumerate(a):
            # self.MyTable.insertRow(y)
            newItem = QtGui.QTableWidgetItem(str(x[0]))
            self.ui.tableWidget_8.setItem(y, 0, newItem)
            newItem = QtGui.QTableWidgetItem(x[2].strftime("%Y-%m-%d %H:%M:%S"))
            self.ui.tableWidget_8.setItem(y, 1, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[3]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_8.setItem(y, 2, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[4]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_8.setItem(y, 3, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[5]))
            self.ui.tableWidget_8.setItem(y, 4, newItem)
            newItem = QtGui.QTableWidgetItem(x[6])
            self.ui.tableWidget_8.setItem(y, 5, newItem)
            newItem = QtGui.QTableWidgetItem(x[7])
            self.ui.tableWidget_8.setItem(y, 6, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[8]))
            self.ui.tableWidget_8.setItem(y, 7, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[9]))
            self.ui.tableWidget_8.setItem(y, 8, newItem)
            newItem = QtGui.QTableWidgetItem(x[10])
            self.ui.tableWidget_8.setItem(y, 9, newItem)
            newItem = QtGui.QTableWidgetItem(x[11])
            self.ui.tableWidget_8.setItem(y, 10, newItem)
            newItem = QtGui.QTableWidgetItem(x[12])
            self.ui.tableWidget_8.setItem(y, 11, newItem)
            newItem = QtGui.QTableWidgetItem(x[13])
            self.ui.tableWidget_8.setItem(y, 12, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[14]))
            self.ui.tableWidget_8.setItem(y, 13, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[15]))
            self.ui.tableWidget_8.setItem(y, 14, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[16]))
            self.ui.tableWidget_8.setItem(y, 15, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[17]))
            self.ui.tableWidget_8.setItem(y, 16, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[18]))
            self.ui.tableWidget_8.setItem(y, 17, newItem)
            newItem = QtGui.QTableWidgetItem(array('u', x[19]).tostring()[::2].decode('gbk'))
            self.ui.tableWidget_8.setItem(y, 18, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[20]))
            self.ui.tableWidget_8.setItem(y, 19, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[21]))
            self.ui.tableWidget_8.setItem(y, 20, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[22]))
            self.ui.tableWidget_8.setItem(y, 21, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[23]))
            self.ui.tableWidget_8.setItem(y, 22, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[24]))
            self.ui.tableWidget_8.setItem(y, 23, newItem)
        cur.close()
        con.close()

    # MigEDB的显示设计:
    def dxcse(self):
        con = pymssql.connect(host=', port=, user=, password=,
                              database='')
        cur = con.cursor()
        PlanId = int(str(self.ui.lineEdit_29.text()))
        cur.execute('Select * from MigrationEDB where planid >= %d' % PlanId)
        j = cur.fetchall()
        b = len(j)
        self.ui.tableWidget_9.setRowCount(b)
        self.ui.tableWidget_9.setColumnCount(11)
        self.ui.tableWidget_9.setHorizontalHeaderLabels(
            ['EdbID', 'PlanID', 'SourceVIP', 'TargetVIP', 'SourceEDB', 'SourceDBSize', 'ZipDbSize',
             'SourceStatus', 'TargetStatus', 'ZipDiffsize', 'isBackDiff'])
        for y, x in enumerate(j):
            newItem = QtGui.QTableWidgetItem(str(x[0]))
            self.ui.tableWidget_9.setItem(y, 0, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[1]))
            self.ui.tableWidget_9.setItem(y, 1, newItem)
            newItem = QtGui.QTableWidgetItem(x[2])
            self.ui.tableWidget_9.setItem(y, 2, newItem)
            newItem = QtGui.QTableWidgetItem(x[3])
            self.ui.tableWidget_9.setItem(y, 3, newItem)
            newItem = QtGui.QTableWidgetItem(x[4])
            self.ui.tableWidget_9.setItem(y, 4, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[5]))
            self.ui.tableWidget_9.setItem(y, 5, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[6]))
            self.ui.tableWidget_9.setItem(y, 6, newItem)
            newItem = QtGui.QTableWidgetItem(x[7])
            self.ui.tableWidget_9.setItem(y, 7, newItem)
            newItem = QtGui.QTableWidgetItem(x[8])
            self.ui.tableWidget_9.setItem(y, 8, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[9]))
            self.ui.tableWidget_9.setItem(y, 9, newItem)
            newItem = QtGui.QTableWidgetItem(str(x[10]))
            self.ui.tableWidget_9.setItem(y, 10, newItem)
        cur.close()
        con.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ca = Cao()
    ca.show()
    sys.exit(app.exec_())