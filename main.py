''' tkinter + bd
Суть: окно 500х500, размер менять нельзя, отображается таблица с данными из БД.
Табличку сделайте users с полями: id, username, password
'''
import tkinter as Tk
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


window_one = Tk.Tk()
window_one.title('пупупууу')
window_one.geometry('500x500')
window_one.resizable(False, False)


window_two = Tk.Tk()
window_two.title('берерара')
window_two.geometry('500x500')
window_two.resizable(False, False)
window_two.withdraw()
window_two.protocol('WM_DELETE_WINDOW', on_close_second_window)


table = ttk.Treeview(window_one, columns=("ID", 'Username', "Password"),
                     show='headings')
table.column('ID', width=50)
table.column('Username', width=100)
table.column('Password', width=100)

table.heading('ID', text='ID')
table.heading('Username', text='Username')
table.heading('Password', text='Password')

table.pack(expand=True, fill='both')

nestr = Button(text='Работать с данными', command=window_two_show)
nestr.pack(pady=20)


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
