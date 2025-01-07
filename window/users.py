''' users '''
import tkinter as tk
from tkinter import ttk, Button
from window.window_one import frame_one, frame_two, window_one
from controller.users_con import open_user_window, open_user_edit_window, \
    open_user_delete_window, close_user_window, submit_user_form, \
    close_user_edit_window_con, submit_edit_user_form, close_user_delete_window, \
    submit_delete_user_form

table = ttk.Treeview(frame_one, columns=("ID", 'Username', "Password"),
                     show='headings', height=6)
table.column('ID', width=50)
table.column('Username', width=100)
table.column('Password', width=100)

table.heading('ID', text='ID')
table.heading('Username', text='Username')
table.heading('Password', text='Password')

table.grid()

gerate_but = Button(frame_two, text='Создать запись',
                    command=lambda: open_user_window(window_two))
del_but = Button(frame_two, text='Изменить запись',
                 command=lambda: open_user_edit_window(window_three))
apd_but = Button(frame_two, text='Удалить запись',
                 command=lambda: open_user_delete_window(window_four))


gerate_but.grid(row=0, column=0, padx=20, pady=10)
del_but.grid(row=1, column=0, padx=20, pady=10)
apd_but.grid(row=2, column=0, padx=20, pady=10)


# Окно Users для создания записи в таблице


window_two = tk.Toplevel(window_one)
window_two.title('Создание записи Users')
window_two.geometry('300x300')
window_two.resizable(False, False)
window_two.withdraw()
window_two.protocol('WM_DELETE_WINDOW', lambda: close_user_window(window_two))

frame_create = tk.Frame(window_two, width=300, height=300)
frame_create.grid(row=0, column=0)

app_username_text = ttk.Label(frame_create, text='Добавить username')
app_username_form = ttk.Entry(frame_create, justify='left')
app_password_text = ttk.Label(frame_create, text='Добавить password')
app_password_form = ttk.Entry(frame_create, justify='left')
create_but = ttk.Button(frame_create, text='Создать',
                        command=lambda:
                        submit_user_form(app_username_form.get(), app_password_form.get()))

app_username_text.grid(row=0, column=0, padx=10, pady=10)
app_username_form.grid(row=0, column=1, padx=10, pady=10)
app_password_text.grid(row=1, column=0, padx=10, pady=10)
app_password_form.grid(row=1, column=1, padx=10, pady=10)
create_but.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# Окно Users для редактирования записи в таблице


window_three = tk.Toplevel(window_one)
window_three.title('Редактирование записи Users')
window_three.geometry('300x300')
window_three.resizable(False, False)
window_three.withdraw()
window_three.protocol('WM_DELETE_WINDOW', lambda: close_user_edit_window_con(window_three))

old_user = ttk.Label(window_three, text='Старый username')
old_user_form = ttk.Entry(window_three, justify='left')
new_user = ttk.Label(window_three, text='Новый username')
new_user_form = ttk.Entry(window_three, justify='left')
old_pass = ttk.Label(window_three, text='Старый password')
old_pas_form = ttk.Entry(window_three, justify='left')
new_pas = ttk.Label(window_three, text='Новый password')
new_pass_form = ttk.Entry(window_three, justify='left')
but_app = ttk.Button(window_three, text='Изменить данные',
                     command=lambda:
                     submit_edit_user_form(old_user_form.get(), old_pas_form.get(),
                                           new_user_form.get(), new_pass_form.get()))

old_user.grid(row=0, column=0, padx=10, pady=10)
old_user_form.grid(row=0, column=1, padx=10, pady=10)
new_user.grid(row=1, column=0, padx=10, pady=10)
new_user_form.grid(row=1, column=1, padx=10, pady=10)
old_pass.grid(row=2, column=0, padx=10, pady=10)
old_pas_form.grid(row=2, column=1, padx=10, pady=10)
new_pas.grid(row=3, column=0, padx=10, pady=10)
new_pass_form.grid(row=3, column=1, padx=10, pady=10)
but_app.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Окно Users для удаления записи в таблице


window_four = tk.Toplevel(window_one)
window_four.title('Удаление данных Users')
window_four.geometry('450x100')
window_four.resizable(False, False)
window_four.withdraw()
window_four.protocol('WM_DELETE_WINDOW', lambda: close_user_delete_window(window_four))


user_del = ttk.Label(window_four,
                     text='Введите username, который необходимо удалить')
user_del_form = ttk.Entry(window_four, justify='left')
user_del_but = ttk.Button(window_four, text='Удалить username',
                          command=lambda:
                          submit_delete_user_form(user_del_form.get()))

user_del.grid(row=0, column=0, padx=10, pady=10)
user_del_form.grid(row=0, column=1, padx=10, pady=10)
user_del_but.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
