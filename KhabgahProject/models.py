from django.db import models

# Create your models here.

class myuser(models.Model):
    fn=models.CharField(max_length=50)
    ln=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    un=models.CharField(max_length=30)
    pw=models.CharField(max_length=50)

class myuserh(models.Model):
    fn=models.CharField(max_length=50)
    ln=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    un=models.CharField(max_length=30)
    pw=models.CharField(max_length=50)
    num=models.CharField(max_length=50)
    serial=models.CharField(max_length=50)

class myadmin(models.Model):
    email=models.Field(max_length=50)
    pw=models.Field('9012606043')



#
# class RSS(models.Model):
#     Link = models.CharField(max_length=150)
#     Agency = models.CharField(max_length=50)
#     Category = models.CharField(max_length=50)
#     g=models.CharField(max_length=20)





