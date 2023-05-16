import smtplib
smtpObj = smtplib.SMTP('smtp.office365.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('email','password')
smtpObj.sendmail('youremail', 'sender email', 'Subject: Solong.\n Dear Alice, so long and thanks for all ''the fish. Sincerely, Rohith')
smtpObj.quit()