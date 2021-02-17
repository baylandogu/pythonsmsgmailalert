

#!/usr/bin/env python

import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to

	user = "gönderen@gmail.com"
	msg['from'] = user
	password = "Applikasyon Key Gmail"

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(user, password)
	server.send_message(msg)

	server.quit()


if __name__ == '__main__':
	email_alert("Hey ", "Merhaba, https://github.com/baylandogu > Projelerimi burada yayınlıyorum YouTube Kanalım <Vuln5> Projelerimin büyümesinde bana yardım et ^^", "alıcı@gmail.com")