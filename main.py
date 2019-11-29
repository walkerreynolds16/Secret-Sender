import smtplib
import csv
from random import shuffle
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

file_name = "participants.txt"

def importFile():
    objs = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            objs.append(row)

    shuffle(objs)
    sendEmails(objs)

def sendEmails(objects):
    server = smtplib.SMTP(config.SMTP_ADDRESS, config.SMTP_PORT)
    server.starttls()
    server.login(config.SECRET_SENDER_EMAIL, config.SECRET_SENDER_PASSWORD)

    # item[0] = email address
    # item[1] = name of the person
    # item[2] = mailing address
    for i in range(len(objects)):
        item = objects[i]
        msg = MIMEMultipart()
        msg['From'] = config.SECRET_SENDER_EMAIL
        msg['To'] = item[0]

        person_assigned = ""
        if((i + 1) > len(objects) - 1):
            person_assigned = objects[0]
        else:
            person_assigned = objects[i+1]


        # Subject of the email, change to your liking
        msg['Subject'] = "Test Message Subject"

        # Body of the email, change to your liking
        body = "Test message\n Assigned Person = " + person_assigned[0]

        msg.attach(MIMEText(body, 'plain'))
        server.sendmail(config.SECRET_SENDER_EMAIL, item[0], msg.as_string())
    
    server.quit()



if __name__ == '__main__':
    importFile()