# A Mech themed football manager style game
# Modules
import sqlite3
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
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
        button = QPushButton("Push Me")

        self.setCentralWidget(button)


# Custom Methods/Functions
def view_team(name):
    for row in cur.execute(f"SELECT * FROM Teams WHERE name IS '{name}'"):
        print(row)


# GUI
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Mainloop
app.exec()
