from django.db import models
from NA.validators import validate_file_extension
# Create your models here.
class Customer(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=30)

class Resume(models.Model):
    file = models.FileField(validators=[validate_file_extension])
