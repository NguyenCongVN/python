import mailbox
from bs4 import BeautifulSoup
def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets

def handleerror(errmsg, emailmsg,cs):
    print()
    print(errmsg)
    print("This error occurred while decoding with ",cs," charset.")
    print("These charsets were found in the one email.",getcharsets(emailmsg))
    print("This is the subject:",emailmsg['subject'])
    print("This is the sender:",emailmsg['From'])

def getbodyfromemail(msg):
    body = None
    receiver = None
    #Walk through the parts of the email to find the text body.
    if msg.is_multipart():
        for part in msg.walk():
            # If part is multipart, walk through the subparts.
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/html':
                        # Get the subpart payload (i.e the message body)
                        body = subpart.get_payload(decode=True)
                        receiver = msg['To']
                        # charset = subpart.get_charset()

            # Part isn't multipart so get the email body
            elif part.get_content_type() == 'text/html':
                body = part.get_payload(decode=True)
                #charset = part.get_charset()

    # If this isn't a multi-part message then get the payload (i.e the message body)
    elif msg.get_content_type() == 'text/html':
        body = msg.get_payload(decode=True)

   # No checking done to match the charset with the correct part.
    for charset in getcharsets(msg):
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            handleerror("UnicodeDecodeError: encountered.",msg,charset)
        except AttributeError:
             handleerror("AttributeError: encountered" ,msg,charset)
    return [body , receiver]
def CopyLink(email , path1):
    # path1 = r'C:\Users\Admin\Documents\38-KU-feb-aol-fix2073-2128\38-KU-feb-aol-fix2073-2128\data\profile\default\Mail'
    path3 = r'\Inbox'
    link = ''
    for i in range(56):
        try:
            if i == 55:
                break
            folderName = ''
            if i == 0:
                folderName = '\pop.mail.yahoo.com'
            else:
                folderName = '\pop.mail.yahoo-{number}.com'.format(number=i)
            mboxfile = path1 + folderName + path3
            for thisemail in mailbox.mbox(mboxfile):
                [body , receiver] = getbodyfromemail(thisemail)
                parsed_html = BeautifulSoup(body)
                value = parsed_html.body.find_all("a", string=" Approve or Deny.")
                if value:
                    if receiver == email:
                        link = value[len(value) - 1]['href']
        except:
            continue
    if value == '':
        return 0
    else:
        return link
