from django.conf.urls import patterns, include, url

from django.contrib import admin
import rest.views


admin.autodiscover()

urlpatterns = patterns('rest.views',
                       # Examples:
                       # url(r'^$', 'opsdriod.views.home', name='home'),
                       url(r'^tasks/date/(?P<date>[0-9]{8})/$', 'query_metadata', {'query':'date'}),
                       url(r'^tasks/exec_id/(?P<exec_id>[\w]+)/$', 'query_metadata', {'query':'instance'}),
                       url(r'^tasks/list/(?P<type>[\w]+)/$', 'query_metadata', {'query':'list'}),
)


