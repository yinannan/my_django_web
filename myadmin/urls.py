from django.conf.urls import url
from . import views,viewsgoods,viewsorders

urlpatterns = [

#----------------------------------登陆--------------------------------------

	url(r'^login$', views.adminLogin, name="adminLogin"),#登陆跳转
	url(r'^dologin$', views.adminDologin, name="adminDologin"),#登陆执行
    url(r'^logout$', views.adminLogout, name="adminLogout"),#退出
    url(r'^help$', views.help, name="help"),#帮助
    url(r'^yanzhengma$', views.yanzhengma, name="yanzhengma"),#验证码
   
#----------------------------------会员信息---------------------------------------

    url(r'^$', views.adminIndex, name="adminIndex"),#后台首页
    url(r'^see/(?P<pIndex>[0-9]*)$', views.adminSee, name="adminSee"),#浏览
    url(r'^add$', views.adminAdd, name="adminAdd"),#添加表单
    url(r'^insert$', views.adminInsert, name="adminInsert"),#添加数据
    url(r'^del/(?P<uid>[0-9]+)$', views.adminDel, name="adminDel"),#删除
    url(r'^edit/(?P<uid>[0-9]+)$', views.adminEdit, name="adminEdit"),#编辑页面
    url(r'^update$', views.adminupdate, name="adminupdate"),#更新数据  

    url(r'^editpass/(?P<uid>[0-9]+)$', views.admineditpass, name="admineditpass"),#修改密码
    url(r'^updatepass$', views.updatepass, name="updatepass"),#执行密码修改

#-----------------------------------商品类别信息--------------------------------------

    url(r'^typeliu$', viewsgoods.typeliu, name="typeliu"),
    url(r'^typeadd/(?P<tid>[0-9]*)$', viewsgoods.typeadd, name="typeadd"),
    url(r'^typeinsert$', viewsgoods.typeinsert, name="typeinsert"),
    url(r'^typedel/(?P<uid>[0-9]+)$', viewsgoods.typedel, name="typedel"),
    url(r'^typeedit/(?P<uid>[0-9]+)$', viewsgoods.typeedit, name="typeedit"),
    url(r'^typeupdate/(?P<tid>[0-9]+)$', viewsgoods.typeupdate, name="typeupdate"), 

#------------------------------------商品信息-------------------------------------

    url(r'^goodssee/(?P<pIndex>[0-9]*)$', viewsgoods.goodssee, name="goodssee"),
    url(r'^goodsadd$', viewsgoods.goodsadd, name="goodsadd"),
    url(r'^goodsinsert$', viewsgoods.goodsinsert, name="goodsinsert"),
    url(r'^goodsdel/(?P<uid>[0-9]+)$', viewsgoods.goodsdel, name="goodsdel"),
    url(r'^goodsedit/(?P<uid>[0-9]+)$', viewsgoods.goodsedit, name="goodsedit"),
    url(r'^goodsupdate$', viewsgoods.goodsupdate, name="goodsupdate"), 

#---------------------------------------订单信息----------------------------------

    url(r'^orderssee/(?P<pIndex>[0-9]+)$', viewsorders.orderssee, name="orderssee"),
    url(r'^orderdetail/(?P<oid>[0-9]+)$', viewsorders.orderdetail, name="orderdetail"),
    url(r'^orderedit/(?P<uid>[0-9]+)$', viewsorders.orderedit, name="orderedit"),
    url(r'^orderdoedit$', viewsorders.orderdoedit, name="orderdoedit"), 
    
]
