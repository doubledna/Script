# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class DmModels(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100, null = False)
    url = models.CharField(max_length = 200, null = False)
