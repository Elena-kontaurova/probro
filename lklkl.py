''' kjkk'''
import tkinter as tk
from tkinter import ttk, Button, messagebox
from connect import Users, Education, Inform, db


#  получение данных из таблиц


def dow_dan():
    ''' данные из таблица users'''
    us_list = Users.select()
    for user in us_list:
        table.insert('', 'end', values=(user.id, user.username, user.password))


def dow_dan_inforn():
    ''' Данные из таблица inforn'''
    inf_list = Inform.select()
    for usess in inf_list:
        table_two.insert('', 'end', values=(usess.id, usess.age, usess.email))


def dow_dan_educa():
    ''' Данные из таблица education'''
    us_list = Education.select()
    for user in us_list:
        table_three.insert('', 'end', values=(user.id, user.group,
                                              user.specialization))


# Открытие окон для создания записи в таблице


def window_two_show():
    ''' открыть создание окно - useres'''
    window_two.deiconify()


def window_two_two_show():
    ''' открыть создание окно - inform'''
    window_two_two.deiconify()


def window_two_three_show():
    ''' открыть создание окно - education'''
    window_two_three.deiconify()


# открытие окон для редактирования записей в таблице


def window_three_show():
    ''' открыть редакт окно - users'''
    window_three.deiconify()


def window_three_two_show():
    ''' открыть редакт окно - inform'''
    window_three_two.deiconify()


def window_three_three_show():
    ''' открыть редакт окно - education'''
    window_three_three.deiconify()


# открытие окон для удаления записией в таблицах


def window_four_show():
    ''' открыть удаление окно - users'''
    window_four.deiconify()


def window_four_two_show():
    ''' открыть удаление окно - inform'''
    window_four_two.deiconify()


def window_four_three_show():
    ''' открыть удаление окно - education'''
    window_four_three.deiconify()


# закрытие окон для создания записей в таблице


def on_close_second_window():
    ''' закрыть создание окно - users'''
    window_two.withdraw()


def on_close_second_two_window():
    ''' закрыть создание окно - inform'''
    window_two_two.withdraw()


def on_close_second_three_window():
    ''' закрыть создание окно - education'''
    window_two_three.withdraw()

# закрытие окон для редактирования записей в таблице


def on_close_three_window():
    ''' закрыть редак окно - users'''
    window_three.withdraw()


def on_close_three_two_window():
    ''' закрыть редак окно - infowm'''
    window_three_two.withdraw()


def on_close_three_three_window():
    ''' закрыть редак окно - education'''
    window_three_three.withdraw()


# Закрытие окон для удаления записей в таблице


def on_close_four_window():
    ''' закрыть удалние окно - users'''
    window_four.withdraw()


def on_close_four_two_window():
    ''' закрыть удаление окно - inform'''
    window_four_two.withdraw()


def on_close_four_three_window():
    ''' закрыть удаление окно - education'''
    window_four_three.withdraw()


# методы для создания записей в таблице


def form_submit():
    ''' создание записи в бд - useres'''
    username = app_username_form.get()
    password = app_password_form.get()

    Users.create(username=username, password=password)
    messagebox.showinfo("baaazaaa", "Данные добавлены успешно!")
    app_username_form.delete(0, tk.END)  # Очистка поля ввода имени
    app_password_form.delete(0, tk.END)  # Очистка поля ввода возраста


def form_submit_two():
    ''' Создание записи в бд - inform'''
    age = app_age_form.get()
    email = app_email_form.get()

    Inform.create(age=age, email=email)
    messagebox.showinfo("baaazaaa", "Данные добавлены успешно!")
    app_age_form.delete(0, tk.END)
    app_email_form.delete(0, tk.END)


def form_submit_three():
    ''' Создание записи в бд - education'''
    group = app_gr_form.get()
    specialization = app_spe_form.get()

    Education.create(group=group, specialization=specialization)
    messagebox.showinfo("baaazaaa", "Данные добавлены успешно!")
    app_gr_form.delete(0, tk.END)
    app_spe_form.delete(0, tk.END)


# методы для редактирования записей в таблице


def form_redac():
    ''' редактирование записи в таблица - users'''
    old_users = old_user_form.get()
    new_users = new_user_form.get()
    old_pas = old_pas_form.get()
    new_pass = new_pass_form.get()

    user = Users.get(Users.username == old_users, Users.password == old_pas)
    user.username = new_users
    user.password = new_pass
    user.save()

    messagebox.showinfo('Baaazaaa', 'Данные успешно обновленны')
    old_user_form.delete(0, tk.END)
    new_user_form.delete(0, tk.END)
    old_pas_form.delete(0, tk.END)
    new_pass_form.delete(0, tk.END)


