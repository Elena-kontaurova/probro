''' бд'''
from peewee import MySQLDatabase, Model, IntegerField, CharField

db = MySQLDatabase('baaazaaa', user='root', password='lenok',
                   host='localhost', port=3306)


class BaseModel(Model):
    ''' jkj'''
    class Meta:
        ''' kjkjkjk'''
        database = db


class Users(BaseModel):
    '''Пользователь'''
    id = IntegerField(primary_key=True)
    username = CharField()
    password = CharField()


class Inform(BaseModel):
    ''' Информация о пользователе'''
    id = IntegerField(primary_key=True)
    age = IntegerField()
    email = CharField()


class Education(BaseModel):
    '''Образование'''
    id = IntegerField(primary_key=True)
    group = IntegerField()
    specialization = CharField()


db.connect()
db.create_tables([Users, Inform, Education],  safe=True)
db.close()
