from django.contrib import admin

from .models import Resume, SigninModel

class SigninAdmin(admin.ModelAdmin):
    list_display= ['name']


admin.site.register(Resume)
admin.site.register(SigninModel,SigninAdmin)
