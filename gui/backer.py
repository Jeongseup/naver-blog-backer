import os
import sys

from PyQt5.QtCore import QCoreApplication, QFile, Qt, QTimer, QBasicTimer
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QLineEdit, \
	QRadioButton, QFileDialog, QInputDialog, QProgressDialog
from PyQt5.QtWidgets import QMessageBox


def load_stylesheet(app, res="./src/style.qss"):
	rc = QFile(res)
	rc.open(QFile.ReadOnly)
	content = rc.readAll().data()
	app.setStyleSheet(str(content, "utf-8"))


class MyApp(QWidget):

	def __init__(self):
		super().__init__()

		self.myId = ''
		self.myPath = ''
		self.myOption = ''

		self.initUI()

	def initUI(self):
		vBox = QVBoxLayout()

		vBox.addWidget(self.statusGroup())
		vBox.addStretch(1)
		vBox.addWidget(self.optionGroup())

		self.setLayout(vBox)
		self.setWindowIcon(QIcon('./src/icon.png'))
		self.setWindowTitle('네이버 블로그 백커')
		self.resize(500, 400)
		self.show()

	# ==============================================================

	def statusGroup(self):
		groupBox = QGroupBox('현재 설정된 옵션값')
		groupBox.setFlat(True)

		vBox = QVBoxLayout()
		vBox.addLayout(self.statusBox())

		groupBox.setLayout(vBox)
		return groupBox

	def statusBox(self):

		self.statusLabel = QLabel(self.statusText())
		self.statusLabel.setAlignment(Qt.AlignVCenter)
		hBox = QHBoxLayout()
		hBox.addWidget(self.statusLabel)

		return hBox

	# ==============================================================
	def optionGroup(self):
		groupBox = QGroupBox('백업 옵션')
		groupBox.setFlat(True)

		vBox = QVBoxLayout()
		vBox.addLayout(self.radioBox())
		vBox.addLayout(self.idBox())
		vBox.addLayout(self.pathBox())
		vBox.addLayout(self.buttonBox())
		groupBox.setLayout(vBox)
		return groupBox

	def radioBox(self):

		hBox = QHBoxLayout()

		optionLabel = QLabel('옵션을 선택하세요 : ')
		hBox.addWidget(optionLabel)

		radioButton = QRadioButton('[옵션1] 백업')
		radioButton.option = "backup"
		radioButton.toggled.connect(self.onClicked)
		hBox.addWidget(radioButton)

		radioButton = QRadioButton('[옵션2] 백링크')
		radioButton.option = "backlink"
		radioButton.toggled.connect(self.onClicked)
		hBox.addWidget(radioButton)

		radioButton = QRadioButton('[옵션3] 모두')
		radioButton.option = "both"
		radioButton.toggled.connect(self.onClicked)
		hBox.addWidget(radioButton)

		return hBox

	def idBox(self):
		idLabel = QLabel('네이버 아이디를 입력하세요 : ')

		inputIdLine = QLineEdit()
		inputIdLine.returnPressed.connect(self.enterId)

		hBox = QHBoxLayout()
		hBox.addWidget(idLabel)
		hBox.addWidget(inputIdLine)

		return hBox

	def pathBox(self):
		pathLabel = QLabel('저장경로를 선택하세요 : ')

		pathButton = QPushButton('저장경로 선택')
		pathButton.pressed.connect(self.pathDialog)

		hBox = QHBoxLayout()
		hBox.addWidget(pathLabel)
		hBox.addWidget(pathButton)

		return hBox

	def buttonBox(self):
		runButton = QPushButton('Run')
		cancelButton = QPushButton('Cancel')

		runButton.clicked.connect(self.authDialog)
		cancelButton.clicked.connect(QCoreApplication.instance().quit)

		hBox = QHBoxLayout()
		hBox.addStretch(1)
		hBox.addWidget(runButton)
		hBox.addWidget(cancelButton)
		hBox.addStretch(1)

		return hBox

	def closeEvent(self, event):
		print(event)

	# ==============================================================
	def statusText(self):
		if self.myPath != '' or self.myId != '' or self.myOption != '':
			return \
				f'''입력된 아이디는 : {self.myId}\n입력된 옵션은 : {self.myOption}\n입력된 저장경로 : {self.myPath}'''
		else:
			return '안녕하세요, 네이버 블로거 백커입니다 :)'

	def onClicked(self):
		radioButton = self.sender()
		if radioButton.isChecked():
			print(f' [DEV] User entered the id, {radioButton.option}')
			self.myOption = radioButton.option
			self.statusLabel.setText(self.statusText())

	def enterId(self):
		inputIdLine = self.sender()
		inputId = inputIdLine.text()

		print(f' [DEV] User entered the id, {inputId}')

		self.myId = inputId
		self.statusLabel.setText(self.statusText())

	def pathDialog(self):
		defaultPath = os.path.expanduser('~') + '/downloads'
		dirPath = QFileDialog.getExistingDirectory(self, "Open Empty Directory", defaultPath)

		# 선택하지 않았을 경우
		if dirPath is '':
			print('no select')
		else:
			print(f' [DEV] User selected path, {dirPath}')

			self.myPath = dirPath
			self.statusLabel.setText(self.statusText())
			pass

	def authDialog(self):
		text, ok = QInputDialog.getText(self, 'Auth Dialog', 'Enter the token : ')

		if ok:

			# print(f' [DEV] Token is {text}')

			# 토큰값 체크
			if True:
				print('시작')

				progress = QProgressDialog("Run", "서비스를 시작합니다.", 0, 100, self)
				progress.show()

				# progress.setAutoClose(False)

				# btn = QPushButton('Cancel')
				# btn.setEnabled(False)
				# progress.setCancelButton(btn)

				# progress.setValue(0)

		else:
				QMessageBox.information(self, "ERROR", "올바르지 않은 토큰값입니다.")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	# load_stylesheet(app)
	app.setFont(QFont('엘리스 디지털배움체 OTF'))
	ex = MyApp()
	sys.exit(app.exec_())
