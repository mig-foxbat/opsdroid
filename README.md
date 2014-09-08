opsdriod
========

An Andriod client for Opswise with Django based web server as middleware between the mobile client and the Opswise Master Node.


Api Calls

#### List all Tasks for a given date
```
http://localhost:8000/tasks/date/20140830/
```

#### List all Tasks for a given type
```
http://localhost:8000/tasks/list/ops_task_monitor/
```

#### Task info. Task qualified by Sys_id
```
http://localhost:8000/tasks/exec_id/00b1af097f0000010f60a5ef9c14f8cc/
```

#### Task run log

```
http://localhost:8000/tasks/log/agent/opswise-agent-name/43a59c7c7f0000016b5650e0b6f5b4d0/
```
