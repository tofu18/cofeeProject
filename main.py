import sys, sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem


class MyWidget(QWidget):
    def __init__(self):
        print('a')
        super().__init__()
        uic.loadUi('main.ui', self)
        self.fill()

    def showForm(self):
        if self.sender() == self.pushButton:
            purpose = 'add'
        else:
            purpose = 'change'
        self.second_form = Form(purpose, self)
        self.second_form.show()

    def fill(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        a = cur.execute("""SELECT * from coffee""").fetchall()
        con.commit()
        con.close()
        self.tableWidget.setRowCount(len(a))
        for i in range(len(a)):
            for j in range(len(a[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(a[i][j])))
        self.pushButton.clicked.connect(self.showForm)
        self.pushButton_2.clicked.connect(self.showForm)


class Form(QWidget):
    def __init__(self, purpose, other):
        super().__init__()
        self.other = other
        uic.loadUi('addEditCoffeeForm.ui', self)
        if purpose == 'add':
            self.lineEdit.hide()
            self.label.hide()
        self.purpose = purpose
        self.pushButton.clicked.connect(self.add)

    def add(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        id, name, roast, grain, taste, price, volume = self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text()

        if self.purpose == 'add':
            cur.execute("""INSERT into coffee(name, roast, grain, taste, price, volume) VALUES(?, ?, ?, ?, ?, ?)""",
                        (name, roast, grain, taste, price, volume))
        else:

            cur.execute(
                """UPDATE coffee SET name = ?, roast = ?, grain = ?, taste = ?, price = ?, volume = ? WHERE id = ?""",
                (name, roast, grain, taste, price, volume, id))
        con.commit()
        con.close()
        self.hide()
        self.other.fill()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
