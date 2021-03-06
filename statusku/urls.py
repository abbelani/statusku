from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# importing all api classes from tastypie
from notes.api import *

import settings

urlpatterns = patterns('',
    # Examples:
    #  url(r'^$', 'statusku.views.home', name='home'),
    # url(r'^statusku/', include('statusku.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # rest api autogenerated with tastypie
    url(r'^api/', include(v1_api.urls)),
    
    # notes urls in notes directory                   
    url(r'^notes/', include('notes.urls')),
    
    # hack to get static files served both locally and on heroku                   
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
                       )

