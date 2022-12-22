from peewee import *

db = SqliteDatabase('users_database.db')


class UserData(Model):

    telegram_username = CharField()
    fm_username = CharField()
    fm_email = CharField()
    fm_id = IntegerField()
    chat_id = IntegerField()
    telegram_user_id = IntegerField()

    class Meta:
        database = db
        db_table = 'users'



