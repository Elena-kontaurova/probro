''' так внешка '''
from connect import db
from controller.users_con import load_users
from controller.inform_con import load_inform
from controller.educa_con import load_education
from window.window_one import window_one
from window.users import table, window_two, window_three, window_four
from window.inform import table_two, window_two_two, window_three_two, window_four_two
from window.education import table_three, window_two_three, window_three_three, \
    window_four_three


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
load_users(table)
load_inform(table_two)
load_education(table_three)
db.close()

window_one.protocol('WM_DELETE_WINDOW', on_close_main_window)

window_one.mainloop()
