from tkinter import *


def click_file_but(var, text):
    var.append(text)
    return var


def click_logpas(new, var_1, var_2):
    new.append(var_1)
    new.append(var_2)
    return new


def file_buttons(root):
    var = []
    file_format = ['pdf', 'zip', 'mp3', 'mp4', 'txt', 'jpeg', 'jpg', 'png']
    frame = Frame(root)
    frame.pack(side=BOTTOM)
    button_1 = Button(frame, text=file_format[0], fg='blue', padx=15, pady=10, command=lambda: click_file_but(var, file_format[0]))
    button_1.pack(side=LEFT)
    button_2 = Button(frame, text=file_format[1], fg='blue', padx=15, pady=10, command=lambda: click_file_but(var, file_format[1]))
    button_2.pack(side=LEFT)
    button_3 = Button(frame, text=file_format[2], fg='blue', padx=15, pady=10, command=lambda: click_file_but(var, file_format[2]))
    button_3.pack(side=LEFT)
    button_4 = Button(frame, text=file_format[3], fg='blue', padx=15, pady=10, command=lambda: click_file_but(var, file_format[3]))
    button_4.pack(side=LEFT)
    button_5 = Button(frame, text=file_format[4], fg='blue', padx=15, pady=10, command=lambda: click_file_but(var, file_format[4]))
    button_5.pack(side=LEFT)
    button_6 = Button(frame, text=file_format[5], fg='blue', padx=15, pady=10, command=lambda: click_file_but(var, file_format[5]))
    button_6.pack(side=LEFT)
    button_7 = Button(frame, text=file_format[6], fg='blue', padx=15, pady=10, command=lambda: click_file_but(var, file_format[6]))
    button_7.pack(side=LEFT)
    button_8 = Button(frame, text=file_format[7], fg='blue', padx=15, pady=10, command=lambda: click_file_but(var, file_format[7]))
    button_8.pack(side=LEFT)
    return var


def menu(root):
    menu = Menu(root)
    root.config(menu=menu)
    menu.add_cascade(label='About')
    menu.add_cascade(label='Contact')
    menu.add_cascade(label='Help')


def input_text_field(root):
    new_list = []
    input_1 = Entry(root, width=40, borderwidth=2, fg='purple')
    input_1.pack()
    input_2 = Entry(root, width=40, borderwidth=2, fg='purple')
    input_2.pack()
    button = Button(root, text='Submit', fg='blue', padx=15, pady=1, command=lambda: click_logpas(new_list, input_1.get(), input_2.get()))
    button.pack()
    return new_list


def text(root):
    t = Label(root, height=2, width=75, fg='blue', bg='gray55', text="Enter your login and password:")
    t.pack()


def graphic_interface():
    root = Tk()
    root.title("Email scraper")
    root.configure(background="ivory4")
    root.minsize(500, 400)
    root.resizable(0, 0)


    files_formats = file_buttons(root)
    menu(root)
    text(root)
    log_pass = input_text_field(root)


    root.mainloop()

    #print(files_formats)

    if len(log_pass) >= 2:
        login = log_pass[0]
        password = log_pass[1]

graphic_interface()
