from django.contrib import admin
from .models import NewTaskForm, EditField, Notes

# Register your models here.
admin.site.register(NewTaskForm)
admin.site.register(EditField)
admin.site.register(Notes)