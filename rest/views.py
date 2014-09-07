# Create your views here.
import utils
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods




@require_http_methods(['GET'])
def query_metadata(request,**kwargs):

    key_mapping = {
    'date' : 'date'
    ,'instance':'exec_id'
    ,'list': 'type'
    }

    sql = utils.compose_sql(kwargs['query'],kwargs[key_mapping[kwargs['query']]])
    result = utils.execute_query(sql)
    response = HttpResponse(result,content_type="text/plain")
    return response

@require_http_methods(['GET'])
def get_job_log(request,agent=None,exec_id=None):
    result = utils.read_remote_file(agent,exec_id)
    response = HttpResponse(result,content_type="text/plain")
    return response







