''' education view'''
from tkinter import messagebox
from connect import Education


def display_inform(table_three, educations):
    ''' Отоброжаем'''
    for user in educations:
        table_three.insert('', 'end', values=(user.id, user.group, user.specialization))


def show_edu_open_window(window):
    ''' Отобразить открыть окно - education'''
    window.deiconify()


def show_edu_edit_window(window):
    ''' открыть редакт окно education'''
    window.deiconify()


def show_edu_delete_window(window):
    ''' Показать окно для удаления education '''
    window.deiconify()


def close_edu_open_window(window):
    ''' Закрыть создание окно education'''
    window.withdraw()


def close_edu_edit_window(window):
    ''' Закрыть редакт окно education'''
    window.withdraw()


def close_edu_delete_window(window):
    ''' Закрыть удаление окно education'''
    window.withdraw()


def create_education(group, specialization):
    ''' Функция для создания записи inform '''
    Education.create(group=group, specialization=specialization)
    messagebox.showinfo("Успех", "Данные добавлены успешно!")


def edit_education(old_group, old_speci, new_group, new_speci):
    ''' Функция для редактирования записи education'''
    edu = Education.get(Education.group == old_group,
                        Education.specialization == old_speci)
    edu.group = new_group
    edu.specialization = new_speci
    edu.save()
    messagebox.showinfo('Успех', 'Данные успешно обновленны')


def delete_education(group, specialization):
    ''' Функция для удаления education'''
    if not group or not specialization:
        messagebox.showerror('Ошибка', 'Укажите group and specialization для удаления')
        return

    delli = Education.delete().where(Education.group == group,
                                     Education.specialization == specialization).execute()

    if delli:
        messagebox.showinfo("Успех", "Данные успешно удалены")
    else:
        messagebox.showwarning("Не найдено", "Данные не найден")
