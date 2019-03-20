from django.conf.urls import url
from . import views,viewsorders

urlpatterns = [

#--------------------------------------登陆+注册---------------------------------------

	url(r'^login/$', views.weblogin, name="weblogin"),#登陆
	url(r'^dologin/$', views.webdologin, name="webdologin"),#执行登陆
	url(r'^logout/$', views.weblogout, name="weblogout"),#退出
	url(r'^webzhuce$', views.webzhuce, name="webzhuce"),#跳转注册
	url(r'^webdozhuce$', views.webdozhuce, name="webdozhuce"),#执行注册
	url(r'^webquit$', views.webquit, name="webquit"),#注册先退出
	url(r'^webin$', views.webin, name="webin"),#退出先登录
	url(r'^webyanzhengma$', views.webyanzhengma, name="webyanzhengma"),#验证码

#--------------------------------------个人中心---------------------------------------

	url(r'^webmyself$', viewsorders.webmyself, name="webmyself"),#个人中心
	url(r'^webmyselfdetail/(?P<oid>[0-9]*)$', viewsorders.webmyselfdetail, name="webmyselfdetail"),#个人中心
	url(r'^webmyselfedit/(?P<uid>[0-9]*)$', viewsorders.webmyselfedit, name="webmyselfedit"),#修改个人中心
	url(r'^webmyselfdoedit$', viewsorders.webmyselfdoedit, name="webmyselfdoedit"),#执行修改个人中心
	url(r'^webmyselfeditpass/(?P<aid>[0-9]*)$', viewsorders.webmyselfeditpass, name="webmyselfeditpass"),#个人中心密码修改
	url(r'^webmyselfdoeditpass$', viewsorders.webmyselfdoeditpass, name="webmyselfdoeditpass"),#执行个人中心密码修改
	url(r'^webmyselfshouhuo/(?P<oid>[0-9]*)$', viewsorders.webmyselfshouhuo, name="webmyselfshouhuo"),#执行个人中心收货
	
#--------------------------------------前台---------------------------------------

	url(r'^$', views.webIndex, name="webIndex"),#前台首页
	url(r'^list$', views.weblist, name="weblist"),#前台首页
	url(r'^list/(?P<tid>[0-9]*)$', views.weblist, name="weblist2"),#前台列表
	url(r'^detail/(?P<tid>[0-9]*)$', views.webdetail, name="webdetail"),#前台商品详情

#--------------------------------------购物车---------------------------------------

	url(r'^che/(?P<tid>[0-9]*)$', views.webche, name="webche"),#前台购物车
	url(r'^baseche$', views.webbaseche, name="webbaseche"),#前台购物车
	url(r'^clearche$', views.webclearche, name="webclearche"),#清空购物车
	url(r'^delche/(?P<tid>[0-9]*)$', views.webdelche, name="webdelche"),#删除购物车

#--------------------------------------订单---------------------------------------	

	url(r'^orders$', viewsorders.orders,name='orders'), #订单浏览
    url(r'^ordersconfirm$', viewsorders.ordersconfirm,name='ordersconfirm'), #订单确认
    url(r'^ordersinsert$', viewsorders.ordersinsert,name='ordersinsert'), #执行订单添加
    url(r'^ordersinfo$', viewsorders.ordersinfo,name='ordersinfo'), #订单信息
    url(r'^beend$', viewsorders.beend, name="beend"),#订单结束
    url(r'^endche$', viewsorders.endche, name="endche"),#结帐购物车
    url(r'^nobuy$', viewsorders.nobuy, name="nobuy"), #没有购买提示

]