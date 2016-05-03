from django.conf.urls import patterns, include
from django.conf.urls import url,patterns,include

urlpatterns= [
	
	url(r'home','User.views.home_User',name='User_home'),

		]