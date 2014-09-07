select
name
,version
,summary
,cast(last_run as char) as last_run
,sys_updated_by
,sys_created_by
,sys_id
from ops_task
where sys_class_name = '{{task_type}}';