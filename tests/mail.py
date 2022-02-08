from _socket import gaierror
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secrets

authToken = secrets.token_urlsafe(16)

load_dotenv()
APP_SENDER = os.getenv('SENDER')
APP_PASSWORD = os.getenv('PASSWORD')

PORT = 465
SERVER = "smtp.gmail.com"
messageContent = f'''
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.

${authToken}
Thank You
'''

if __name__ == '__main__':
	# specify the sender’s and receiver’s email addresses
	APP_RECEVIER = input("Please enter your receiver address : ")

	message = MIMEMultipart()

	message['FROM'] = APP_SENDER
	message['To'] = APP_RECEVIER
	message['Subject'] = 'NAVER BLOG BACKER Auth Mail by Jeongseup'

	message.attach(MIMEText(messageContent, 'plain'))

	try:
		# send your message with credentials specified above
		with smtplib.SMTP_SSL(SERVER, PORT) as server:
			server.login(APP_SENDER, APP_PASSWORD)
			server.sendmail(APP_SENDER, APP_RECEVIER, message.as_string())

		# tell the script to report if your message was sent or which errors need to be fixed
		print('Sent')
	except (gaierror, ConnectionRefusedError):
		print('Failed to connect to the server. Bad connection settings?')
	except smtplib.SMTPServerDisconnected:
		print('Failed to connect to the server. Wrong user/password?')
	except smtplib.SMTPException as e:
		print('SMTP error occurred: ' + str(e))
