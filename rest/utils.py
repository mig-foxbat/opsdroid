from django.db import connection
from django.template import Template,Context
from django.conf import settings
import os.path,json


__author__ = 'chlr'

param_mapping = {
    'date':'run_date'
   ,'instance':'exec_id'
   ,'list':'task_type'
}

def execute_query(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    result = json.dumps([dict(zip([col[0] for col in cursor.description],row)) for row in rows],indent=4,sort_keys=True)
    cursor.close()
    return result


def compose_sql(query,param):
    querystring =  open(os.path.join(settings.TEMPLATE_DIR,'rest',query+'.sql')).read()
    t =Template(querystring)
    print({param_mapping[query]:param})
    return t.render(Context({param_mapping[query]:param}))












