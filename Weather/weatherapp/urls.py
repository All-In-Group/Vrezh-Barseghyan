from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:info_id>', views.info, name='info'),
    path('api/city', views.get_city_by_id, name='city')
]
