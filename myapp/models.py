# -*- coding: utf-8 -*-
from django.db import models

class myapp(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish_date = models.DateTimeField('published date')
    gPlus = models.IntegerField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