def form_redac_two():
    ''' редактирование записи в таб - infown'''
    old_agee = old_age_form.get()
    new_agee = new_age_form.get()
    old_emaill = old_email_form.get()
    new_emaill = new_email_form.get()

    ini = Inform.get(Inform.age == old_agee, Inform.email == old_emaill)
    ini.age = new_agee
    ini.email = new_emaill
    ini.save()
    messagebox.showinfo('Baaazaaa', 'Данные успешно обновленны')
    old_age_form.delete(0, tk.END)
    new_age_form.delete(0, tk.END)
    old_email_form.delete(0, tk.END)
    new_email_form.delete(0, tk.END)


def form_redac_three():
    ''' редактирование записи в таб - education'''
    old_group = old_gro_form.get()
    new_group = new_gro_form.get()
    old_speci = old_spe_form.get()
    new_speci = new_spe_form.get()

    edu = Education.get(Education.group == old_group,
                        Education.specialization == old_speci)
    edu.group = new_group
    edu.specialization = new_speci
    edu.save()
    messagebox.showinfo('Baaazaaa', 'Данные успешно обновленны')
    old_gro_form.delete(0, tk.END)
    new_gro_form.delete(0, tk.END)
    old_spe_form.delete(0, tk.END)
    new_spe_form.delete(0, tk.END)


# методы для удаления записей в таблице


def del_username():
    ''' Удаление строки из таблицы - infown'''
    del_user = user_del_form.get()

    qwer = Users.delete().where(Users.username == del_user)
    qwer.execute()
    messagebox.showinfo("Baaazaaa", "Пользователь успещно удален")
    user_del_form.delete(0, tk.END)
    update_id()


def del_email_two():
    ''' Удаление строки из таблица - inform'''
    del_ema = email_del_form.get()

    dede = Inform.delete().where(Inform.email == del_ema)
    dede.execute()
    messagebox.showinfo("Baaazaaa", "Пользователь успещно удален")
    email_del_form.delete(0, tk.END)
    update_id_two()


def del_group_spe():
    ''' Удаление строки из таблица - education'''
    grou_dell = gro_del_form.get()
    spec_del = spe_del_form.get()

    delli = Education.delete().where(Education.group == grou_dell,
                                     Education.specialization == spec_del)
    delli.execute()
    messagebox.showinfo("Baaazaaa", "Пользователь успещно удален")
    gro_del_form.delete(0, tk.END)
    spe_del_form.delete(0, tk.END)
    update_id_three()


# методы для обновления ID после удаления


def update_id():
    ''' Обновление id после удаления'''
    print('a')


def update_id_two():
    ''' Обновление ID после удаления строки из таблицы Inform '''
    print('a')


def update_id_three():
    ''' Обновление id после удаления'''
    print('a')


#  создание главноего окна


window_one = tk.Tk()
window_one.geometry('500x500')
window_one.resizable(False, False)

frame_one = tk.Frame(window_one, width=250, height=160, bg='blue')
frame_two = tk.Frame(window_one, width=250, height=160)
frame_three = tk.Frame(window_one, width=250, height=165)
frame_four = tk.Frame(window_one, width=100, height=165)
frame_five = tk.Frame(window_one, width=400, height=165)
frame_six = tk.Frame(window_one, width=100, height=165)

frame_one.grid(row=0, column=0)
frame_two.grid(row=0, column=1)
frame_three.grid(row=1, column=0)
frame_four.grid(row=1, column=1)
frame_five.grid(row=2, column=0)
frame_six.grid(row=2, column=1)


# создание первой таблица users


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
                    command=window_two_show)
del_but = Button(frame_two, text='Изменить запись',
                 command=window_three_show)
apd_but = Button(frame_two, text='Удалить запись',
                 command=window_four_show)


gerate_but.grid(row=0, column=0, padx=20, pady=10)
del_but.grid(row=1, column=0, padx=20, pady=10)
apd_but.grid(row=2, column=0, padx=20, pady=10)


# Создание второй таблица Inform

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
                            command=window_two_two_show)
apd_but_two = ttk.Button(frame_four, text='Изменить данные',
                         command=window_three_two_show)
del_but_two = ttk.Button(frame_four, text='Удалить записи',
                         command=window_four_two_show)

create_but_two.grid(row=0, column=0, padx=20, pady=10)
apd_but_two.grid(row=1, column=0, padx=20, pady=10)
del_but_two.grid(row=2, column=0, padx=20, pady=10)

# создание третьей таблица - education

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
                              command=window_two_three_show)
apd_but_three = ttk.Button(frame_six, text='Изменить данные',
                           command=window_three_three_show)
del_but_three = ttk.Button(frame_six, text='Удалить записи',
                           command=window_four_three_show)

