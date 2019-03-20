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
    def userdef(self):
        return {'id':self.id,'username':self.username,'name':self.name,'adress':self.adress,'phone':self.phone,'code':self.code,'email':self.email,'sex':self.sex,}
   

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
    def zidian(self):
        return {'id':self.id,'goods':self.goods,'picname':self.picname,'price':self.price,'m':1}
    
class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    adress = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField()
    status = models.IntegerField()
    total = models.IntegerField()

    def ordersdef(self):
        return{'uid':self.uid,'linkname':self.linkname,'adress':self.adress,'code':self.code,'phone':self.phone,'addtime':self.addtime,'status':self.status,'total':self.total}

class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    num = models.IntegerField()
   
    def detaildef(self):
        return{'orderid':self.orderid,'goodsid':self.goodsid,'name':self.name,'price':self.price,'num':self.num}


