# pyqt_starbucks.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView,QLabel
from starbucksCrawl import starbucksCrawl
from tabulate import tabulate
from starbucks2 import *
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Starbucks Logic')

        font = QFont()
        font.setPointSize(14)   # Change font size


        self.example1 = QLabel(self)
        self.example1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.example2 = QLabel(self)
        self.example2.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.example3 = QLabel(self)
        self.example3.setTextInteractionFlags(Qt.TextSelectableByMouse)


        self.example1.setText("coffee ∧ coffee → coffee ∧ coffee")
        self.example2.setText("coffee ∧ coffee → coffee ∧ tea")
        self.example3.setText("coffee ∧ ¬coffee ∨ tea → coffee ∨ milk ∨ coffee")


        self.lineEdit = QLineEdit()
        self.button = QPushButton('Calculate')
        self.label1 = QLabel(self)
        self.label1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label2 = QLabel(self)
        self.label2.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.lineEdit.setFont(font)
        self.button.setFont(font)
        self.label1.setFont(font)
        font.setPointSize(17)
        self.label2.setFont(font)


        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.button.clicked.connect(self.on_click)

        vbox = QVBoxLayout()
        vbox.addWidget(self.example1)
        vbox.addWidget(self.example2)
        vbox.addWidget(self.example3)
        vbox.addWidget(self.lineEdit)
        vbox.addWidget(self.button)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.tableWidget)

        self.setLayout(vbox)

        self.show()

    @pyqtSlot()
    def on_click(self):
        starBucks = starbucks2()
        crawl = starbucksCrawl()
        inputString = starBucks.main(self.lineEdit.text())
        df, i = crawl.get_truth_table(inputString)

        self.label1.setText("논리식 변환 결과 : " + inputString)
        self.label2.setText(crawl.calculateTrueOrFalse(df,i))

        df.columns = [str(c) for c in df.columns]
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        for row in df.iterrows():
            for column in range(df.shape[1]):
                item = QTableWidgetItem(str(row[1][column]))
                if column == i:  # Change color for i-th column
                    item.setBackground(QBrush(QColor(255, 0, 0, 127)))
                self.tableWidget.setItem(row[0], column, item)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())





# pyinstaller --onefile --add-data "chromedriver.exe;." --add-data "starbucksCrawl.py;." --add-data "starbucks2.py;." pyqt_starbucks.py
