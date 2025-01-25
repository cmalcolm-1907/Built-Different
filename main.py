# A Mech themed football manager style game
# Modules
import sqlite3
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

# Constants and Variables
# datbase connection and cursor
con = sqlite3.connect("builtdifferent.db")
cur = con.cursor()



class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):    
        super().__init__(parent)

        self.setWindowTitle("Built Different")

        self.resize(400, 200)

        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)

        menu = self.menuBar()

        button_action = QAction(QIcon("bug.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        

# Custom Methods/Functions
def view_team(name):
    for row in cur.execute(f"SELECT * FROM Teams WHERE name IS '{name}'"):
        print(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())