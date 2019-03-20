from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Goods,Type
import time,json,os
from django.core.paginator import Paginator
from PIL import Image


#----------------------------------------------商品信息---------------------------------------

#浏览
def goodssee(request,pIndex):
	list = Goods.objects.filter()
	for ob in list:
		typelist = Type.objects.filter(id = ob.typeid)
		for i in typelist:
			ob.typename = i.name
	p = Paginator(list,5)
	if pIndex == '':
		pIndex = '1'
	pIndex = int(pIndex)
	list2 = p.page(pIndex)
	plist = p.page_range
	return render(request,"myadmin/goods/see.html",{'list2':list2,'pindex':pIndex,'plist':plist})

#添加商品
def goodsadd(request):
	list = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	for ab in list :
		ab.pname = '...'*(ab.path.count(',')-1)
	context = {"typelist":list}
	return render(request,"myadmin/goods/add.html",context)

#执行商品添加
def goodsinsert(request):
	try:
		myfile = request.FILES.get("picname", None)
		if not myfile:
			return HttpResponse("没有上传文件信息！")
		filename= str(time.time())+"."+myfile.name.split('.').pop()
		destination = open(os.path.join("./static/goods/",filename),'wb+')
		for chunk in myfile.chunks():      
			destination.write(chunk)  
		destination.close()
		im = Image.open("./static/goods/"+filename)
		im.thumbnail((206,206))
		im.save("./static/goods/"+filename,'jpeg')
		im.thumbnail((150, 150))
		im.save("./static/goods/m_"+filename, 'jpeg')
		im.thumbnail((60, 60))
		im.save("./static/goods/s_"+filename, 'jpeg')
		
		ob = Goods()
		ob.typeid = request.POST['typeid']
		ob.goods = request.POST['goods']
		ob.company = request.POST['company']
		ob.picname = filename
		ob.descr = request.POST['descr']
		ob.price = request.POST['price']
		ob.state = request.POST['state']
		ob.store = request.POST['store']
		ob.num = request.POST['num']
		ob.clicknum = request.POST['clicknum']
		ob.addtime = time.time()
		ob.save()
		context = {'info':'商品添加成功'}
	except:
		context = {'info':'商品添加失败'}
	return render(request,"myadmin/goods/info.html",context)

#商品删除
def goodsdel(request,uid):
	try:
		ob = Goods.objects.get(id = uid)
		ob.delete()
		os.remove("./static/goods/"+ob.picname) 
		os.remove("./static/goods/s_"+ob.picname) 
		os.remove("./static/goods/m_"+ob.picname) 
		context = {'info':'商品删除成功!'}
	except:
		context = {'info':'商品删除失败!'}
	return render(request,"myadmin/goods/info.html",context)

#商品编辑
def goodsedit(request,uid):
	list = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	for ab in list :
		ab.pname = '...'*(ab.path.count(',')-1)
	ob = Goods.objects.get(id = uid)
	context = {'goods':ob,'types':list}
	return render(request,"myadmin/goods/edit.html",context)

#执行商品编辑
def goodsupdate(request):
	try:
		oldpicname = request.POST['oldpicname']
		flag = False
		if None != request.FILES.get("pic"):
			myfile = request.FILES.get("pic", None)
			if not myfile:
				return HttpResponse("没有上传文件信息！")
			filename= str(time.time())+"."+myfile.name.split('.').pop()
			destination = open(os.path.join("./static/goods/",filename),'wb+')
			for chunk in myfile.chunks():      
				destination.write(chunk)  
			destination.close()
			im = Image.open("./static/goods/"+filename)
			im.thumbnail((206,206))
			im.save("./static/goods/"+filename,'jpeg')
			im.thumbnail((150, 150))
			im.save("./static/goods/m_"+filename, 'jpeg')
			im.thumbnail((60, 60))
			im.save("./static/goods/s_"+filename, 'jpeg')
			flag = True
			picname = filename
		else:
			print('q')
			picname = oldpicname
		ob = Goods.objects.get(id = request.POST['id'])
		ob.goods = request.POST['goods']
		ob.typeid = request.POST['typeid']
		ob.descr = request.POST['descr']
		ob.price = request.POST['price']
		ob.state = request.POST['state']
		ob.picname = picname
		ob.save()
		context = {'info':'商品修改成功!'}
		if flag:
			os.remove("./static/goods/m_"+ oldpicname)
			print('1')
			os.remove("./static/goods/s_"+ oldpicname)
			os.remove("./static/goods/"+ oldpicname)
	except:
		context = {'info':'商品修改失败!'}
		if flag:
			os.remove("./static/goods/m_"+picname)
			os.remove("./static/goods/s_"+picname)
			os.remove("./static/goods/"+picname)
		
	return render (request,"myadmin/goods/info.html",context)	


#---------------------------------end 商品信息-----------------------------------------


#---------------------------------------商品类别信息----------------------------------

#类别浏览
def typeliu(request):
	list = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	for ab in list :
		ab.pname = '...'*(ab.path.count(',')-1)
	context = {"typelist":list}
	return render(request,"myadmin/type/see.html",context)

#添加类别
def typeadd(request,tid):
	if tid == '0':
		context = {'pid':0,'path':'0,','name':'根类别'}
	else:
		ob = Type.objects.get(id = tid )
		context = {'pid':ob.id,'path':ob.path+str(ob.id)+',','name':ob.name}
	return render(request,"myadmin/type/add.html",context)

#商品类别添加
def typeinsert(request):
	try:
		ob = Type()
		ob.pid  = request.POST['pid']
		ob.name = request.POST['name']
		ob.path = request.POST['path']
		ob.save()
		context = {'info':'商品类别添加成功'}
	except:
		context = {'info':'商品类别添加失败'}
	return render(request,"myadmin/type/info.html",context)

#类别删除
def typedel(request,uid):
	try:
		ob = Type.objects.filter(pid = uid).count()
		if ob > 0 :
			context = {'info':'商品类别删除失败!还有子类别!'}
			return render(request,"myadmin/type/info.html",context)
		else:
			sb = Type.objects.get(id = uid)
			sb.delete()
			context = {'info':'商品类别删除成功!'}
	except:
		context = {'info':'商品类别删除失败!'}
	return render(request,"myadmin/type/info.html",context)

#商品类别编辑
def typeedit(request,uid):
	ob = Type.objects.get(id = uid)
	context = {'type':ob}
	return render(request,"myadmin/type/edit.html",context)

#执行商品类别编辑
def typeupdate(request,tid):
	try:
		ob = Type.objects.get(id = tid)
		ob.id = request.POST['id']
		ob.path = request.POST['path']
		ob.name = request.POST['name']
		ob.save()
		context = {'info':'商品修改成功!'}
	except:
		context = {'info':'商品修改失败!'}
	return render (request,"myadmin/type/info.html",context)	

#---------------------------------end 商品类别信息-------------------------------

