from django.urls import path
from . import views

app_name='dict_pad'

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download, name='download')
]
