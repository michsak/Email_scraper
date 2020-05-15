from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os


def about_button():
    if os.path.isfile("about.txt"):
        path = os.path.join("about.txt")
        os.system(path)
    else:
        os.chdir("./about_contact_help")
        path = os.path.join("about.txt")
        os.system(path)


def contact_button():
    if os.path.isfile("contact.txt"):
        path = os.path.join("contact.txt")
        os.system(path)
    else:
        os.chdir("./about_contact_help")
        path = os.path.join("contact.txt")
        os.system(path)


def help_button():
    if os.path.isfile("help.txt"):
        path = os.path.join("help.txt")
        os.system(path)
    else:
        os.chdir("./about_contact_help")
        path = os.path.join("help.txt")
        os.system(path)
    
    
def click_file_but(var, text):
    var.append(text)
    for j in var:
        if var.count(j) > 1:
            var.remove(j)
    return var


def search_filepath(var):
    filename = filedialog.askdirectory()
    var.append(filename)
    return var


def pres_but(button):
    pres_col = 'thistle3'
    if button['state'] == NORMAL:
        button['state'] == DISABLED
        button.config(relief=SUNKEN, bg=pres_col)


def click_logpas(new, var_1, var_2, var_3):
    new.append(var_1)
    new.append(var_2)
    new.append(var_3)
    return new


def mapping(time):
    dict_1 = {"1 day": "1", "2 days": "2", "3 days": "3", "4 days": "4", "5 days": "5", "6 days": "6", "1 week": "7", "2 weeks": "14", "3 weeks": "21", "4 weeks": "28"}
    for key, value in dict_1.items():
        if time == key:
            time = value
    return time


def file_buttons(root):
    var = []
    file_format = ['pdf', 'zip', 'doc', 'docx', 'jpg', 'jpeg', 'gif', 'png', 'pptx', 'xlsx', 'rar', 'avi']
    bg_color = 'floral white'
    fg_color = 'black'
    font = 'Normal 8'
    pres_col = 'thistle3'
    padx = 8
    pady = 9
    width = 4
    frame = Frame(root)
    frame.pack(side=LEFT)
    button_1 = Button(root, text=file_format[0], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[0]), pres_but(button_1)])
    button_1.place(x=109, y=91)
    button_2 = Button(root, text=file_format[1], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[1]), pres_but(button_2)])
    button_2.place(x=163, y=91)
    button_3 = Button(root, text=file_format[2], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[2]), pres_but(button_3)])
    button_3.place(x=216, y=91)
    button_4 = Button(root, text=file_format[3], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[3]), pres_but(button_4)])
    button_4.place(x=269, y=91)
    button_5 = Button(root, text=file_format[4], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[4]), pres_but(button_5)])
    button_5.place(x=109, y=138)
    button_6 = Button(root, text=file_format[5], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[5]), pres_but(button_6)])
    button_6.place(x=163, y=138)
    button_7 = Button(root, text=file_format[6], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[6]), pres_but(button_7)])
    button_7.place(x=216, y=138)
    button_8 = Button(root, text=file_format[7], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[7]), pres_but(button_8)])
    button_8.place(x=269, y=138)
    button_9 = Button(root, text=file_format[8], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[8]), pres_but(button_9)])
    button_9.place(x=109, y=185)
    button_10 = Button(root, text=file_format[9], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[9]), pres_but(button_10)])
    button_10.place(x=163, y=185)
    button_11 = Button(root, text=file_format[10], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[10]), pres_but(button_11)])
    button_11.place(x=216, y=185)
    button_12 = Button(root, text=file_format[11], activebackground=pres_col, fg=fg_color, font=font, width=width, bg=bg_color, padx=padx, pady=pady, command=lambda: [click_file_but(var, file_format[11]), pres_but(button_12)])
    button_12.place(x=269, y=185)
    return var


def menu(root):
    menu = Menu(root)
    root.config(menu=menu)
    menu.add_command(label='About', command=lambda: about_button())
    menu.add_command(label='Contact', command=lambda: contact_button())
    menu.add_command(label='Help', command=lambda: help_button())


def input_text_field(root, new_list):
    bg_color = 'lavender blush'
    empty_place = Label(root, bg=bg_color)
    empty_place.place(x=0, y=0)
    log = Label(root, text='Login', bg=bg_color)
    log.place(x=48, y=20)
    pas = Label(root, text='Password', bg=bg_color)
    pas.place(x=40, y=41)
    date = Label(root, text='Period of time', bg=bg_color)
    date.place(x=23, y=63)
    input_1 = Entry(root, width=35, borderwidth=1, fg='black')
    input_1.place(x=109, y=20)
    input_2 = Entry(root, width=35, borderwidth=1, fg='black', show='*')
    input_2.place(x=109, y=41)
    choice_box = ttk.Combobox(root, values=["1 day", "2 days", "3 days", "4 days", "5 days", "6 days", "1 week", "2 weeks", "3 weeks", "4 weeks"],
                              state="readonly", width=34, style="TEntry")
    choice_box.place(x=110, y=63)
    start_button = Button(root, text='START', fg='black', bg='chartreuse3', borderwidth=7, activebackground='forest green', width=8, height=1, padx=5, pady=5, command=lambda: [click_logpas(new_list, input_1.get(), input_2.get(), choice_box.get()), root.quit()])
    start_button.place(x=174, y=280)
    browse_button = Button(root, text='Browse directory', fg='black', bg='floral white', borderwidth=4, activebackground='thistle3', width=13, padx=3, pady=3, command=lambda: search_filepath(new_list))
    browse_button.place(x=159, y=230)
    return new_list


def graphic_interface():
    root = Tk()
    root.title("Email scraper")
    root.configure(background="lavender blush")
    root.minsize(400, 400)
    root.resizable(0, 0)
    new_list = []

    files_formats = file_buttons(root)
    menu(root)
    log_pass_place_time = input_text_field(root, new_list)
    root.mainloop()

    if (len(log_pass_place_time) >= 3 and (log_pass_place_time[0] != '' and log_pass_place_time[1] != '' and
                                          log_pass_place_time[2] != '' and log_pass_place_time[3] != '')):
        place = log_pass_place_time[0]
        login = log_pass_place_time[1]
        password = log_pass_place_time[2]
        per_of_time = mapping(log_pass_place_time[3])
        return login, password, place, per_of_time, tuple(files_formats)
