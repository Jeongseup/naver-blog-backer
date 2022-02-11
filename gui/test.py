import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

SIZE = 5

def doGenerate(setValue):
    for x2 in range(SIZE):
        # if x2 == 4:
        #     raise Exception('에러 발생!')
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec_()
        setValue(x2 + 1)
        print(x2, SIZE)
        print(f' [DEV] {x2/SIZE * 100}. % 완료했습니다.')

    print('Done')


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.genAudioButton = QPushButton('Generate', self)
        self.genAudioButton.clicked.connect(self.generate)
        self.setCentralWidget(self.genAudioButton)

        self.show()

    def closeEvent(self, event):
        print(event)

    def generate(self):
        try:

            progress = QProgressDialog('Work in progress', None, 0, SIZE, self)
            progress.setWindowTitle("Generating files...")
            progress.setWindowModality(Qt.WindowModal)
            progress.show()

            progress.setValue(0)
            doGenerate(progress.setValue)

        except Exception as e:
            errBox = QMessageBox()
            errBox.setWindowTitle('Error')
            errBox.setText('Error: ' + str(e))
            errBox.addButton(QMessageBox.Ok)
            errBox.exec()
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ret = app.exec_()
    sys.exit(ret)
