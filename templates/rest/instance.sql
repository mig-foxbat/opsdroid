select
sys_class_name,
task_id,
name,
summary,
invoked_by,
DATE_FORMAT(queued_time,'%Y-%m-%d') as queued_time,
DATE_FORMAT(start_time,'%Y-%m-%d') as start_time,
DATE_FORMAT(end_time,'%Y-%m-%d') as end_time,
task_ref_count,
status_code,
agent,
workflow_id,
trigger_id,
duration_seconds,
retry_maximum,
retry_counter,
retry_indefinitely,
retry_interval,
attempt_count
from ops_exec where
sys_id = '{{exec_id}}';