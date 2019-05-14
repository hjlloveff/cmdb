#encoding: utf-8

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import datetime
class iteminfo(models.Model):
     id = models.AutoField(primary_key= True,blank=True)
     name = models.CharField(max_length=64,null=False,unique=True,blank=True)
     iteminfo = models.CharField(max_length=64, null=False, unique=True,blank=True)

class hostaccessinfo(models.Model):
     id = models.AutoField(primary_key= True)
     name = models.CharField(max_length=64,null=False,unique=True)
     accessinfo = models.CharField(max_length=64, null=True, unique=True)
     feiyong = models.FloatField(max_length=64, null=True, blank=True)


class hostinfo(models.Model):
      id = models.AutoField(primary_key= True)
      name = models.CharField(max_length=128,null=True,unique=True)
      hostname = models.CharField(max_length=128,null=True,unique=True)
      sn = models.CharField(max_length=128,null=True,unique=True)
      expire_date = models.DateField(null=True,blank=True)
      inip = models.CharField(max_length=128,null=True,unique=True)
      outip = models.CharField(max_length=128,null=True,unique=True)
      weihuren = models.CharField(max_length=128,null=True,unique=True)
      neicun = models.CharField(max_length=64, null=True, unique=True)
      cpu = models.CharField(max_length=64, null=True, unique=True)
      shujuzhongxin = models.CharField(max_length=128, null=True)
      xiangmu = models.CharField(max_length=128, null=True)
      hostaccsess_id = models.ForeignKey(to="hostaccessinfo",to_field="id",on_delete=models.CASCADE,null=True)
      hostitem_id = models.ForeignKey(to="iteminfo",to_field="id",on_delete=models.CASCADE,null=True)
