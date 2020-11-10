import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from .models import NewTaskForm


def index(request):
    tasks = NewTaskForm.objects.all()
    # add_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render(request, "notes/index.html", {
        "tasks": tasks,
    })


def add(request):
    if request.method == "POST":
        task = request.POST["task"]
        description = request.POST["description"]
        if task == '' or description == '':
            return HttpResponseRedirect(reverse("add"))
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ins = NewTaskForm(task_title=task,
                          task_description=description,
                          creation_date=time,
                          last_modified=time)
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
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        old_task.last_modified = time
        task_description = request.POST["description"]
        if task_description != '':
            old_task.task_description = task_description
        if task_text != '':
            old_task.task_title = task_text
        old_task.save()
    return HttpResponseRedirect(reverse("index"))


def delete(request, note_id):
    if request.method == "POST":
        this_task = NewTaskForm.objects.get(pk=note_id)
        this_task.delete()
    return HttpResponseRedirect(reverse("index"))
