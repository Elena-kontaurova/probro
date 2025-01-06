''' inform view'''
# import tkinter as tk
from tkinter import messagebox
from connect import Inform


def display_inform(table_inf, informs):
    ''' Отображение информации в таблице'''
    for usess in informs:
        table_inf.insert('', 'end', values=(usess.id, usess.age, usess.email))


def show_inf_open_window(window):
    ''' Открыть окно создать - inform'''
    window.deiconify()


def show_inf_edit_window(window):
    ''' открыть редакт окно inform'''
    window.deiconify()


def show_inf_delete_window(window):
    ''' Показать окно для удаления inform '''
    window.deiconify()


def close_inf_open_window(window):
    ''' Закрыть создание окно inform'''
    window.withdraw()


def close_inf_edit_window(window):
    ''' Закрыть редакт окно inform'''
    window.withdraw()


def close_inf_delete_window(window):
    ''' Закрыть удаление окно inform'''
    window.withdraw()


def create_inform(age, email):
    ''' Функция для создания записи inform '''
    Inform.create(age=age, email=email)
    messagebox.showinfo("Успех", "Данные добавлены успешно!")


def edit_inform(old_agee, old_emaill, new_agee, new_emaill):
    ''' Функция для редактирования записи inform '''
    ini = Inform.get(Inform.age == old_agee, Inform.email == old_emaill)
    ini.age = new_agee
    ini.email = new_emaill
    ini.save()
    messagebox.showinfo('Успех', 'Данные успешно обновленны')


def delete_inform(email):
    ''' Функция для удаления inform'''
    if not email:
        messagebox.showerror('Ошибка', 'Укажите email для удаления')
        return

    dede = Inform.delete().where(Inform.email == email).execute()

    if dede:
        messagebox.showinfo("Успех", "Email успешно удален")
    else:
        messagebox.showwarning("Не найдено", "Email не найден")
