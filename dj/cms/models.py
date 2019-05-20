from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=23)
    phone = models.CharField(max_length=23)
    adder = models.CharField(max_length=23)

    def __str__(self):
        return self.id