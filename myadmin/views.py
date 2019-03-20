from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Users,Type
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import time,json

#---------------------------登录退出----------------------------

#登陆
def adminLogin(request):
	return render(request,"myadmin/login.html")

#登录执行
def adminDologin(request):
	verifycode = request.session['verifycode']
	code = request.POST['code']
	if verifycode != code:
		context = {'info':'验证码错误！'}
		return render(request,"myadmin/login.html",context)
	try:
		user = Users.objects.get(username = request.POST['usersname'])
		if user.state == 0:
			import hashlib
			m = hashlib.md5() 
			m.update(bytes(request.POST['password'],encoding="utf8"))
			if user.password == m.hexdigest():
				request.session['adminuser'] = user.username
				return redirect(reverse('adminIndex'))
			else:
				context = {'info':'登录密码错误！'}
		else:
			context = {'info':'此用户非管理员用户！'}
	except:
		context = {'info':'用户名不存在！'}
	return render(request,"myadmin/login.html",context)

#退出
def adminLogout(request):
	del request.session['adminuser']
	return redirect(reverse('adminLogin')) 

#帮助
def help(request):
	return render(request,"myadmin/help.html")

#验证码
def yanzhengma(request):
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
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
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

#---------------------------------end 登录退出---------------------------------------

#后台首页
def adminIndex(request):
	return render(request,"myadmin/index.html")


#--------------------------------会员---------------------------------------

#浏览
def adminSee(request,pIndex):
	list = Users.objects.filter()
	#实例化分页
	p = Paginator(list,10)
	if pIndex == '':
		pIndex = '1'
	pIndex = int(pIndex)
	list2 = p.page(pIndex)
	plist = p.page_range
	return render(request,"myadmin/users/see.html",{'userslist':list2,'pIndex':pIndex,'plist':plist})

#添加表单
def adminAdd(request):
	return render(request,"myadmin/users/add.html")

#执行添加
def adminInsert(request):
	try:
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
		ob.state = request.POST['state']
		ob.addtime = request.POST['addtime']
		ob.save()
		context = {'info':'添加成功'}
	except:
		context = {'info':'添加失败'}
	return render(request,"myadmin/users/info.html",context)

#删除
def adminDel(request,uid):
	try:
		ob = Users.objects.get(id = uid)
		ob.delete()
		context = {'info':'删除成功!'}
	except:
		context = {'info':'失败!'}
	return render(request,"myadmin/users/info.html",context)

#编辑
def adminEdit(request,uid):
	ob = Users.objects.get(id = uid)
	context = {'users':ob}
	return render(request,"myadmin/users/edit.html",context)

#执行编辑
def adminupdate(request):
	try:
		ob = Users.objects.get(id = request.POST['id'])
		ob.username = request.POST['username']
		ob.sex = request.POST['sex']
		ob.adress = request.POST['adress']
		ob.code = request.POST['code']
		ob.phone = request.POST['phone']
		ob.email = request.POST['email']
		ob.state = request.POST['state']
		ob.addtime = request.POST['addtime']
		ob.save()
		context = {'info':'修改成功!'}
	except:
		context = {'info':'修改失败!'}
	return render (request,"myadmin/users/info.html",context)

#修改密码
def admineditpass(request,uid):
	ob = Users.objects.get(id = uid)
	context = {'users':ob}
	return render(request,"myadmin/users/editpass.html",context)

#执行密码修改
def updatepass(request):
	try:
		ob = Users.objects.get(id=request.POST['id'])
		import hashlib
		m = hashlib.md5() 
		m.update(bytes(request.POST['password'],encoding="utf8"))
		ob.password = m.hexdigest()
		ob.save()
		context = {'info':"密码修该成功！"}
	except:
		context = {'info':"密码修改失败！"}
	return render(request,"myadmin/users/info.html",context)

#------------------------end 会员信息-----------------------------------------




