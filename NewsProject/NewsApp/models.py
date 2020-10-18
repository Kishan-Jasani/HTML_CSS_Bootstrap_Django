from django.db import models
# Create your models here.
class News(models.Model):
    news = models.CharField(max_length=150)

class Query_data(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

class Query_data1(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    query = models.CharField(max_length=200)

class Resume(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    file = models.FileField(upload_to='static/resume/%Y-%m-%d')
