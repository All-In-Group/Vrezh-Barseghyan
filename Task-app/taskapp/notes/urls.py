from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('<int:note_id>', views.note, name='note'),
    path('<int:note_id>/update', views.update, name='update'),
    path('<int:note_id>/delete', views.delete, name='delete'),

]
