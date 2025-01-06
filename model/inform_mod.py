''' inform model'''
from connect import Inform


def get_all_inform():
    ''' Полученпие всех inform'''
    return Inform.select()
