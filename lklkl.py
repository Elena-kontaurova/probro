''' kjkk'''
import tkinter as tk
from tkinter import ttk, Button, messagebox
from connect import Users, db


def dow_dan():
    ''' данные бд'''
    us_list = Users.select()
    for user in us_list:
        table.insert('', 'end', values=(user.id, user.username, user.password))


def window_two_show():
    ''' открыть второе окно'''
    window_two.deiconify()


def window_three_show():
    ''' открыть третье окно'''
    window_three.deiconify()


def on_close_second_window():
    ''' закрыть второе окно'''
    window_two.withdraw()


def on_close_three_window():
    ''' закрыть третье окно'''
    window_three.withdraw()


def form_submit():
    ''' создание записи в бд'''
    username = app_username_form.get()
    password = app_password_form.get()

    Users.create(username=username, password=password)
    messagebox.showinfo("baaazaaa", "Данные добавлены успешно!")
    app_username_form.delete(0, tk.END)  # Очистка поля ввода имени
    app_password_form.delete(0, tk.END)  # Очистка поля ввода возраста


def form_redac():
    ''' редактирование записи в бд'''
    print('good')


# создание главноего окна


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
                 command=window_three_show)
apd_but = Button(frame_two, text='Удалить запись',
                 command=window_two_show)

gerate_but.grid(row=0, column=0)
del_but.grid(row=0, column=1)
apd_but.grid(row=0, column=2)


# создание второго окна, для создания записи в бд

window_two = tk.Tk()
window_two.title('Создание записи')
window_two.geometry('300x300')
window_two.resizable(False, False)
window_two.withdraw()
window_two.protocol('WM_DELETE_WINDOW', on_close_second_window)


frame_create = tk.Frame(window_two, width=300, height=300)
frame_create.grid(row=0, column=0)


app_username_text = ttk.Label(frame_create, text='Добавить username')
app_username_form = ttk.Entry(frame_create, justify='left')
app_password_text = ttk.Label(frame_create, text='Добавить password')
app_password_form = ttk.Entry(frame_create, justify='left')
create_but = ttk.Button(frame_create, text='Создать',
                        command=form_submit)

app_username_text.grid(row=0, column=0, padx=10, pady=10)
app_username_form.grid(row=0, column=1, padx=10, pady=10)
app_password_text.grid(row=1, column=0, padx=10, pady=10)
app_password_form.grid(row=1, column=1, padx=10, pady=10)
create_but.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# создание третьего окна для изменения записи


window_three = tk.Tk()
window_three.title('Редактирование записи')
window_three.geometry('300x300')
window_three.resizable(False, False)
window_three.withdraw()
window_three.protocol('WM_DELETE_WINDOW', on_close_three_window)

old_user = ttk.Label(window_three, text='Старый username')
old_user_form = ttk.Entry(window_three, justify='left')
new_user = ttk.Label(window_three, text='Новый username')
new_user_form = ttk.Entry(window_three, justify='left')
old_pass = ttk.Label(window_three, text='Старый password')
old_pas_form = ttk.Entry(window_three, justify='left')
new_pas = ttk.Label(window_three, text='Новый password')
new_pass_form = ttk.Entry(window_three, justify='left')
but_app = ttk.Button(window_three, text='Изменить данные',
                     command=form_redac)

old_user.grid(row=0, column=0, padx=10, pady=10)
old_user_form.grid(row=0, column=1, padx=10, pady=10)
new_user.grid(row=1, column=0, padx=10, pady=10)
new_user_form.grid(row=1, column=1, padx=10, pady=10)
old_pass.grid(row=2, column=0, padx=10, pady=10)
old_pas_form.grid(row=2, column=1, padx=10, pady=10)
new_pas.grid(row=3, column=0, padx=10, pady=10)
new_pass_form.grid(row=3, column=1, padx=10, pady=10)
but_app.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# конец прог


def on_close_main_window():
    ''' прерывание программы, при закрытии основного окна'''
    if window_two is not None and window_two.winfo_exists():
        window_two.destroy()
    if window_three is not None and window_three.winfo_exists():
        window_three.destroy()
    window_one.destroy()


db.connect()
dow_dan()
db.close()

window_one.protocol('WM_DELETE_WINDOW', on_close_main_window)

window_one.mainloop()
