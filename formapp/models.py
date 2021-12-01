from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Student(models.Model):
    first_name = models.CharField(primary_key=True, max_length=40)
    last_name = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=40, null=True)
    zipcode = models.CharField(max_length=5, null=True)

class NewForm(models.Model):
    first_name = models.CharField(primary_key=True, max_length=40)
    last_name = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=40, null=True)
    #zipcode = models.CharField(validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')], max_length=4, null=True)
    #zipcode = models.IntegerField(min_length=5, max_length=5, null=True)
    #zipcode = models.IntegerField(validators=[MaxLengthValidator(5),MinLengthValidator(5)], null=True)
    zipcode = models.CharField(max_length=5, null=True)
