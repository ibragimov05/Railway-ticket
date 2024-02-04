from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Main_file(QWidget):
    def show_login(self):
        from login import Login
        self.program = Login()
        self.close()
        self.program.show()
        
app = QApplication([])
dastur = Main_file()
dastur.show_login()
sys.exit(app.exec_())
