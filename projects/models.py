from django.db import models
from django.conf import settings

# Create your models here.
PROJECT_STATUS = [
    ("PLANNING" ,"Planning"),
    ("ACTIVE","Active"),
    ("COMPLETED","Completed"),
    ("ON_HOLD" , "On Hold"),
]
class Project(models.Model):

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["team","name"],
                name="unique_project_per_team",
            )
        ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    team = models.ForeignKey("teams.Team", on_delete= models.PROTECT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    status = models.CharField(max_length=15,
                              choices=PROJECT_STATUS,
                              default="PLANNING")
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}--> {self.created_by.username}"
