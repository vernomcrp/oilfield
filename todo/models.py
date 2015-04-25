from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User)
    task = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return u"{task} by {user}".format(task=task, user=user)
    
    