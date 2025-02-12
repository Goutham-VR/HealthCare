from django.db import models
from datetime import date
from Guest.models import *

class tbl_mystatus(models.Model):
    mystatus_age = models.CharField(max_length=10)
    mystatus_height=models.CharField(max_length=10)
    mystatus_weight=models.CharField(max_length=10)
    mystatus_bloodgroup=models.CharField(max_length=10)
    mystatus_bmi=models.CharField(max_length=10)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    
class tbl_complaint(models.Model):
    comp_subject=models.CharField(max_length=100)
    comp_details=models.CharField(max_length=500)
    comp_date=models.DateField(auto_now_add=True)
    comp_reply=models.CharField(max_length=500, null=True)
    comp_reply_date=models.DateField(null=True)
    comp_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)