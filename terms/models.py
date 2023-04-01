from django.db import models

# Create your models here.

# terms/models.py


class Keyword(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name