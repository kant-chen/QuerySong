##########################################
#程式檔名：qry_song.py
#程式名稱：卡拉OK歌曲查詢
#程式類別：主程式
##########################################
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_qry_song import *
from PyQt4.QtSql import *   #180421 add

class main(QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        self.update_table()
        
        
    def update_table(self):
        print('請在這裡維護ui物件的自訂義設定')
        ui = Ui_MainWindow()
        
        #ui.setupUi(MainWindow)
        #ui.pb_sing002.setText("搜尋歌手")
        
      
    
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #180421 add --s
    #QSqlDatabase.drivers()
    db = QSqlDatabase.addDatabase("QSQLITE")
        
    db.setDatabaseName = ("D:\\Coding\\Python\\py_folder\\qt_program\\qry_song\\crazyktv.db3")
    db.open()
    if not db.open():
        print("Initialize fail")
        msg = QMessageBox()
        err_str = db.lastError().text()
        print(err_str)
        #msg.warning(None, "phone Log","Database Error: %1"  %s err_str)
        sys.exit(1)
        #180421 add --e
    MainWindow = QtGui.QMainWindow()
    
    main()
    
    main.update_table(main)
    MainWindow.show()
    sys.exit(app.exec_())
