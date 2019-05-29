
##########################################
#程式檔名：ui_qry_song.py
#程式名稱：卡拉OK歌曲查詢
#程式類別：ui檔自動產生的畫面配置檔
##########################################
#180415   新增FUNCITON:tb_1_clear()，將資料放入畫面表格中#
#180421   增加資料庫連接# -*- coding: utf-8 -*-
#180512   調整ui檔，使之支援畫面大小調整時自動縮放物件   
#180513   新增hot_key(全局熱鍵)
# Form implementation generated from reading ui file 'qry_song.ui'
#
# Created by: PyQt5 UI code generator 5.6.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *   #180421 add
import keyboard   #180513 add
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(631, 515)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(631, 491))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gb_001 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_001.sizePolicy().hasHeightForWidth())
        self.gb_001.setSizePolicy(sizePolicy)
        self.gb_001.setObjectName(_fromUtf8("gb_001"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gb_001)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.hb_001 = QtWidgets.QHBoxLayout()
        self.hb_001.setObjectName(_fromUtf8("hb_001"))
        self.lbl_sing002 = QtWidgets.QLabel(self.gb_001)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微軟正黑體"))
        font.setPointSize(12)
        self.lbl_sing002.setFont(font)
        self.lbl_sing002.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_sing002.setObjectName(_fromUtf8("lbl_sing002"))
        self.hb_001.addWidget(self.lbl_sing002)
        self.sing002 = QtWidgets.QLineEdit(self.gb_001)
        self.sing002.setObjectName(_fromUtf8("sing002"))
        self.hb_001.addWidget(self.sing002)
        self.pb_sing002 = QtWidgets.QPushButton(self.gb_001)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微軟正黑體"))
        font.setPointSize(10)
        self.pb_sing002.setFont(font)
        self.pb_sing002.setObjectName(_fromUtf8("pb_sing002"))
        self.hb_001.addWidget(self.pb_sing002)
        self.verticalLayout_3.addLayout(self.hb_001)
        self.hb_002 = QtWidgets.QHBoxLayout()
        self.hb_002.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.hb_002.setObjectName(_fromUtf8("hb_002"))
        self.lbl_song002 = QtWidgets.QLabel(self.gb_001)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微軟正黑體"))
        font.setPointSize(12)
        self.lbl_song002.setFont(font)
        self.lbl_song002.setObjectName(_fromUtf8("lbl_song002"))
        self.hb_002.addWidget(self.lbl_song002)
        self.song002 = QtWidgets.QLineEdit(self.gb_001)
        self.song002.setObjectName(_fromUtf8("song002"))
        self.hb_002.addWidget(self.song002)
        self.pb_song002 = QtWidgets.QPushButton(self.gb_001)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微軟正黑體"))
        font.setPointSize(10)
        self.pb_song002.setFont(font)
        self.pb_song002.setObjectName(_fromUtf8("pb_song002"))
        self.hb_002.addWidget(self.pb_song002)
        self.verticalLayout_3.addLayout(self.hb_002)
        self.horizontalLayout.addWidget(self.gb_001)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_exit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_exit.sizePolicy().hasHeightForWidth())
        self.pb_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微軟正黑體"))
        font.setPointSize(10)
        self.pb_exit.setFont(font)
        self.pb_exit.setObjectName(_fromUtf8("pb_exit"))
        self.horizontalLayout.addWidget(self.pb_exit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tb_1 = QtWidgets.QTableWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_1.sizePolicy().hasHeightForWidth())
        self.tb_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tb_1.setFont(font)
        self.tb_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tb_1.setColumnCount(3)
        self.tb_1.setObjectName(_fromUtf8("tb_1"))
        item = QtWidgets.QTableWidgetItem()
        self.tb_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_1.setHorizontalHeaderItem(2, item)
        
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        #self.tb_1.setItem(0, 1, item)
        #self.tb_1.horizontalHeader().setCascadingSectionResizes(True)           #設定表頭寬度開合的方法
        self.tb_1.horizontalHeader().setDefaultSectionSize(150) #設定表頭預設宽度
        self.tb_1.horizontalHeader().setMinimumSectionSize(50) #設定表頭最小寬度
        self.remark = QtWidgets.QLineEdit(self.splitter)
        self.remark.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微軟正黑體"))
        font.setPointSize(10)
        self.remark.setFont(font)
        self.remark.setObjectName(_fromUtf8("remark"))
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.lbl_sing002.setBuddy(self.sing002)
        self.lbl_song002.setBuddy(self.song002)
        self.retranslateUi(MainWindow)
        self.table_init()
        self.signal_trigger(MainWindow)
        self.tb_1_clear(False)
        
        
    def signal_trigger(self, MainWindow):
        
        self.pb_exit.clicked.connect(MainWindow.close)
        self.pb_exit.toggled['bool'].connect(self.tb_1.clear)
        self.pb_sing002.clicked.connect(self.pb_sing002_clicked)
        self.pb_song002.clicked.connect(self.pb_song002_clicked)
        self.pb_sing002.toggled['bool'].connect(self.pb_sing002_clicked)
        self.pb_song002.toggled['bool'].connect(self.pb_song002_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #180513 add --s
        keyboard.add_hotkey('ctrl+k', self.pb_song002_clicked, suppress=False)  # qyery by sing002
        keyboard.add_hotkey('ctrl+enter', self.pb_song002_clicked, suppress=False)  # qyery by sing002
        #180513 add --e
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "卡拉OK歌曲查詢", None))
        self.gb_001.setTitle(_translate("MainWindow", "查詢", None))
        self.lbl_sing002.setText(_translate("MainWindow", "歌手名稱", None))
        self.pb_sing002.setText(_translate("MainWindow", "搜尋", None))
        self.lbl_song002.setText(_translate("MainWindow", "歌曲名稱", None))
        self.pb_song002.setText(_translate("MainWindow", "搜尋", None))
        self.pb_exit.setText(_translate("MainWindow", "離開", None))
        self.tb_1.setSortingEnabled(True)
        
    #表格物件初始化
    def table_init(self):
        self.tb_1.setRowCount(0)
        self.tb_1.setColumnCount(3)
        self.tb_1.setObjectName(_fromUtf8("tb_1"))
        item = self.tb_1.horizontalHeaderItem(0)
        item.setText(_translate("self", "歌手", None))
        l_size = QtCore.QSize(300, 30)
        l_size.setWidth(300)
        item.setSizeHint(l_size)
        item = self.tb_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow","歌曲名稱", None))
        l_size = QtCore.QSize(300,  30)
        l_size.setWidth(300)
        item.setSizeHint(l_size)
        item = self.tb_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "曲號", None))
        l_size = QtCore.QSize(300, 30)
        l_size.setWidth(300)
        item.setSizeHint(l_size)
    #180415 add --s
    #依照資料列的數量，新增一列並給欄位值
    def tb_1_clear(self, flag = True):
        print('請在這裡維護table')
        self.flag = flag 
        if self.flag == False:
            return
        self.tb_1.setRowCount(0)

    def connect_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        #filename = "D:\\Coding\\Python\\py_folder\\qt_program\\qry_song\\crazyktv.db3"
        filename = "crazyktv.db3"
        db.setDatabaseName(filename)
        print(QSqlDatabase.isDriverAvailable("QSQLITE"))
        if not db.open():
            print("Initialize fail")
            err_str = db.lastError().text()
            print(err_str)
    
    def pb_sing002_clicked(self):
        if self.sing002.text() != "":
            self.query_tb_1("Song_Singer")
        
    def pb_song002_clicked(self):
        if self.song002.text() !="":
            self.query_tb_1("Song_SongName")

    def query_tb_1(self, p_col=None):
        self.tb_1_clear()
        query = QSqlQuery()
        l_wc = None   #輸入的查詢條件
        if p_col == "Song_Singer":
            l_text = self.sing002.text()
            l_text = "%" + l_text + "%"
            l_wc = p_col + " LIKE '%s'"  % l_text
        elif p_col == "Song_SongName":
            l_text = self.song002.text()
            l_text = "%" + l_text + "%"
            l_wc = p_col + " LIKE '%s'"  % l_text
        l_sql = "SELECT Song_Singer,Song_SongName,Song_Id"\
                   "  FROM ktv_Song,ktv_Singer"\
                   " WHERE Song_Singer = Singer_Name"
        
        if l_wc is None:
            #如果沒有輸入查詢條件，不要查詢出東西來，以防資料量龐大，查詢時間會非常久
            l_wc = "1=2"
            return
        l_sql = l_sql + " AND " + l_wc
        l_i = 0
        l_dict = {}
        
        query.exec_(l_sql)
        #塞資料到表格時，需先關避sort功能，塞完資料才可開啟
        self.tb_1.setSortingEnabled(False)
        while query.next():
            l_return1 = query.value(0)
            l_return2 = query.value(1)
            l_return3 = query.value(2)
            l_return = []
            l_return.append(query.value(0))
            l_return.append(query.value(1))
            l_return.append(query.value(2))
            row = l_i
            self.tb_1.insertRow(row)   #新增一列
            item0 = QtWidgets.QTableWidgetItem()
            item1 = QtWidgets.QTableWidgetItem()
            item2 = QtWidgets.QTableWidgetItem()
            str0 = l_return[0]
            str1 = l_return[1]
            str2 = str(l_return[2])
            item0.setText(str0)
            item0.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
            self.tb_1.setItem(row, 0, item0)
            item1.setText(str1)
            item1.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
            self.tb_1.setItem(row, 1, item1)
            item2.setText(str2)
            item2.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
            self.tb_1.setItem(row, 2, item2)
            
            l_i = l_i + 1
        self.remark.setText("共查詢到%i筆資料" % l_i)
        #塞資料到表格時，需先關避sort功能，塞完資料才可開啟
        self.tb_1.setSortingEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.connect_db()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
   # keyboard.wait()   #180513 add


