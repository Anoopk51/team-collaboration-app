from django.db import models
from django.conf import settings

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length = 100 , unique = True)
    description = models.TextField(blank = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.PROTECT)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


# for joinRequest

STATUS_CHOICES = [("PENDING","Pending"),
                  ("APPROVED","Approved"),
                  ("REJECTED","Rejected")]

class JoinRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.PROTECT)
    team = models.ForeignKey("Team" , on_delete= models.PROTECT)
    status = models.CharField(max_length= 10 , choices= STATUS_CHOICES , default= "PENDING")
    requested_at = models.DateTimeField(auto_now_add= True)
    reviewed_at = models.DateTimeField(null = True ,blank= True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete= models.PROTECT, null = True , blank = True, related_name = 'reviewed_requests'
    )

    def __str__(self):
        return f"{self.user.username} -> {self.team.name} ({self.status})"
