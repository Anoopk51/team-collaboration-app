from django.db import models
from users.models import User


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length = 100 , unique = True)
    description = models.TextField(blank = True)
    created_by = models.ForeignKey(User , on_delete = models.PROTECT)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
