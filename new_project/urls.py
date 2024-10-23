from django.contrib import admin
from django.urls import path
from new_app import views
from dotenv import load_dotenv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
