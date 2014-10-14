from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('rest.views',
                       # Examples:
                       # url(r'^$', 'opsdriod.views.home', name='home'),
                       url(r'^tasks/date/(?P<date>[0-9]{8})/$', 'query_metadata', {'query':'date'}),
                       url(r'^tasks/exec_id/(?P<exec_id>[\w]+)/$', 'query_metadata', {'query':'instance'}),
                       url(r'^tasks/list/(?P<type>[\w]+)/$', 'query_metadata', {'query':'list'}),
                       url(r'^tasks/log/agent/(?P<agent>.+)/(?P<exec_id>[\w]+)/$', 'get_job_log'),
                       url(r'^tasks/history/(?P<task_id>[\w]+)/$', 'query_metadata', {'query':'history'}),
                       url(r'^triggers/list/$', 'query_trigger_names'),
                       url(r'^triggers/ops_trigger_cron/(?P<trigger_id>[\w]+)/$', 'query_metadata',{'query':'cron'}),
                       url(r'^triggers/ops_trigger_time/(?P<trigger_id>[\w]+)/$', 'query_metadata',{'query':'time'}),
                       url(r'^actions/(?P<action>[\w]+)/ops_task_unix/(?P<task_id>[\w]+)/$', 'task_action'),
)


