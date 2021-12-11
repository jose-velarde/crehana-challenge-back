from django.db import models

# Create your models here.
class Person(models.Model):
    # DO NOT EDIT
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=7)
    created_date = models.DateTimeField()
    def __str__(self):
        return self.first_name + " " + self.last_name
