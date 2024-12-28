''' tkinter + bd
Суть: окно 500х500, размер менять нельзя, отображается таблица с данными из БД.
Табличку сделайте users с полями: id, username, password
'''
import tkinter as Tk
from tkinter import ttk
from connect import Users, db


def dow_dan():
    ''' iuiu'''
    us_list = Users.select()
    for user in us_list:
        table.insert('', 'end', values=(user.id, user.username, user.password))


root = Tk.Tk()
root.title('пупупууу')
root.geometry('500x500')
root.resizable(False, False)

table = ttk.Treeview(root, columns=("ID", 'Username', "Password"),
                     show='headings')
table.column('ID', width=50)
table.column('Username', width=100)
table.column('Password', width=100)

table.heading('ID', text='ID')
table.heading('Username', text='Username')
table.heading('Password', text='Password')

table.pack(expand=True, fill='both')

db.connect()
dow_dan()
db.close()
root.mainloop()
