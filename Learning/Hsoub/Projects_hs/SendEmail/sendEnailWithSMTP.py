import smtplib

sender_email = 'faristaleek@gmail.com'
rec_email = 'or.sammour@gmail.com'
password = 'vmxxwkbsikrflxsz'
message = 'Subject: Python.\nplapalpala '

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print('Login success')
server.sendmail(sender_email, rec_email, message)
print('Email has been sent to', rec_email)
server.quit()