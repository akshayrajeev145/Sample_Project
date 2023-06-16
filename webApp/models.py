from django.db import models

# Create your models here.

class usersignupDB(models.Model):
    userName = models.CharField(max_length=100,null=True,blank=True)
    userEmail = models.EmailField(max_length=100,null=True,blank=True)
    userMobile = models.IntegerField(null=True,blank=True)
    userPassword = models.CharField(max_length=100,null=True,blank=True)
    userImage = models.ImageField(upload_to="userProfile",null=True,blank=True)



class contactDB(models.Model):
    contactName = models.CharField(max_length=100,null=True,blank=True)
    contactEmail = models.CharField(max_length=100,null=True,blank=True)
    contactSubject = models.CharField(max_length=100,null=True,blank=True)
    contactMessage = models.CharField(max_length=1000,null=True,blank=True)

class cartDB(models.Model):
    cartUserName = models.CharField(max_length=100,null=True,blank=True) 
    cartName = models.CharField(max_length=100,null=True,blank=True)
    cartDescription = models.CharField(max_length=1000,null=True,blank=True)
    cartQuandity = models.IntegerField(null=True,blank=True)
    cartPrice = models.IntegerField(null=True,blank=True)


class checkoutBD(models.Model):
    checkoutName = models.CharField(max_length=100,null=True,blank=True) 
    checkoutEmail = models.CharField(max_length=100,null=True,blank=True) 
    checkoutNumber = models.CharField(max_length=100,null=True,blank=True) 
    checkoutAddress = models.CharField(max_length=1000,null=True,blank=True) 
    checkoutCountry = models.CharField(max_length=100,null=True,blank=True) 
    checkoutState = models.CharField(max_length=100,null=True,blank=True) 





