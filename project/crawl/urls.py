from django.contrib import admin
from django.urls import path
from . import views, views_register, views_extra

urlpatterns = [
	path('get/', views.crawlBlogs, name = 'crawlBlogs'),
	path('register/', views_register.signUp, name = 'signUp'),
	path('login/', views_register.login, name = 'login'),
	path('logout/', views_register.logout, name = 'logout'),
	path('get/<str:tag>', views.getBlogs, name = 'getBlogs'),
	path('show/', views.showHistory, name = 'showHistory'),
	path('auto/<str:word>', views_extra.autoComplete, name = 'autoComplete'),
	path('typo/<str:word>', views_extra.typoSuggest, name = 'typoSuggest')
]