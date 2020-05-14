import imaplib
import email
from email.header import decode_header
import os
import re
import traceback
import datetime


def log():
    print("Write down your login and password\nLogin:")
    login = input()
    print("Pasword:")
    password = input()

    reg_exp = re.compile(r'@\w+.\w+')
    domain = reg_exp.findall(login)
    domain = str(domain).replace('@', "").replace('[', "").replace(']', "").replace("'", "")

    imap = imaplib.IMAP4_SSL("imap.{}".format(domain))
    imap.login(login, password)
    return imap


def fromwho_subject(el_1, el_2):
    el_1 = "Subject: " + str(el_1) + "\n"
    el_2 = "From: " + str(el_2) + "\n"
    txt = el_1 + el_2
    return txt


def extensions():
    print('Choose the file extension:\npdf\nzip\ntxt\nmp3')
    ext = "." + str(input()).lower()
    return ext


def reading_emails(extension, my_path, delay):
    os.chdir(my_path)
    mail_interior = log()
    status, messages = mail_interior.select('INBOX')
    mail_nb = int(messages[0])
    mail_date = []
    final_mail_nb = 0
    z = 1

    for i in range(mail_nb, 0, -1):
        res, msg = mail_interior.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                try:
                    today = datetime.datetime.today()
                    today = today.strftime("%d %m %Y")
                    today = datetime.datetime.strptime(today, '%d %m %Y')
                    reg_exp = re.compile(r'(Date: (.*?)\d\d\d\d)')
                    date = reg_exp.findall(str(msg))
                    for x, y in date:
                        mail_date.append(x)
                        str_searched_date = str(mail_date)[-13:-2]
                    str_searched_date = datetime.datetime.strptime(str_searched_date, '%d %b %Y')
                    nb_days_str = str(today-str_searched_date)
                    reg_exp_2 = re.compile(r'(\d+)')
                    res = reg_exp_2.search(nb_days_str)
                    nb_days_int = int(res.group())  #NUMBER OF DAYS TO LOOP
                    final_mail_nb += 1
                except (KeyError, TypeError):
                    pass
        if nb_days_int > delay:
            break

    for i in range(mail_nb, mail_nb-final_mail_nb, -1):
        a = 0
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
                for part in msg.walk():
                    content_disposition = str(part.get("Content-Disposition"))
                    if "attachment" in content_disposition:
                        filename = part.get_filename()
                        if filename.endswith(extension):
                            try:
                                if not os.path.isdir(subject):
                                    reg_expr = re.compile(r'\w+')
                                    subject = str(reg_expr.findall(subject))
                                    subject = subject[2:-2].replace(",", "").replace(" ", "_").replace("'", "")
                                    try:
                                        os.mkdir(subject)
                                    except FileExistsError:
                                        subject = subject + ' ({})'.format(str(z))
                                        z += 1
                                        os.mkdir(subject)
                                    path = os.path.join(subject, "Sender and subject.txt")
                                    re_exp = re.compile(r'\<.*?\>')
                                    clear = str(re_exp.findall(msg.get("From")))
                                    clear = clear[3:-3]
                                    body_init = fromwho_subject(subject, clear)
                                    open(path, "w").write(body_init)
                                filepath = os.path.join(subject, filename)
                                open(filepath, "wb").write(part.get_payload(decode=True))
                            except UnicodeDecodeError as e:
                                if a == 0:
                                    error_file = open("error_log.txt", 'a')
                                    error_file.write(traceback.format_exc(e))
                                    error_file.close()
                                    print("error with opening mail {}".format(subject))
                                    a += 1
                                pass
    mail_interior.close()
    mail_interior.logout()


if __name__ == "__main__":
    path = "C:/Users/micha/OneDrive/Documents/Programowanie/Python/Email_scraper"
    delay = 8
    ext = extensions()
    reading_emails(ext, path, delay)
