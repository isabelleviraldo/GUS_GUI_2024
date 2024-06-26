import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
 
 
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing window...")
