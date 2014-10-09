from django.db import connection
from django.template import Template,Context
from django.conf import settings
import os.path,json,paramiko,config


######################### One Time Initialization when module loads #########################################
__author__ = 'chlr'

param_mapping = {
    'date':'run_date'
    ,'instance':'exec_id'
    ,'list':'task_type'
    ,'history':'task_id'
    }

#ssh = paramiko.SSHClient()
#ssh.load_host_keys(config.ssh['known_hosts'])

######################### One Time Initialization when module loads #########################################

def execute_query(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.          fetchall()
    result = json.dumps([dict(zip([col[0] for col in cursor.description],row)) for row in rows],indent=4,sort_keys=True)
    cursor.close()
    return result


def compose_sql(query,param):
    querystring =  open(os.path.join(settings.TEMPLATE_DIR,'rest',query+'.sql')).read()
    t =Template(querystring)
    return t.render(Context({param_mapping[query]:param}))


def read_remote_file(agent,sys_id,file_type):
    ssh.connect(agent,username = config.ssh['user'],pkey = paramiko.DSSKey.from_private_key_file(config.ssh['privatekeyfile']))
    sftp = ssh.open_sftp()
    try:
        f = sftp.open(os.path.join(config.ssh['base_dir'],sys_id+'_'+file_type),'r')
        output = f.read()
    except IOError:
        output = ''
    sftp.close()
    ssh.close()
    return output


def get_agent_host_name(agent_sys_id):
    sql = "select host_name from ops_agent where sys_id = '%s';"
    cursor = connection.cursor()
    cursor.execute(sql % (agent_sys_id,))
    row = cursor.fetchone()
    cursor.close()
    return row[0]


