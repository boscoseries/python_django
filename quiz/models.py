from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(
        max_length=200, verbose_name='description', null=True)
created_date = models.DateField(auto_now=True)
url = models.URLField(verbose_name='url', null=True)