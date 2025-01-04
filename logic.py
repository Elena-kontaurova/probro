''' логика'''
from connect import Users, Inform, Education
from ui import table, table_two, table_three, window_four, window_two, \
        window_two_two, window_two_three, window_three, window_three_two, \
        window_three_three, window_four_two, window_four_three, window_one


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
