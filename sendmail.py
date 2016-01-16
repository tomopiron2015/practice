#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

class sendGmail:
    username, password = 'chump.2006@gmail.com', 'Wni1Geyf'

    def __init__(self, to, sub, body):
        host, port = 'smtp.gmail.com', 465
        msg = MIMEText(body)
        msg['Subject'] = sub
        msg['From'] = self.username
        msg['To'] = to

        smtp = smtplib.SMTP_SSL(host, port)
        smtp.ehlo()
        smtp.login(self.username, self.password)
        smtp.mail(self.username)
        smtp.rcpt(to)
        smtp.data(msg.as_string())
        smtp.quit()

if __name__ == '__main__':
    to = 'ww030ww.2011@gmail.com'
    sub = 'Send by Python smtplib'
    body = 'Send by Python Scrit,¥ntest send.'
    sendGmail(to, sub, body)