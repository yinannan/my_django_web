from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import re

class AdminMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        urllist = ['/myadmin/login','/myadmin/logout','/myadmin/dologin','/myadmin/yanzhengma']
        path = request.path
        if re.match("/myadmin",path) and (path not in urllist):
            if "adminuser" not in request.session:
                return redirect(reverse('adminLogin'))
        response = self.get_response(request)
        return response
       
