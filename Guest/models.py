from django.db import models
from Admin.models import *
from Guest.models import *

class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=30)
    user_gender=models.CharField(max_length=15)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=150)
    user_photo=models.FileField( upload_to="Assets/user/photo")
    place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    
class tbl_newuser(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=70)
    user_password=models.CharField(max_length=30)
    