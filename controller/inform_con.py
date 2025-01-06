''' inform controller'''
from tkinter import messagebox
from model.inform_mod import get_all_inform
from view.inf_u import display_inform, show_inf_open_window, show_inf_delete_window, \
    show_inf_edit_window, close_inf_open_window, close_inf_edit_window, \
    close_inf_delete_window, create_inform, edit_inform, delete_inform


def load_inform(table_two):
    ''' Загружать и отображать'''
    informs = get_all_inform()
    display_inform(table_two, informs)


def open_inform_open_window(window):
    ''' Котроллер для открытия создан inform'''
    show_inf_open_window(window)


def open_inform_edit_window(window):
    ''' Контроллер для открытия редак inform'''
    show_inf_edit_window(window)


def open_inf_delete_window(window):
    ''' Контроллер для открытия окна удаления inform'''
    show_inf_delete_window(window)


def close_inform_open_window(window):
    ''' Контроллер для закрытия окна создания inf'''
    close_inf_open_window(window)


def close_inform_edit_window(window):
    ''' Контроллер для закрытия окна редак inf'''
    close_inf_edit_window(window)


def close_inform_delete_window(window):
    ''' Контроллер для закрытия окна удаления inf'''
    close_inf_delete_window(window)


def submit_inform_form(age, email):
    ''' Контроллер для создания inform '''
    if age and email:
        create_inform(age, email)
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля!")


def submit_edit_inform_form(old_agee, new_agee, old_emaill, new_emaill):
    ''' Контроллер для редактирования inform '''
    if old_agee and old_emaill and new_agee and new_emaill:
        edit_inform(old_agee, old_emaill, new_agee, new_emaill)
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля!")


def submit_delete_inf_form(email):
    ''' Контроллер для удаления inform '''
    delete_inform(email)
