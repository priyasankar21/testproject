from django.db import models


class contact(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    desc=models.TextField(max_length=1000)


        