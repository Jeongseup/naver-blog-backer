import sys, os

from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication, QFileDialog, QDesktopWidget, QGridLayout, \
	QLabel, QLineEdit, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont


# from naverblogbacker.blog import BlogPost

class MyApp(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		# first widget
		self.idLine = QLineEdit()
		self.idLine.returnPressed.connect(self.enterId)

		# second widget
		savePathBtn = QPushButton('Select Empty Folder')
		savePathBtn.pressed.connect(self.showDialog)

		# third widget
		self.settingLable1 = QLabel('하단에서 당신의 아이디를 입력해주세요 :)')

		# ========================================================================

		grid = QGridLayout()
		grid.addWidget(QLabel('Current Status:'), 0, 0)
		grid.addWidget(self.settingLable1, 0, 1)

		grid.addWidget(QLabel('Enter your naver ID : '), 1, 0)
		grid.addWidget(self.idLine, 1, 1)

		grid.addWidget(QLabel('Choose save directory :'), 2, 0)
		grid.addWidget(savePathBtn, 2, 1)

		# ========================================================================

		self.setLayout(grid)
		self.setWindowIcon(QIcon('./src/icon.png'))
		self.setWindowTitle('Naver Blog Backer')
		self.resize(600, 400)
		self.center()
		self.show()

	# self.textEdit = QTextEdit()
	# self.setCentralWidget(self.textEdit)
	# openFile.triggered.connect(self.showDialog)
	# btn = QPushButton('Quit', self)

	def enterId(self):
		text = self.idLine.text()

		print('현재 입력된 텍스트 :', text)

		self.settingLable1.setText(f'현재 입력된 아이디는 "{text}" 입니다.')
		self.settingLable1.adjustSize()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def showDialog(self):
		defaultPath = os.path.expanduser('~') + '/downloads'
		dirPath = QFileDialog.getExistingDirectory(self, "Open Empty Directory", defaultPath)

		print(dirPath, type(dirPath))

		# 선택하지 않았을 경우
		if dirPath is '':
			print('no select')
		else:
			pass

def load_stylesheet(app, res="./src/style.qss"):
        rc = QFile(res)
        rc.open(QFile.ReadOnly)
        content = rc.readAll().data()
        app.setStyleSheet(str(content, "utf-8"))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	load_stylesheet(app)
	app.setFont(QFont('엘리스 디지털배움체 OTF'))
	ex = MyApp()
	sys.exit(app.exec_())
