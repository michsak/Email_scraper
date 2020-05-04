import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import re


def log():
    print("Write down your login and password\nLogin:")
    username = input()
    print("Pasword:")
    password = input()

    imap = imaplib.IMAP4_SSL("imap.wp.pl")
    imap.login(username, password)
    return imap


def reading_emails():
    mail_interior = log()
    il_char = ['<', '>', '/', '%', '&', '#', '?', ':']
    status, messages = mail_interior.select('INBOX')
    how_many_less = 850
    mail_nb = int(messages[0])

    for i in range(mail_nb, mail_nb-how_many_less, -1):
        res, msg = mail_interior.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                from_ = msg.get("From")
                print("Subject: ", subject)
                print("From: ", from_)
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            print(body)
                        elif "attachment" in content_disposition:
                            filename = part.get_filename()
                            if filename:
                                if not os.path.isdir(subject):              #MAKING FOLDERS
                                    reg_expr = re.compile(r'\w+')
                                    subject = str(reg_expr.findall(subject))
                                    subject = subject.replace(",", "").replace("'", "").replace('[', "").replace(']', "")
                                    os.mkdir(subject)
                                filepath = os.path.join(subject, filename)
                                open(filepath, "wb").write(part.get_payload(decode=True))
                    else:
                        content_type = msg.get_content_type()   #string type
                        body = str(msg.get_payload(decode=True))     #here is the problem
                        if content_type == "text/plain":
                            print(body)
                    if content_type == "text/html":
                        if not os.path.isdir(subject):
                            reg_expr = re.compile(r'\w+')
                            subject = str(reg_expr.findall(subject))
                            subject = subject.replace(",", "").replace("'", "").replace('[', "").replace(']', "")
                            os.mkdir(subject)
                        filename = f"{subject[:50]}.html"
                        filepath = os.path.join(subject, filename)
                        open(filepath, "w").write(body)
                        webbrowser.open(filepath)
                    print("="*100)
    mail_interior.close()
    mail_interior.logout()

if __name__ == "__main__":
    reading_emails()