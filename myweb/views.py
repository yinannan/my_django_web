from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Users,Type,Goods
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import time 

#---------------------------------登陆-----------------------------

#登陆
def weblogin(request):
	if 'user' in request.session:
		return redirect(reverse('webmyself'))
	return render(request,"myweb/login.html")

#执行登陆
def webdologin(request):
	verifycode = request.session['verifycode']
	code = request.POST['code']
	if verifycode != code:
		context = {'info':'验证码错误！'}
		return render(request,"myweb/login.html",context)
	try:
		user = Users.objects.get(name=request.POST['username'])
		if user.state == 1:
			import hashlib
			m = hashlib.md5() 
			m.update(bytes(request.POST['password'],encoding="utf8"))
			if user.password == m.hexdigest():
				request.session['user'] = user.userdef()
				return redirect(reverse('webIndex'))
			else:
				context = {'info':'登录密码错误！'}
		else:
			context = {'info':'此用户非登陆用户！'}
	except:
		context = {'info':'用户名不存在！'}
	return render(request,"myweb/login.html",context)

#---------------------------------退出-----------------------------

#退出
def weblogout(request):
	if 'user'  in request.session:
		del request.session['user']
	if 'buy' in request.session:
		del request.session['buy']#退出清除购物车信息
	return render(request,"myweb/login.html")

#退出先登录
def webin(request):
	return render(request,"myweb/webin.html")

#---------------------------------验证码-----------------------------

#验证码
def webyanzhengma(request):
	import random
	from PIL import Image, ImageDraw, ImageFont
	bgcolor = (242,164,247)
	width = 100
	height = 25
	im = Image.new('RGB', (width, height), bgcolor)
	draw = ImageDraw.Draw(im)
	for i in range(0, 100):
	    xy = (random.randrange(0, width), random.randrange(0, height))
	    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
	    draw.point(xy, fill=fill)
	str1 = '1234567890'
	rand_str = ''
	for i in range(0, 4):
	    rand_str += str1[random.randrange(0, len(str1))]
	font = ImageFont.truetype('static/STXIHEI.TTF', 21)
	fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
	draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
	draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
	draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
	draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
	del draw
	request.session['verifycode'] = rand_str
	import io
	buf = io.BytesIO()
	im.save(buf, 'png')
	return HttpResponse(buf.getvalue(),'image/png')


#---------------------------------注册-----------------------------

#注册
def webzhuce(request):
	if 'user' in request.session:
		return redirect(reverse('webquit'))
	return render(request,"myweb/zhuce.html")

#注册退出提示
def webquit(request):
	return render(request,"myweb/quit.html")

#执行会员注册
def webdozhuce(request):
	ob = Users()
	ob.username = request.POST['username']
	ob.name = request.POST['name']
	
	import hashlib
	m = hashlib.md5() 
	m.update(bytes(request.POST['password'],encoding="utf8"))
	ob.password = m.hexdigest()

	ob.sex = request.POST['sex']
	ob.adress = request.POST['adress']
	ob.code = request.POST['code']
	ob.phone = request.POST['phone']
	ob.email = request.POST['email']
	# ob.state = request.POST['state']
	ob.addtime =time.time()
	ob.save()
	return render(request,"myweb/zhuceinfo.html")

#---------------------------------前台-----------------------------

#函数
def public(request):
	context = {}
	context['typelist'] = Type.objects.filter(pid = 0)
	return context

#首页
def webIndex(request):
	context = public(request)
	return render(request,"myweb/index.html",context)

#列表
def weblist(request,tid=0):
	context = public(request)
	if tid == 0:
		context['goodslist'] = Goods.objects.all()
	else:
		context['types'] = Type.objects.filter(pid=tid)
		if request.GET.get('ttid',None):
			context['goodslist'] = Goods.objects.filter(typeid=request.GET['ttid'])
		else:
			context['goodslist'] = Goods.objects.filter(typeid__in=Type.objects.only('id').filter(path__contains=','+str(tid)+','))
	return render(request,'myweb/list.html',context)


#详情
def webdetail(request,tid):
	context = public(request)
	ob = Goods.objects.get(id = tid)
	ob.clicknum += 1
	ob.save()
	context['goodslist'] = ob  
	return render(request,"myweb/detail.html",context)

#购物车无参数
def webbaseche(request):
	return render(request,"myweb/che.html")

#购物车
def webche(request,tid):
	a = Goods.objects.get(id = tid)
	goods = a.zidian()
	goods['m']=int(request.POST['m'])

	if "buy" in request.session:
		buys = request.session['buy']
	else:
		buys={}
	if tid in buys:
		buys[tid]['m']+=goods['m']
	else:
		buys[tid] = goods
	request.session['buy'] = buys
	return redirect(reverse('webbaseche'))

#清除购物车
def webclearche(request):
	request.session['buy'] = {}
	return render(request,"myweb/che.html")

#删除购物车
def webdelche(request,tid):
	buys = request.session['buy']
	del buys[tid]
	request.session['buy'] = buys
	return redirect(reverse('webbaseche')) 
	

