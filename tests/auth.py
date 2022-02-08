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
	message['Subject'] = 'NAVER BLOG BACKER Auth Mail by Jeongseup'

	messageContent = f'''
	This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.

	{token}
	Thank You
	'''
	message.attach(MIMEText(messageContent, 'plain'))

	return message.as_string()

def sendToken(receiver):

	SMTP_PORT = 465
	SMTP_SERVER = "smtp.gmail.com"

	authToken = createToken()
	sender, password = loginSender()
	message = createMessage(sender, receiver, authToken)

	try:
		with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
			server.login(sender, password)
			server.sendmail(sender, receiver, message)

		print('Sent')
		return authToken

	except (gaierror, ConnectionRefusedError):
		print('Failed to connect to the server. Bad connection settings?')
	except smtplib.SMTPServerDisconnected:
		print('Failed to connect to the server. Wrong user/password?')
	except smtplib.SMTPException as e:
		print('SMTP error occurred: ' + str(e))