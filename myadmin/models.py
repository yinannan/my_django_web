from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    adress = models.CharField(max_length=255)
    sex = models.IntegerField(default=1)
    phone = models.CharField(max_length=16)
    code = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    addtime = models.IntegerField(max_length=11)

    class Meta:
        db_table='myweb_users'
   

class Type(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=1)
    path = models.CharField(max_length=255)
    class Meta:
        db_table='myweb_type'

class Goods(models.Model):
    typeid = models.IntegerField(default=1)
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.TextField()
    price = models.IntegerField()
    picname = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.IntegerField(max_length=11)

    class Meta:
        db_table='myweb_goods'
    
class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    adress = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField()
    status = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        db_table='myweb_orders'
   

class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    num = models.IntegerField()
           
    class Meta:
        db_table='myweb_detail'