from django.db import models

# Create your models here.
class Data(models.Model):

    accno = models.IntegerField(unique=True)
    name = models.CharField(max_length=264,unique=False)
    contact = models.CharField(max_length=264,unique=False)
    email = models.EmailField(max_length=264,unique=True)
    addr = models.CharField(max_length=500,unique=False)
    city = models.CharField(max_length=500,unique=False)
    state = models.CharField(max_length=500,unique=False)
    zip = models.CharField(max_length=500,unique=False)
    password = models.CharField(max_length=4,unique=True,default="0000")

    def __str__(self):
        return str(self.fname)


'''
class Update(models.Model):

    accno = models.ForeignKey(Data, on_delete=models.PROTECT)
    balance = models.FloatField(unique=False)
    def __str__(self):
        return str(self.balance)
'''