create_but_three.grid(row=0, column=0, padx=20, pady=10)
apd_but_three.grid(row=1, column=0, padx=20, pady=10)
del_but_three.grid(row=2, column=0, padx=20, pady=10)

# создание второго окна, для создания записи в таблице - users


window_two = tk.Tk()
window_two.title('Создание записи Users')
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


# СОздание второго окна, для создания записи в бд, таблица Inform


window_two_two = tk.Tk()
window_two_two.title('Создание записи Inform')
window_two_two.geometry('300x300')
window_two_two.resizable(False, False)
window_two_two.withdraw()
window_two_two.protocol('WM_DELETE_WINDOW', on_close_second_two_window)

frame_create_info = tk.Frame(window_two_two, width=300, height=300)
frame_create_info.grid(row=0, column=0)

app_age_text = ttk.Label(frame_create_info, text='Добавить age')
app_age_form = ttk.Entry(frame_create_info, justify='left')
app_email_text = ttk.Label(frame_create_info, text='Добавить email')
app_email_form = ttk.Entry(frame_create_info, justify='left')
create_but_infowm = ttk.Button(frame_create_info, text='Создать',
                               command=form_submit_two)

app_age_text.grid(row=0, column=0, padx=10, pady=10)
app_age_form.grid(row=0, column=1, padx=10, pady=10)
app_email_text.grid(row=1, column=0, padx=10, pady=10)
app_email_form.grid(row=1, column=1, padx=10, pady=10)
create_but_infowm.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# создание второго окна, для создания записи в таблице Education


window_two_three = tk.Tk()
window_two_three.title('Создание записи Education')
window_two_three.geometry('300x300')
window_two_three.resizable(False, False)
window_two_three.withdraw()
window_two_three.protocol('WM_DELETE_WINDOW', on_close_second_three_window)

frame_create_edu = tk.Frame(window_two_three, width=300, height=300)
frame_create_edu.grid(row=0, column=0)

app_gr_text = ttk.Label(frame_create_edu, text='Добавить group')
app_gr_form = ttk.Entry(frame_create_edu, justify='left')
app_spe_text = ttk.Label(frame_create_edu, text='Добавить specialization')
app_spe_form = ttk.Entry(frame_create_edu, justify='left')
create_but_edu = ttk.Button(frame_create_edu, text='Создать',
                            command=form_submit_three)

app_gr_text.grid(row=0, column=0, padx=10, pady=10)
app_gr_form.grid(row=0, column=1, padx=10, pady=10)
app_spe_text.grid(row=1, column=0, padx=10, pady=10)
app_spe_form.grid(row=1, column=1, padx=10, pady=10)
create_but_edu.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# создание третьего окна для изменения записи, в таблице - users


window_three = tk.Tk()
window_three.title('Редактирование записи Users')
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


# создание третьего окна, для изменения записи в  таблице - inform


window_three_two = tk.Tk()
window_three_two.title('Редактирование записи Infowm')
window_three_two.geometry('300x300')
window_three_two.resizable(False, False)
window_three_two.withdraw()
window_three_two.protocol('WM_DELETE_WINDOW', on_close_three_two_window)

old_age = ttk.Label(window_three_two, text='Старый age')
old_age_form = ttk.Entry(window_three_two, justify='left')
new_age = ttk.Label(window_three_two, text='Новый age')
new_age_form = ttk.Entry(window_three_two, justify='left')
old_email = ttk.Label(window_three_two, text='Старый emial')
old_email_form = ttk.Entry(window_three_two, justify='left')
new_email = ttk.Label(window_three_two, text='Новый email')
new_email_form = ttk.Entry(window_three_two, justify='left')
but_app_inf = ttk.Button(window_three_two, text='Изменить данные',
                         command=form_redac_two)

old_age.grid(row=0, column=0, padx=10, pady=10)
old_age_form.grid(row=0, column=1, padx=10, pady=10)
new_age.grid(row=1, column=0, padx=10, pady=10)
new_age_form.grid(row=1, column=1, padx=10, pady=10)
old_email.grid(row=2, column=0, padx=10, pady=10)
old_email_form.grid(row=2, column=1, padx=10, pady=10)
new_email.grid(row=3, column=0, padx=10, pady=10)
new_email_form.grid(row=3, column=1, padx=10, pady=10)
but_app_inf.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Создание третьего окна, для изменения записи в таблице - Education

window_three_three = tk.Tk()
window_three_three.title('Редактирование записи Education')
window_three_three.geometry('300x300')
window_three_three.resizable(False, False)
window_three_three.withdraw()
window_three_three.protocol('WM_DELETE_WINDOW', on_close_three_three_window)

