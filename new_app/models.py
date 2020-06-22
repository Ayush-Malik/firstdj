from django.db import models

# Create your models here.


class Contact(models.Model):

    name = models.CharField(max_length=122 , null = True)
    email = models.EmailField(max_length=122 , null = True)
    phone = models.CharField(max_length=122 , null = True)
    dropdown = models.CharField(max_length =122)
    desc  = models.TextField(null = True)
   

    def __str__(self): # Change The name of objects of Contact class
        return self.name
