from django.db import models

class List(models.Model):
    #list = models.TextField()
    pass

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List)

