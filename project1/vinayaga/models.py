from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class detail(models.Model):
    Company_name=models.CharField(max_length=40)
    Company_address=models.CharField(max_length=100)
    Landmark=models.CharField(max_length=40)
    District=models.CharField(max_length=15)
    State=models.CharField(max_length=15)
    Pincode=models.IntegerField()
    Mobile_number=models.IntegerField()
    Email=models.EmailField(max_length=20)
    Machine_name=models.CharField(max_length=30)
    Machine_condition=models.TextField(max_length=1000)
    Price=models.IntegerField()
    Image = models.ImageField(upload_to='images/', default="")
    

class buyer(models.Model):
    Company_name=models.CharField(max_length=40)
    Person_name=models.CharField(max_length=40)
    Email=models.CharField(max_length=20)
    Address=models.TextField(max_length=1000)
    Mobile_number=models.IntegerField()