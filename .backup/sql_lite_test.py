from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *





print(QSqlDatabase.drivers())
print(QSqlDatabase.isDriverAvailable("QSQLITE"))
db = QSqlDatabase()
db.addDatabase("QSQLITE")
db.setDatabaseName = ("crazyktv.db3")

if not db.open():
    print("Initialize fail")
    msg = QMessageBox()
    msg.warning(None, "phone Log", 
        QString("Database Error: %1").arg(db.lastError().text()))
    sys.exit(1)
