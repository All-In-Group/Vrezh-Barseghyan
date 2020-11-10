from django.db import models


# Create your models here.
class NewTaskForm(models.Model):
    task_title = models.TextField(max_length=64)
    task_description = models.TextField(max_length=256)
    creation_date = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
