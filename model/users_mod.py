''' users model'''
from connect import Users


def get_all_users():
    ''' Получение всех users'''
    return Users.select()
