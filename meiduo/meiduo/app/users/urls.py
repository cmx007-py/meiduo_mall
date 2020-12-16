from django.contrib import admin
from django.urls import path,include,re_path
from . import views
import re

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    re_path(r'^username/(?P<username>[a-zA-Z0-9_-]{5,20})/count/',views.UsernameCountView.as_view())
]