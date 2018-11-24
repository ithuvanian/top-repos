from django.urls import path

from . import views

app_name = 'lists'
urlpatterns = [
    path('<str:lang>/', views.index, name='index'),
]
