from django.db import models

# Create your models here.
class NewTaskForm(models.Model):
    task = models.TextField(max_length=256)


class EditField(models.Model):
    change = models.TextField(max_length=256)

class Notes(models.Model):
    taskname = models.ForeignKey(NewTaskForm, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

