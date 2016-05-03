"""stockprediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
    Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from . import views
from stockapp import views
from track import views
admin.autodiscover()


urlpatterns = [
    url(r'^$', 'stockapp.views.index', name='index'),
    url(r'^news/$', 'stockapp.views.news', name='news'),
    url( r'^search/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.search', name='search_stock' ),
    url( r'^search/graph/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.graph_data', name='graph' ),
    url( r'^search/graph/(?P<name>[a-zA-Z0-9_.-]+)/(?P<day>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.search1', name='graph_time1' ),
    url( r'^search/graph1/(?P<name>[a-zA-Z0-9_.-]+)/(?P<days>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.graph_data_time', name='graph_time' ),
    url( r'^search/rsi/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.rsi', name='graph_rsi1' ),
    url( r'^search/rsi1/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.rsi_data', name='graph_rsi' ),
    url( r'^search/candlestick/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.candlestick', name='graph_candlestick1' ),
    url( r'^search/candlestick1/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.candlestick_data', name='graph_candlestick' ),
    url( r'^search/trendline/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.trendline', name='graph_trendline1' ),
    url( r'^search/trendline1/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.trendline_data', name='graph_trendline' ),
    url( r'^search/volume/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.volume', name='graph_volume1' ),
    url( r'^search/volume1/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.volume_data', name='graph_volume' ),
    url( r'^search/close/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.close', name='graph_close1' ),
    url( r'^search/close1/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.close_data', name='graph_close' ),
    url( r'^search/macd/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.macd', name='graph_macd1' ),
    url( r'^search/macd1/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.macd_data', name='graph_macd' ),
    # url( r'^search/1day/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.day1', name='graph_1day1' ),
    # url( r'^search/1day1/(?P<name>[a-zA-Z0-9_.-]+)/$', 'stockapp.views.day1_data', name='graph_1day' ),
    url(r'^track2/ajax/', 'track.views.track_ajax1', name='track_ajax1'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^User/', include('User.urls')),
    url(r'^track/$', 'track.views.track', name='track'),
    url(r'^track1/ajax/', 'track.views.track_ajax', name='track_ajax'),
    url(r'^User/', include('User.urls')),
    url( r'^query1', 'stockapp.views.query1', name='query1' ),
    url( r'^query2', 'stockapp.views.query2', name='query2' ),
    url( r'^query3', 'stockapp.views.query3', name='query3' ),
    url( r'^query4', 'stockapp.views.query4', name='query4' ),
    url( r'^query5', 'stockapp.views.query5', name='query5' ),
    url(r'^compare1/ajax/', 'stockapp.views.compare_ajax', name='compare_ajax'),
    url( r'^compare', 'stockapp.views.compare', name='compare' ),


]

urlpatterns+=    [
url(r'^login/','django.contrib.auth.views.login',
        {'template_name':'login.html'},
        name='stockprediction_login'),
    url(r'^logout/','django.contrib.auth.views.logout',
        {'next_page':'index'},
        name='stockprediction_logout'),
]