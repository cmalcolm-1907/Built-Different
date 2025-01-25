# A Mech themed football manager style game
# Modules
import sqlite3
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QComboBox,
    QPushButton,
)
import sys

# Constants and Variables
# datbase connection and cursor
con = sqlite3.connect("builtdifferent.db")
cur = con.cursor()


# Custom Classes
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Built Different")
        combobox1 = QComboBox()
        combobox1.addItem("One")
        combobox1.addItem("Two")
        combobox1.addItem("Three")
        combobox1.addItem("Four")

        combobox2 = QComboBox()
        combobox2.addItems(["One", "Two", "Three", "Four"])

        combobox3 = QComboBox()
        combobox3.addItems(["One", "Two", "Three", "Four"])
        combobox3.insertItem(2, "Hello!")

        combobox4 = QComboBox()
        combobox4.addItems(["One", "Two", "Three", "Four"])
        combobox4.insertItems(2, ["Hello!", "again"])

        layout = QVBoxLayout()
        layout.addWidget(combobox1)
        layout.addWidget(combobox2)
        layout.addWidget(combobox3)
        layout.addWidget(combobox4)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


# Custom Methods/Functions
def view_team(name):
    for row in cur.execute(f"SELECT * FROM Teams WHERE name IS '{name}'"):
        print(row)


# GUI
app = QApplication(sys.argv)
w = MainWindow()
w.show()

# Mainloop
app.exec()
