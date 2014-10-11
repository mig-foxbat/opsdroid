SELECT
a.name
,a.version
,CASE WHEN enabled = 0 THEN 'false' ELSE 'True' END AS enabled
,d.name AS task_name
,c.name AS calendar_name
,skip_count
,DATE_FORMAT(a.next_scheduled_time,'%Y-%m-%d %H:%i:%s') as next_scheduled_time
,a.sys_created_by
,DATE_FORMAT(a.sys_created_on,'%Y-%m-%d %H:%i:%s') as sys_created_on
,a.sys_updated_by
,DATE_FORMAT(a.sys_updated_on,'%Y-%m-%d %H:%i:%s') as sys_updated_on
,CASE WHEN b.time_style = 1 THEN 'Fixed Time' WHEN b.time_style = 2 THEN 'Interval' ELSE '' END as time_style
,b.time
,b.time_interval
,CASE WHEN b.time_interval_units = 1 THEN 'Seconds' WHEN b.time_interval_units = 2 THEN 'Minutes'  WHEN b.time_interval_units = 3 THEN 'Hours' END as interval_units
,starting_at as offset
FROM ops_trigger a
INNER JOIN ops_trigger_time b
ON a.sys_id =  b.sys_id
LEFT OUTER JOIN ops_calendar c
ON a.calendar = c.sys_id
LEFT OUTER JOIN ops_task d
ON a.task = d.sys_id
WHERE a.sys_id = '{{trigger_id}}';