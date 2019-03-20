from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import re

class WebMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        path = request.path
        urllist = ['/myweb/baseche',]
        if re.match("/myweb",path) and (path  in urllist):
            if "user" not in request.session :
                return redirect(reverse('weblogin'))
        response = self.get_response(request)
        return response

       
