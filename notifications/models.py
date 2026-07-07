from django.db import models
from django.conf import settings
# Create your models here.


NOTIFICATION_CHOICES = [
    ("TASK_ASSIGNED","Task_Assigned"),
    ("COMMENT_ADDED","Comment_Added"),
    ("JOIN_APPROVED","Join_Approved"),
]
class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.PROTECT , related_name= 'notifications')

    message = models.TextField()

    notification_type = models.CharField(max_length=14, choices=NOTIFICATION_CHOICES , default="COMMENT_ADDED")

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} --> {self.notification_type}"