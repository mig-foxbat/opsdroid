SELECT
t.ls_enabled,
t.name,
t.retry_indefinitely,
t.retry_interval,
t.retry_maximum,
t.summary,
t.sys_class_name,
DATE_FORMAT(t.sys_created_on,'%Y-%m-%d %H:%i:%s') as task_created_by,
t.sys_created_by,
t.sys_id,
t.sys_updated_by,
DATE_FORMAT(t.sys_updated_on,'%Y-%m-%d %H:%i:%s') as task_updated_on,
DATE_FORMAT(e.workflow_start_time,'%Y-%m-%d %H:%i:%s') as workflow_start_time,
e.workflow_id,
e.trigger_id,
e.task_ref_count,
e.status_description,
e.status_code,
DATE_FORMAT(e.start_time,'%Y-%m-%d %H:%i:%s') as start_time,
e.start_held_reason,
DATE_FORMAT(e.queued_time,'%Y-%m-%d %H:%i:%s') as queued_time,
e.invoked_by,
e.execution_user,
DATE_FORMAT(e.end_time,'%Y-%m-%d %H:%i:%s') as end_time,
e.duration_seconds,
e.duration,
e.attempt_count,
e.agent
FROM 
ops_task t 
LEFT OUTER JOIN
ops_exec e
ON t.sys_id = e.task_id
WHERE cast(e.sys_updated_on as date) = {{run_date}}
or cast(e.sys_updated_on as date) = {{run_date}};