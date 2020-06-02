from django.urls import include, path

from . import views

urlpatterns = [
    path('mosaic', views.mosaic_page, name='mosaic_page'),
    path('mosaic/request', views.mosaic, name='mosaic'),
]