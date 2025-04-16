from django.db import models


class studentlist(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    guardian_name = models.CharField(max_length=30)
    classs = models.IntegerField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
