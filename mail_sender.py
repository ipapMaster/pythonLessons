# pip install python-dotenv
import smtplib
import mimetypes
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(email, subject, text):
    """
    :param email: Ваш другой адрес для тестирования
    :param subject: Тема сообщения
    :param text: Сам текст сообщения
    """
    address_from = os.getenv('FROM')
    password = os.getenv('PASSWORD')

    msg = MIMEMultipart()
    msg['FROM'] = address_from
    msg['TO'] = email
    msg['SUBJECT'] = subject
    body = text
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL(os.getenv('HOST'), os.getenv('PORT'))
    server.login(address_from, password)
    server.send_message(msg)
    server.quit()
    return True
