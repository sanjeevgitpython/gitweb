from django.db import models

# Create your models here.
class Links(models.Model):
    adress=models.CharField(max_length=500,null=True,blank=True)
    strname=models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.strname
