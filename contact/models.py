from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=22)
    middle_name = models.CharField(max_length=18)
    last_name = models.CharField(max_length=22)
    email = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=13)
    active = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def deactivate(self):
        self.active = False;
        self.save()

    def __str__(self):
        return self.first_name + " " + self.last_name