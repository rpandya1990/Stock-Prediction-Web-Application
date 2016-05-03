from django.conf.urls import url, include
from django.contrib import admin    

from track import views


urlpatterns = [
    url(r'^track1/ajax/', 'track.views.track_ajax', name='track_ajax'),
    url(r'^track2/ajax/', 'track.views.track_ajax1', name='track2_ajax'),
    #url(r'^track/', 'track.views.track', name='track'),
    
]