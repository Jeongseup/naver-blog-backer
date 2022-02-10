from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton, QMessageBox
import ProgressBar
import sys

class App(QWidget):
def __init__(self):
    super().__init__()
    self.title = 'PyQt5 button - pythonspot.com'
    self.left = 200
    self.top = 200
    self.width = 320
    self.height = 200
    self.initUI()

def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    button = QPushButton('PyQt5 button', self)
    button.setToolTip('This is an example button')
    button.move(100, 70)
    button.clicked.connect(self.on_click)

    self.show()

def on_click(self):
    print('PyQt5 button click')

    app1 = QApplication(sys.argv)
    window = QDialog()
    ui = ProgressBar.Ui_Form()
    ui.setupUi(window)
    window.show()

    for i in range(0, 100):
        ui.setValue(((i + 1) / 100) * 100)

    app1.quit()

    QMessageBox.information(self, "Message", "Data Loaded")

if __name__ == '__main__':
app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())