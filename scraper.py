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


def fromwho_subject(el_1, el_2):
    el_1 = "Subject: " + str(el_1) + "\n"
    el_2 = "From: " + str(el_2) + "\n"
    txt = el_1 + el_2
    return txt


def reading_emails():
    mail_interior = log()
    status, messages = mail_interior.select('INBOX')
    how_many = 10
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
                        path = os.path.join(subject, "body.txt")
                        body_init = fromwho_subject(subject, msg.get("From"))
                        open(path, "w").write(body_init)
                except UnicodeDecodeError:
                    pass

                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        print(part.get_payload(decode=True))
                        try:
                            body = part.get_payload(decode=True).decode("utf-8")    #AND HERE, ACUTALLY GET_PAYLOAD IS THE PROBLEM
                        except:
                            print("error")
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            path = os.path.join(subject, "body.txt")
                            open(path, "a", encoding='utf-8').write(body)
                        elif "attachment" in content_disposition:
                            filename = part.get_filename()
                            if filename:
                                try:
                                    filepath = os.path.join(subject, filename)
                                except UnicodeDecodeError:
                                    pass
                                try:
                                    open(filepath, "wb").write(part.get_payload(decode=True))
                                except OSError:
                                    pass
                else:
                    content_type = msg.get_content_type()
                    #print(msg.get_payload(decode=True).decode("utf-8")) #here html_scraper needed!!!
                    try:
                        body = msg.get_payload(decode=True).decode("utf-8")
                        if content_type == "text/plain":
                            path = os.path.join(subject, "body.txt")
                            open(path, "a", encoding='utf-8').write(body)
                    except UnicodeDecodeError:
                        #print("error")
                        pass
                if content_type == "text/html":
                    try:
                        filename = "network_site.html"
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
