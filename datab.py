''' база'''
from tkinter import messagebox
import tkinter as tk
from connect import Users, Inform, Education
from ui import app_username_form, app_password_form, app_age_form, \
            app_email_form, app_gr_form, app_spe_form, old_user_form, \
            new_pass_form, old_pas_form, new_user_form, old_age_form, new_age_form, \
            old_email_form, new_email_form, old_gro_form, old_spe_form, new_gro_form, \
            new_spe_form, user_del_form, email_del_form, gro_del_form, spe_del_form


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


def del_email_two():
    ''' Удаление строки из таблица - inform'''
    del_ema = email_del_form.get()

    dede = Inform.delete().where(Inform.email == del_ema)
    dede.execute()
    messagebox.showinfo("Baaazaaa", "Пользователь успещно удален")
    email_del_form.delete(0, tk.END)


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
