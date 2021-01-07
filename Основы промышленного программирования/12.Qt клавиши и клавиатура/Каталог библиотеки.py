import sys
import math
import sqlite3
from PyQt5.QtGui import QPixmap

from functools import partial
from PyQt5 import uic  # Импортируем uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QMainWindow, QVBoxLayout, QLineEdit, QScrollArea, QGridLayout, QGroupBox, QFormLayout, \
    QAbstractScrollArea, QLabel


class BookWidget(QMainWindow):
    def __init__(self, info):
        super().__init__()
        uic.loadUi('book.ui', self)
        self.setWindowTitle("book")
        self.info = info
        self.name.setText(self.info[1])
        con = sqlite3.connect('bibliotecabooks.db')

        # Создание курсора
        cur = con.cursor()
        author = cur.execute(f"""SELECT author FROM authors
                         WHERE id = {self.info[2]}""").fetchall()
        for i in author:
            for j in i:
                author = j
                self.author.setText(author)
        self.year.setText(str(self.info[3]))
        result = cur.execute(f"""SELECT genre FROM genres
                                 WHERE id = {str(self.info[4])}""").fetchall()
        for i in result:
            self.genre.setText(*i)
        if self.info[5]:
            self.path = f'pic/{author}/{self.info[5]}'
        else:
            self.path = f'pic/standart.png'
        con.close()
        self.image_load()

    def image_load(self):
        self.pixmap = QPixmap(self.path)
        self.image = QLabel(self)
        self.image.move(20, 20)
        self.image.resize(250, 380)
        self.image.setPixmap(self.pixmap)



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('biblioteca.ui', self)
        self.for_name_now = True
        self.find_button.clicked.connect(self.find)
        self.toolButton.clicked.connect(self.regim)

    def find(self):
        con = sqlite3.connect('bibliotecabooks.db')

        # Создание курсора
        cur = con.cursor()
        if self.lineEdit.text() == '':
            con.close()
        else:
            if self.for_name_now:
                result = cur.execute(f"""SELECT name FROM books
                                            WHERE name LIKE '{self.lineEdit.text().capitalize()}%'""").fetchall()
            else:
                result = cur.execute(f"""SELECT name FROM books
                                            WHERE author_id=(SELECT id FROM authors 
                                    WHERE author LIKE '{self.lineEdit.text().capitalize()}%')""").fetchall()

            con.close()
            formLayout = QFormLayout()
            groupBox = QGroupBox()
            self.comboList = []
            for i in sorted(result):
                self.button = QPushButton(*i)
                self.button.clicked.connect(self.button_click)
                self.comboList.append(self.button)
                formLayout.addRow(self.button)
            groupBox.setLayout(formLayout)
            self.scrollArea.setWidget(groupBox)
            self.scrollArea.setWidgetResizable(True)
            self.show()

    def button_click(self):
        con = sqlite3.connect('bibliotecabooks.db')

        # Создание курсора
        cur = con.cursor()
        sender = self.sender()
        a = sender.text()
        self.result = cur.execute(f"""SELECT * FROM books
                                 WHERE name = '{a}'""").fetchall()
        con.close()
        self.w = BookWidget(*self.result)
        self.w.show()

    def regim(self):
        if self.toolButton.text() == 'Название':
            self.toolButton.setText('Актер')
            self.for_name_now = False
        else:
            self.toolButton.setText('Название')
            self.for_name_now = True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
