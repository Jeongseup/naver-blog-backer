import os
import sys

from PyQt5.QtCore import QCoreApplication, QFile, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QLineEdit, \
	QRadioButton, QFileDialog, QInputDialog, QProgressDialog, QMessageBox
from naverblogbacker.blog import BlogCrawler
from naverblogbacker.post import BlogPost
from naverblogbacker.utils import createNewDirectory


class ProgressCrawler(BlogCrawler):
	def crawling(self, dirPath, setValue):
		urlPrefix = f'https://blog.naver.com/{self.targetId}/'

		if len(self.postList) == 0:
			raise (Exception(f'[ERROR] postList 함수가 정상적으로 실행되지 않았습니다.'))

		for i, post in enumerate(self.postList):
			tempPostDir = dirPath + "/" + post['logNo']

			if not createNewDirectory(tempPostDir):
				raise Exception(f"[ERROR] : {post['logNo']}포스트 폴더가 정상적으로 생성되지 않았습니다.")

			tempPostUrl = urlPrefix + post['logNo']
			tempPost = BlogPost(tempPostUrl, isDevMode=self.isDevMode)
			tempPost.run(dirPath=tempPostDir)

			if BlogPost.errorCount != 0:
				BlogCrawler.errorPost += 1

			# 포스트 백업 후 클래스 변수 초기화
			BlogPost.errorCount = 0

			print(f' [DEV] {(i / len(self.postList) * 100):.2f} % 완료했습니다.')
			setValue(i + 1)

		print(f' [DEV] User service complete!')
		return True

	def backlinking(self, dirPath, setValue):
		urlPrefix = f'https://blog.naver.com/PostView.naver?blogId={self.targetId}&logNo='
		filePath = dirPath + '/' + 'backlink.txt'

		if len(self.postList) == 0:
			raise (Exception(f'[ERROR] postList 함수가 정상적으로 실행되지 않았습니다.'))

		try:
			with open(filePath, mode='w', encoding='utf-8') as fp:
				data = ''

				for i, post in enumerate(self.postList):
					txt = ''
					txt += post['title']
					txt += '\n'
					txt += urlPrefix + post['logNo']
					txt += '\n\n'

					data += txt

					print(f' [DEV] {(i / len(self.postList) * 100):.2f} % 완료했습니다.')
					setValue(i + 1)

				fp.write(data)
				print(f' [DEV] User service complete!')
			return True
		except Exception as e:
			raise Exception(e)


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
		groupBox = QGroupBox('서비스 옵션')
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

		optionLabel = QLabel('이용할 서비스를 선택하세요 : ')
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
		pathLabel = QLabel('저장경로를 선택하세요         : ')
		pathButton = QPushButton('저장경로 선택')

		pathButton.pressed.connect(self.pathDialog)

		hBox = QHBoxLayout()
		hBox.addWidget(pathLabel)
		hBox.addWidget(pathButton)

		return hBox

	def buttonBox(self):
		runButton = QPushButton('    Run    ')
		cancelButton = QPushButton('Cancel')

		runButton.clicked.connect(self.authDialog)
		cancelButton.clicked.connect(QCoreApplication.instance().quit)

		hBox = QHBoxLayout()
		hBox.addStretch(1)
		hBox.addWidget(runButton)
		hBox.addWidget(cancelButton)
		hBox.addStretch(1)

		return hBox

	# == [FUNCTIONS] =========================================================

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
		# authToken = auth.sendToken(f'{self.myId}@naver.com')

		if ok:
			# 토큰값 체크
			# if str(authToken) == str(inputToken):
			if True:
				self.progressDialog()
			else:
				QMessageBox.information(self, "ERROR", "올바르지 않은 토큰값입니다.")

	def progressDialog(self):
		try:
			if self.myOption is 'backlink':
				myBlog = ProgressCrawler(targetId=self.myId, skipSticker=True, isDevMode=False)

				postLength = len(myBlog.postList)
				print(f' [DEV] {postLength}개의 포스트 데이터 추가, 프로그레스 다이얼로그 생성')

				progressServiceMessage = "서비스를 진행 중 입니다."
				progress = QProgressDialog(progressServiceMessage, None, 0, postLength, self)

				progress.setWindowTitle("Progress about Running")
				progress.setWindowIcon(QIcon('./src/icon.png'))
				progress.setWindowModality(Qt.WindowModal)

				progress.show()
				progress.setValue(0)

				# 정상적으로 종료시
				if myBlog.backlinking(dirPath=self.myPath, setValue=progress.setValue):
					self.msgBox()

			elif self.myOption is 'backup':
				myBlog = ProgressCrawler(targetId=self.myId, skipSticker=True, isDevMode=False)

				postLength = len(myBlog.postList)
				print(f' [DEV] {postLength}개의 포스트 데이터 추가, 프로그레스 다이얼로그 생성')

				progressServiceMessage = "서비스를 진행 중 입니다."
				progress = QProgressDialog(progressServiceMessage, None, 0, postLength, self)

				progress.setWindowTitle("Progress about Running")
				progress.setWindowIcon(QIcon('./src/icon.png'))
				progress.setWindowModality(Qt.WindowModal)

				progress.show()
				progress.setValue(0)

				# 정상적으로 종료시
				if myBlog.crawling(dirPath=self.myPath, setValue=progress.setValue):
					self.msgBox()

			else:
				raise Exception('[MESSAGE] 죄송합니다, 현재 이 기능은 지원하지 않습니다.')

		except Exception as e:
			errBox = QMessageBox()
			errBox.setWindowTitle('Error')
			errBox.setWindowIcon(QIcon('./src/icon.png'))
			errBox.setText('Error: ' + str(e))
			errBox.addButton(QMessageBox.Ok)
			errBox.exec()
			return

	def msgBox(self):
		msgBox = QMessageBox()
		msgBox.setWindowIcon(QIcon('./src/icon.png'))
		msgBox.setWindowTitle('Info')
		msgBox.setWindowModality(Qt.WindowModal)
		msgBox.setText('완료되었습니다.\n 이 창을 닫으시면 프로그램을 종료합니다.')
		msgBox.addButton(QMessageBox.Ok)
		msgBox.exec()

		os.startfile(self.myPath)
		sys.exit(0)


def load_stylesheet(app, res="./src/backer.qss"):
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
