from django.db import models

class Jone(models.Model):
    name =  models.CharField(max_length=60 , verbose_name="الاسم الكامل" )
    email = models.EmailField(unique=True ,  verbose_name="البريد الإلكتروني")
    phone = models.IntegerField(null=True , blank=True , verbose_name="رقم الهاتف")
    skills = models.CharField(max_length=100 ,  verbose_name="المهارات")
    experience = models.CharField(max_length=120, verbose_name="الخبرة")
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "متقدم"
        verbose_name_plural = "المتقدمين"
    
class Register(models.Model):
    firstname = models.CharField(max_length=50 , verbose_name="name" )
    username = models.CharField(max_length=50 , verbose_name="username" )
    email = models.EmailField(  unique=True , max_length=50 , verbose_name="name" )
    password = models.CharField(max_length=20 , verbose_name='password')

    def __str__(self):
        return self.username
    
    def __str__(self):
        return self.password
    
    
    def __str__(self):
        return self.email
    

class Logins(models.Model):
    username = models.CharField(max_length=23 , verbose_name="username")
    password = models.CharField(max_length=23 , verbose_name="password")

    def __str__(self):
        return self.username
    
    def __str__(self):
        return self.password
    

    
    
