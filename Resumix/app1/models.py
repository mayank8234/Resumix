from django.db import models

# Create your models here.
state_choices = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh ", "Arunachal Pradesh "),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"), ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"), ("Odisha", "Odisha"), ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"),
    ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"),
    ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))


class Resume(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    strength = models.CharField(max_length=200, default=True)
    experience = models.CharField(max_length=300, default=True)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=state_choices, max_length=100)
    mobile = models.PositiveIntegerField(default=True)
    email = models.EmailField(max_length=100)
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)


class SigninModel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.IntegerField()


# class Login(models.Model):
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
