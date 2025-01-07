''' inform'''
import tkinter as tk
from tkinter import ttk
from window.window_one import frame_four, frame_three, window_one
from controller.inform_con import open_inform_open_window, open_inform_edit_window, \
    open_inf_delete_window, close_inform_open_window, submit_inform_form, \
    close_inform_edit_window, submit_edit_inform_form, close_inform_delete_window, \
    submit_delete_inf_form


table_two = ttk.Treeview(frame_three, columns=("Id", "Age", "Email"),
                         show='headings', height=6)
table_two.column('Id', width=50)
table_two.column('Age', width=50)
table_two.column('Email', width=150)

table_two.heading('Id', text='Id')
table_two.heading('Age', text='Age')
table_two.heading('Email', text='Email')

table_two.grid()

create_but_two = ttk.Button(frame_four, text='Создать запись',
                            command=lambda: open_inform_open_window(window_two_two))
apd_but_two = ttk.Button(frame_four, text='Изменить данные',
                         command=lambda: open_inform_edit_window(window_three_two))
del_but_two = ttk.Button(frame_four, text='Удалить записи',
                         command=lambda: open_inf_delete_window(window_four_two))

create_but_two.grid(row=0, column=0, padx=20, pady=10)
apd_but_two.grid(row=1, column=0, padx=20, pady=10)
del_but_two.grid(row=2, column=0, padx=20, pady=10)


# СОздание второго окна, для создания записи в бд, таблица Inform


window_two_two = tk.Toplevel(window_one)
window_two_two.title('Создание записи Inform')
window_two_two.geometry('300x300')
window_two_two.resizable(False, False)
window_two_two.withdraw()
window_two_two.protocol('WM_DELETE_WINDOW', lambda: close_inform_open_window(window_two_two))

frame_create_info = tk.Frame(window_two_two, width=300, height=300)
frame_create_info.grid(row=0, column=0)

app_age_text = ttk.Label(frame_create_info, text='Добавить age')
app_age_form = ttk.Entry(frame_create_info, justify='left')
app_email_text = ttk.Label(frame_create_info, text='Добавить email')
app_email_form = ttk.Entry(frame_create_info, justify='left')
create_but_infowm = ttk.Button(frame_create_info, text='Создать',
                               command=lambda:
                               submit_inform_form(app_age_form.get(), app_email_form.get()))

app_age_text.grid(row=0, column=0, padx=10, pady=10)
app_age_form.grid(row=0, column=1, padx=10, pady=10)
app_email_text.grid(row=1, column=0, padx=10, pady=10)
app_email_form.grid(row=1, column=1, padx=10, pady=10)
create_but_infowm.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# создание третьего окна, для изменения записи в  таблице - inform


window_three_two = tk.Toplevel(window_one)
window_three_two.title('Редактирование записи Infowm')
window_three_two.geometry('300x300')
window_three_two.resizable(False, False)
window_three_two.withdraw()
window_three_two.protocol('WM_DELETE_WINDOW',
                          lambda: close_inform_edit_window(window_three_two))

old_age = ttk.Label(window_three_two, text='Старый age')
old_age_form = ttk.Entry(window_three_two, justify='left')
new_age = ttk.Label(window_three_two, text='Новый age')
new_age_form = ttk.Entry(window_three_two, justify='left')
old_email = ttk.Label(window_three_two, text='Старый emial')
old_email_form = ttk.Entry(window_three_two, justify='left')
new_email = ttk.Label(window_three_two, text='Новый email')
new_email_form = ttk.Entry(window_three_two, justify='left')
but_app_inf = ttk.Button(window_three_two, text='Изменить данные',
                         command=lambda:
                         submit_edit_inform_form(old_age_form.get(), new_age_form.get(),
                                                 old_email_form.get(), new_email_form.get()))

old_age.grid(row=0, column=0, padx=10, pady=10)
old_age_form.grid(row=0, column=1, padx=10, pady=10)
new_age.grid(row=1, column=0, padx=10, pady=10)
new_age_form.grid(row=1, column=1, padx=10, pady=10)
old_email.grid(row=2, column=0, padx=10, pady=10)
old_email_form.grid(row=2, column=1, padx=10, pady=10)
new_email.grid(row=3, column=0, padx=10, pady=10)
new_email_form.grid(row=3, column=1, padx=10, pady=10)
but_app_inf.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Создание чевертого окна, для удаления данных таблица - Infown


window_four_two = tk.Toplevel(window_one)
window_four_two.title('Удаление данных Inform')
window_four_two.geometry('450x100')
window_four_two.resizable(False, False)
window_four_two.withdraw()
window_four_two.protocol('WM_DELETE_WINDOW',
                         lambda: close_inform_delete_window(window_four_two))

email_del = ttk.Label(window_four_two,
                      text='Введите email, который необходимо удалить')
email_del_form = ttk.Entry(window_four_two, justify='left')
email_del_but = ttk.Button(window_four_two, text='Удалить email',
                           command=lambda: submit_delete_inf_form(email_del_form.get()))

email_del.grid(row=0, column=0, padx=10, pady=10)
email_del_form.grid(row=0, column=1, padx=10, pady=10)
email_del_but.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
