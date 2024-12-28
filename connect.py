''' бд'''
from peewee import MySQLDatabase, Model, IntegerField, CharField

db = MySQLDatabase('baaazaaa', user='root', password='lenok',
                   host='localhost', port=3306)


class Users(Model):
    '''Пользователь'''
    id = IntegerField(primary_key=True)
    username = CharField()
    password = CharField()

    class Meta:
        ''' kjkjkjk'''
        database = db


db.connect()
db.create_tables([Users],  safe=True)
db.close()
