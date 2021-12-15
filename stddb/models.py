from django.db import models

# Create your models here.
class studentInfo(models.model):
    fname = models.CharField(max_length=50)
    mname =  models.CharField(max_length=50)
    lname =  models.CharField(max_length=50)
    rno = models.IntegerField()
    mobile = models.BigIntegerFields()



