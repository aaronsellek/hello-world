from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    intro = models.TextField(null=True
    
    def __str__(self):
        return self.name

