from django.db import models


class SignUp(models.Model):
    username = models.CharField(max_length=50)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    email =models.EmailField()
    phone = models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    re_password=models.CharField(max_length=50)

    
    def __str__(self):
       return f'{self.username}-{self.email}'

class survey(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    age= models.IntegerField()
    phone= models.CharField(max_length=10)
    Suffer = models.CharField(max_length=10)
    Vaccine = models.CharField(max_length=10)
    Getout = models.CharField(max_length=10)
    Symptoms = models.CharField(max_length=10)
    Vaccinate = models.CharField(max_length=10)
    Doses = models.CharField(max_length=10)
    Dosesymptoms = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)

    def __str__(self):
       return f'{self.name}-{self.phone}'
           
