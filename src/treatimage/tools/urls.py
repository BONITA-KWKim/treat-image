from django.urls import include, path

from . import views

urlpatterns = [
    path('request/mosaic', views.mosaic, name='mosaic'),
]