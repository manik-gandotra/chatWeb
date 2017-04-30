from django.conf.urls import include, url
from . import views
import django

urlpatterns = [
	url(r'^$',  views.about, name='about'),
	url(r'^new/$', views.new_room, name='new_room'),
	url(r'^create_room/$', views.create_room, name='create_room'),
	url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
	url(r'^accounts/register/$', views.register, name='register'),
	url(r'^accounts/register/complete/$', views.registration_complete,name='registration_complete'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
	url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
]
