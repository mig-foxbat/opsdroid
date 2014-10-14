# Create your views here.
import utils,json,config
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods





@require_http_methods(['GET'])
def query_trigger_names(request):
    sql = 'SELECT sys_id,sys_class_name,name from ops_trigger;'
    result = utils.execute_query(sql)
    response = HttpResponse(result,content_type="text/plain")
    return response;



@require_http_methods(['GET'])
def query_metadata(request,**kwargs):

    key_mapping = {
    'date' : 'date'
    ,'instance':'exec_id'
    ,'list': 'type'
    ,'history' : 'task_id'
    ,'cron':'trigger_id'
    ,'time':'trigger_id'
    }

    sql = utils.compose_sql(kwargs['query'],kwargs[key_mapping[kwargs['query']]])
    result = utils.execute_query(sql)
    response = HttpResponse(result,content_type="text/plain")
    return response

@require_http_methods(['GET'])
def get_job_log(request,agent=None,exec_id=None):
    stdout = utils.read_remote_file(agent,exec_id,'stdout')
    stderr = utils.read_remote_file(agent,exec_id,'stderr')
    result = { 'stdout': stdout
                ,'stderr' : stderr }
    response = HttpResponse(json.dumps(result,indent=4),content_type="text/plain")
    return response


@require_http_methods(['GET'])
def task_action(request,**kwargs):
    form_date = {
            'sysparm_processor':'OpswiseWorkflowProcessor'
            ,'sysparm_type':'command'
            ,'command_name':kwargs['action']
            ,'sys_id':kwargs['task_id']
            ,'user_name':request.GET['user_name']
            ,'user_password':request.GET['user_password']
    }
    url  = config.opswise_urls['base']+config.opswise_urls['action']
    reponse = HttpResponse(utils.post_to_opswise(url,form_date),content_type="text/plain")
    return reponse










