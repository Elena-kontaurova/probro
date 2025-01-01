''' kjkk'''
import tkinter as tk
from tkinter import ttk, Button
from connect import Users, db


def dow_dan():
    ''' данные бд'''
    us_list = Users.select()
    for user in us_list:
        table.insert('', 'end', values=(user.id, user.username, user.password))


def window_two_show():
    ''' открыть второе окно'''
    window_two.deiconify()


def on_close_second_window():
    ''' закрыть второе окно'''
    window_two.withdraw()


window_one = tk.Tk()
window_one.geometry('500x500')
window_one.resizable(False, False)

frame_one = tk.Frame(window_one, width=500, height=250, bg='blue')
frame_two = tk.Frame(window_one, width=500, height=250, bg='green')

frame_one.grid(row=0, column=0, columnspan=2)
frame_two.grid(row=1, column=0, columnspan=2)


table = ttk.Treeview(frame_one, columns=("ID", 'Username', "Password"),
                     show='headings')
table.column('ID', width=100)
table.column('Username', width=200)
table.column('Password', width=200)

table.heading('ID', text='ID')
table.heading('Username', text='Username')
table.heading('Password', text='Password')

table.grid(row=0, column=0, columnspan=2)

gerate_but = Button(frame_two, text='Создать запись',
                    command=window_two_show)
del_but = Button(frame_two, text='Изменить запись',
                 command=window_two_show)
apd_but = Button(frame_two, text='Удалить запись',
                 command=window_two_show)

gerate_but.grid(row=0, column=0)
del_but.grid(row=0, column=1)
apd_but.grid(row=0, column=2)


window_two = tk.Tk()
window_two.title('Создание записи')
window_two.geometry('250x250')
window_two.resizable(False, False)
window_two.withdraw()
window_two.protocol('WM_DELETE_WINDOW', on_close_second_window)

app_username_text = ttk.Label(window_two, text='Добавить username')
app_username_form = ttk.Label(window_two, text='Добавить')
app_password_text = ttk.Label(window_two, text='Добавить password')
app_password_form = ttk.Label(window_two, text='Добавить')
but_create = ttk.Label(window_two, text='Добавить')
create_but = ttk.Button(window_two, text='Создать',
                        command=on_close_second_window)

app_username_text.grid(row=0, column=0)
app_username_form.grid(row=0, column=1)
app_password_text.grid(row=1, column=0)
app_password_form.grid(row=1, column=1)
create_but.grid(row=2, column=0, columnspan=2)


def on_close_main_window():
    ''' прерывание программы, при закрытии основного окна'''
    if window_two is not None and window_two.winfo_exists():
        window_two.destroy()
    window_one.destroy()


db.connect()
dow_dan()
db.close()

window_one.protocol('WM_DELETE_WINDOW', on_close_main_window)

window_one.mainloop()
