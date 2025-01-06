''' users controller'''
from tkinter import messagebox
from model.users_mod import get_all_users
from view.user_u import display_users, show_user_open_window, show_user_delete_window, \
    show_user_edit_window, close_user_open_window, close_user_edit_window, \
    close_user_delete_window, create_user, edit_user, delete_user


def load_users(table):
    ''' Загружает пользователей и отображает их в таблице '''
    users = get_all_users()
    display_users(table, users)


def open_user_window(window):
    ''' Контроллер для открытия создания users'''
    show_user_open_window(window)


def open_user_edit_window(window):
    ''' Контроллер для открытия редактирования users'''
    show_user_edit_window(window)


def open_user_delete_window(window):
    ''' Контроллер для открытия окна удаления users'''
    show_user_delete_window(window)


def close_user_window(window):
    ''' Контроллер для закрытия создания users'''
    close_user_open_window(window)


def close_user_edit_window_con(window):
    ''' Контроллер для закрытия редак users'''
    close_user_edit_window(window)


def close_user_delete_window_con(window):
    ''' Контроллер для закрытия удаления users'''
    close_user_delete_window(window)


def submit_user_form(username, password):
    ''' Контроллер для создания пользователя '''
    if username and password:
        create_user(username, password)
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля!")


def submit_edit_user_form(old_username, old_password, new_username, new_password):
    ''' Контроллер для редактирования пользователя '''
    if old_username and old_password and new_username and new_password:
        edit_user(old_username, old_password, new_username, new_password)
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля!")


def submit_delete_user_form(username):
    ''' Контроллер для удаления пользователя '''
    delete_user(username)
