
from _socket import gaierror
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secrets


def createToken():
	return secrets.token_urlsafe(16)


def loginSender():
	load_dotenv('./.env')
	APP_SENDER = os.getenv('SENDER')
	APP_PASSWORD = os.getenv('PASSWORD')

	return APP_SENDER, APP_PASSWORD


def createMessage(sender, receiver, token):
	message = MIMEMultipart()

	message['FROM'] = sender
	message['To'] = receiver
	message['Subject'] = '[NAVER BLOG BACKER] 프로그램 인증 메일'

	messageContent = f'''
	안녕하세요. 네이버 블로거 백커입니다. 
	우선 해당 프로그램을 이용해주셔서 감사합니다 :) 


	본 프로그램은 개인들이 정성스레 작성한 포스트 데이터를 보다 안전한 개인 공간에 저장하고 싶어하는 분들과
	다른 백링크 서비스 없이 직접 개인 포스트들을 구글 검색엔진에 노출시키고 하고 싶어하는 분들을 위해 서비스를 제공하고 있습니다.


	다만, 본래 목적과 달리 악용의 여지가 생길 수 있기에
	임시적인 방편으로 이와 같은 개인 메일 인증 절차를 추가하였습니다. 


	아래의 토큰 데이터 값을(괄호 안에 있는 값) 제 프로그램에 입력하시면 정상적으로 이후 서비스가 동작됩니다.
	토큰 데이터 값 : >>> {token} <<<


	좋은 하루 되세요. 
	감사합니다.


	P.S	
	프로그램이 만족스러우셨다면?
	아래 적힌 제 블로그에 방문하셔서 안부나 댓글 하나씩만 부탁드립니다.
	블로그 주소 : https://blog.naver.com/thswjdtmq4
	'''
	message.attach(MIMEText(messageContent, 'plain'))

	return message.as_string()


def sendToken(receiver, sender="default", password=1234):
	if sender == "default":
		sender, password = loginSender()

	SMTP_PORT = 465
	SMTP_SERVER = "smtp.gmail.com"

	authToken = createToken()
	message = createMessage(sender, receiver, authToken)

	try:
		with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
			server.login(sender, password)
			server.sendmail(sender, receiver, message)

		return authToken

	except (gaierror, ConnectionRefusedError):
		print('Failed to connect to the server. Bad connection settings?')
	except smtplib.SMTPServerDisconnected:
		print('Failed to connect to the server. Wrong user/password?')
	except smtplib.SMTPException as e:
		print('SMTP error occurred: ' + str(e))
