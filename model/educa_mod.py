''' education model'''
from connect import Education


def get_all_educa():
    ''' Получение всех education'''
    return Education.select()
