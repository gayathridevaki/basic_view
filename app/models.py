from django.db import models


# Create your models here.
class school(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)

    def __str__(self):
        return self.sname