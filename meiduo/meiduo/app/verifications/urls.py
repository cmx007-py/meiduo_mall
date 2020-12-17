from django.contrib import admin
from django.urls import path,include,re_path
from . import views
import re

urlpatterns = [
    re_path('image_codes/(?P<uuid>[\w-])',views.ImageCodeView.as_view()),

]