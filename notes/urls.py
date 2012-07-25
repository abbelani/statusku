from django.conf.urls import patterns, include, url

urlpatterns = patterns('notes.views',
    url(r'^$', 'index'),
    url(r'^add/$', 'add'),
    # url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
