import win32com.client
ol=win32com.client.Dispatch("outlook.application")
olmailitem=0x0 #size of the new email
newmail=ol.CreateItem(olmailitem)
newmail.Subject= 'Testing Mail'
newmail.To='rooparohith29@gmail.com'
newmail.CC='rohithjayaram31@gmail.com'
newmail.Body= 'Hello, this is a test email to showcase how to send emails from Python and Outlook.'
newmail.Send()