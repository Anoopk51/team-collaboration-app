from django.db import models
from django.conf import settings


# Create your models here.

PRIORITY_CHOICES = [
    ("LOW","Low"),
    ("MEDIUM","Medium"),
    ("HIGH","High"),
]

TASK_STATUS = [
    ("TODO" , "To Do"),
    ("IN_PROGRESS" , "In Progress"),
    ("DONE" , "Done"),
]

class Task(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project','title'] , name = "unique_task_per_project")
        ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    project = models.ForeignKey("projects.Project" ,on_delete= models.PROTECT)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.PROTECT,
                                    null=True,
                                    blank=True,
                                    related_name="assigned_tasks")
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL , 
                                    on_delete= models.PROTECT,
                                    related_name="created_tasks")
    
    status = models.CharField(max_length=11 ,choices= TASK_STATUS , default="TODO")
    priority = models.CharField(max_length=10 ,choices= PRIORITY_CHOICES ,default="MEDIUM")
    due_date = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return f"{self.project.name} -->  {self.title}"
