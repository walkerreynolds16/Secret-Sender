import smtplib
import csv
from random import shuffle
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

filename = "participants.txt"

smtpAddress = "smtp.gmail.com"
smtpPort = 587

sendingEmail = "secretpizzasender@gmail.com"
sendingPassword = "Z95fwTEh1bJ1"

def importFile():
    objs = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            objs.append(row)

    shuffle(objs)
    sendEmails(objs)

def sendEmails(objects):
    server = smtplib.SMTP(smtpAddress, smtpPort)
    server.starttls()
    server.login(sendingEmail, sendingPassword)

    # item[0] = email address
    # item[1] = name of the person
    # item[2] = mailing address
    for i in range(len(objects)):
        item = objects[i]
        msg = MIMEMultipart()
        msg['From'] = sendingEmail
        msg['To'] = item[0]

        personAssigned = ""
        if((i + 1) > len(objects) - 1):
            personAssigned = objects[0]
        else:
            personAssigned = objects[i+1]


        # Subject of the email, change to your liking
        msg['Subject'] = "Test Message Subject"

        # Body of the email, change to your liking
        body = "Test message\n Assigned Person = " + personAssigned[0]

        msg.attach(MIMEText(body, 'plain'))
        server.sendmail(sendingEmail, item[0], msg.as_string())
    
    server.quit()



if __name__ == '__main__':
    importFile()