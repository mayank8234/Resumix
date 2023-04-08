import re
from django.http import HttpResponse
from .models import SigninModel


def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        mobile = request.POST['mobile']
        email = request.POST['email']
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            pass
        else:
            return HttpResponse("invalid email")
        s = SigninModel.objects.all()
        list=[]
        for i in s:
            list.append(i.email)
        if email not in list:
            password = request.POST['password']
            obj = SigninModel(name=name, location=location, mobile=mobile, email=email, password=password)
            obj.save()
            return HttpResponse("Successfully Signin")
        else:
            return HttpResponse("already signin please log in  ")





