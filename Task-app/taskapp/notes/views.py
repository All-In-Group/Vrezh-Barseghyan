from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.forms import ModelForm
# Create your views here.
from .models import NewTaskForm, EditField, Notes
import numpy as np


def index(request):
    tasks = NewTaskForm.objects.all()
    return render(request, "notes/index.html", {
        "tasks": tasks
    })



def add(request):
    if request.method == "POST":
        task = request.POST["task"]
        if task == '':
            return HttpResponseRedirect(reverse("add"))
        ins = NewTaskForm(task=task)
        ins.save()
    else:
        return render(request, "notes/add.html", )
    return render(request, "notes/add.html", )


def note(request, note_id):
    note = NewTaskForm.objects.get(pk=note_id)
    return render(request, "notes/note.html", {
        "task": note
    })

def update(request, note_id):
    if request.method == "POST":
        old_task = NewTaskForm.objects.get(pk=note_id)
        task_text = request.POST["edit"]
        old_task.task = task_text
        old_task.save()
    return HttpResponseRedirect(reverse("index"))


def delete(request, note_id):
    if request.method == "POST":
        this_task = NewTaskForm.objects.get(pk = note_id)
        this_task.delete()
    return HttpResponseRedirect(reverse("index"))


# del request.session["tasks"][0]


# sarqel task.id taskeri hamar hanel note
