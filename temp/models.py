from django.db import models


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=200, verbose_name='Information')
    year = models.DateField(verbose_name='year')
    info = models.TextField(verbose_name='Information')

    def __str__(self):
        return self.name

