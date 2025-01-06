''' education controller'''
from tkinter import messagebox
from model.educa_mod import get_all_educa
from view.educ_u import display_inform, show_edu_open_window, show_edu_delete_window, \
    show_edu_edit_window, close_edu_open_window, close_edu_edit_window, \
    close_edu_delete_window, create_education, edit_education, delete_education


def load_education(table_three):
    ''' Загружать и отображать'''
    educations = get_all_educa()
    display_inform(table_three, educations)


def open_educa_open_window(window):
    ''' Контроллер для открытия окна создания edu'''
    show_edu_open_window(window)


def open_educa_edit_window(window):
    ''' Контроллер для открытия окна редактирования edu'''
    show_edu_edit_window(window)


def open_edu_delete_window(window):
    ''' Контроллер для открытия окна удаления edu '''
    show_edu_delete_window(window)


def close_educ_open_window(window):
    ''' Контроллер для закрытия окна создания edu'''
    close_edu_open_window(window)


def close_educ_edit_window(window):
    ''' Контроллер для закрытия окна редак edu'''
    close_edu_edit_window(window)


def close_educ_delete_window(window):
    ''' Контроллер для закрытия окна удаления edu'''
    close_edu_delete_window(window)


def submit_educa_form(group, specialization):
    ''' Контроллер для создания education '''
    if group and specialization:
        create_education(group, specialization)
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля!")


def submit_edit_educa_form(old_group, old_speci, new_group, new_speci):
    ''' Контроллер для редактирования education'''
    if old_group and old_speci and new_group and new_speci:
        edit_education(old_group, old_speci, new_group, new_speci)
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля!")


def submit_delete_educ_form(group, specialization):
    ''' Контроллер для удаления education '''
    delete_education(group, specialization)
