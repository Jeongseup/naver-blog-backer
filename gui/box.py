import sys

from PyQt5.QtCore import QCoreApplication, QFile
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox


# main(myId, myPath, myOption)

class MyApp(QWidget):

	def __init__(self):
		super().__init__()

		self.myId = None
		self.myOption = None
		self.myPath = None

		self.initUI()

	def initUI(self):

		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addWidget(self.optionGroup())
		vbox.addStretch(1)
		# vbox.addWidget(self.statusGroup())
		vbox.addStretch(1)

		self.setLayout(vbox)
		self.setWindowTitle('Box Layout')
		self.setGeometry(300, 300, 300, 200)
		self.show()

	def optionGroup(self):
		groupBox = QGroupBox('옵션들')
		groupBox.setFlat(True)

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
		idLable = QLabel('아이디를 입력하세요 : ')

		hBox = QHBoxLayout()
		hBox.addStretch(1)
		hBox.addWidget(idLable)
		hBox.addStretch(1)

		return hBox

if __name__ == '__main__':
	app = QApplication(sys.argv)
	# load_stylesheet(app)
	app.setFont(QFont('엘리스 디지털배움체 OTF'))
	ex = MyApp()
	sys.exit(app.exec_())
