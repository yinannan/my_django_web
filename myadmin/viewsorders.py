from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Goods,Type,Orders,Detail
import time,json,os
from django.core.paginator import Paginator
from PIL import Image

#--------------------------订单信息-----------------------------------

#订单浏览页面
def orderssee(request,pIndex):
	list = Orders.objects.filter()
	p = Paginator(list,10)
	if pIndex == '':
		pIndex = '1'
	pIndex = int(pIndex)
	list2 = p.page(pIndex)
	plist = p.page_range
	return render(request,"myadmin/orders/see.html",{'list2':list2,'pindex':pIndex,'plist':plist})

#查看订单详情
def orderdetail(request,oid):
	ob = Detail.objects.filter(orderid = oid)
	context = {'detailxq':ob}
	return render(request,"myadmin/orders/detailxq.html",context)

#订单编辑
def orderedit(request,uid):
	list = Orders.objects.get(id = uid)
	context = {'ob':list}
	return render(request,"myadmin/orders/orderedit.html",context)

#执行订单编辑
def orderdoedit(request):
	try:
		ob = Orders.objects.get(id = request.POST['id'])
		ob.status = request.POST['status']
		print(ob.status)
		print(1)
		ob.save()
		context = {'info':'订单状态修改成功!'}
	except:
		context = {'info':'订单状态修改失败!'}
	return render (request,"myadmin/orders/info.html",context)	

#-----------------------end 订单信息------------------------------

