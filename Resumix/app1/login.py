import re

from django.http import HttpResponse
from .models import SigninModel




def login(request):
    if request.method =="POST":
        email = request.POST['email']
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            pass
        else:
            return HttpResponse("invalid email")
        password = request.POST['password']
        s = SigninModel.objects.all()
        list = []
        for i in s:
            list.append(i.email)
            list.append(i.password)
        if email in list:
            return HttpResponse(" your successfully login ")
        else:
            return HttpResponse(" pls first signin")