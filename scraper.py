import imaplib
import email
from email.header import decode_header
import os
import re


def log():
    print("Write down your login and password\nLogin:")
    login = input()
    print("Pasword:")
    password = input()

    reg_exp = re.compile(r'@\w+.\w+')
    domain = reg_exp.findall(login)
    domain = str(domain).replace('@', "").replace('[', "").replace(']', "").replace("'", "").replace("'", "")

    imap = imaplib.IMAP4_SSL("imap.{}".format(domain))
    imap.login(login, password)
    return imap


def reading_emails():
    mail_interior = log()
    status, messages = mail_interior.select('INBOX')
    how_many = 20
    z = 0
    mail_nb = int(messages[0])

    for i in range(mail_nb, mail_nb-how_many, -1):
        res, msg = mail_interior.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    try:
                        subject = subject.decode()
                    except UnicodeDecodeError:
                        pass
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
                                try:
                                    if not os.path.isdir(subject):
                                        reg_expr = re.compile(r'\w+')
                                        subject = str(reg_expr.findall(subject))
                                        subject = subject.replace(",", "").replace("'", "").replace('[', "").replace(']', "")
                                        try:
                                            os.mkdir(subject)
                                        except FileExistsError:
                                            subject = subject + ' ({})'.format(str(z))
                                            z += 1
                                            os.mkdir(subject)
                                    filepath = os.path.join(subject, filename)
                                except UnicodeDecodeError:
                                    pass
                                try:
                                    open(filepath, "wb").write(part.get_payload(decode=True))
                                except OSError:
                                    pass
                else:
                    content_type = msg.get_content_type()
                    try:
                        body = msg.get_payload(decode=True).decode()     #here is the problem
                        if content_type == "text/plain":
                            print(body)
                    except UnicodeDecodeError:
                        pass
                if content_type == "text/html":
                    try:
                        if not os.path.isdir(subject):
                            reg_expr = re.compile(r'\w+')
                            subject = str(reg_expr.findall(subject))
                            subject = subject.replace(",", "").replace("'", "").replace('[', "").replace(']', "")
                            try:
                                os.mkdir(subject)
                            except FileExistsError:
                                subject = subject + ' ({})'.format(str(z))
                                z += 1
                                os.mkdir(subject)
                        filename = f"{subject[:50]}.html"
                        filepath = os.path.join(subject, filename)
                        try:
                            open(filepath, "w").write(body)
                        except (UnicodeEncodeError, FileNotFoundError):
                            pass
                    except UnicodeDecodeError:
                        pass
    mail_interior.close()
    mail_interior.logout()


if __name__ == "__main__":
    reading_emails()