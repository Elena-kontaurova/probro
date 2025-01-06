''' users view'''
# import tkinter
from tkinter import messagebox
from connect import Users


def display_users(table, users):
    ''' Отображает пользователей в переданной таблице '''
    for user in users:
        table.insert('', 'end', values=(user.id, user.username, user.password))


def show_user_open_window(window):
    ''' открыть создание окно users'''
    window.deiconify()


def show_user_edit_window(window):
    ''' открыть редакт окно users'''
    window.deiconify()


def show_user_delete_window(window):
    ''' Показать окно для удаления users '''
    window.deiconify()


def close_user_open_window(window):
    ''' Закрыть создание окно users'''
    window.withdraw()


def close_user_edit_window(window):
    ''' Закрыть редакт окно users'''
    window.withdraw()


def close_user_delete_window(window):
    ''' Закрыть удаление окно users'''
    window.withdraw()


def create_user(username, password):
    ''' Функция для создания записи пользователя '''
    Users.create(username=username, password=password)
    messagebox.showinfo("Успех", "Данные добавлены успешно!")


def edit_user(old_username, old_password, new_username, new_password):
    ''' Функция для редактирования записи пользователя '''
    user = Users.get(Users.username == old_username, Users.password == old_password)
    user.username = new_username
    user.password = new_password
    user.save()

    messagebox.showinfo('Успех', 'Данные успешно обновлены')


def delete_user(username):
    ''' Функция для удаления пользователя '''
    if not username:
        messagebox.showerror('Ошибка', 'Укажите имя пользователя для удаления')
        return

    deleted_count = Users.delete().where(Users.username == username).execute()

    if deleted_count:
        messagebox.showinfo("Успех", "Пользователь успешно удален")
    else:
        messagebox.showwarning("Не найдено", "Пользователь не найден")
