''' education'''
import tkinter as tk
from tkinter import ttk
from window.window_one import frame_five, frame_six, window_one
from controller.educa_con import open_educa_open_window, open_educa_edit_window, \
    open_edu_delete_window, close_educ_open_window, close_educ_edit_window, \
    close_educ_delete_window, submit_educa_form, submit_edit_educa_form, \
    submit_delete_educ_form

table_three = ttk.Treeview(frame_five,
                           columns=('Id', 'Group', 'Specialization'),
                           show='headings', height=6)
table_three.column('Id', width=50)
table_three.column('Group', width=50)
table_three.column('Specialization', width=150)

table_three.heading('Id', text='Id')
table_three.heading('Group', text='Group')
table_three.heading('Specialization', text='Specialization')
table_three.grid()

create_but_three = ttk.Button(frame_six, text='Создать запись',
                              command=lambda: open_educa_open_window(window_two_three))
apd_but_three = ttk.Button(frame_six, text='Изменить данные',
                           command=lambda: open_educa_edit_window(window_three_three))
del_but_three = ttk.Button(frame_six, text='Удалить записи',
                           command=lambda: open_edu_delete_window(window_four_three))

create_but_three.grid(row=0, column=0, padx=20, pady=10)
apd_but_three.grid(row=1, column=0, padx=20, pady=10)
del_but_three.grid(row=2, column=0, padx=20, pady=10)


# создание второго окна, для создания записи в таблице Education


window_two_three = tk.Toplevel(window_one)
window_two_three.title('Создание записи Education')
window_two_three.geometry('300x300')
window_two_three.resizable(False, False)
window_two_three.withdraw()
window_two_three.protocol('WM_DELETE_WINDOW',
                          lambda: close_educ_open_window(window_two_three))

frame_create_edu = tk.Frame(window_two_three, width=300, height=300)
frame_create_edu.grid(row=0, column=0)

app_gr_text = ttk.Label(frame_create_edu, text='Добавить group')
app_gr_form = ttk.Entry(frame_create_edu, justify='left')
app_spe_text = ttk.Label(frame_create_edu, text='Добавить specialization')
app_spe_form = ttk.Entry(frame_create_edu, justify='left')
create_but_edu = ttk.Button(frame_create_edu, text='Создать',
                            command=lambda:
                            submit_educa_form(app_gr_form.get(), app_spe_form.get()))

app_gr_text.grid(row=0, column=0, padx=10, pady=10)
app_gr_form.grid(row=0, column=1, padx=10, pady=10)
app_spe_text.grid(row=1, column=0, padx=10, pady=10)
app_spe_form.grid(row=1, column=1, padx=10, pady=10)
create_but_edu.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# Создание третьего окна, для изменения записи в таблице - Education

window_three_three = tk.Toplevel(window_one)
window_three_three.title('Редактирование записи Education')
window_three_three.geometry('300x300')
window_three_three.resizable(False, False)
window_three_three.withdraw()
window_three_three.protocol('WM_DELETE_WINDOW',
                            lambda: close_educ_edit_window(window_three_three))

old_gro = ttk.Label(window_three_three, text='Старый group')
old_gro_form = ttk.Entry(window_three_three, justify='left')
new_gro = ttk.Label(window_three_three, text='Новый group')
new_gro_form = ttk.Entry(window_three_three, justify='left')
old_spe = ttk.Label(window_three_three, text='Старый specialization')
old_spe_form = ttk.Entry(window_three_three, justify='left')
new_spe = ttk.Label(window_three_three, text='Новый specialization')
new_spe_form = ttk.Entry(window_three_three, justify='left')
but_spe_edu = ttk.Button(window_three_three, text='Изменить данные',
                         command=lambda:
                         submit_edit_educa_form(old_gro_form.get(), old_spe_form.get(),
                                                new_gro_form.get(), new_spe_form.get()))

old_gro.grid(row=0, column=0, padx=10, pady=10)
old_gro_form.grid(row=0, column=1, padx=10, pady=10)
new_gro.grid(row=1, column=0, padx=10, pady=10)
new_gro_form.grid(row=1, column=1, padx=10, pady=10)
old_spe.grid(row=2, column=0, padx=10, pady=10)
old_spe_form.grid(row=2, column=1, padx=10, pady=10)
new_spe.grid(row=3, column=0, padx=10, pady=10)
new_spe_form.grid(row=3, column=1, padx=10, pady=10)
but_spe_edu.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Создание чевертого окна, для удаления данных таблица - Education


window_four_three = tk.Toplevel(window_one)
window_four_three.title('Удаление данных Education')
window_four_three.geometry('460x150')
window_four_three.resizable(False, False)
window_four_three.withdraw()
window_four_three.protocol('WM_DELETE_WINDOW',
                           lambda: close_educ_delete_window(window_four_three))

gro_del = ttk.Label(window_four_three,
                    text='Введите group, который необходимо удалить')
gro_del_form = ttk.Entry(window_four_three, justify='left')
spe_del = ttk.Label(window_four_three,
                    text='Введите specialization, который необходимо удалить')
spe_del_form = ttk.Entry(window_four_three, justify='left')
email_del_but = ttk.Button(window_four_three, text='Удалить',
                           command=lambda:
                           submit_delete_educ_form(gro_del_form.get(), spe_del_form.get()))

gro_del.grid(row=0, column=0, padx=10, pady=10)
gro_del_form.grid(row=0, column=1, padx=10, pady=10)
spe_del.grid(row=1, column=0, padx=10, pady=10)
spe_del_form.grid(row=1, column=1, padx=10, pady=10)
email_del_but.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
