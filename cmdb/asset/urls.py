#encoding: utf-8
from django.urls import path

from . import views

app_name = 'asset'
urlpatterns = [
    path('', views.index, name='index'),
    path('hostinfo/', views.hostinfo, name="hostinfo"),
    path('jifang/', views.jifang, name="jifang"),
    path('alihost/', views.alihost, name="alihost"),
    path('detail-<nid>/', views.detail),
    path('edit-<nid>/', views.edit),
]
