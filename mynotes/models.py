from django.db import models

# Create your models here.
class MyNotes(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField('Posted on')
