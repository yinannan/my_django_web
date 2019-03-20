from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .models import Type,Goods,Orders,Detail,Users
import time

#-----------------------------------------订单------------------------------------
#没有选择购买商品
def nobuy(request):
    return render(request,"myweb/nobuy.html")

#订单表单页
def orders(request):
    ids = request.GET['gids']
    if ids == '':
        return redirect(reverse('nobuy'))
    gids = ids.split(',')
    buys = request.session['buy']
    orderlist = {}
    total = 0
    for gid in gids:
        orderlist[gid] = buys[gid]
        total += orderlist[gid]['price']*orderlist[gid]['m'] 
        print(total)
    request.session['orderlist'] = orderlist
    request.session['total'] = total
    return render(request,"myweb/orders.html")

#订单确认页
def ordersconfirm(request):
    return render(request,"myweb/ordersconfirm.html")

#执行订单添加
def ordersinsert(request):
    orders = Orders()
    orders.uid = request.session['user']['id']
    orders.linkman = request.POST['linkman']
    orders.adress = request.POST['adress']
    orders.code = request.POST['code']
    orders.phone = request.POST['phone']
    orders.addtime = time.time()
    orders.total = request.session['total']
    orders.status = 0
    orders.save()
    orderlist = request.session['orderlist']
    for shop in orderlist.values():
        print(shop)
        detail = Detail()
        detail.orderid = orders.id
        detail.goodsid = shop['id']
        detail.name = shop['goods']
        detail.price = shop['price']
        detail.num = shop['m']
        detail.save()
    orderlist =  request.session['orderlist']
    shoplist =  request.session['buy']
    for i in orderlist:
        del shoplist[i]
    del request.session['orderlist']
    context = {'info': "下单成功：订单id号："+str(orders.id)}
    return redirect(reverse('ordersinfo'),context)

#购买成功
def ordersinfo(request):
    request.session['buy'] = {}
    return render(request,"myweb/end.html")

def beend(request):
    return render(request,"myweb/index.html")

def endche(request):
    return render(request,"myweb/che.html")

#-------------------------------个人中心----------------------------------

#个人中心
def webmyself(request):
    myuser = request.session['user']
    list = Orders.objects.filter(uid = myuser['id'])
    context= {'list':list,'myusers':myuser}
    return render(request,"myweb/myself.html",context)

#个人中心详情
def webmyselfdetail(request,oid):
    ob = Detail.objects.filter(orderid = oid)
    for i in ob:
        good = Goods.objects.filter(id = i.goodsid)
        for j in good:
            i.picname = j.picname
    context = {'mydetail':ob}
    return render(request,"myweb/mydetail.html",context)

#修改个人中心
def webmyselfedit(request,uid):
    ob = Users.objects.get(id = uid)
    context = {'myuser':ob}
    return render(request,"myweb/myselfedit.html",context)

#中心个人中心修改
def webmyselfdoedit(request):
    ob = Users.objects.get(id = request.POST['id'])
    ob.username = request.POST['username']
    ob.sex = request.POST['sex']
    ob.adress = request.POST['adress']
    ob.code = request.POST['code']
    ob.phone = request.POST['phone']
    ob.save()
    return render (request,"myweb/domyselfedit.html")

#个人中心修改密码
def webmyselfeditpass(request,aid):
    ob = Users.objects.get(id = aid)
    context = {'myselfusers':ob}
    return render(request,"myweb/myselfeditpass.html",context)

#执行密码修改
def webmyselfdoeditpass(request):
    ob = Users.objects.get(id=request.POST['id'])
    import hashlib
    m = hashlib.md5() 
    m.update(bytes(request.POST['password'],encoding="utf8"))
    ob.password = m.hexdigest()
    ob.save()
    return render(request,"myweb/editpass.html")

#确认收货
def webmyselfshouhuo(request,oid):
    ob = Orders.objects.get(id = oid)
    if ob.status != 2:
        ob.status = 2
        ob.save()
        context = {'info':"收货成功！感谢亲的购买！"}
    else:
        context={'info':"亲！已经收货！"}

    return render(request,"myweb/shouhuo.html",context)
