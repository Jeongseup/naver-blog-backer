import sys

from PyQt5.QtCore import QCoreApplication, QFile
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QLineEdit

class MyApp(QWidget):

	def __init__(self):
		super().__init__()

		self.myId = None
		self.myPath = None
		self.myOption = None

		self.initUI()

	def initUI(self):

		vBox = QVBoxLayout()
		vBox.addStretch(1)
		vBox.addWidget(self.optionGroup())
		vBox.addStretch(1)
		vBox.addWidget(self.statusGroup())
		vBox.addStretch(1)

		self.setLayout(vBox)
		self.setWindowIcon(QIcon('./src/icon.png'))
		self.setWindowTitle('NAVER BLOG BACKER')
		# self.setGeometry(300, 300, 300, 200)
		self.show()

	# ==============================================================
	def statusGroup(self):
		groupBox = QGroupBox('현재 옵션')
		# groupBox.setFlat(True)

		vBox = QVBoxLayout()
		vBox.addLayout(self.statusBox())

		groupBox.setLayout(vBox)
		return groupBox

	def statusBox(self):
		label1 = QLabel('Status Label', self)
		label1.setAlignment(Qt.AlignCenter)

		label2 = QLabel('Second Label', self)
		label2.setAlignment(Qt.AlignVCenter)

		lbl_red.setStyleSheet("color: red;"
							  "border-style: solid;"
							  "border-width: 2px;"
							  "border-color: #FA8072;"
							  "border-radius: 3px")

		lbl_green.setStyleSheet("color: green;"
								"background-color: #7FFFD4")

		font1 = label1.font()
		font1.setPointSize(20)

		idLabel = QLabel('네이버 아이디를 입력하세요 : ')
		inputIdLine = QLineEdit()
		inputIdLine.returnPressed.connect(self.enterId)

		hBox = QHBoxLayout()
		hBox.addStretch(1)
		hBox.addWidget(idLabel)
		hBox.addWidget(inputIdLine)
		hBox.addStretch(1)

		return hBox

	# ==============================================================
	def optionGroup(self):
		groupBox = QGroupBox('옵션들')
		# groupBox.setFlat(True)

		vBox = QVBoxLayout()
		vBox.addLayout(self.idBox())
		vBox.addLayout(self.buttonBox())

		groupBox.setLayout(vBox)
		return groupBox

	def buttonBox(self):
		# buttons
		okButton = QPushButton('OK')
		cancelButton = QPushButton('Cancel')
		cancelButton.clicked.connect(QCoreApplication.instance().quit)

		hBox = QHBoxLayout()
		hBox.addStretch(1)
		hBox.addWidget(okButton)
		hBox.addWidget(cancelButton)
		hBox.addStretch(1)

		return hBox

	def idBox(self):
		idLabel = QLabel('네이버 아이디를 입력하세요 : ')
		inputIdLine = QLineEdit()
		inputIdLine.returnPressed.connect(self.enterId)

		hBox = QHBoxLayout()
		hBox.addStretch(1)
		hBox.addWidget(idLabel)
		hBox.addWidget(inputIdLine)
		hBox.addStretch(1)

		return hBox

	# ==============================================================

	def enterId(self):
		inputIdLine = self.sender()
		inputId = inputIdLine.text()

		print(f' [DEV] User entered the id, {inputId}')
		self.myId = inputId

		# self.settingLable1.setText(f'현재 입력된 아이디는 "{text}" 입니다.')
		# self.settingLable1.adjustSize()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	# load_stylesheet(app)
	app.setFont(QFont('엘리스 디지털배움체 OTF'))
	ex = MyApp()
	sys.exit(app.exec_())
