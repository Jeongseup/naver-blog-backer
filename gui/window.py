import sys, os
from PyQt5.QtCore import QFile
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QFileDialog, QDesktopWidget, QGridLayout, \
	QLabel, QLineEdit, QWidget, QPushButton, QRadioButton
from PyQt5.QtGui import QIcon, QFont


def load_stylesheet(app, res="./src/style.qss"):
	rc = QFile(res)
	rc.open(QFile.ReadOnly)
	content = rc.readAll().data()
	app.setStyleSheet(str(content, "utf-8"))


class MyApp(QWidget):

	def __init__(self):
		super().__init__()
		self.myId = None
		self.myOption = None

		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		grid.addWidget(QLabel('Choose one option'), 0, 0)

		radioButton = QRadioButton('[옵션1] 백업')
		radioButton.option = "backup"
		radioButton.toggled.connect(self.onClicked)
		grid.addWidget(radioButton, 0, 1)

		radioButton = QRadioButton('[옵션2] 백링크')
		radioButton.option = "backlink"
		radioButton.toggled.connect(self.onClicked)
		grid.addWidget(radioButton, 0, 2)

		radioButton = QRadioButton('[옵션3] 모두')
		radioButton.option = "both"
		radioButton.toggled.connect(self.onClicked)
		grid.addWidget(radioButton, 0, 3)

		#  widget
		self.idLine = QLineEdit()
		self.idLine.returnPressed.connect(self.enterId)

		# second widget
		savePathBtn = QPushButton('Select Empty Folder')
		savePathBtn.pressed.connect(self.showDialog)

		# third widget
		self.settingLable1 = QLabel('하단에서 당신의 아이디를 입력해주세요 :)')

		# buttons
		okButton = QPushButton('OK')

		cancelButton = QPushButton('Cancel')
		cancelButton.clicked.connect(QCoreApplication.instance().quit)

		# ========================================================================



		grid.addWidget(QLabel('Current Status:'), 1, 0)
		grid.addWidget(self.settingLable1, 1, 1)

		grid.addWidget(QLabel('Enter your naver ID : '), 2, 0)
		grid.addWidget(self.idLine, 2, 1)

		grid.addWidget(QLabel('Choose save directory :'), 3, 0)
		grid.addWidget(savePathBtn, 3, 1)

		grid.addWidget(okButton, 4, 0)
		grid.addWidget(cancelButton, 4, 1)

		# ========================================================================

		self.setLayout(grid)
		self.setWindowIcon(QIcon('./src/icon.png'))
		self.setWindowTitle('Naver Blog Backer')
		self.center()
		self.show()

	# self.textEdit = QTextEdit()
	# self.setCentralWidget(self.textEdit)
	# openFile.triggered.connect(self.showDialog)
	# btn = QPushButton('Quit', self)

	def onClicked(self, option):
		radioButton = self.sender()
		if radioButton.isChecked():
			print(f'Click the {radioButton.option}')
			self.myOption = radioButton.option


	def enterId(self):
		text = self.idLine.text()

		print('현재 입력된 텍스트 :', text)

		self.settingLable1.setText(f'현재 입력된 아이디는 "{text}" 입니다.')
		self.settingLable1.adjustSize()

	def enterOption(self):
		print(self)

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


if __name__ == '__main__':
	app = QApplication(sys.argv)
	# load_stylesheet(app)
	# app.setFont(QFont('엘리스 디지털배움체 OTF'))
	ex = MyApp()
	sys.exit(app.exec_())
