from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Resume, SigninModel

def home(request):
    return HttpResponse("home page")


def resumes(request):
    data = Resume.objects.all()
    list = []
    for i in data:
        resume = {'name': i.name, 'DOB': i.DOB, 'gender': i.gender, 'locality': i.locality, 'city': i.city,
                  'strength': i.strength, 'experience': i.experience, 'pin': i.pin, 'state': i.state,
                  'mobile': i.mobile, 'email': i.email, 'job_city': i.job_city}
        list.append(resume)
    dict = {'resumes': list, 'total_resumes': 2}
    return JsonResponse(dict)


def resume_id_list():
    data = Resume.objects.all()
    list = []
    for i in data:
        list.append(i.id)
    return list

def resume(request,id):
    list = resume_id_list()
    # data = Resume.objects.get(id=id)
    if id in list:
        data = Resume.objects.get(id=id)
        resume = {'name': data.name, 'DOB': data.DOB, 'gender': data.gender, 'locality': data.locality, 'city': data.city,
              'strength': data.strength, 'experience': data.experience, 'pin': data.pin, 'state': data.state,
              'mobile': data.mobile, 'email': data.email, 'job_city': data.job_city}
        list = [resume]
        dict = {'resume': list}
        return JsonResponse(dict)
    else:
        return HttpResponse("This id  {}  resume is not available".format(id))

def resume_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        DOB = request.POST['DOB']
        gender = request.POST['gender']
        locality = request.POST['locality']
        # strenght = request.GET['strength']
        experience = request.POST['experience']
        pin = request.POST['pin']
        state = request.POST['state']
        mobile= request.POST['mobile']
        email = request.POST['email']
        job_city = request.POST['job_city']
        # profile_image = request.GET['profile_image']
        # my_file= request.GET['my_file']
        data = Resume(name=name,DOB=DOB,gender=gender,locality=locality,
                  experience=experience,pin=pin,state=state,mobile=mobile,email=email,
                  job_city=job_city)
        data.save()
        return HttpResponse("create your resume")

def edit(request, pk):
    try:
        resume = Resume.objects.get(id=pk)
    except Resume.DoesNotExist:
        return HttpResponse("This resume does not exist")

    if request.method == 'POST':
        name = request.POST.get('name', resume.name)
        DOB = request.POST.get('DOB', resume.DOB)
        gender = request.POST.get('gender', resume.gender)
        locality = request.POST.get('locality', resume.locality)
        city = request.POST.get('city', resume.city)
        strength = request.POST.get('strength', resume.strength)
        experience = request.POST.get('experience', resume.experience)
        pin = request.POST.get('pin', resume.pin)
        state = request.POST.get('state', resume.state)
        mobile = request.POST.get('mobile', resume.mobile)
        email = request.POST.get('email', resume.email)
        job_city = request.POST.get('job_city', resume.job_city)

        resume.name = name
        resume.DOB = DOB
        resume.gender = gender
        resume.locality = locality
        resume.city = city
        resume.strength = strength
        resume.experience = experience
        resume.pin = pin
        resume.state = state
        resume.mobile = mobile
        resume.email = email
        resume.job_city = job_city

        # save the updated resume object to the database
        resume.save()

        return HttpResponse("Resume updated successfully")