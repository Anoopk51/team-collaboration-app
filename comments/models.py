from django.db import models
from django.conf import settings
# Create your models here.

class Comment(models.Model):
    task = models.ForeignKey('tasks.Task' , on_delete = models.PROTECT , related_name = "comments")

    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.PROTECT , related_name = "comments")

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.user.username} --> {self.task.title}"
