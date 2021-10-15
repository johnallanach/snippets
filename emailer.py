import smtplib

# SMTP object represents a connection to an SMTP mail server and has
# methods for sending emails.
server = smtplib.SMTP('smtp.gmail.com', 587)
#server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.starttls()

try:
    # login with email and password
    email_address = 'herbbanjoes@gmail.com'
    email_password = 'An0nym0us'
    server.login(email_address, email_password)
except:
    print ('Something went wrong with login..')

sent_from = email_address
to = ['shanejobber@gmail.com']
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
