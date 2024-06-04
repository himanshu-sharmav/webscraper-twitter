from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('run_script/', views.run_script, name='run_script'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

