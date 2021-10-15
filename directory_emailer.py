import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def emailer(filepath):

    # set emails and password
    sender_address = 'herbbanjoes@gmail.com'
    sender_password = 'An0nym0us'
    receiver_address = 'shanejobber@gmail.com'
  
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Attachment: ' + str(filepath).split("\\")[-1]

    message_body = '''Hello,
    Please see attached document.
    Thank you
    '''

    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(message_body, 'plain'))

    attachment_file_name = filepath
    attachment_file = open(attachment_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attachment_file).read())
    encoders.encode_base64(payload) #encode the attachment

    #add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attachment_file_name)
    message.attach(payload)

    try:  
        #Create SMTP session for sending the mail
        server = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.starttls() #enable security
        server.login(sender_address, sender_password) #login with mail_id and password
        text = message.as_string()
        server.sendmail(sender_address, receiver_address, text)
        server.quit()
    except:
        print ('Something went wrong with sending ' + str(filepath).split("\\")[-1])


def main():

    directory_path = r"C:\Users\Shane\Dropbox\Dev\Scratch\data"

    file_count = 0
    for item in os.scandir(directory_path):
        if item.is_file():
            file_count += 1

    if file_count > 0:
        item_count = 1
        for item in os.scandir(directory_path):
            if item.is_file():
                filepath = item.path
                print ("Emailing file %d of %d..." % (item_count, file_count))
                emailer(filepath)
                item_count += 1
        print('Email(s) sent.')
    else:
        print ("No files in directory.")


if __name__ == '__main__':
    main()
