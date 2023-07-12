from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phoneNumber=models.CharField(max_length=120)
    date=models.DateField()
    

    def __str__(self):
        return self.name
class OptionInfo(models.Model):
    type=models.CharField(max_length=30)
    pass


    