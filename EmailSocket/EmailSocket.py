#!/usr/bin/env python


import smtplib
from email.mime.text import MIMEText

class EmailSocket():
   def __init__(self):
	self.empfaenger = 'YOURNAME@googlemail.com'
	self.sender = 'YOURNAME@googlemail.com'
	self.smtpserver = 'smtp.googlemail.com:587'
	self.smtpusername = 'YOURNAME@googlemail.com'
	self.smtppassword = 'YOURPASSWORD'
	self.usetls = True


   def sendEmail(self, titel, inhalt):

	msg = MIMEText(inhalt)
	msg['From'] = self.sender
	msg['To'] = self.empfaenger
	msg['Subject'] = titel
	server = smtplib.SMTP(self.smtpserver)

	if self.usetls:
	  server.starttls()
	if self.smtpusername and self.smtppassword:
	  server.login(self.smtpusername, self.smtppassword)
	server.sendmail(self.sender, self.empfaenger, msg.as_string())
	server.quit()
