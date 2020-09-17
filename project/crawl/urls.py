from django.contrib import admin
from django.urls import path
from . import views, views_register

urlpatterns = [
	path('get/', views.crawlBlogs, name = 'crawlBlogs'),
	path('register/', views_register.signUp, name = 'signUp'),
	path('login/', views_register.login, name = 'login'),
	path('logout/', views.logout, name = 'logout'),
	path('get/<str:tag>', views.getBlogs, name = 'getBlogs'),
	path('show/', views.showHistory, name = 'showHistory'),
	path('auto/<str:word>', views.autoComplete, name = 'autoComplete')
]