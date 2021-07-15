from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):

    longLink = models.TextField()
    hash = models.TextField()
    clicks = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now=True)
    linkId = models.IntegerField(primary_key=True)

