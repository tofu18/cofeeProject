import sys, sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        a = cur.execute("""SELECT * from coffee""").fetchall()
        con.commit()
        con.close()
        self.tableWidget.setRowCount(len(a))
        for i in range(len(a)):
            for j in range(len(a[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(a[i][j])))

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())