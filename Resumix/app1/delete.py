from django.http import JsonResponse, HttpResponse

from .models import Resume


def resume_delete(request, pk):
    try:
        resume = Resume.objects.get(id=pk)
    except Resume.DoesNotExist:
        return HttpResponse("This resume does not exist")
    Resume.objects.filter(id=pk).delete()
    return HttpResponse("successfully delete your resume")