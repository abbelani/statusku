# from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
#from django.template.defaultfilters import slugify


class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
   # title = models.CharField(max_length=200)
   # slug = models.SlugField()
    body = models.TextField()

    #def __unicode__(self):
       # return self.title

    def save(self, *args, **kwargs):
        return super(Note, self).save(*args, **kwargs)
