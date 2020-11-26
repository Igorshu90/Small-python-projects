import smtplib
import datetime
import time

USER = ''
PSW = ''
TIME_STUMP = 60 * 60
RECIPIENTS = ['gilkuh@gmail.com']
SUBJECT = 'אני לא חבר ליכוד מבקש לא לשלוח לי יותר הודעות סמס לנייד '
BODY = 'מבקש לא לשלוח יותר הודעות למספר 0547903798.' \
       ' אני ישלח מייל בתוכנה אוטומטית פעם בשעה עד שעקבל התייחסות לבקשה שלי.' \
       ' חשוב לציין שכבר ביקשתי לא לשלוח הודעות ואני עדיין מקבל  . עד שהקבל התייחסות לבקשה שלי'


def send_email(user, pwd, recipient, subject, body):
    fromm = user
    to = recipient if isinstance(recipient, list) else [recipient]

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (fromm, ", ".join(to), subject, body)
    message = message.encode('utf-8')
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(fromm, to, message)
        server.close()
        print('successfully sent the mail')
    except IndexError:
        print("failed to send mail")


while True:
    for recipient in RECIPIENTS:
        send_email(USER, PSW, recipient, SUBJECT, BODY)
    now = datetime.datetime.now()
    print(f'send mail time: {now.strftime("%Y-%m-%d %H:%M:%S")}')
    time.sleep(TIME_STUMP)
