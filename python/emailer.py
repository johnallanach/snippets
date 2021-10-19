import smtplib

from config import SENDER_ADDRESS, SENDER_PASSWORD, RECEIVER_ADDRESS


# SMTP object represents a connection to an SMTP mail server and has
# methods for sending emails.
server = smtplib.SMTP('smtp.gmail.com', 587)
#server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.starttls()

try:
    # login with email and password
    email_address = SENDER_ADDRESS
    email_password = SENDER_PASSWORD
    server.login(email_address, email_password)
except:
    print ('Something went wrong with login..')

sent_from = email_address
to = [RECEIVER_ADDRESS]
subject = 'Python Emailer'
body = 'This email is a test.'

email_text = '''Hello,
    This email was sent programmatically using a python script.
    Thank you
    '''

try:
    server.sendmail(sent_from, to, email_text)
    server.close()
    print ('Email sent!')
except:
    print ('Something went wrong with email sending..')
