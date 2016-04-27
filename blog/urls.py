'''
Created on 27/04/2016

@author: seacosta
'''
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]