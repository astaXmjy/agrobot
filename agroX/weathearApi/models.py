
from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.CharField(max_length=300)
