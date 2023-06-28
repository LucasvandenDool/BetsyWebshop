# Models go here
from peewee import *

db = SqliteDatabase('BestieBetsy.db')


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = AutoField()
    name = CharField(unique= True, max_length= 50)
    street = CharField(max_length= 50)
    housenumber = IntegerField()
    postal = CharField(max_length= 6)
    card = IntegerField()

class Product(BaseModel):
    owner = ForeignKeyField(User, backref='products', null= True)
    name = CharField(max_length= 50)
    description = CharField(max_length= 100, null= True)
    price = FloatField()
    amount = IntegerField()

class Tags(BaseModel):
    name = CharField(max_length= 20)

class Product_tag(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tags)

class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='transactions')
    seller = ForeignKeyField(User, backref='transactions')
    product = ForeignKeyField(Product, backref='transactions')
    amount = IntegerField()
    price = FloatField()
    total = FloatField()
    date = DateTimeField()


models = (User, Product, Tags, Product_tag, Transaction)

def start_up():
    connection = db.connect()

    if connection:
        print('Connected to database.')

    with db:
        db.drop_tables(models)
        db.create_tables(models)