old_gro = ttk.Label(window_three_three, text='Старый group')
old_gro_form = ttk.Entry(window_three_three, justify='left')
new_gro = ttk.Label(window_three_three, text='Новый group')
new_gro_form = ttk.Entry(window_three_three, justify='left')
old_spe = ttk.Label(window_three_three, text='Старый specialization')
old_spe_form = ttk.Entry(window_three_three, justify='left')
new_spe = ttk.Label(window_three_three, text='Новый specialization')
new_spe_form = ttk.Entry(window_three_three, justify='left')
but_spe_edu = ttk.Button(window_three_three, text='Изменить данные',
                         command=form_redac_three)

old_gro.grid(row=0, column=0, padx=10, pady=10)
old_gro_form.grid(row=0, column=1, padx=10, pady=10)
new_gro.grid(row=1, column=0, padx=10, pady=10)
new_gro_form.grid(row=1, column=1, padx=10, pady=10)
old_spe.grid(row=2, column=0, padx=10, pady=10)
old_spe_form.grid(row=2, column=1, padx=10, pady=10)
new_spe.grid(row=3, column=0, padx=10, pady=10)
new_spe_form.grid(row=3, column=1, padx=10, pady=10)
but_spe_edu.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Создание чевертого окна, для удаления данных таблица - Users

window_four = tk.Tk()
window_four.title('Удаление данных Users')
window_four.geometry('450x100')
window_four.resizable(False, False)
window_four.withdraw()
window_four.protocol('WM_DELETE_WINDOW', on_close_four_window)


user_del = ttk.Label(window_four,
                     text='Введите username, который необходимо удалить')
user_del_form = ttk.Entry(window_four, justify='left')
user_del_but = ttk.Button(window_four, text='Удалить username',
                          command=del_username)

user_del.grid(row=0, column=0, padx=10, pady=10)
user_del_form.grid(row=0, column=1, padx=10, pady=10)
user_del_but.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


# Создание чевертого окна, для удаления данных таблица - Infown


window_four_two = tk.Tk()
window_four_two.title('Удаление данных Inform')
window_four_two.geometry('450x100')
window_four_two.resizable(False, False)
window_four_two.withdraw()
window_four_two.protocol('WM_DELETE_WINDOW', on_close_four_two_window)

email_del = ttk.Label(window_four_two,
                      text='Введите email, который необходимо удалить')
email_del_form = ttk.Entry(window_four_two, justify='left')
email_del_but = ttk.Button(window_four_two, text='Удалить email',
                           command=del_email_two)

email_del.grid(row=0, column=0, padx=10, pady=10)
email_del_form.grid(row=0, column=1, padx=10, pady=10)
email_del_but.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Создание чевертого окна, для удаления данных таблица - Education


window_four_three = tk.Tk()
window_four_three.title('Удаление данных Education')
window_four_three.geometry('460x150')
window_four_three.resizable(False, False)
window_four_three.withdraw()
window_four_three.protocol('WM_DELETE_WINDOW', on_close_four_three_window)

gro_del = ttk.Label(window_four_three,
                    text='Введите group, который необходимо удалить')
gro_del_form = ttk.Entry(window_four_three, justify='left')
spe_del = ttk.Label(window_four_three,
                    text='Введите specialization, который необходимо удалить')
spe_del_form = ttk.Entry(window_four_three, justify='left')
email_del_but = ttk.Button(window_four_three, text='Удалить',
                           command=del_group_spe)

gro_del.grid(row=0, column=0, padx=10, pady=10)
gro_del_form.grid(row=0, column=1, padx=10, pady=10)
spe_del.grid(row=1, column=0, padx=10, pady=10)
spe_del_form.grid(row=1, column=1, padx=10, pady=10)
email_del_but.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# конец прог


def on_close_main_window():
    ''' прерывание программы, при закрытии основного окна'''
    if window_two is not None and window_two.winfo_exists():
        window_two.destroy()
    if window_two_two is not None and window_two_two.winfo_exists():
        window_two_two.destroy()
    if window_two_three is not None and window_two_three.winfo_exists():
        window_two_three.destroy()
    if window_three is not None and window_three.winfo_exists():
        window_three.destroy()
    if window_three_two is not None and window_three_two.winfo_exists():
        window_three_two.destroy()
    if window_three_three is not None and window_three_three.winfo_exists():
        window_three_three.destroy()
    if window_four is not None and window_four.winfo_exists():
        window_four.destroy()
    if window_four_two is not None and window_four_two.winfo_exists():
        window_four_two.destroy()
    if window_four_three is not None and window_four_three.winfo_exists():
        window_four_three.destroy()
    window_one.destroy()


db.connect()
dow_dan()
dow_dan_inforn()
dow_dan_educa()
db.close()

window_one.protocol('WM_DELETE_WINDOW', on_close_main_window)

window_one.mainloop()
