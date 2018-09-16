from django.db import models


class Log(models.Model):
    request = models.CharField(max_length=1028)
    response = models.CharField(max_length=1018)
    date = models.DateTimeField(auto_now_add=True)