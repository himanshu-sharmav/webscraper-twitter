from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run_script/', views.run_script, name='run_script'),
    
]
