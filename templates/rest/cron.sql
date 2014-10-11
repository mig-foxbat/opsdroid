SELECT
a.name
,a.version
,CASE WHEN enabled = 0 THEN 'false' ELSE 'True' END AS enabled
,d.name AS task_name
,c.name AS calendar_name
,CASE WHEN skip_active = 0 THEN 'False' ELSE 'True' END as skip_when_active
,DATE_FORMAT(a.next_scheduled_time,'%Y-%m-%d %H:%i:%s') as next_scheduled_time
,a.sys_created_by
,DATE_FORMAT(a.sys_created_on,'%Y-%m-%d %H:%i:%s') as sys_created_on
,a.sys_updated_by
,DATE_FORMAT(a.sys_updated_on,'%Y-%m-%d %H:%i:%s') as sys_updated_on
,criteria
FROM ops_trigger a
INNER JOIN ops_trigger_cron b
ON a.sys_id =  b.sys_id
LEFT OUTER JOIN ops_calendar c
ON a.calendar = c.sys_id
LEFT OUTER JOIN ops_task d
ON a.task = d.sys_id
WHERE a.sys_id = '{{trigger_id}}';