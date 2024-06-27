from django.contrib import admin 
from django.urls import path 
from resume.views import *

urlpatterns = [ 
	path('', home, name = 'home'), 
	path('resume/', gen_resume, name = 'resume'), 
	path("admin/", admin.site.urls), 
] 
