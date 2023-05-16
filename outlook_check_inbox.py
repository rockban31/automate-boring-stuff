from imapclient import imapclient

imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
imapObj.login('rohithjayaram31@outlook.com','9eD@kkiom5GdN0Sw')
imapObj_info = imapObj.select_folder('inbox')
print('%d messages in inbox' % imapObj_info[b'EXISTS'])
imapObj.select_folder('inbox', readonly=True)
messages = imapObj.search(['FROM', 'admin@credly.com'])
print("%d messages from our best friend" % len(messages))
