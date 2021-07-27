from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('/',views.index),
	path('/<int:course_id>',views.detail,name='detail'),
]