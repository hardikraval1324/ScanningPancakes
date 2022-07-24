import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import json

# The mail addresses and password
sender_address = '******@gmail.com'
sender_pass = '**********'
# Setup the MIME

# fetch email into this dynamic list
r = open("reciepents.json",)
reciepents = json.load(r)
r.close()

# this function sends the email
def sendmail(sender_address, receiver_address, subject, content, receiver_name, receiver_id):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    # The subject line
    message['Subject'] = subject
    # The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))
    attach_file_name = './Test QR/'+str(receiver_id)+'.png'
    with open(attach_file_name, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name=os.path.basename(attach_file_name))
    message.attach(image)
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print(f"Mail Sent to {receiver_name}")


subject = '✨ Freshers 2021!'

# makes the content

def func_content_final(content):
    greeting = "Hello " + reciever_name + ",\n"
    signature = "\n\nps - Don't share your QR codes with anyone xD"
    content_ = greeting + content + signature
    return content_

# for sending mails in a loop
for i in range(len(reciepents)):
    content = '''Download the below QR code and don't forget to bring it on 18th!'''
    reciever_name = reciepents[i]["name"]
    content_final = func_content_final(content)
    sendmail(sender_address, reciepents[i]["email"],
             subject, content_final, reciever_name,i+1)
    print(f'sent to {reciepents[i]["name"]}')
