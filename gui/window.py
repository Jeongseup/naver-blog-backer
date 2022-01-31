import sys, os
from PyQt5.QtWidgets import QApplication, QTextEdit, QFileDialog, QDesktopWidget, QGridLayout, \
	QLabel, QLineEdit, QWidget, QPushButton
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		# first widget
		self.idLine = QLineEdit()
		self.idLine.returnPressed.connect(self.enterId)

		# second widget
		self.savePathBtn = QPushButton('Select Empty Folder')
		self.savePathBtn.pressed.connect(self.showDialog)

		# third widget
		self.resultLbl1 = QLabel('Entered your naver id is ...')

		grid = QGridLayout()
		grid.addWidget(QLabel('Enter your naver ID : '), 0, 0)
		grid.addWidget(QLabel('Choose save directory :'), 1, 0)
		grid.addWidget(QLabel('RESULT:'), 2, 0)

		grid.addWidget(self.idLine, 0, 1)
		grid.addWidget(self.savePathBtn, 1, 1)
		grid.addWidget(self.resultLbl1, 2, 1)

		self.setLayout(grid)
		self.setWindowIcon(QIcon('./src/icon.png'))
		self.setWindowTitle('Naver Blog Backer')
		self.setGeometry(300, 300, 300, 200)
		self.center()
		self.show()

	# self.textEdit = QTextEdit()
	# self.setCentralWidget(self.textEdit)
	# openFile.triggered.connect(self.showDialog)
	# btn = QPushButton('Quit', self)

	def enterId(self):
		print('enter id')

	def append_text(self):
		text = self.le.text()
		self.tb.append(text)
		self.le.clear()

	def clear_text(self):
		self.tb.clear()

	def text_changed(self):
		text = self.te.toPlainText()
		self.lbl2.setText('The number of words is ' + str(len(text.split())))

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
	# def text_changed(self):
	#
	#     text = self.te.toPlainText()
	#     self.lbl2.setText('The number of words is ' + str(len(text.split())))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyApp()

	sys.exit(app.exec_())
