import imapclient
import pprint
import pyzmail

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

rec_email = 'faristaleek@gmail.com'
password = 'vmxxwkbsikrflxsz'
imapObj.login(rec_email, password)

# pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ALL'])

# print(UIDs)
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
# pprint.pprint(rawMessages)

message = pyzmail.PyzMessage.factory(rawMessages[1][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part.get_payload().decode(message.text_part.charset))
imapObj.logout()