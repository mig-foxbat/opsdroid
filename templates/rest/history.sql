select
task_ref_count
,DATE_FORMAT(queued_time,'%Y-%m-%d %H:%i:%s') as queued_time
,DATE_FORMAT(start_time,'%Y-%m-%d %H:%i:%s') as start_time
,DATE_FORMAT(end_time,'%Y-%m-%d %H:%i:%s') as end_time
,CASE WHEN start_time IS NULL THEN '' ELSE TIME_FORMAT(TIMEDIFF( coalesce(end_time,current_timestamp ), coalesce(start_time,current_timestamp ) ),'%H:%i:%s')  END as duration
from ops_exec
where task_id = '{{task_id}}'
order by task_ref_count desc limit 100;